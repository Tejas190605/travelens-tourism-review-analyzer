def test_analyze_review_api_endpoint(client):
    payload = {
        "review_text": "The beach was beautiful but the area was extremely crowded."
    }
    response = client.post("/api/analyze-review", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "raw_text" in data
    assert "cleaned_text" in data
    assert "sentiment" in data
    assert "confidence" in data
    assert "probabilities" in data
    assert "detected_aspects" in data
    assert "extracted_keywords" in data
    assert "latency_ms" in data
    assert isinstance(data["latency_ms"], float)

    # Check aspects
    aspects = {a["aspect"]: a["sentiment"] for a in data["detected_aspects"]}
    assert "Attractions" in aspects
    assert aspects["Attractions"] == "positive"
    assert "Crowd" in aspects
    assert aspects["Crowd"] == "negative"

def test_analyze_review_empty_payload(client):
    response = client.post("/api/analyze-review", json={"review_text": ""})
    assert response.status_code == 422

def test_get_model_metrics_api(client):
    response = client.get("/api/analysis/model-metrics")
    assert response.status_code == 200
    data = response.json()
    assert "model_architecture" in data
    assert "accuracy" in data
    assert "macro_f1" in data or "f1_score_macro" in data
    assert "confusion_matrix" in data
    assert "total_sample_count" in data
    assert data["total_sample_count"] >= 6000
    assert "baseline_comparison" in data
    assert "dataset_quality" in data
