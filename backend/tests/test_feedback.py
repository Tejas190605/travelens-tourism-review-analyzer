import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db.database import get_db, Base, engine
from app.db.models import User, Destination, IssueReport
from app.core.security import hash_password, create_access_token


@pytest.fixture
def test_data(db_session):
    # Ensure a destination exists
    dest = db_session.query(Destination).first()
    if not dest:
        dest = Destination(
            name="Test Destination",
            country="India",
            category="Heritage",
            description="A test destination"
        )
        db_session.add(dest)
        db_session.commit()
        db_session.refresh(dest)

    # Ensure admin user
    admin = db_session.query(User).filter(User.email == "admin@example.com").first()
    if not admin:
        admin = User(
            name="Admin User",
            email="admin@example.com",
            password_hash=hash_password("adminpass123"),
            role="admin"
        )
        db_session.add(admin)
        db_session.commit()
        db_session.refresh(admin)

    # Ensure regular user
    reg_user = db_session.query(User).filter(User.email == "user@example.com").first()
    if not reg_user:
        reg_user = User(
            name="Regular User",
            email="user@example.com",
            password_hash=hash_password("userpass123"),
            role="user"
        )
        db_session.add(reg_user)
        db_session.commit()
        db_session.refresh(reg_user)

    return {"destination_id": dest.id, "admin": admin, "user": reg_user}

def test_submit_issue_report_success(client, test_data):
    dest_id = test_data["destination_id"]
    payload = {
        "destination_id": dest_id,
        "issue_type": "Outdated price or opening hours",
        "comment": "Ticket price changed from 50 to 100",
        "contact_email": "reporter@example.com"
    }
    response = client.post("/api/feedback/report", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["status"] == "success"
    assert "report_id" in data
    assert data["report_id"] > 0

def test_submit_issue_report_invalid_destination(client):
    payload = {
        "destination_id": 999999,
        "issue_type": "Outdated price or opening hours",
        "comment": "Non-existent place"
    }
    response = client.post("/api/feedback/report", json=payload)
    assert response.status_code == 404

def test_submit_issue_report_comment_too_long(client, test_data):
    dest_id = test_data["destination_id"]
    payload = {
        "destination_id": dest_id,
        "issue_type": "Outdated price or opening hours",
        "comment": "x" * 1001
    }
    response = client.post("/api/feedback/report", json=payload)
    assert response.status_code == 422

def test_get_issue_reports_unauthorized(client):
    response = client.get("/api/feedback/reports")
    assert response.status_code == 401

def test_get_issue_reports_forbidden_for_regular_user(client, test_data):
    user = test_data["user"]
    token = create_access_token(data={"sub": user.email, "role": user.role})
    response = client.get(
        "/api/feedback/reports",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 403

def test_get_issue_reports_admin_success(client, test_data):
    admin = test_data["admin"]
    token = create_access_token(data={"sub": admin.email, "role": admin.role})
    response = client.get(
        "/api/feedback/reports",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)

