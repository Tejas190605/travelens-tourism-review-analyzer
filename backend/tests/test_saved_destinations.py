import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def auth_headers(client):
    login_res = client.post("/api/auth/login", json={
        "email": "traveler@travelens.com",
        "password": "userpassword123"
    })
    assert login_res.status_code == 200
    token = login_res.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

def test_saved_destinations_lifecycle(client, auth_headers):
    # 1. Bookmark destination 1
    res_save = client.post("/api/saved-destinations/1", headers=auth_headers)
    assert res_save.status_code == 201
    assert res_save.json()["is_saved"] is True

    # 2. Check status
    res_status = client.get("/api/saved-destinations/1/status", headers=auth_headers)
    assert res_status.status_code == 200
    assert res_status.json()["is_saved"] is True

    # 3. Retrieve list
    res_list = client.get("/api/saved-destinations", headers=auth_headers)
    assert res_list.status_code == 200
    saved_items = res_list.json()
    assert any(item["destination_id"] == 1 for item in saved_items)

    # 4. Remove bookmark
    res_del = client.delete("/api/saved-destinations/1", headers=auth_headers)
    assert res_del.status_code == 200
    assert res_del.json()["is_saved"] is False

    # 5. Status should be False
    res_status_after = client.get("/api/saved-destinations/1/status", headers=auth_headers)
    assert res_status_after.status_code == 200
    assert res_status_after.json()["is_saved"] is False

def test_saved_destinations_unauthorized(client):
    res = client.get("/api/saved-destinations")
    assert res.status_code == 401

def test_saved_destinations_multi_user_isolation(client):
    """Verify that saved destinations are strictly isolated between different users."""
    # 1. Login User A (traveler@travelens.com)
    res_a = client.post("/api/auth/login", json={
        "email": "traveler@travelens.com",
        "password": "userpassword123"
    })
    assert res_a.status_code == 200
    token_a = res_a.json()["access_token"]
    headers_a = {"Authorization": f"Bearer {token_a}"}

    # 2. Register and login User B
    res_b_reg = client.post("/api/auth/register", json={
        "name": "Second Traveler",
        "email": "traveler_b_isolation@travelens.com",
        "password": "SecurePassword123!"
    })
    assert res_b_reg.status_code == 201

    res_b = client.post("/api/auth/login", json={
        "email": "traveler_b_isolation@travelens.com",
        "password": "SecurePassword123!"
    })
    assert res_b.status_code == 200
    token_b = res_b.json()["access_token"]
    headers_b = {"Authorization": f"Bearer {token_b}"}

    # 3. User A saves destinations 1 and 2
    client.post("/api/saved-destinations/1", headers=headers_a)
    client.post("/api/saved-destinations/2", headers=headers_a)

    # 4. User B checks saved destinations - MUST be empty, cannot see User A's bookmarks
    b_list = client.get("/api/saved-destinations", headers=headers_b).json()
    assert len(b_list) == 0

    # 5. User B tries to delete destination 1 (saved by User A)
    client.delete("/api/saved-destinations/1", headers=headers_b)

    # 6. User A's bookmarks must still exist intact (User B cannot delete User A's bookmark)
    a_list = client.get("/api/saved-destinations", headers=headers_a).json()
    a_dest_ids = [item["destination_id"] for item in a_list]
    assert 1 in a_dest_ids
    assert 2 in a_dest_ids

    # 7. User B saves destination 3
    client.post("/api/saved-destinations/3", headers=headers_b)

    # 8. Verify User A only sees their own bookmarks, not User B's
    a_list_updated = client.get("/api/saved-destinations", headers=headers_a).json()
    a_dest_ids_updated = [item["destination_id"] for item in a_list_updated]
    assert 3 not in a_dest_ids_updated
    assert set(a_dest_ids_updated) == {1, 2}

    # 9. Verify User B only sees destination 3
    b_list_updated = client.get("/api/saved-destinations", headers=headers_b).json()
    b_dest_ids_updated = [item["destination_id"] for item in b_list_updated]
    assert b_dest_ids_updated == [3]

