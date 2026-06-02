from fastapi.testclient import TestClient
from app.main import app
from app.database.database import dbUser

client = TestClient(app)


def setup_function():
    dbUser.clear()


def test_create_user():

    response = client.post(
        "/user",
        json={
            "id": 1,
            "name": "John",
            "email": "john@gmail.com",
            "age": 25,
            "password": "123456"
        }
    )

    assert response.status_code == 201
    assert response.json()["name"] == "John"


def test_get_user_by_id():

    dbUser[1] = {
        "id": 1,
        "name": "John",
        "email": "john@gmail.com",
        "age": 25,
        "password": "123456"
    }

    response = client.get("/user/1")

    assert response.status_code == 200


def test_delete_user():

    client.post(
        "/user",
        json={
            "id": 1,
            "name": "John",
            "email": "john@gmail.com",
            "age": 25,
            "password": "123456"
        }
    )

    response = client.delete("/user/1")

    assert response.status_code == 204