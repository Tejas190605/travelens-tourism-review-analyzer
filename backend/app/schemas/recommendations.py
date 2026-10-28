from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field

class UserPriorityWeights(BaseModel):
    adventure: int = Field(3, ge=1, le=5, description="Priority for outdoor activities, scenery, and hiking")
    relaxation: int = Field(3, ge=1, le=5, description="Priority for quietness, serenity, and low crowd stress")
    family: int = Field(3, ge=1, le=5, description="Priority for safety, cleanliness, and accommodation comfort")
    food: int = Field(3, ge=1, le=5, description="Priority for culinary culture, dining, and eateries")
    heritage: int = Field(3, ge=1, le=5, description="Priority for historical landmarks, museums, and temples")
    nightlife: int = Field(3, ge=1, le=5, description="Priority for vibrant evening culture and dining")
    budget: int = Field(3, ge=1, le=5, description="Priority for affordability and good value for money")
    region_filter: Optional[str] = None
    budget_filter: Optional[str] = None

class DestinationRecommendation(BaseModel):
    destination_id: int
    name: str
    country: str
    state_or_region: Optional[str] = None
    category: str
    region: Optional[str] = None
    budget_tier: Optional[str] = None
    indicative_daily_budget: Optional[str] = None
    image_url: Optional[str] = None
    average_rating: float
    total_reviews: int
    match_percentage: float
    top_matches: List[str]
    trade_offs: List[str]
    explanation: str

class RecommendationResponse(BaseModel):
    priorities: Dict[str, Any]
    recommendations: List[DestinationRecommendation]
