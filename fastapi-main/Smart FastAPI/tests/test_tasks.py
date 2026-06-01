from http import client


def test_create_task():
    response = client.post("/api/v1/tasks", json={
        "title": "Test Task",
        "description": "Test",
        "priority": "high"
    })
    assert response.status_code in [200, 401]