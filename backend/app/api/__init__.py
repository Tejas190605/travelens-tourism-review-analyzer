from app.api.auth import router as auth_router
from app.api.destinations import router as destinations_router
from app.api.reviews import router as reviews_router
from app.api.analysis import router as analysis_router
from app.api.recommendations import router as recommendations_router

__all__ = [
    "auth_router",
    "destinations_router",
    "reviews_router",
    "analysis_router",
    "recommendations_router"
]
