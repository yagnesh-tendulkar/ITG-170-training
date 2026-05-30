"""Pytest fixtures for test client and test DB (placeholder)."""
import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)
