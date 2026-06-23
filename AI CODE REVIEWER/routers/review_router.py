# ─────────────────────────────────────────────
# routers/review_router.py
#
# LEARNING NOTE:
# This router handles all code review operations.
#
# Notice the pattern:
#   - Every route uses Depends(get_current_user) to require login
#   - Routes call services (not direct DB queries) — clean separation
#   - async def is used for routes that call AI (which takes time)
# ─────────────────────────────────────────────

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List

from database import get_db
import models
import schemas
from auth import get_current_user
from services import review_service

router = APIRouter(prefix="/reviews", tags=["Reviews"])


@router.post("/analyze", response_model=schemas.ReviewResponse, status_code=201)
async def analyze_code(
    review_data: schemas.ReviewCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """
    Submit code for AI review.

    This is an 'async' route because calling the AI API can take a few
    seconds. Using async means FastAPI can handle other requests while
    waiting — important for scalability!
    """
    review = await review_service.create_review(
        db=db,
        user_id=current_user.id,
        review_data=review_data,
    )
    return review_service.model_to_response(review)


@router.get("/history", response_model=List[schemas.ReviewSummary])
def get_history(
    skip: int = Query(default=0, ge=0, description="How many reviews to skip (for pagination)"),
    limit: int = Query(default=20, ge=1, le=100, description="Max reviews to return"),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """
    Get paginated review history for the current user.

    Query params: ?skip=0&limit=20
    Example: /reviews/history?skip=20&limit=20  (page 2)
    """
    reviews = review_service.get_user_reviews(db, current_user.id, skip, limit)

    import json
    return [
        schemas.ReviewSummary(
            id=r.id,
            title=r.title,
            language=r.language,
            overall_score=r.overall_score,
            bug_count=len(json.loads(r.bugs) if r.bugs else []),
            created_at=r.created_at,
        )
        for r in reviews
    ]


@router.get("/dashboard", response_model=schemas.DashboardStats)
def get_dashboard(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """Get dashboard statistics for the current user"""
    return review_service.get_dashboard_stats(db, current_user.id)


@router.get("/{review_id}", response_model=schemas.ReviewResponse)
def get_review(
    review_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """Get a specific review by ID (must belong to current user)"""
    review = review_service.get_review_by_id(db, review_id, current_user.id)
    if not review:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Review #{review_id} not found."
        )
    return review_service.model_to_response(review)


@router.delete("/{review_id}", status_code=204)
def delete_review(
    review_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    """
    Delete a review.
    Returns 204 No Content on success (no response body needed).
    """
    deleted = review_service.delete_review(db, review_id, current_user.id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Review #{review_id} not found."
        )
