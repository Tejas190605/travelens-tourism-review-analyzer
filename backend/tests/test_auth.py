def test_user_registration_success(client):
    payload = {
        "name": "New Traveler",
        "email": "newtraveler@example.com",
        "password": "strongpassword123"
    }
    response = client.post("/api/auth/register", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_user_registration_duplicate_email(client):
    payload = {
        "name": "Duplicate Traveler",
        "email": "admin@travelens.com",
        "password": "password123"
    }
    response = client.post("/api/auth/register", json=payload)
    assert response.status_code == 400
    assert "already exists" in response.json()["detail"]

def test_user_login_success(client):
    payload = {
        "email": "admin@travelens.com",
        "password": "adminpassword123"
    }
    response = client.post("/api/auth/login", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data

def test_user_login_invalid_password(client):
    payload = {
        "email": "admin@travelens.com",
        "password": "wrongpassword"
    }
    response = client.post("/api/auth/login", json=payload)
    assert response.status_code == 401
