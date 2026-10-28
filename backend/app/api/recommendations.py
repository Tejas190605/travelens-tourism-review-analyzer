from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.recommendations import UserPriorityWeights, RecommendationResponse
from app.services.recommendations import generate_recommendations

router = APIRouter(prefix="/recommendations", tags=["Recommendations"])

@router.post("", response_model=RecommendationResponse)
def get_recommendations_endpoint(
    priorities: UserPriorityWeights,
    top_n: int = Query(6, ge=1, le=12),
    db: Session = Depends(get_db)
):
    """
    Computes explainable personalized destination recommendations matching
    user priorities (1-5 scale) against empirical ASTMA 9-aspect analytics.
    """
    return generate_recommendations(priorities=priorities, db=db, top_limit=top_n)
