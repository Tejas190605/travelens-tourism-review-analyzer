import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# Base Directory of backend
BACKEND_DIR = Path(__file__).resolve().parent.parent.parent
DEFAULT_DB_PATH = (BACKEND_DIR / "travelens.db").as_posix()

class Settings(BaseSettings):
    PROJECT_NAME: str = "TRAVELENS"
    VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    # Database
    DATABASE_URL: str = f"sqlite:///{DEFAULT_DB_PATH}"

    # Security
    SECRET_KEY: str = "dev-secret-key-travelens-review-analyzer-2026"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours

    # Paths
    MODELS_DIR: Path = BACKEND_DIR / "models"
    DATA_DIR: Path = BACKEND_DIR / "data"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
