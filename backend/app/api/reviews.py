from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session, joinedload

from app.db.database import get_db
from app.db.models import Destination, Review, ReviewAspect
from app.schemas.review import ReviewOut

router = APIRouter(tags=["Reviews"])

@router.get("/destinations/{destination_id}/reviews", response_model=List[ReviewOut])
def get_destination_reviews(
    destination_id: int,
    aspect: Optional[str] = Query(None, description="Filter by aspect (e.g. Cleanliness, Food)"),
    sentiment: Optional[str] = Query(None, description="Filter by sentiment (positive, neutral, negative)"),
    rating: Optional[int] = Query(None, ge=1, le=5, description="Filter by rating (1-5)"),
    db: Session = Depends(get_db)
):
    # Check if destination exists
    dest = db.query(Destination).filter(Destination.id == destination_id).first()
    if not dest:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Destination with ID {destination_id} not found"
        )

    q = db.query(Review).options(joinedload(Review.aspects)).filter(Review.destination_id == destination_id)

    if sentiment:
        q = q.filter(Review.sentiment == sentiment.lower())

    if rating is not None:
        q = q.filter(Review.rating == rating)

    reviews = q.all()

    if aspect:
        aspect_lower = aspect.lower()
        filtered_reviews = []
        for r in reviews:
            if any(asp.aspect.lower() == aspect_lower for asp in r.aspects):
                filtered_reviews.append(r)
        return filtered_reviews

    return reviews

@router.get("/reviews", response_model=List[ReviewOut])
def list_reviews(
    sentiment: Optional[str] = Query(None, description="Filter by sentiment"),
    rating: Optional[int] = Query(None, ge=1, le=5, description="Filter by rating (1-5)"),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db)
):
    q = db.query(Review).options(joinedload(Review.aspects))
    if sentiment:
        q = q.filter(Review.sentiment == sentiment.lower())
    if rating is not None:
        q = q.filter(Review.rating == rating)
    return q.limit(limit).all()
