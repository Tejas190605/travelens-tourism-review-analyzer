from typing import List, Dict, Any
from sqlalchemy.orm import Session

from app.db.models import Destination
from app.services.analytics import get_destination_analytics
from app.schemas.recommendations import UserPriorityWeights, DestinationRecommendation, RecommendationResponse

# Mapping from user travel priority dimension to underlying 9-aspect scoring vectors
PRIORITY_ASPECT_MAP = {
    "adventure": [("Attractions", 0.7), ("Transport", 0.3)],
    "relaxation": [("Crowd", 0.6), ("Safety", 0.4)],
    "family": [("Safety", 0.4), ("Cleanliness", 0.4), ("Accommodation", 0.2)],
    "food": [("Food", 0.75), ("Hospitality", 0.25)],
    "heritage": [("Attractions", 0.8), ("Hospitality", 0.2)],
    "nightlife": [("Food", 0.5), ("Transport", 0.3), ("Attractions", 0.2)],
    "budget": [("Price", 1.0)],
}

def generate_recommendations(
    priorities: UserPriorityWeights,
    db: Session,
    top_limit: int = 6
) -> RecommendationResponse:
    """
    Computes an explainable, preference-weighted destination match score (0-100%)
    based strictly on empirical review-derived aspect analytics.
    Returns ranked destinations with top matching factors and explicit trade-offs.
    """
    destinations = db.query(Destination).all()
    priority_dict = priorities.model_dump()
    
    region_filter = priority_dict.pop("region_filter", None)
    budget_filter = priority_dict.pop("budget_filter", None)

    results: List[DestinationRecommendation] = []
    
    # Calculate sum of user weights
    total_user_weight = sum(priority_dict.values()) or 1
    
    for dest in destinations:
        if region_filter and region_filter.lower() != "all":
            if (dest.region or "").lower() != region_filter.lower() and (dest.country or "").lower() != region_filter.lower():
                continue

        if budget_filter and budget_filter.lower() != "all":
            if (dest.budget_tier or "").lower() != budget_filter.lower():
                continue

        analytics = get_destination_analytics(dest.id, db)
        aspects = analytics.get("aspects", {})
        
        # Calculate weighted compatibility score
        weighted_score_sum = 0.0
        aspect_evaluations: Dict[str, float] = {}
        
        for priority_key, user_weight in priority_dict.items():
            mappings = PRIORITY_ASPECT_MAP.get(priority_key, [])
            dim_score = 0.0
            
            for asp_name, asp_weight in mappings:
                asp_data = aspects.get(asp_name, {})
                score_val = asp_data.get("aspect_score")
                score = score_val if score_val is not None else 50.0
                dim_score += score * asp_weight
                aspect_evaluations[asp_name] = score
                
            weighted_score_sum += dim_score * user_weight
            
        base_match_pct = round(weighted_score_sum / total_user_weight, 1)
        # Clamp between 20% and 99%
        match_percentage = max(20.0, min(99.0, base_match_pct))
        
        # Identify strong matches (aspects with score >= 70 where priority was active)
        top_matches = []
        for asp_name, score in aspect_evaluations.items():
            if score >= 75:
                top_matches.append(f"{asp_name} (Acclaim: {int(score)}/100)")
            elif score >= 65 and len(top_matches) < 2:
                top_matches.append(f"{asp_name} (Favorable: {int(score)}/100)")
                
        if not top_matches:
            top_matches.append("Balanced baseline experience across core categories")
            
        # Identify trade-offs (aspects with score <= 50 or notable frictions)
        trade_offs = []
        for asp_name, score in aspect_evaluations.items():
            if score <= 40:
                trade_offs.append(f"Lower score on {asp_name} ({int(score)}/100)")
            elif score <= 50 and len(trade_offs) < 2:
                trade_offs.append(f"Moderate traveller friction regarding {asp_name}")
                
        if not trade_offs:
            # Check crowd or price specifically as natural travel trade-offs
            crowd_score = aspect_evaluations.get("Crowd", 50)
            price_score = aspect_evaluations.get("Price", 50)
            if crowd_score <= 55:
                trade_offs.append(f"Peak season crowd congestion ({int(crowd_score)}/100)")
            elif price_score <= 55:
                trade_offs.append("Elevated expenditure & tour costs")
            else:
                trade_offs.append("Minor seasonal variation in local amenities")
                
        # Compose neutral, data-driven explanation
        top_aspect_names = [m.split(" (")[0] for m in top_matches[:2]]
        trade_off_names = [t.split(" (")[0] for t in trade_offs[:1]]
        
        explanation = (
            f"Aligns strongly with your priorities due to visitor satisfaction in {', '.join(top_aspect_names)}. "
            f"Note potential trade-offs in {', '.join(trade_off_names)} based on analysed traveller feedback."
        )
        
        results.append(
            DestinationRecommendation(
                destination_id=dest.id,
                name=dest.name,
                country=dest.country,
                state_or_region=dest.state_or_region,
                category=dest.category,
                region=dest.region,
                budget_tier=dest.budget_tier,
                indicative_daily_budget=dest.indicative_daily_budget,
                image_url=dest.image_url,
                average_rating=analytics.get("average_rating", 0.0),
                total_reviews=analytics.get("review_count", 0),
                match_percentage=match_percentage,
                top_matches=top_matches[:3],
                trade_offs=trade_offs[:2],
                explanation=explanation
            )
        )
        
    # Sort descending by match percentage
    results.sort(key=lambda r: (r.match_percentage, r.average_rating), reverse=True)
    
    return RecommendationResponse(
        priorities=priorities.model_dump(),
        recommendations=results[:top_limit]
    )
