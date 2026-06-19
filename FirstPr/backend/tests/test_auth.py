import uuid
from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_register_and_login_cycle():
    email = f"testuser+{uuid.uuid4().hex}@example.com"
    password = "testpass123"
    response = client.post("/api/auth/register", json={"name": "Test User", "email": email, "password": password})
    assert response.status_code == 200
    assert response.json()["email"] == email

    login_response = client.post("/api/auth/login", json={"email": email, "password": password})
    assert login_response.status_code == 200
    data = login_response.json()
    assert data["token_type"] == "bearer"
    assert data["access_token"]


def test_failed_login_returns_401():
    response = client.post("/api/auth/login", json={"email": "bad@example.com", "password": "nopass"})
    assert response.status_code == 401
