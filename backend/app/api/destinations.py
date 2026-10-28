from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.db.database import get_db
from app.db.models import Destination, Review
from app.schemas.destination import DestinationOut

router = APIRouter(prefix="/destinations", tags=["Destinations"])

@router.get("", response_model=List[DestinationOut])
def list_destinations(
    query: Optional[str] = Query(None, description="Search by name, country, region or city"),
    category: Optional[str] = Query(None, description="Filter by category (Heritage, Nature, Coastal, etc.)"),
    region: Optional[str] = Query(None, description="Filter by region (India, Europe, Asia, Americas, Africa, etc.)"),
    budget_tier: Optional[str] = Query(None, description="Filter by budget tier (Budget, Moderate, Luxury)"),
    sort_by: Optional[str] = Query(None, description="Sort results by rating, reviews, or name"),
    db: Session = Depends(get_db)
):
    q = db.query(Destination)

    if query:
        search = f"%{query}%"
        q = q.filter(
            (Destination.name.ilike(search)) |
            (Destination.country.ilike(search)) |
            (Destination.state_or_region.ilike(search)) |
            (Destination.region.ilike(search))
        )

    if category and category.lower() != "all":
        q = q.filter(Destination.category.ilike(category))

    if region and region.lower() != "all":
        q = q.filter(Destination.region.ilike(region))

    if budget_tier and budget_tier.lower() != "all":
        q = q.filter(Destination.budget_tier.ilike(budget_tier))

    destinations = q.all()

    # Enrich with review count and average rating
    result = []
    for d in destinations:
        rev_stats = db.query(
            func.count(Review.id).label("count"),
            func.avg(Review.rating).label("avg_rating")
        ).filter(Review.destination_id == d.id).first()

        total_reviews = rev_stats.count if rev_stats and rev_stats.count else 0
        avg_rating = round(float(rev_stats.avg_rating), 1) if rev_stats and rev_stats.avg_rating else 0.0

        dest_dict = {
            "id": d.id,
            "name": d.name,
            "country": d.country,
            "state_or_region": d.state_or_region,
            "region": d.region,
            "description": d.description,
            "category": d.category,
            "image_url": d.image_url,
            "attractions": d.attractions,
            "activities": d.activities,
            "recommended_duration": d.recommended_duration,
            "best_season": d.best_season,
            "transport_info": d.transport_info,
            "budget_tier": d.budget_tier,
            "indicative_daily_budget": d.indicative_daily_budget,
            "practical_tips": d.practical_tips,
            "suggested_itinerary": d.suggested_itinerary,
            "created_at": d.created_at,
            "total_reviews": total_reviews,
            "average_rating": avg_rating
        }
        result.append(DestinationOut(**dest_dict))

    # Apply sorting if requested
    if sort_by == "rating":
        result.sort(key=lambda x: (x.average_rating or 0, x.total_reviews or 0), reverse=True)
    elif sort_by == "reviews":
        result.sort(key=lambda x: (x.total_reviews or 0, x.average_rating or 0), reverse=True)
    elif sort_by == "name":
        result.sort(key=lambda x: x.name.lower())

    return result

@router.get("/{destination_id}", response_model=DestinationOut)
def get_destination(destination_id: int, db: Session = Depends(get_db)):
    destination = db.query(Destination).filter(Destination.id == destination_id).first()
    if not destination:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Destination with ID {destination_id} not found"
        )

    rev_stats = db.query(
        func.count(Review.id).label("count"),
        func.avg(Review.rating).label("avg_rating")
    ).filter(Review.destination_id == destination.id).first()

    total_reviews = rev_stats.count if rev_stats and rev_stats.count else 0
    avg_rating = round(float(rev_stats.avg_rating), 1) if rev_stats and rev_stats.avg_rating else 0.0

    return DestinationOut(
        id=destination.id,
        name=destination.name,
        country=destination.country,
        state_or_region=destination.state_or_region,
        region=destination.region,
        description=destination.description,
        category=destination.category,
        image_url=destination.image_url,
        attractions=destination.attractions,
        activities=destination.activities,
        recommended_duration=destination.recommended_duration,
        best_season=destination.best_season,
        transport_info=destination.transport_info,
        budget_tier=destination.budget_tier,
        indicative_daily_budget=destination.indicative_daily_budget,
        practical_tips=destination.practical_tips,
        suggested_itinerary=destination.suggested_itinerary,
        created_at=destination.created_at,
        total_reviews=total_reviews,
        average_rating=avg_rating
    )
