from app.db.models import User, Destination, Review, ReviewAspect, UserPreference
from app.core.security import hash_password

def test_database_user_creation_and_cascade(db_session):
    # Test User
    user = User(
        name="Test Traveler",
        email="cascade_test@travelens.com",
        password_hash=hash_password("securepassword"),
        role="user"
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    assert user.id is not None

    # Add Preference
    pref = UserPreference(user_id=user.id, category="Food", weight=5.0)
    db_session.add(pref)
    db_session.commit()
    assert pref.id is not None

    # Verify relationship
    assert len(user.preferences) == 1

def test_destination_review_cascade(db_session):
    # Create destination
    dest = Destination(
        name="Test Island",
        country="Test Country",
        category="Coastal",
        description="A beautiful test island"
    )
    db_session.add(dest)
    db_session.commit()
    db_session.refresh(dest)

    # Create review
    review = Review(
        destination_id=dest.id,
        review_text="Amazing beach and fresh seafood but expensive hotel.",
        rating=4,
        sentiment="positive"
    )
    db_session.add(review)
    db_session.commit()
    db_session.refresh(review)

    # Create aspect
    aspect = ReviewAspect(
        review_id=review.id,
        aspect="Food",
        sentiment="positive",
        score=1.0
    )
    db_session.add(aspect)
    db_session.commit()

    assert len(dest.reviews) >= 1
    assert len(review.aspects) >= 1
