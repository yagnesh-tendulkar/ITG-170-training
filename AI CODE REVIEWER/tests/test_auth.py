# ─────────────────────────────────────────────
# tests/test_auth.py
#
# LEARNING NOTE:
# These are "integration tests" — they test the full HTTP request/response
# cycle including routing, validation, DB writes, and JWT creation.
#
# Test naming convention: test_<what>_<scenario>
# Examples:
#   test_register_success     → happy path
#   test_register_duplicate   → error case
#   test_login_wrong_password → error case
#
# ASSERTIONS (assert):
#   We check both the HTTP status code AND the response body.
#   A 200 OK with an empty body is not a success — always check content!
# ─────────────────────────────────────────────

import pytest


class TestRegister:
    """Tests for POST /auth/register"""

    def test_register_success(self, client):
        """Happy path: register a new user, get back user info"""
        response = client.post("/auth/register", json={
            "username": "newuser",
            "email": "new@example.com",
            "password": "password123",
        })

        # Check HTTP status: 201 Created
        assert response.status_code == 201

        data = response.json()
        # Check the response body contains expected fields
        assert data["email"] == "new@example.com"
        assert data["username"] == "newuser"
        assert data["is_active"] is True
        assert "id" in data
        # CRITICAL: password must never appear in any response
        assert "password" not in data
        assert "hashed_password" not in data

    def test_register_duplicate_email(self, client, test_user):
        """Error case: try to register with an already-used email"""
        response = client.post("/auth/register", json={
            "username": "differentuser",
            "email": "test@example.com",   # same as test_user
            "password": "password123",
        })

        # Should be rejected with 400 Bad Request
        assert response.status_code == 400
        assert "already exists" in response.json()["detail"].lower()

    def test_register_duplicate_username(self, client, test_user):
        """Error case: try to register with a taken username"""
        response = client.post("/auth/register", json={
            "username": "testuser",        # same as test_user
            "email": "different@example.com",
            "password": "password123",
        })

        assert response.status_code == 400
        assert "taken" in response.json()["detail"].lower()

    def test_register_invalid_email(self, client):
        """Validation: Pydantic should reject malformed email"""
        response = client.post("/auth/register", json={
            "username": "user1",
            "email": "not-an-email",      # invalid format
            "password": "password123",
        })

        # FastAPI returns 422 Unprocessable Entity for validation errors
        assert response.status_code == 422

    def test_register_short_password(self, client):
        """Validation: password must be at least 6 characters"""
        response = client.post("/auth/register", json={
            "username": "user1",
            "email": "user1@example.com",
            "password": "abc",            # too short
        })

        assert response.status_code == 422

    def test_register_short_username(self, client):
        """Validation: username must be at least 3 characters"""
        response = client.post("/auth/register", json={
            "username": "ab",             # too short
            "email": "user1@example.com",
            "password": "password123",
        })

        assert response.status_code == 422


class TestLogin:
    """Tests for POST /auth/login"""

    def test_login_success(self, client, test_user):
        """Happy path: correct credentials → get JWT token"""
        response = client.post("/auth/login", json={
            "email": "test@example.com",
            "password": "testpass123",
        })

        assert response.status_code == 200

        data = response.json()
        # Check token structure
        assert "access_token" in data
        assert data["token_type"] == "bearer"
        assert len(data["access_token"]) > 50  # JWT tokens are long strings

        # Check embedded user info
        assert data["user"]["email"] == "test@example.com"
        assert data["user"]["username"] == "testuser"

    def test_login_wrong_password(self, client, test_user):
        """Error case: wrong password → 401 Unauthorized"""
        response = client.post("/auth/login", json={
            "email": "test@example.com",
            "password": "wrongpassword",
        })

        assert response.status_code == 401
        # Generic error message (prevents email enumeration attacks)
        assert "Invalid" in response.json()["detail"]

    def test_login_nonexistent_email(self, client):
        """Error case: email not registered → 401 (same message as wrong password)"""
        response = client.post("/auth/login", json={
            "email": "nobody@example.com",
            "password": "password123",
        })

        assert response.status_code == 401

    def test_login_missing_fields(self, client):
        """Validation: missing required fields"""
        response = client.post("/auth/login", json={
            "email": "test@example.com",
            # missing password
        })

        assert response.status_code == 422


class TestGetMe:
    """Tests for GET /auth/me"""

    def test_get_me_success(self, client, test_user, auth_headers):
        """Happy path: valid token → get user profile"""
        response = client.get("/auth/me", headers=auth_headers)

        assert response.status_code == 200
        data = response.json()
        assert data["email"] == "test@example.com"
        assert data["username"] == "testuser"
        assert "hashed_password" not in data

    def test_get_me_no_token(self, client):
        """Error case: no token → 401"""
        response = client.get("/auth/me")
        assert response.status_code == 401

    def test_get_me_invalid_token(self, client):
        """Error case: invalid/tampered token → 401"""
        response = client.get("/auth/me", headers={
            "Authorization": "Bearer this.is.not.a.valid.token"
        })
        assert response.status_code == 401
