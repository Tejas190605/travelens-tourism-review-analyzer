def test_protected_me_without_token(client):
    response = client.get("/api/auth/me")
    assert response.status_code == 401

def test_protected_me_with_valid_token(client):
    # Login first
    login_res = client.post("/api/auth/login", json={
        "email": "traveler@travelens.com",
        "password": "userpassword123"
    })
    assert login_res.status_code == 200
    token = login_res.json()["access_token"]

    # Access protected /api/auth/me
    headers = {"Authorization": f"Bearer {token}"}
    me_res = client.get("/api/auth/me", headers=headers)
    assert me_res.status_code == 200
    user_data = me_res.json()
    assert user_data["email"] == "traveler@travelens.com"
    assert user_data["name"] == "Traveler Jane"
    assert user_data["role"] == "user"

def test_protected_me_with_invalid_token(client):
    headers = {"Authorization": "Bearer invalid_garbage_token"}
    response = client.get("/api/auth/me", headers=headers)
    assert response.status_code == 401
