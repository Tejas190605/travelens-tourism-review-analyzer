from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.db.database import get_db
from app.db.models import User, Destination, SavedDestination, Review
from app.api.auth import get_current_user, security_scheme
from app.core.security import decode_access_token
from app.schemas.saved_destinations import SavedDestinationOut, SavedStatusResponse
from app.schemas.destination import DestinationOut

router = APIRouter(prefix="/saved-destinations", tags=["Saved Destinations"])

@router.get("", response_model=List[SavedDestinationOut])
def get_user_saved_destinations(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Retrieves all bookmarked destinations for the authenticated traveller with aggregated ratings."""
    saved = db.query(SavedDestination).filter(SavedDestination.user_id == current_user.id).all()
    result = []
    for item in saved:
        d = item.destination
        rev_stats = db.query(
            func.count(Review.id).label("count"),
            func.avg(Review.rating).label("avg_rating")
        ).filter(Review.destination_id == d.id).first()

        total_reviews = rev_stats.count if rev_stats and rev_stats.count else 0
        avg_rating = round(float(rev_stats.avg_rating), 1) if rev_stats and rev_stats.avg_rating else 0.0

        dest_out = DestinationOut(
            id=d.id,
            name=d.name,
            country=d.country,
            state_or_region=d.state_or_region,
            region=d.region,
            category=d.category,
            description=d.description,
            image_url=d.image_url,
            attractions=d.attractions,
            activities=d.activities,
            recommended_duration=d.recommended_duration,
            best_season=d.best_season,
            transport_info=d.transport_info,
            budget_tier=d.budget_tier,
            indicative_daily_budget=d.indicative_daily_budget,
            practical_tips=d.practical_tips,
            suggested_itinerary=d.suggested_itinerary,
            created_at=d.created_at,
            total_reviews=total_reviews,
            average_rating=avg_rating
        )
        result.append(SavedDestinationOut(
            id=item.id,
            user_id=item.user_id,
            destination_id=item.destination_id,
            created_at=item.created_at,
            destination=dest_out
        ))
    return result

@router.post("/{destination_id}", response_model=SavedStatusResponse, status_code=status.HTTP_201_CREATED)
def save_destination(
    destination_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Bookmarks a destination to the user's travel shortlist."""
    dest = db.query(Destination).filter(Destination.id == destination_id).first()
    if not dest:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Destination with ID {destination_id} not found"
        )

    existing = db.query(SavedDestination).filter(
        SavedDestination.user_id == current_user.id,
        SavedDestination.destination_id == destination_id
    ).first()

    if not existing:
        new_saved = SavedDestination(user_id=current_user.id, destination_id=destination_id)
        db.add(new_saved)
        db.commit()

    return {"destination_id": destination_id, "is_saved": True}

@router.delete("/{destination_id}", response_model=SavedStatusResponse)
def remove_saved_destination(
    destination_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Removes a destination from the user's saved travel shortlist."""
    record = db.query(SavedDestination).filter(
        SavedDestination.user_id == current_user.id,
        SavedDestination.destination_id == destination_id
    ).first()

    if record:
        db.delete(record)
        db.commit()

    return {"destination_id": destination_id, "is_saved": False}

@router.get("/{destination_id}/status", response_model=SavedStatusResponse)
def get_saved_status(
    destination_id: int,
    db: Session = Depends(get_db),
    credentials = Depends(security_scheme)
):
    """Checks if a destination is currently saved by the visitor (handles optional auth)."""
    if not credentials:
        return {"destination_id": destination_id, "is_saved": False}

    payload = decode_access_token(credentials.credentials)
    if not payload or "sub" not in payload:
        return {"destination_id": destination_id, "is_saved": False}

    user = db.query(User).filter(User.email == payload["sub"]).first()
    if not user:
        return {"destination_id": destination_id, "is_saved": False}

    exists = db.query(SavedDestination).filter(
        SavedDestination.user_id == user.id,
        SavedDestination.destination_id == destination_id
    ).first()

    return {"destination_id": destination_id, "is_saved": bool(exists)}
