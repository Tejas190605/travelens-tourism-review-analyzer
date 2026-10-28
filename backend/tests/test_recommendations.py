import pytest
from fastapi.testclient import TestClient
from app.main import app

def test_recommendations_endpoint_success(client):
    payload = {
        "adventure": 5,
        "relaxation": 4,
        "family": 3,
        "food": 5,
        "heritage": 4,
        "nightlife": 2,
        "budget": 3
    }
    response = client.post("/api/recommendations?top_n=4", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "recommendations" in data
    assert len(data["recommendations"]) <= 4
    
    first = data["recommendations"][0]
    assert "destination_id" in first
    assert "name" in first
    assert "match_percentage" in first
    assert 20 <= first["match_percentage"] <= 100
    assert "top_matches" in first
    assert len(first["top_matches"]) > 0
    assert "trade_offs" in first
    assert "explanation" in first

def test_recommendations_validation_failure(client):
    # priority out of bounds (0 is invalid since ge=1)
    payload = {
        "adventure": 0,
        "relaxation": 4,
        "family": 3,
        "food": 5,
        "heritage": 4,
        "nightlife": 2,
        "budget": 3
    }
    response = client.post("/api/recommendations", json=payload)
    assert response.status_code == 422

def test_recommendations_with_region_filter(client):
    payload = {
        "adventure": 4,
        "relaxation": 4,
        "family": 4,
        "food": 4,
        "heritage": 4,
        "nightlife": 3,
        "budget": 3,
        "region_filter": "India"
    }
    response = client.post("/api/recommendations?top_n=3", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "recommendations" in data
    assert len(data["recommendations"]) <= 3
    for dest in data["recommendations"]:
        assert dest["region"] == "India" or dest["country"] == "India"

def test_recommendations_with_budget_filter(client):
    payload = {
        "adventure": 3,
        "relaxation": 3,
        "family": 3,
        "food": 3,
        "heritage": 3,
        "nightlife": 3,
        "budget": 5,
        "budget_filter": "Budget"
    }
    response = client.post("/api/recommendations?top_n=3", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "recommendations" in data
    for dest in data["recommendations"]:
        assert dest["budget_tier"].lower() == "budget"

def test_recommendations_unmatched_filter_recovery(client):
    payload = {
        "adventure": 3,
        "relaxation": 3,
        "family": 3,
        "food": 3,
        "heritage": 3,
        "nightlife": 3,
        "budget": 3,
        "region_filter": "NonExistentRegion999"
    }
    response = client.post("/api/recommendations", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "recommendations" in data
    assert len(data["recommendations"]) == 0

def test_recommendations_explainability_integrity(client):
    payload = {
        "adventure": 5,
        "relaxation": 1,
        "family": 1,
        "food": 5,
        "heritage": 5,
        "nightlife": 1,
        "budget": 1
    }
    response = client.post("/api/recommendations?top_n=2", json=payload)
    assert response.status_code == 200
    data = response.json()
    for rec in data["recommendations"]:
        assert isinstance(rec["top_matches"], list)
        assert len(rec["top_matches"]) > 0
        assert isinstance(rec["trade_offs"], list)
        assert len(rec["trade_offs"]) > 0
        assert isinstance(rec["explanation"], str)
        assert len(rec["explanation"]) > 10
