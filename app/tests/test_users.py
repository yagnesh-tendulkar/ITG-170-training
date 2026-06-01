def test_create_user(client):
    resp = client.post("/users", json={
        "name": "Alice", "email": "alice@example.com",
        "password": "secret123", "age": 22
    })
    assert resp.status_code == 201
    data = resp.json()
    assert data["email"] == "alice@example.com"
    assert "id" in data


def test_create_user_underage(client):
    resp = client.post("/users", json={
        "name": "Bob", "email": "bob@example.com",
        "password": "secret", "age": 16
    })
    assert resp.status_code == 422


def test_duplicate_email(client):
    payload = {"name": "Charlie", "email": "charlie@example.com",
               "password": "pass123", "age": 30}
    client.post("/users", json=payload)
    resp = client.post("/users", json=payload)
    assert resp.status_code == 409


def test_login(client):
    client.post("/users", json={
        "name": "Dan", "email": "dan@example.com",
        "password": "mypassword", "age": 28
    })
    resp = client.post("/users/login", json={
        "email": "dan@example.com", "password": "mypassword"
    })
    assert resp.status_code == 200
    assert "access_token" in resp.json()


def test_login_invalid_credentials(client):
    resp = client.post("/users/login", json={
        "email": "nobody@example.com", "password": "wrong"
    })
    assert resp.status_code == 401


def test_get_users(client):
    resp = client.get("/users")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
