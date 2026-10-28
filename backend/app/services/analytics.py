from typing import Dict, Any, List, Optional
from collections import defaultdict
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.db.models import Destination, Review, ReviewAspect, ALLOWED_ASPECTS

def get_destination_analytics(destination_id: int, db: Session) -> Dict[str, Any]:
    """
    Calculates empirical destination-level analytics directly from the database:
    overall review volume, average rating, sentiment distribution, and granular 9-aspect breakdown.
    """
    destination = db.query(Destination).filter(Destination.id == destination_id).first()
    if not destination:
        return {}

    reviews = db.query(Review).filter(Review.destination_id == destination_id).all()
    review_count = len(reviews)

    if review_count == 0:
        return {
            "destination_id": destination.id,
            "destination": destination.name,
            "review_count": 0,
            "average_rating": 0.0,
            "sentiment": {
                "positive": 0.0,
                "neutral": 0.0,
                "negative": 0.0
            },
            "aspects": {}
        }

    # Rating & Canonical Sentiment totals
    ratings = [r.rating for r in reviews if r.rating is not None]
    avg_rating = round(float(sum(ratings) / len(ratings)), 1) if ratings else 0.0

    pos_reviews = sum(1 for r in reviews if r.sentiment == "positive")
    neu_reviews = sum(1 for r in reviews if r.sentiment == "neutral")
    neg_reviews = sum(1 for r in reviews if r.sentiment == "negative")

    sentiment_dict = {
        "positive": round((pos_reviews / review_count) * 100, 1),
        "neutral": round((neu_reviews / review_count) * 100, 1),
        "negative": round((neg_reviews / review_count) * 100, 1)
    }

    # ASTMA ML Model Prediction Totals
    ml_pos = sum(1 for r in reviews if r.predicted_sentiment == "positive")
    ml_neu = sum(1 for r in reviews if r.predicted_sentiment == "neutral")
    ml_neg = sum(1 for r in reviews if r.predicted_sentiment == "negative")
    ml_total = ml_pos + ml_neu + ml_neg
    model_sentiment_dict = {
        "positive": round((ml_pos / ml_total) * 100, 1) if ml_total > 0 else 0.0,
        "neutral": round((ml_neu / ml_total) * 100, 1) if ml_total > 0 else 0.0,
        "negative": round((ml_neg / ml_total) * 100, 1) if ml_total > 0 else 0.0
    } if ml_total > 0 else None

    # Query all aspects associated with these reviews
    review_ids = [r.id for r in reviews]
    aspect_records = db.query(ReviewAspect).filter(ReviewAspect.review_id.in_(review_ids)).all()

    aspect_groups = defaultdict(lambda: {"pos": 0, "neu": 0, "neg": 0, "total": 0})
    for asp in aspect_records:
        asp_name = asp.aspect
        aspect_groups[asp_name]["total"] += 1
        if asp.sentiment == "positive":
            aspect_groups[asp_name]["pos"] += 1
        elif asp.sentiment == "negative":
            aspect_groups[asp_name]["neg"] += 1
        else:
            aspect_groups[asp_name]["neu"] += 1

    aspects_result = {}
    for asp_name in ALLOWED_ASPECTS:
        data = aspect_groups.get(asp_name, {"pos": 0, "neu": 0, "neg": 0, "total": 0})
        m_count = data["total"]
        if m_count > 0:
            pos_cnt = data["pos"]
            neu_cnt = data["neu"]
            neg_cnt = data["neg"]
            # ASTMA Aspect score formula (0 - 100):
            # score = ((pos + 0.5*neu) / total) * 100
            score = round(((pos_cnt + 0.5 * neu_cnt) / m_count) * 100, 1)
            aspects_result[asp_name] = {
                "mention_count": m_count,
                "positive_count": pos_cnt,
                "neutral_count": neu_cnt,
                "negative_count": neg_cnt,
                "sentiment": {
                    "positive_pct": round((pos_cnt / m_count) * 100, 1),
                    "neutral_pct": round((neu_cnt / m_count) * 100, 1),
                    "negative_pct": round((neg_cnt / m_count) * 100, 1)
                },
                "aspect_score": score
            }
        else:
            aspects_result[asp_name] = {
                "mention_count": 0,
                "positive_count": 0,
                "neutral_count": 0,
                "negative_count": 0,
                "sentiment": {"positive_pct": 0.0, "neutral_pct": 0.0, "negative_pct": 0.0},
                "aspect_score": None  # Insufficient data, never fabricate 50.0
            }

    return {
        "destination_id": destination.id,
        "destination": destination.name,
        "review_count": review_count,
        "average_rating": avg_rating,
        "sentiment": sentiment_dict,
        "model_sentiment": model_sentiment_dict,
        "aspects": aspects_result
    }

def get_destination_sentiment_trend(destination_id: int, db: Session) -> Dict[str, Any]:
    """
    Computes chronological monthly sentiment breakdown for a destination.
    Returns:
    {
       "destination_id": int,
       "destination": str,
       "trend_available": bool,
       "sample_size": int,
       "date_range": str,
       "monthly_trends": [{"month": "2026-03", "review_count": 5, "positive_pct": 80.0, ...}]
    }
    """
    destination = db.query(Destination).filter(Destination.id == destination_id).first()
    if not destination:
        return {"trend_available": False, "monthly_trends": []}

    reviews = db.query(Review).filter(
        Review.destination_id == destination_id,
        Review.review_date.isnot(None)
    ).order_by(Review.review_date.asc()).all()

    if not reviews:
        return {
            "destination_id": destination.id,
            "destination": destination.name,
            "trend_available": False,
            "message": "Trend analysis requires dated reviews",
            "sample_size": 0,
            "date_range": None,
            "monthly_trends": []
        }

    monthly_buckets = defaultdict(lambda: {"pos": 0, "neu": 0, "neg": 0, "total": 0})
    for r in reviews:
        month_key = r.review_date.strftime("%Y-%m")
        monthly_buckets[month_key]["total"] += 1
        if r.sentiment == "positive":
            monthly_buckets[month_key]["pos"] += 1
        elif r.sentiment == "negative":
            monthly_buckets[month_key]["neg"] += 1
        else:
            monthly_buckets[month_key]["neu"] += 1

    # Generate all calendar months between earliest and latest review date for proportional timeline
    min_date = reviews[0].review_date
    max_date = reviews[-1].review_date

    cur_year = min_date.year
    cur_month = min_date.month
    end_year = max_date.year
    end_month = max_date.month

    all_months = []
    while (cur_year < end_year) or (cur_year == end_year and cur_month <= end_month):
        all_months.append(f"{cur_year:04d}-{cur_month:02d}")
        cur_month += 1
        if cur_month > 12:
            cur_month = 1
            cur_year += 1

    trends = []
    for m in all_months:
        b = monthly_buckets.get(m, {"pos": 0, "neu": 0, "neg": 0, "total": 0})
        tot = b["total"]
        trends.append({
            "month": m,
            "review_count": tot,
            "positive_count": b["pos"],
            "neutral_count": b["neu"],
            "negative_count": b["neg"],
            "positive_pct": round((b["pos"] / tot) * 100, 1) if tot > 0 else 0.0,
            "neutral_pct": round((b["neu"] / tot) * 100, 1) if tot > 0 else 0.0,
            "negative_pct": round((b["neg"] / tot) * 100, 1) if tot > 0 else 0.0,
            "has_data": tot > 0
        })

    return {
        "destination_id": destination.id,
        "destination": destination.name,
        "trend_available": len(reviews) >= 2,
        "sample_size": len(reviews),
        "date_range": f"{all_months[0]} to {all_months[-1]}" if all_months else None,
        "monthly_trends": trends
    }
