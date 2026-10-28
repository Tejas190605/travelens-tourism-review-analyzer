from app.ml.predict import predict_sentiment, map_confidence_to_band

def test_predict_sentiment_positive():
    text = "The historic architecture was magnificent and food was delicious!"
    result = predict_sentiment(text)
    assert result["sentiment"] in ["positive", "neutral", "negative"]
    assert "confidence" in result
    assert "confidence_band" in result
    assert result["confidence_band"] in ["High", "Moderate", "Low"]
    assert "probabilities" in result
    assert isinstance(result["confidence"], float)
    assert result["confidence"] > 0

def test_predict_sentiment_negative():
    text = "Terrible experience, filthy dirty hotel and aggressive pickpockets everywhere."
    result = predict_sentiment(text)
    assert result["sentiment"] == "negative"
    assert result["confidence"] >= 0.4
    assert result["confidence_band"] in ["High", "Moderate", "Low"]

def test_predict_sentiment_empty_string():
    result = predict_sentiment("")
    assert result["sentiment"] == "neutral"
    assert result["confidence_band"] == "Low"

def test_map_confidence_to_band_thresholds():
    # High: >= 0.75
    assert map_confidence_to_band(0.75) == "High"
    assert map_confidence_to_band(0.95) == "High"
    assert map_confidence_to_band(1.0) == "High"

    # Moderate: >= 0.55 and < 0.75
    assert map_confidence_to_band(0.7499) == "Moderate"
    assert map_confidence_to_band(0.55) == "Moderate"
    assert map_confidence_to_band(0.65) == "Moderate"

    # Low (indicative only): < 0.55
    assert map_confidence_to_band(0.5499) == "Low"
    assert map_confidence_to_band(0.33) == "Low"
    assert map_confidence_to_band(0.0) == "Low"

    # Missing / None / Invalid
    assert map_confidence_to_band(None) == "Low"
    assert map_confidence_to_band("invalid") == "Low"
