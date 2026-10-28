from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Float,
    DateTime,
    ForeignKey,
    CheckConstraint,
    func
)
from sqlalchemy.orm import relationship
from app.db.database import Base

ALLOWED_ASPECTS = [
    "Attractions",
    "Food",
    "Cleanliness",
    "Price",
    "Crowd",
    "Safety",
    "Transport",
    "Accommodation",
    "Hospitality"
]

PREFERENCE_CATEGORIES = [
    "Adventure",
    "Relaxation",
    "Family",
    "Food",
    "Heritage",
    "Nightlife",
    "Budget"
]

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), default="user", nullable=False)  # "user" | "admin"
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    preferences = relationship("UserPreference", back_populates="user", cascade="all, delete-orphan")
    saved_destinations = relationship("SavedDestination", back_populates="user", cascade="all, delete-orphan")


class Destination(Base):
    __tablename__ = "destinations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), index=True, nullable=False)
    country = Column(String(100), index=True, nullable=False)
    state_or_region = Column(String(100), nullable=True)
    region = Column(String(50), index=True, nullable=True)  # e.g. "India", "Europe", "Asia", "Americas", "Africa", "Oceania", "Middle East"
    description = Column(Text, nullable=False)
    category = Column(String(50), index=True, nullable=False)
    image_url = Column(String(500), nullable=True)
    
    # Rich Travel Guide Attributes
    attractions = Column(Text, nullable=True)  # JSON or comma-separated list of top attractions
    activities = Column(Text, nullable=True)   # JSON or comma-separated list of top experiences
    recommended_duration = Column(String(50), nullable=True)  # e.g. "3-4 days"
    best_season = Column(String(100), nullable=True)          # e.g. "October to March"
    transport_info = Column(Text, nullable=True)              # Nearest airport, train, local transit options
    budget_tier = Column(String(30), index=True, nullable=True)  # "Budget" | "Moderate" | "Luxury"
    indicative_daily_budget = Column(String(100), nullable=True)  # e.g. "$40 - $70 / ₹3,500 - ₹6,000"
    practical_tips = Column(Text, nullable=True)              # Safety, clothing, permits, local customs advice
    suggested_itinerary = Column(Text, nullable=True)         # Day-by-day suggested plan
    
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    reviews = relationship("Review", back_populates="destination", cascade="all, delete-orphan")


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    destination_id = Column(Integer, ForeignKey("destinations.id", ondelete="CASCADE"), nullable=False, index=True)
    review_text = Column(Text, nullable=False)
    rating = Column(Integer, nullable=False)
    review_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    # Sentiment Fields
    sentiment = Column(String(20), nullable=False)  # Canonical review sentiment ("positive", "neutral", "negative") derived from rating
    predicted_sentiment = Column(String(20), nullable=True)  # Model text prediction ("positive", "neutral", "negative")
    prediction_confidence = Column(Float, nullable=True)     # Confidence of model prediction (0.0 - 1.0)
    is_mixed = Column(Integer, default=0, nullable=False)    # 1 if review contains contrasting aspect polarities, else 0
    data_source = Column(String(50), default="curated_demonstration_corpus", nullable=False)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    __table_args__ = (
        CheckConstraint("rating >= 1 AND rating <= 5", name="check_rating_range"),
    )

    @property
    def rating_sentiment(self) -> str:
        """Derives ground-truth polarity directly from traveler star rating."""
        if self.rating >= 4:
            return "positive"
        elif self.rating == 3:
            return "neutral"
        else:
            return "negative"

    destination = relationship("Destination", back_populates="reviews")
    aspects = relationship("ReviewAspect", back_populates="review", cascade="all, delete-orphan")


class ReviewAspect(Base):
    __tablename__ = "review_aspects"

    id = Column(Integer, primary_key=True, index=True)
    review_id = Column(Integer, ForeignKey("reviews.id", ondelete="CASCADE"), nullable=False, index=True)
    aspect = Column(String(50), index=True, nullable=False)
    sentiment = Column(String(20), nullable=False)  # "positive", "neutral", "negative"
    score = Column(Float, default=1.0, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    review = relationship("Review", back_populates="aspects")


class UserPreference(Base):
    __tablename__ = "user_preferences"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    category = Column(String(50), nullable=False)
    weight = Column(Float, default=1.0, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    user = relationship("User", back_populates="preferences")


class SavedDestination(Base):
    __tablename__ = "saved_destinations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    destination_id = Column(Integer, ForeignKey("destinations.id", ondelete="CASCADE"), nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    user = relationship("User", back_populates="saved_destinations")
    destination = relationship("Destination")


class IssueReport(Base):
    __tablename__ = "issue_reports"

    id = Column(Integer, primary_key=True, index=True)
    destination_id = Column(Integer, ForeignKey("destinations.id", ondelete="CASCADE"), nullable=False, index=True)
    issue_type = Column(String(100), nullable=False)
    comment = Column(String(1000), nullable=True)
    contact_email = Column(String(255), nullable=True)
    status = Column(String(20), default="open", nullable=False)  # "open" | "resolved" | "dismissed"
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    destination = relationship("Destination")

