from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, ConfigDict

class DestinationBase(BaseModel):
    name: str
    country: str
    state_or_region: Optional[str] = None
    region: Optional[str] = None
    description: str
    category: str
    image_url: Optional[str] = None
    attractions: Optional[str] = None
    activities: Optional[str] = None
    recommended_duration: Optional[str] = None
    best_season: Optional[str] = None
    transport_info: Optional[str] = None
    budget_tier: Optional[str] = None
    indicative_daily_budget: Optional[str] = None
    practical_tips: Optional[str] = None
    suggested_itinerary: Optional[str] = None

class DestinationCreate(DestinationBase):
    pass

class DestinationOut(DestinationBase):
    id: int
    created_at: datetime
    total_reviews: Optional[int] = 0
    average_rating: Optional[float] = 0.0

    model_config = ConfigDict(from_attributes=True)
