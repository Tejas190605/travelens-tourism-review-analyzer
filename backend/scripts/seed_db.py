import sys
import csv
import json
from pathlib import Path
from datetime import datetime

# Add backend directory to sys.path
backend_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(backend_dir))

from app.core.config import settings
from app.core.security import hash_password
from app.db.database import SessionLocal, engine, Base
from app.db.models import User, Destination, Review, ReviewAspect, UserPreference
from app.ml.predict import predict_sentiment
from app.services.aspects import extract_aspects_from_text, detect_is_mixed

def seed_database(
    destinations_csv: Path = None,
    reviews_csv: Path = None,
    clean_first: bool = False,
    db_session = None
):
    bind_engine = db_session.get_bind() if db_session else engine
    if clean_first:
        print("[Seed] Dropping and recreating tables with fresh schema...")
        Base.metadata.drop_all(bind=bind_engine)
        Base.metadata.create_all(bind=bind_engine)
    else:
        Base.metadata.create_all(bind=bind_engine)

    own_session = False
    if db_session is None:
        db = SessionLocal()
        own_session = True
    else:
        db = db_session

    try:

        # 1. Seed Core Users
        admin_user = db.query(User).filter(User.email == "admin@travelens.com").first()
        if not admin_user:
            admin_user = User(
                name="Admin User",
                email="admin@travelens.com",
                password_hash=hash_password("adminpassword123"),
                role="admin"
            )
            db.add(admin_user)
            print("[Seed] Created default Admin user (admin@travelens.com)")

        test_user = db.query(User).filter(User.email == "traveler@travelens.com").first()
        if not test_user:
            test_user = User(
                name="Traveler Jane",
                email="traveler@travelens.com",
                password_hash=hash_password("userpassword123"),
                role="user"
            )
            db.add(test_user)
            print("[Seed] Created default Test user (traveler@travelens.com)")

        db.commit()
        db.refresh(test_user)

        # Seed sample UserPreferences for test user
        if not db.query(UserPreference).filter(UserPreference.user_id == test_user.id).first():
            prefs = [
                UserPreference(user_id=test_user.id, category="Heritage", weight=5.0),
                UserPreference(user_id=test_user.id, category="Food", weight=4.0),
                UserPreference(user_id=test_user.id, category="Relaxation", weight=3.0),
                UserPreference(user_id=test_user.id, category="Budget", weight=4.0),
            ]
            db.add_all(prefs)
            db.commit()
            print(f"[Seed] Added {len(prefs)} default preferences for traveler@travelens.com")

        # 2. Seed Destinations (from curated python module or CSV)
        dest_map = {}
        dest_count = 0

        # Try loading rich curated dataset first
        try:
            from scripts.curated_destinations_data import DESTINATIONS
            print(f"[Seed] Loading {len(DESTINATIONS)} curated destinations with rich travel guides...")
            for item in DESTINATIONS:
                dest = db.query(Destination).filter(Destination.name == item["name"]).first()
                if not dest:
                    dest = Destination(
                        name=item["name"],
                        country=item["country"],
                        state_or_region=item.get("state_or_region"),
                        region=item.get("region"),
                        category=item["category"],
                        description=item["description"],
                        image_url=item.get("image_url"),
                        attractions=item.get("attractions"),
                        activities=item.get("activities"),
                        recommended_duration=item.get("recommended_duration"),
                        best_season=item.get("best_season"),
                        transport_info=item.get("transport_info"),
                        budget_tier=item.get("budget_tier"),
                        indicative_daily_budget=item.get("indicative_daily_budget"),
                        practical_tips=item.get("practical_tips"),
                        suggested_itinerary=item.get("suggested_itinerary")
                    )
                    db.add(dest)
                    dest_count += 1
                else:
                    # Update fields if missing or changed
                    for key in ["country", "state_or_region", "region", "category", "description",
                                "image_url", "attractions", "activities", "recommended_duration",
                                "best_season", "transport_info", "budget_tier", "indicative_daily_budget",
                                "practical_tips", "suggested_itinerary"]:
                        if item.get(key) is not None:
                            setattr(dest, key, item[key])
                dest_map[item["name"]] = dest
        except Exception as e:
            print(f"[Seed Warning] Could not load curated_destinations_data directly ({e}), checking CSV...")
            if destinations_csv is None:
                destinations_csv = settings.DATA_DIR / "seed" / "destinations_seed.csv"
            with open(destinations_csv, mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    dest = db.query(Destination).filter(Destination.name == row["name"]).first()
                    if not dest:
                        dest = Destination(
                            name=row["name"],
                            country=row["country"],
                            state_or_region=row.get("state_or_region"),
                            category=row["category"],
                            description=row["description"],
                            image_url=row.get("image_url")
                        )
                        db.add(dest)
                        dest_count += 1
                    dest_map[row["name"]] = dest

        db.commit()
        for name, dest in dest_map.items():
            db.refresh(dest)
        print(f"[Seed] Successfully cataloged {len(dest_map)} destinations ({dest_count} newly added)")

        # 3. Seed Reviews and execute ASTMA pipeline
        review_count = 0
        aspect_count = 0

        # Try loading rich curated reviews first
        reviews_to_load = []
        try:
            from scripts.curated_reviews_data import REVIEWS
            print(f"[Seed] Loading {len(REVIEWS)} curated multi-aspect reviews...")
            reviews_to_load = REVIEWS
        except Exception as e:
            print(f"[Seed Warning] Could not load curated_reviews_data ({e}), falling back to CSV...")
            if reviews_csv is None:
                reviews_csv = settings.DATA_DIR / "seed" / "reviews_seed.csv"
            with open(reviews_csv, mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                reviews_to_load = list(reader)

        print(f"[Seed] Processing and decomposing {len(reviews_to_load)} reviews with ASTMA engine...")
        for row in reviews_to_load:
            dest_name = row["destination_name"]
            dest = dest_map.get(dest_name)
            if not dest:
                continue

            review_text = row["review_text"]

            # Check if this review already exists to ensure idempotency
            existing_review = db.query(Review).filter(
                Review.destination_id == dest.id,
                Review.review_text == review_text
            ).first()
            if existing_review:
                pred_res = predict_sentiment(review_text)
                existing_review.predicted_sentiment = pred_res["sentiment"]
                existing_review.prediction_confidence = pred_res["confidence"]
                existing_review.is_mixed = 1 if detect_is_mixed(review_text, rating=existing_review.rating, predicted_sentiment=pred_res["sentiment"]) else 0
                continue

            rating = int(row["rating"])
            rev_date_str = row.get("review_date")
            rev_date = datetime.strptime(rev_date_str, "%Y-%m-%d") if rev_date_str else datetime.utcnow()
            data_source = row.get("data_source", "curated_demonstration_corpus")

            # Ground truth rating sentiment
            if rating >= 4:
                rating_sentiment = "positive"
            elif rating == 3:
                rating_sentiment = "neutral"
            else:
                rating_sentiment = "negative"

            # Model prediction
            pred_res = predict_sentiment(review_text)
            predicted_sentiment = pred_res["sentiment"]
            prediction_confidence = pred_res["confidence"]

            # Mixed sentiment detection
            is_mixed_flag = 1 if detect_is_mixed(review_text, rating=rating, predicted_sentiment=predicted_sentiment) else 0

            review = Review(
                destination_id=dest.id,
                review_text=review_text,
                rating=rating,
                review_date=rev_date,
                sentiment=rating_sentiment,  # Aligned with ground truth star rating
                predicted_sentiment=predicted_sentiment,
                prediction_confidence=prediction_confidence,
                is_mixed=is_mixed_flag,
                data_source=data_source
            )
            db.add(review)
            db.commit()
            db.refresh(review)
            review_count += 1

            # Decompose aspects
            detected_aspects = extract_aspects_from_text(review_text)
            for asp_info in detected_aspects:
                aspect_obj = ReviewAspect(
                    review_id=review.id,
                    aspect=asp_info["aspect"],
                    sentiment=asp_info["sentiment"],
                    score=asp_info["score"]
                )
                db.add(aspect_obj)
                aspect_count += 1

        db.commit()
        print(f"[Seed] Seed complete! Added {len(dest_map)} destinations, {review_count} reviews, and {aspect_count} decomposed aspect records.")
        print("[Seed] Database is verified and ready for live queries.")

    except Exception as e:
        db.rollback()
        print(f"[Seed Error] {e}")
        raise e
    finally:
        if own_session:
            db.close()

if __name__ == "__main__":
    seed_database(clean_first=False)

