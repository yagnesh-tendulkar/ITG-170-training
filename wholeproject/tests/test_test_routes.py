from fastapi.testclient import TestClient
from app.main import app
from app.database.database import dbTest

client = TestClient(app)


def setup_function():
    dbTest.clear()


def test_create_test():

    response = client.post(
        "/test/test",
        json={
            "id": 1,
            "name": "Sample",
            "email": "sample@gmail.com",
            "age": 25
        }
    )

    assert response.status_code == 201


def test_get_all_tests():

    response = client.get("/test/test")

    assert response.status_code == 200