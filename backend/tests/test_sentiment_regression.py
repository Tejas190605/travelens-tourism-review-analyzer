import pytest
from app.db.models import Destination, Review, ReviewAspect
from app.services.aspects import detect_is_mixed

def test_sentiment_no_high_star_negative_mismatch(db_session):
    """Verify that no reviews with rating 4 or 5 have sentiment='negative'."""
    mismatches = db_session.query(Review).filter(
        Review.rating >= 4,
        Review.sentiment == "negative"
    ).all()
    assert len(mismatches) == 0, f"Found {len(mismatches)} high-rating reviews labeled negative"

def test_sentiment_no_low_star_positive_mismatch(db_session):
    """Verify that no reviews with rating 1 or 2 have sentiment='positive'."""
    mismatches = db_session.query(Review).filter(
        Review.rating <= 2,
        Review.sentiment == "positive"
    ).all()
    assert len(mismatches) == 0, f"Found {len(mismatches)} low-rating reviews labeled positive"

def test_mixed_sentiment_detection_and_flagging(db_session):
    """Verify that mixed reviews are accurately flagged in the database and by detect_is_mixed."""
    mixed_reviews = db_session.query(Review).filter(Review.is_mixed == 1).all()
    assert len(mixed_reviews) > 0, "Expected mixed reviews to be identified in curated dataset"
    
    # Test helper directly
    test_mixed_text = "The scenery was absolutely breathtaking and magnificent, but the local transportation was terrible and overcrowded."
    assert detect_is_mixed(test_mixed_text, rating=3) is True
    
    test_pure_positive = "Everything was absolutely wonderful, beautiful, clean, and we loved every single moment!"
    assert detect_is_mixed(test_pure_positive, rating=5) is False

def test_destination_catalogue_counts_and_uniqueness(db_session):
    """Verify destination catalogue contains at least 50 destinations with unique image URLs."""
    destinations = db_session.query(Destination).filter(Destination.name != "Test Island").all()
    assert len(destinations) >= 50, f"Expected at least 50 destinations, found {len(destinations)}"
    
    image_urls = [d.image_url for d in destinations if d.image_url]
    assert len(image_urls) == len(destinations), "Every curated destination must have an image URL"
    assert len(image_urls) == len(set(image_urls)), "Image URLs must be unique across all destinations"

def test_destination_rich_fields_populated(db_session):
    """Verify that destinations have rich travel guide information populated."""
    sample = db_session.query(Destination).filter(Destination.name == "Jaipur").first()
    assert sample is not None
    assert sample.region == "India"
    assert sample.budget_tier is not None
    assert sample.attractions is not None
    assert sample.suggested_itinerary is not None
    assert sample.practical_tips is not None
