def test_get_destinations_list(client):
    response = client.get("/api/destinations")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 12
    # Verify field schema
    first = data[0]
    assert "id" in first
    assert "name" in first
    assert "country" in first
    assert "category" in first
    assert "total_reviews" in first
    assert "average_rating" in first

def test_get_destinations_search_filter(client):
    # Search for Kyoto
    response = client.get("/api/destinations?query=Kyoto")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert data[0]["name"] == "Kyoto"

def test_get_destinations_category_filter(client):
    response = client.get("/api/destinations?category=Heritage")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    for d in data:
        assert d["category"].lower() == "heritage"

def test_get_single_destination_success(client):
    response = client.get("/api/destinations/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "name" in data

def test_get_single_destination_not_found(client):
    response = client.get("/api/destinations/999999")
    assert response.status_code == 404
