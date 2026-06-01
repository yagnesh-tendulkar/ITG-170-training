from http import client


def test_get_users():
    response = client.get("/api/v1/users")
    assert response.status_code == 200