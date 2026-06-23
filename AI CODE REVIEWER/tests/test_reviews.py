# ─────────────────────────────────────────────
# tests/test_reviews.py
#
# LEARNING NOTE:
# These tests cover the core feature: code reviews.
# Key pattern used: Arrange → Act → Assert (AAA)
#
#   Arrange: set up the state (user, auth token, existing reviews)
#   Act:     make the HTTP request
#   Assert:  check the response
#
# Notice how mock_ai is passed as a fixture to avoid real AI calls.
# The test still exercises all the code — routing, validation, DB writes —
# it just substitutes the AI response with a known fixed value.
# ─────────────────────────────────────────────

import pytest
import json


class TestAnalyze:
    """Tests for POST /reviews/analyze"""

    def test_analyze_success(self, client, auth_headers, mock_ai):
        """Happy path: submit code → get AI review back"""
        response = client.post("/reviews/analyze", json={
            "title": "Test Review",
            "language": "Python",
            "code_snippet": "def foo():\n    x = 1\n    return x",
        }, headers=auth_headers)

        assert response.status_code == 201

        data = response.json()
        # Check all required fields are present
        assert data["title"] == "Test Review"
        assert data["language"] == "Python"
        assert "bugs" in data
        assert "optimizations" in data
        assert "best_practices" in data
        assert "summary" in data
        assert "overall_score" in data
        assert "id" in data
        assert "created_at" in data

        # Check mock AI data was stored correctly
        assert len(data["bugs"]) == 2
        assert data["bugs"][0]["severity"] == "high"
        assert data["overall_score"] == 75.0

    def test_analyze_requires_auth(self, client, mock_ai):
        """Security: endpoint must reject unauthenticated requests"""
        response = client.post("/reviews/analyze", json={
            "title": "Test",
            "language": "Python",
            "code_snippet": "def foo(): pass",
        })
        # No auth headers → 401
        assert response.status_code == 401

    def test_analyze_code_too_short(self, client, auth_headers, mock_ai):
        """Validation: code_snippet must be at least 10 characters"""
        response = client.post("/reviews/analyze", json={
            "title": "Test",
            "language": "Python",
            "code_snippet": "x = 1",   # only 5 chars
        }, headers=auth_headers)

        assert response.status_code == 422

    def test_analyze_missing_title(self, client, auth_headers, mock_ai):
        """Validation: title is required"""
        response = client.post("/reviews/analyze", json={
            "language": "Python",
            "code_snippet": "def foo():\n    return 42",
        }, headers=auth_headers)

        assert response.status_code == 422

    def test_analyze_stores_in_db(self, client, auth_headers, mock_ai, db):
        """Integration: verify the review is actually persisted to the database"""
        import models as m

        response = client.post("/reviews/analyze", json={
            "title": "DB Test Review",
            "language": "JavaScript",
            "code_snippet": "function add(a, b) { return a + b; }",
        }, headers=auth_headers)

        assert response.status_code == 201
        review_id = response.json()["id"]

        # Directly query the test database to confirm it was saved
        db_review = db.query(m.Review).filter(m.Review.id == review_id).first()
        assert db_review is not None
        assert db_review.title == "DB Test Review"
        assert db_review.language == "JavaScript"
        assert db_review.overall_score == 75.0


class TestHistory:
    """Tests for GET /reviews/history"""

    def _create_review(self, client, headers, mock_ai, title="Review", lang="Python"):
        """Helper: quickly create a review for use in other tests"""
        client.post("/reviews/analyze", json={
            "title": title,
            "language": lang,
            "code_snippet": "def placeholder(): pass\n# some code",
        }, headers=headers)

    def test_history_empty(self, client, auth_headers):
        """New user should have empty history"""
        response = client.get("/reviews/history", headers=auth_headers)
        assert response.status_code == 200
        assert response.json() == []

    def test_history_returns_reviews(self, client, auth_headers, mock_ai):
        """After creating reviews, they should appear in history"""
        self._create_review(client, auth_headers, mock_ai, "Review 1")
        self._create_review(client, auth_headers, mock_ai, "Review 2")

        response = client.get("/reviews/history", headers=auth_headers)
        assert response.status_code == 200

        data = response.json()
        assert len(data) == 2

        # History returns ReviewSummary — check expected fields
        assert "id" in data[0]
        assert "title" in data[0]
        assert "language" in data[0]
        assert "overall_score" in data[0]
        assert "bug_count" in data[0]
        assert "created_at" in data[0]
        # code_snippet should NOT be in summary (it's a heavy field)
        assert "code_snippet" not in data[0]

    def test_history_pagination(self, client, auth_headers, mock_ai):
        """Test skip/limit pagination parameters"""
        # Create 5 reviews
        for i in range(5):
            self._create_review(client, auth_headers, mock_ai, f"Review {i}")

        # Page 1: first 3
        r1 = client.get("/reviews/history?skip=0&limit=3", headers=auth_headers)
        assert len(r1.json()) == 3

        # Page 2: next 2
        r2 = client.get("/reviews/history?skip=3&limit=3", headers=auth_headers)
        assert len(r2.json()) == 2

    def test_history_requires_auth(self, client):
        """Security: history must be protected"""
        response = client.get("/reviews/history")
        assert response.status_code == 401

    def test_history_user_isolation(self, client, test_user, auth_headers, mock_ai, db):
        """
        Security: users should ONLY see their own reviews.
        Create a second user and their review — first user must not see it.
        """
        import models as m
        from auth import hash_password, create_access_token

        # Create a second user directly in DB
        user2 = m.User(
            email="user2@example.com",
            username="user2",
            hashed_password=hash_password("pass2"),
            is_active=True,
        )
        db.add(user2)
        db.commit()
        db.refresh(user2)

        # Create a review for user2
        user2_review = m.Review(
            user_id=user2.id,
            title="User2 Private Review",
            language="Java",
            code_snippet="public class Main {}",
            bugs="[]", optimizations="[]", best_practices="[]",
            summary="private", overall_score=50.0,
        )
        db.add(user2_review)
        db.commit()

        # User1 (test_user) requests history
        response = client.get("/reviews/history", headers=auth_headers)
        assert response.status_code == 200
        titles = [r["title"] for r in response.json()]
        assert "User2 Private Review" not in titles


class TestGetReview:
    """Tests for GET /reviews/{id}"""

    def test_get_review_success(self, client, auth_headers, mock_ai):
        """Happy path: get a specific review by ID"""
        # Create a review first
        create_res = client.post("/reviews/analyze", json={
            "title": "Specific Review",
            "language": "Go",
            "code_snippet": "func main() {\n    fmt.Println(\"hello\")\n}",
        }, headers=auth_headers)
        review_id = create_res.json()["id"]

        # Fetch it by ID
        response = client.get(f"/reviews/{review_id}", headers=auth_headers)
        assert response.status_code == 200

        data = response.json()
        assert data["id"] == review_id
        assert data["title"] == "Specific Review"
        # Full review includes code_snippet (unlike history summary)
        assert "code_snippet" in data
        assert len(data["bugs"]) == 2   # from mock_ai

    def test_get_review_not_found(self, client, auth_headers):
        """Error case: review ID doesn't exist"""
        response = client.get("/reviews/99999", headers=auth_headers)
        assert response.status_code == 404

    def test_get_review_wrong_user(self, client, auth_headers, mock_ai, db):
        """Security: cannot fetch another user's review"""
        import models as m
        from auth import hash_password, create_access_token

        # Create review for a different user
        user2 = m.User(
            email="hacker@example.com",
            username="hacker",
            hashed_password=hash_password("pass"),
            is_active=True,
        )
        db.add(user2)
        db.commit()
        db.refresh(user2)

        other_review = m.Review(
            user_id=user2.id,
            title="Private Review",
            language="Python",
            code_snippet="secret code here",
            bugs="[]", optimizations="[]", best_practices="[]",
            summary="", overall_score=0.0,
        )
        db.add(other_review)
        db.commit()
        db.refresh(other_review)

        # test_user tries to access user2's review → 404 (not 403, for security)
        response = client.get(f"/reviews/{other_review.id}", headers=auth_headers)
        assert response.status_code == 404


class TestDeleteReview:
    """Tests for DELETE /reviews/{id}"""

    def test_delete_success(self, client, auth_headers, mock_ai):
        """Happy path: create then delete a review"""
        create_res = client.post("/reviews/analyze", json={
            "title": "To Delete",
            "language": "Python",
            "code_snippet": "x = 1\ny = 2\nz = x + y",
        }, headers=auth_headers)
        review_id = create_res.json()["id"]

        # Delete it
        del_res = client.delete(f"/reviews/{review_id}", headers=auth_headers)
        assert del_res.status_code == 204  # No Content

        # Confirm it's gone
        get_res = client.get(f"/reviews/{review_id}", headers=auth_headers)
        assert get_res.status_code == 404

    def test_delete_not_found(self, client, auth_headers):
        """Error case: delete nonexistent review"""
        response = client.delete("/reviews/99999", headers=auth_headers)
        assert response.status_code == 404

    def test_delete_requires_auth(self, client):
        """Security: delete must require authentication"""
        response = client.delete("/reviews/1")
        assert response.status_code == 401


class TestDashboard:
    """Tests for GET /reviews/dashboard"""

    def test_dashboard_empty(self, client, auth_headers):
        """New user gets zeroed-out stats"""
        response = client.get("/reviews/dashboard", headers=auth_headers)
        assert response.status_code == 200

        data = response.json()
        assert data["total_reviews"] == 0
        assert data["average_score"] == 0.0
        assert data["total_bugs_found"] == 0
        assert data["most_used_language"] is None
        assert data["recent_reviews"] == []

    def test_dashboard_with_reviews(self, client, auth_headers, mock_ai):
        """Dashboard reflects actual review data"""
        for _ in range(3):
            client.post("/reviews/analyze", json={
                "title": "Dashboard Test",
                "language": "Python",
                "code_snippet": "def example():\n    return True\n# code",
            }, headers=auth_headers)

        response = client.get("/reviews/dashboard", headers=auth_headers)
        assert response.status_code == 200

        data = response.json()
        assert data["total_reviews"] == 3
        assert data["average_score"] == 75.0        # from mock_ai
        assert data["most_used_language"] == "Python"
        assert data["total_bugs_found"] == 6        # 2 bugs × 3 reviews
        assert len(data["recent_reviews"]) == 3

    def test_dashboard_requires_auth(self, client):
        """Security: dashboard must be protected"""
        response = client.get("/reviews/dashboard")
        assert response.status_code == 401
