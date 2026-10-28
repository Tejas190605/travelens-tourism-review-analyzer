from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field, ConfigDict

class AnalyzeReviewRequest(BaseModel):
    review_text: str = Field(..., min_length=5, max_length=5000, description="Raw review text to analyze")

class DetectedAspect(BaseModel):
    aspect: str
    sentiment: str
    score: float
    keywords: List[str] = []

class ExtractedKeyword(BaseModel):
    keyword: str
    score: float
    frequency: Optional[int] = None

class AnalyzeReviewResponse(BaseModel):
    raw_text: str
    cleaned_text: str
    sentiment: str
    confidence: float
    confidence_band: Optional[str] = "Moderate"
    probabilities: Dict[str, float]
    detected_aspects: List[DetectedAspect]
    extracted_keywords: List[ExtractedKeyword]
    clause_analysis: Optional[List[Dict[str, Any]]] = None
    is_mixed: Optional[bool] = False
    latency_ms: Optional[float] = None

class AspectDetail(BaseModel):
    mention_count: int
    positive_count: int
    neutral_count: int
    negative_count: int
    sentiment: Dict[str, float]
    aspect_score: Optional[float] = None

class DestinationAnalyticsResponse(BaseModel):
    destination_id: int
    destination: str
    review_count: int
    average_rating: float
    sentiment: Dict[str, float]
    model_sentiment: Optional[Dict[str, float]] = None
    aspects: Dict[str, AspectDetail]

class MonthlyTrend(BaseModel):
    month: str
    review_count: int
    positive_pct: float
    neutral_pct: float
    negative_pct: float
    positive_count: Optional[int] = 0
    neutral_count: Optional[int] = 0
    negative_count: Optional[int] = 0
    has_data: Optional[bool] = True

class DestinationTrendsResponse(BaseModel):
    destination_id: int
    destination: str
    trend_available: bool
    message: Optional[str] = None
    sample_size: Optional[int] = None
    date_range: Optional[str] = None
    monthly_trends: List[MonthlyTrend] = []

class ModelMetricsResponse(BaseModel):
    model_architecture: str
    dataset_source: Optional[str] = None
    total_sample_count: int
    training_sample_count: int
    test_sample_count: int
    accuracy: float
    precision_macro: float
    recall_macro: float
    f1_score_macro: float
    confusion_matrix: List[List[int]]
    baseline_comparison: Optional[Dict[str, Any]] = None
    dataset_quality: Optional[Dict[str, Any]] = None
