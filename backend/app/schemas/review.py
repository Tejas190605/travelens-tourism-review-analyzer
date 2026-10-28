from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict

class ReviewAspectOut(BaseModel):
    id: int
    aspect: str
    sentiment: str
    score: float
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class ReviewBase(BaseModel):
    destination_id: int
    review_text: str = Field(..., min_length=5)
    rating: int = Field(..., ge=1, le=5)

class ReviewCreate(ReviewBase):
    pass

class ReviewOut(ReviewBase):
    id: int
    review_date: datetime
    sentiment: Optional[str] = None
    rating_sentiment: Optional[str] = None
    predicted_sentiment: Optional[str] = None
    prediction_confidence: Optional[float] = None
    is_mixed: Optional[bool] = False
    data_source: Optional[str] = "curated_demonstration_corpus"
    created_at: datetime
    aspects: List[ReviewAspectOut] = []

    model_config = ConfigDict(from_attributes=True)
