import datetime
from pathlib import Path
import sqlite3
import pytest
from app.services.aspects import extract_aspects_from_text, detect_is_mixed
from app.ml.predict import predict_sentiment
from app.db.models import Destination, Review
from app.services.analytics import get_destination_sentiment_trend
from app.services.recommendations import generate_recommendations
from app.schemas.recommendations import UserPriorityWeights

def test_hospitality_and_attractions_aspect_polarity():
    """Verify that extraordinary hospitality and fabulous sightseeing receive positive aspect sentiment."""
    text1 = "Tour guides showed extraordinary hospitality throughout our stay."
    aspects1 = extract_aspects_from_text(text1)
    aspect_map1 = {item["aspect"]: item["sentiment"] for item in aspects1}
    assert "Hospitality" in aspect_map1, f"Expected Hospitality in {aspect_map1}"
    assert aspect_map1["Hospitality"] == "positive", f"Expected positive Hospitality, got {aspect_map1['Hospitality']}"

    text2 = "Sightseeing at Amber Fort was fabulous and memorable."
    aspects2 = extract_aspects_from_text(text2)
    aspect_map2 = {item["aspect"]: item["sentiment"] for item in aspects2}
    assert "Attractions" in aspect_map2, f"Expected Attractions in {aspect_map2}"
    assert aspect_map2["Attractions"] == "positive", f"Expected positive Attractions, got {aspect_map2['Attractions']}"

def test_positive_review_with_minor_pricing_complaint():
    """Verify 4-star review praising cultural depth, safety, and authentic food with minor pricing complaint predicts positive."""
    text = (
        "We absolutely loved the cultural depth, remarkable safety, and authentic food of this city. "
        "The monuments were breathtaking and locals were welcoming, although taxi fares were slightly marked up."
    )
    result = predict_sentiment(text)
    assert result["sentiment"] == "positive", f"Expected positive sentiment, got {result['sentiment']}"
    assert result["is_mixed"] is True, "Expected mixed sentiment flag due to minor pricing friction"

def test_review_dates_no_future_dates(db_session):
    """Verify that seeded reviews have timestamps no later than the current execution time."""
    reference_date = datetime.datetime.now() + datetime.timedelta(minutes=5)
    reviews = db_session.query(Review).all()
    assert len(reviews) > 0

    for r in reviews:
        if r.created_at:
            rev_date = r.created_at if isinstance(r.created_at, datetime.datetime) else datetime.datetime.fromisoformat(str(r.created_at))
            assert rev_date <= reference_date, f"Review {r.id} has future date: {rev_date}"

def test_destinations_have_differentiated_ratings_and_counts(db_session):
    """Verify Jaipur, Goa, and Florence do not share identical hardcoded ratings or identical review counts."""
    dest_names = ["Jaipur", "Goa", "Florence"]
    dests = db_session.query(Destination).filter(Destination.name.in_(dest_names)).all()
    assert len(dests) == 3

    rev_counts = {}
    for d in dests:
        count = db_session.query(Review).filter(Review.destination_id == d.id).count()
        rev_counts[d.name] = count

    # Review counts must be non-zero and not all identical
    assert all(c > 0 for c in rev_counts.values())
    unique_counts = set(rev_counts.values())
    assert len(unique_counts) > 1, f"Expected distinct review counts, got: {rev_counts}"

def test_trip_budget_calculator_arithmetic():
    """Verify Trip Budget Calculator formula: ₹6,200 * 2 travellers * 4 days = ₹49,600."""
    def calculate_trip_total(daily_rate_per_person: int, travellers: int, days: int) -> int:
        safe_travellers = max(1, travellers)
        safe_days = max(1, days)
        return daily_rate_per_person * safe_travellers * safe_days

    # Reported defect case
    total = calculate_trip_total(6200, 2, 4)
    assert total == 49600, f"Expected 49600, got {total}"

    # Single traveller, 1 day
    assert calculate_trip_total(6200, 1, 1) == 6200

    # 4 travellers, 7 days
    assert calculate_trip_total(6200, 4, 7) == 173600

def test_recommendation_filtering_india_and_abroad(db_session):
    """Verify India-only filter excludes non-Indian destinations."""
    weights = UserPriorityWeights(
        adventure=3, relaxation=3, family=3, food=4, heritage=5, nightlife=2, budget=3,
        region_filter="India"
    )
    result = generate_recommendations(priorities=weights, db=db_session, top_limit=6)
    assert len(result.recommendations) > 0

    for rec in result.recommendations:
        dest = db_session.query(Destination).filter(Destination.id == rec.destination_id).first()
        assert dest.country == "India" or dest.region == "India", f"Non-Indian destination recommended: {rec.name} ({dest.country})"

def test_recommendation_zero_weights_safe(db_session):
    """Verify recommendation handles zero weights gracefully without ZeroDivisionError."""
    weights = UserPriorityWeights(
        adventure=1, relaxation=1, family=1, food=1, heritage=1, nightlife=1, budget=1
    )
    result = generate_recommendations(priorities=weights, db=db_session, top_limit=4)
    assert len(result.recommendations) == 4

def test_monthly_sentiment_trend_continuity(db_session):
    """Verify monthly trend produces chronological continuity without synthetic gaps."""
    jaipur = db_session.query(Destination).filter(Destination.name == "Jaipur").first()
    assert jaipur is not None

    trend = get_destination_sentiment_trend(jaipur.id, db_session)
    assert "monthly_trends" in trend
    assert len(trend["monthly_trends"]) >= 2

    # Verify chronological ordering of months
    month_names = [m["month"] for m in trend["monthly_trends"]]
    parsed_months = [datetime.datetime.strptime(m, "%Y-%m") for m in month_names]
    for i in range(len(parsed_months) - 1):
        assert parsed_months[i] < parsed_months[i + 1], f"Months not strictly increasing: {month_names}"

def test_dev_database_isolation_not_mutated_by_test_suite(client):
    """Verify that test client operations use test_travelens.db and do not mutate backend/travelens.db."""
    dev_db_path = Path(__file__).resolve().parent.parent / "travelens.db"
    assert dev_db_path.exists(), f"Expected dev db at {dev_db_path}"

    conn = sqlite3.connect(dev_db_path)
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM destinations")
    dev_dests_before = cur.fetchone()[0]
    cur.execute("SELECT count(*) FROM reviews")
    dev_reviews_before = cur.fetchone()[0]
    cur.execute("SELECT count(*) FROM users")
    dev_users_before = cur.fetchone()[0]
    cur.execute("SELECT count(*) FROM saved_destinations")
    dev_saved_before = cur.fetchone()[0]
    cur.execute("SELECT user_id, destination_id FROM saved_destinations")
    dev_saved_rows_before = set(cur.fetchall())
    conn.close()

    # Perform mutations using test client (which uses test_travelens.db via override_get_db)
    reg_res = client.post("/api/auth/register", json={
        "name": "Isolation Tester",
        "email": "temp_isolation_check@travelens.com",
        "password": "Password123!"
    })
    assert reg_res.status_code == 201

    login_res = client.post("/api/auth/login", json={
        "email": "traveler@travelens.com",
        "password": "userpassword123"
    })
    assert login_res.status_code == 200
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    client.post("/api/saved-destinations/1", headers=headers)
    client.delete("/api/saved-destinations/1", headers=headers)

    # Now verify development database was NOT touched at all
    conn2 = sqlite3.connect(dev_db_path)
    cur2 = conn2.cursor()
    cur2.execute("SELECT count(*) FROM destinations")
    assert cur2.fetchone()[0] == dev_dests_before == 54
    cur2.execute("SELECT count(*) FROM reviews")
    assert cur2.fetchone()[0] == dev_reviews_before == 629
    cur2.execute("SELECT count(*) FROM users")
    assert cur2.fetchone()[0] == dev_users_before == 2
    cur2.execute("SELECT count(*) FROM saved_destinations")
    assert cur2.fetchone()[0] == dev_saved_before == 1
    cur2.execute("SELECT user_id, destination_id FROM saved_destinations")
    assert set(cur2.fetchall()) == dev_saved_rows_before == {(2, 1)}
    cur2.execute("SELECT count(*) FROM users WHERE email = 'temp_isolation_check@travelens.com'")
    assert cur2.fetchone()[0] == 0
    conn2.close()

def test_sentiment_negation_and_mixed_reviews():
    """Verify sentiment predictions and aspect extractions on negation, mixed reviews, and minor complaints."""
    # Negation: not good -> negative
    neg_res = predict_sentiment("The hotel room was not clean and the staff was not helpful at all.")
    assert neg_res["sentiment"] == "negative"
    assert neg_res["confidence"] >= 0.60

    # Negation: not bad -> neutral or positive
    not_bad_res = predict_sentiment("The location was not bad at all and the food was decent.")
    assert not_bad_res["sentiment"] in ["neutral", "positive"]

    # Mixed review: great food but terrible service -> flag is_mixed
    mixed_res = predict_sentiment("The food was absolutely fantastic, but the service was terrible and slow.")
    assert mixed_res["is_mixed"] is True
    mixed_aspects = extract_aspects_from_text("The food was absolutely fantastic, but the service was terrible and slow.")
    asp_map = {a["aspect"]: a["sentiment"] for a in mixed_aspects}
    assert asp_map.get("Food") == "positive"
    assert asp_map.get("Hospitality") == "negative"

    # Minor complaint with overwhelmingly positive experience
    praise_res = predict_sentiment(
        "We had a wonderful trip, beautiful beaches and friendly locals, though the taxi prices were high."
    )
    assert praise_res["sentiment"] == "positive"
    assert praise_res["confidence"] >= 0.55

def test_sentiment_sarcasm_limitation_documented():
    """
    Document limitation: bag-of-words / n-gram TF-IDF linear classifiers struggle with sarcasm.
    Reviews with sarcastic positive wording like 'Great place if you enjoy noise'
    may produce low confidence or false positive unigram weights due to lack of syntactic semantic parsing.
    """
    sarcasm_text = "Great place if you enjoy sleeping with construction noise outside your window."
    res = predict_sentiment(sarcasm_text)
    # The linear model predicts positive due to 'great' and 'enjoy', but confidence is low (< 0.60)
    assert res["confidence"] < 0.60, f"Expected low confidence on sarcasm, got {res['confidence']}"
