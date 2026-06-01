from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register():
    response = client.post("/api/v1/auth/register", json={
        "name": "Test",
        "email": "test@example.com",
        "password": "test123"
    })
    assert response.status_code in [200, 400]


def test_login():
    response = client.post("/api/v1/auth/login", json={
        "email": "test@example.com",
        "password": "test123"
    })
    assert "access_token" in response.json() or response.status_code == 401