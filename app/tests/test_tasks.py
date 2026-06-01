def test_create_task(client, auth_headers):
    resp = client.post("/tasks", json={
        "title": "Learn FastAPI",
        "description": "Complete middleware implementation",
        "priority": "high",
        "tags": ["backend", "python"]
    }, headers=auth_headers)
    assert resp.status_code == 201
    data = resp.json()
    assert data["title"] == "Learn FastAPI"
    assert data["priority"] == "high"


def test_create_task_short_title(client, auth_headers):
    resp = client.post("/tasks", json={
        "title": "AB",  # too short
        "priority": "low"
    }, headers=auth_headers)
    assert resp.status_code == 422


def test_list_tasks(client, auth_headers):
    resp = client.get("/tasks", headers=auth_headers)
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)


def test_get_task(client, auth_headers):
    create_resp = client.post("/tasks", json={
        "title": "Get single task", "priority": "medium"
    }, headers=auth_headers)
    task_id = create_resp.json()["id"]

    resp = client.get(f"/tasks/{task_id}", headers=auth_headers)
    assert resp.status_code == 200
    assert resp.json()["id"] == task_id


def test_patch_task_status(client, auth_headers):
    create_resp = client.post("/tasks", json={
        "title": "Patch me task", "priority": "low"
    }, headers=auth_headers)
    task_id = create_resp.json()["id"]

    resp = client.patch(f"/tasks/{task_id}", json={"status": "completed"}, headers=auth_headers)
    assert resp.status_code == 200
    assert resp.json()["status"] == "completed"


def test_delete_task(client, auth_headers):
    create_resp = client.post("/tasks", json={
        "title": "Delete me task", "priority": "low"
    }, headers=auth_headers)
    task_id = create_resp.json()["id"]

    resp = client.delete(f"/tasks/{task_id}", headers=auth_headers)
    assert resp.status_code == 204

    get_resp = client.get(f"/tasks/{task_id}", headers=auth_headers)
    assert get_resp.status_code == 404


def test_unauthenticated_access(client):
    resp = client.get("/tasks")
    assert resp.status_code == 401


def test_task_filtering(client, auth_headers):
    client.post("/tasks", json={"title": "High priority task", "priority": "high"}, headers=auth_headers)
    resp = client.get("/tasks?priority=high", headers=auth_headers)
    assert resp.status_code == 200
    for task in resp.json():
        assert task["priority"] == "high"


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "healthy"


def test_metrics(client):
    resp = client.get("/metrics")
    assert resp.status_code == 200
    assert "total_tasks" in resp.json()
