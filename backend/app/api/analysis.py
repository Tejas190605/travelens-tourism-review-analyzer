import time
import json
from pathlib import Path
from typing import List, Dict, Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.database import get_db
from app.schemas.analysis import (
    AnalyzeReviewRequest,
    AnalyzeReviewResponse,
    DetectedAspect,
    ExtractedKeyword,
    DestinationAnalyticsResponse,
    DestinationTrendsResponse,
    ModelMetricsResponse
)
from app.ml.preprocessing import preprocess_for_tfidf
from app.ml.predict import predict_sentiment
from app.services.aspects import extract_aspects_from_text, extract_clause_analysis, detect_is_mixed
from app.services.keywords import extract_keywords, extract_destination_keywords
from app.services.analytics import get_destination_analytics, get_destination_sentiment_trend

router = APIRouter(tags=["Analysis"])

@router.post("/analyze-review", response_model=AnalyzeReviewResponse)
def analyze_review_endpoint(payload: AnalyzeReviewRequest):
    """
    ASTMA Live Analysis Sandbox:
    Accepts raw traveler review text, runs cleaning, supervised sentiment prediction,
    9-aspect extraction, clause-level decomposition, and TF-IDF keyword extraction.
    """
    start_time = time.perf_counter()
    raw_text = payload.review_text.strip()
    if not raw_text:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Review text cannot be empty"
        )

    # 1. Cleaned text
    cleaned_text = preprocess_for_tfidf(raw_text)

    # 2. Supervised Sentiment Prediction
    sentiment_result = predict_sentiment(raw_text)

    # 3. 9-Aspect Decomposition
    raw_aspects = extract_aspects_from_text(raw_text)
    detected_aspects = [
        DetectedAspect(
            aspect=item["aspect"],
            sentiment=item["sentiment"],
            score=item["score"],
            keywords=item.get("keywords", [])
        )
        for item in raw_aspects
    ]

    # 4. Clause Analysis & Mixed Detection
    clauses = extract_clause_analysis(raw_text)
    is_mixed_sentiment = detect_is_mixed(raw_text, predicted_sentiment=sentiment_result["sentiment"])

    # 5. Keyword Extraction
    raw_keywords = extract_keywords(raw_text, top_n=8)
    extracted_keywords = [
        ExtractedKeyword(
            keyword=item["keyword"],
            score=item["score"],
            frequency=item.get("frequency")
        )
        for item in raw_keywords
    ]

    elapsed_ms = round((time.perf_counter() - start_time) * 1000, 2)

    return AnalyzeReviewResponse(
        raw_text=raw_text,
        cleaned_text=cleaned_text,
        sentiment=sentiment_result["sentiment"],
        confidence=sentiment_result["confidence"],
        confidence_band=sentiment_result.get("confidence_band", "Moderate"),
        probabilities=sentiment_result["probabilities"],
        detected_aspects=detected_aspects,
        extracted_keywords=extracted_keywords,
        clause_analysis=clauses,
        is_mixed=is_mixed_sentiment,
        latency_ms=elapsed_ms
    )

@router.get("/analysis/model-metrics", response_model=ModelMetricsResponse)
def get_model_metrics():
    """
    Retrieves stored empirical evaluation metrics for the active ASTMA ML model,
    including baseline comparison and dataset quality summary.
    """
    metrics_path = settings.MODELS_DIR / "model_metrics.json"
    comp_path = settings.MODELS_DIR / "baseline_comparison.json"
    dataset_path = settings.MODELS_DIR / "dataset_metrics.json"

    if not metrics_path.exists():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Model metrics artifact not found. Please run training pipeline first."
        )

    with open(metrics_path, "r", encoding="utf-8") as f:
        metrics_data = json.load(f)

    baseline_comparison = None
    if comp_path.exists():
        with open(comp_path, "r", encoding="utf-8") as f:
            baseline_comparison = json.load(f)

    dataset_quality = None
    if dataset_path.exists():
        with open(dataset_path, "r", encoding="utf-8") as f:
            dataset_quality = json.load(f)

    return ModelMetricsResponse(
        model_architecture=metrics_data.get("model_architecture", "TF-IDF + Logistic Regression"),
        dataset_source=metrics_data.get("dataset_source"),
        total_sample_count=metrics_data["total_sample_count"],
        training_sample_count=metrics_data["training_sample_count"],
        test_sample_count=metrics_data["test_sample_count"],
        accuracy=metrics_data["accuracy"],
        precision_macro=metrics_data["precision_macro"],
        recall_macro=metrics_data["recall_macro"],
        f1_score_macro=metrics_data["f1_score_macro"],
        confusion_matrix=metrics_data["confusion_matrix"],
        baseline_comparison=baseline_comparison,
        dataset_quality=dataset_quality
    )

@router.get("/destinations/{destination_id}/analytics", response_model=DestinationAnalyticsResponse)
def get_destination_analytics_endpoint(destination_id: int, db: Session = Depends(get_db)):
    """
    Returns empirical destination-level analytics aggregated directly from the database:
    review volume, average rating, sentiment distribution, and granular 9-aspect scores.
    """
    analytics = get_destination_analytics(destination_id, db)
    if not analytics:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Destination with ID {destination_id} not found"
        )
    return analytics

@router.get("/destinations/{destination_id}/trends", response_model=DestinationTrendsResponse)
def get_destination_trends_endpoint(destination_id: int, db: Session = Depends(get_db)):
    """
    Returns chronological monthly sentiment distribution trend for a destination.
    """
    trends = get_destination_sentiment_trend(destination_id, db)
    if not trends or "destination_id" not in trends:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Destination with ID {destination_id} not found"
        )
    return trends

@router.get("/destinations/{destination_id}/keywords", response_model=List[ExtractedKeyword])
def get_destination_keywords_endpoint(
    destination_id: int,
    top_n: int = Query(10, ge=1, le=50),
    db: Session = Depends(get_db)
):
    """
    Returns top empirical TF-IDF keywords extracted across all reviews for the destination.
    """
    keywords = extract_destination_keywords(destination_id, db, top_n=top_n)
    return [
        ExtractedKeyword(
            keyword=item["keyword"],
            score=item["score"],
            frequency=item.get("frequency")
        )
        for item in keywords
    ]
