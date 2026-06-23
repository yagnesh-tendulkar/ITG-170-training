# ─────────────────────────────────────────────
# services/review_service.py
#
# LEARNING NOTE:
# The "service layer" contains business logic — the actual work your app does.
# Keeping this separate from the router (HTTP layer) is good practice:
#   - Routers handle HTTP: request parsing, response formatting, status codes
#   - Services handle logic: calling AI, saving to DB, computing stats
# This makes your code easier to test and maintain.
# ─────────────────────────────────────────────

import json
from typing import List, Optional
from sqlalchemy.orm import Session
from collections import Counter

import models
import schemas
from services.ai_service import analyze_code, generate_documentation


async def create_review(
    db: Session,
    user_id: int,
    review_data: schemas.ReviewCreate
) -> models.Review:
    """
    Orchestrates a full code review:
      1. Call the AI service to get analysis
      2. Save the result to the database
      3. Return the saved Review model
    """
    # Step 1: Ask AI to review the code
    ai_result = await analyze_code(review_data.language, review_data.code_snippet)

    # Step 2: Create a new Review record
    # We store arrays as JSON strings in SQLite (SQLite doesn't have array types)
    db_review = models.Review(
        user_id=user_id,
        title=review_data.title,
        language=review_data.language,
        code_snippet=review_data.code_snippet,
        bugs=json.dumps(ai_result.get("bugs", [])),
        optimizations=json.dumps(ai_result.get("optimizations", [])),
        best_practices=json.dumps(ai_result.get("best_practices", [])),
        summary=ai_result.get("summary", ""),
        overall_score=float(ai_result.get("overall_score", 0)),
    )

    db.add(db_review)
    db.commit()           # Save to database
    db.refresh(db_review) # Reload to get the auto-generated id + created_at

    return db_review


def get_review_by_id(db: Session, review_id: int, user_id: int) -> Optional[models.Review]:
    """Fetch a single review — only if it belongs to the current user"""
    return db.query(models.Review).filter(
        models.Review.id == review_id,
        models.Review.user_id == user_id
    ).first()


def get_user_reviews(
    db: Session,
    user_id: int,
    skip: int = 0,
    limit: int = 20
) -> List[models.Review]:
    """Fetch paginated reviews for a user, newest first"""
    return (
        db.query(models.Review)
        .filter(models.Review.user_id == user_id)
        .order_by(models.Review.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


def delete_review(db: Session, review_id: int, user_id: int) -> bool:
    """Delete a review — returns True if deleted, False if not found"""
    review = get_review_by_id(db, review_id, user_id)
    if not review:
        return False
    db.delete(review)
    db.commit()
    return True


def model_to_response(review: models.Review) -> schemas.ReviewResponse:
    """
    Convert a SQLAlchemy Review model → ReviewResponse schema.
    Parses the JSON strings back to Python lists.
    """
    def safe_parse(value: str) -> list:
        try:
            return json.loads(value) if value else []
        except (json.JSONDecodeError, TypeError):
            return []

    return schemas.ReviewResponse(
        id=review.id,
        title=review.title,
        language=review.language,
        code_snippet=review.code_snippet,
        bugs=[schemas.BugItem(**b) for b in safe_parse(review.bugs)],
        optimizations=[schemas.OptimizationItem(**o) for o in safe_parse(review.optimizations)],
        best_practices=[schemas.BestPracticeItem(**p) for p in safe_parse(review.best_practices)],
        summary=review.summary,
        overall_score=review.overall_score,
        created_at=review.created_at,
    )


def get_dashboard_stats(db: Session, user_id: int) -> schemas.DashboardStats:
    """Compute stats for the dashboard page"""
    reviews = db.query(models.Review).filter(models.Review.user_id == user_id).all()

    if not reviews:
        return schemas.DashboardStats(
            total_reviews=0,
            average_score=0.0,
            most_used_language=None,
            total_bugs_found=0,
            recent_reviews=[],
        )

    total = len(reviews)
    avg_score = sum(r.overall_score for r in reviews) / total

    # Find the most commonly reviewed language
    languages = [r.language for r in reviews]
    most_used = Counter(languages).most_common(1)[0][0]

    # Count total bugs across all reviews
    total_bugs = 0
    for r in reviews:
        try:
            bugs = json.loads(r.bugs) if r.bugs else []
            total_bugs += len(bugs)
        except (json.JSONDecodeError, TypeError):
            pass

    # Recent 5 reviews for the dashboard list
    recent = sorted(reviews, key=lambda r: r.created_at, reverse=True)[:5]
    recent_summaries = [
        schemas.ReviewSummary(
            id=r.id,
            title=r.title,
            language=r.language,
            overall_score=r.overall_score,
            bug_count=len(json.loads(r.bugs) if r.bugs else []),
            created_at=r.created_at,
        )
        for r in recent
    ]

    return schemas.DashboardStats(
        total_reviews=total,
        average_score=round(avg_score, 1),
        most_used_language=most_used,
        total_bugs_found=total_bugs,
        recent_reviews=recent_summaries,
    )
