from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.db.database import engine, Base
from app.db import models  # Ensures all models are registered
from app.ml.predict import load_model_artifacts, predict_sentiment
from app.api.auth import router as auth_router
from app.api.destinations import router as destinations_router
from app.api.reviews import router as reviews_router
from app.api.analysis import router as analysis_router
from app.api.recommendations import router as recommendations_router
from app.api.saved_destinations import router as saved_destinations_router
from app.api.feedback import router as feedback_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 1. Ensure all database tables exist (e.g. saved_destinations)
    Base.metadata.create_all(bind=engine)
    # 2. Warm up ML artifacts into memory to eliminate cold-start inference latency
    try:
        load_model_artifacts()
        predict_sentiment("warmup scenic destination")
    except Exception as e:
        print(f"[Warning] ASTMA model warmup skipped: {e}")
    yield

app = FastAPI(
    title=f"{settings.PROJECT_NAME} API",
    description="Backend API for TRAVELENS — Aspect-Sentiment Tourism Destination Review Analyzer",
    version=settings.VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# CORS middleware for React SPA communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permits local development ports (Vite 5173, etc.)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health endpoint required by Phase 2 spec
@app.get("/api/health", tags=["Health"])
def health_check():
    return {
        "status": "ok",
        "app": f"{settings.PROJECT_NAME} API",
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT
    }

# Register API Routers
app.include_router(auth_router, prefix="/api")
app.include_router(destinations_router, prefix="/api")
app.include_router(reviews_router, prefix="/api")
app.include_router(analysis_router, prefix="/api")
app.include_router(recommendations_router, prefix="/api")
app.include_router(saved_destinations_router, prefix="/api")
app.include_router(feedback_router, prefix="/api")

@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to TRAVELENS API",
        "docs": "/docs",
        "health": "/api/health"
    }
