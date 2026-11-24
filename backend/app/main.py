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

    # 2. Automatically seed demo dataset if running with a fresh/empty database
    try:
        from app.db.database import SessionLocal
        from app.db.models import Destination
        db = SessionLocal()
        dest_count = db.query(Destination).count()
        db.close()
        if dest_count == 0:
            print("[Startup] Database is empty. Seeding destinations and review corpus...")
            import sys
            from pathlib import Path
            backend_dir = Path(__file__).resolve().parent.parent
            if str(backend_dir) not in sys.path:
                sys.path.insert(0, str(backend_dir))
            from scripts.seed_db import seed_database
            seed_database(clean_first=False)
            print("[Startup] Demo database seeded successfully.")
    except Exception as e:
        print(f"[Warning] Startup auto-seed check skipped: {e}")

    # 3. Warm up ML artifacts into memory to eliminate cold-start inference latency
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
DEFAULT_ORIGINS = [
    "https://travelens-frontend.onrender.com",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:3000",
]
raw_origins = [o.strip() for o in settings.ALLOWED_ORIGINS.split(",") if o.strip()]
cors_origins = list(dict.fromkeys(DEFAULT_ORIGINS + [o for o in raw_origins if o != "*"]))

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins if cors_origins else ["*"],
    allow_origin_regex=r"https://.*\.onrender\.com",
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
