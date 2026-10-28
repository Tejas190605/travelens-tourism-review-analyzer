def test_destination_analytics_calculation(client):
    response = client.get("/api/destinations/1/analytics")
    assert response.status_code == 200
    data = response.json()
    assert data["destination_id"] == 1
    assert data["destination"] == "Jaipur"
    assert "review_count" in data
    assert data["review_count"] >= 3
    assert "average_rating" in data
    assert isinstance(data["average_rating"], float)

    # Sentiment percentages sum to approximately 100%
    sent = data["sentiment"]
    assert "positive" in sent
    assert "neutral" in sent
    assert "negative" in sent
    total_pct = sent["positive"] + sent["neutral"] + sent["negative"]
    assert 99.0 <= total_pct <= 101.0

    # Aspect calculations
    aspects = data["aspects"]
    assert "Attractions" in aspects
    assert "Food" in aspects
    assert "Cleanliness" in aspects
    food_asp = aspects["Food"]
    assert "mention_count" in food_asp
    assert "aspect_score" in food_asp
    assert 0.0 <= food_asp["aspect_score"] <= 100.0

def test_destination_sentiment_trend_endpoint(client):
    response = client.get("/api/destinations/1/trends")
    assert response.status_code == 200
    data = response.json()
    assert data["destination_id"] == 1
    assert data["trend_available"] is True
    assert "monthly_trends" in data
    assert len(data["monthly_trends"]) > 0
    first_month = data["monthly_trends"][0]
    assert "month" in first_month
    assert "positive_pct" in first_month
    assert "neutral_pct" in first_month
    assert "negative_pct" in first_month

def test_destination_keywords_endpoint(client):
    response = client.get("/api/destinations/1/keywords?top_n=5")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    first_kw = data[0]
    assert "keyword" in first_kw
    assert "score" in first_kw
    assert "frequency" in first_kw

def test_destination_analytics_not_found(client):
    response = client.get("/api/destinations/999999/analytics")
    assert response.status_code == 404
