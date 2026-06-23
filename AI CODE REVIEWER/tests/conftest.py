# ─────────────────────────────────────────────
# tests/conftest.py
#
# LEARNING NOTE:
# conftest.py is a special pytest file — fixtures defined here are
# automatically available to ALL test files without importing them.
#
# KEY CONCEPTS:
#   - Fixtures: reusable setup/teardown code (like @Before in JUnit)
#   - Dependency Override: swap real DB with in-memory test DB
#   - TestClient: lets us make HTTP requests without a real server
#   - Scope: "function" (reset per test) vs "module" (shared per file)
# ─────────────────────────────────────────────

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from unittest.mock import AsyncMock, patch

# Import our app and database components
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from main import app
from database import Base, get_db
from auth import hash_password, create_access_token
import models

# ── Test Database Setup ────────────────────────────────────────────────
# We use an IN-MEMORY SQLite database for testing.
# This means:
#   - Tests run fast (no disk I/O)
#   - Tests are isolated (fresh DB for each test run)
#   - No risk of corrupting your real codereview.db

TEST_DATABASE_URL = "sqlite:///./test_codereview.db"

test_engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


def override_get_db():
    """
    Dependency override: replaces the real DB session with the test DB session.
    FastAPI's dependency injection makes this very clean — we just swap one
    function for another without changing any production code.
    """
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


# ── Fixtures ────────────────────────────────────────────────

@pytest.fixture(scope="function", autouse=True)
def setup_database():
    """
    Create all tables before each test, drop them after.
    scope="function" means this runs fresh for EVERY test function.
    autouse=True means it applies automatically without explicit use.
    """
    Base.metadata.create_all(bind=test_engine)
    yield
    Base.metadata.drop_all(bind=test_engine)


@pytest.fixture(scope="function")
def client():
    """
    A TestClient configured to use our test database.
    TestClient lets you call your FastAPI routes like HTTP calls
    without needing a running server.
    """
    # Override the real DB dependency with the test one
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    # Restore after test
    app.dependency_overrides.clear()


@pytest.fixture
def db():
    """Provide a raw database session for direct DB manipulation in tests"""
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def test_user(db):
    """
    Create a test user directly in the DB (bypassing the API).
    This gives us a user to use in tests without going through registration.
    """
    user = models.User(
        email="test@example.com",
        username="testuser",
        hashed_password=hash_password("testpass123"),
        is_active=True,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@pytest.fixture
def auth_headers(test_user):
    """
    Create a valid JWT token for test_user and return it as
    Authorization headers — ready to use in authenticated requests.
    """
    token = create_access_token(data={"sub": test_user.email})
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def mock_ai():
    """
    Patch the AI service so tests don't make real Gemini API calls.
    This makes tests:
      - Fast (no network round-trips)
      - Deterministic (same result every time)
      - Free (no API quota used)
    We use unittest.mock.AsyncMock because analyze_code is async.
    """
    mock_result = {
        "bugs": [
            {"description": "Test bug 1", "line_hint": "Line 1", "severity": "high"},
            {"description": "Test bug 2", "line_hint": "Line 5", "severity": "low"},
        ],
        "optimizations": [
            {"description": "Test optimization", "impact": "medium"}
        ],
        "best_practices": [
            {"description": "Test best practice", "category": "Testing"}
        ],
        "overall_score": 75,
        "summary": "This is a test summary from mock AI.",
    }
    with patch(
        "services.review_service.analyze_code",
        new_callable=AsyncMock,
        return_value=mock_result
    ) as mock:
        yield mock
