def test_get_destination_reviews(client):
    response = client.get("/api/destinations/1/reviews")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    first = data[0]
    assert "review_text" in first
    assert "rating" in first
    assert "sentiment" in first
    assert "aspects" in first
    assert isinstance(first["aspects"], list)

def test_get_destination_reviews_filter_sentiment(client):
    response = client.get("/api/destinations/1/reviews?sentiment=positive")
    assert response.status_code == 200
    data = response.json()
    for rev in data:
        assert rev["sentiment"] == "positive"

def test_get_destination_reviews_filter_rating(client):
    response = client.get("/api/destinations/1/reviews?rating=4")
    assert response.status_code == 200
    data = response.json()
    for rev in data:
        assert rev["rating"] == 4

def test_get_destination_reviews_filter_aspect(client):
    response = client.get("/api/destinations/1/reviews?aspect=Cleanliness")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_get_destination_reviews_not_found_destination(client):
    response = client.get("/api/destinations/999999/reviews")
    assert response.status_code == 404

def test_list_all_reviews(client):
    response = client.get("/api/reviews?limit=10")
    assert response.status_code == 200
    data = response.json()
    assert len(data) <= 10

def test_list_all_reviews_filter_rating(client):
    response = client.get("/api/reviews?rating=5&limit=10")
    assert response.status_code == 200
    data = response.json()
    for rev in data:
        assert rev["rating"] == 5
