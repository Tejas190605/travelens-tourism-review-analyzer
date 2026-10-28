"""
Dataset Ingestion and Data Quality Processing for ASTMA.
Source: argilla/tripadvisor-hotel-reviews (Hugging Face / Open Source Benchmark)
License: CC-BY-NC-4.0
"""
import json
from pathlib import Path
from typing import Dict, Any, Tuple
import pandas as pd
import numpy as np

from app.core.config import settings

DATASET_URL = "https://huggingface.co/datasets/argilla/tripadvisor-hotel-reviews/resolve/main/data/train-00000-of-00001-0e99e58b23dccc25.parquet"

def download_and_ingest_dataset(
    target_samples_per_class: int = 2000,
    raw_output_path: Path = None,
    processed_output_path: Path = None,
    metrics_output_path: Path = None
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """
    Downloads legitimate TripAdvisor review dataset, performs data validation,
    cleaning, rating normalization, balanced sampling, and calculates data quality metrics.
    """
    if raw_output_path is None:
        raw_output_path = settings.DATA_DIR / "raw" / "tripadvisor_reviews_raw.csv"
    if processed_output_path is None:
        processed_output_path = settings.DATA_DIR / "processed" / "tripadvisor_reviews_processed.csv"
    if metrics_output_path is None:
        metrics_output_path = settings.MODELS_DIR / "dataset_metrics.json"

    raw_output_path.parent.mkdir(parents=True, exist_ok=True)
    processed_output_path.parent.mkdir(parents=True, exist_ok=True)
    metrics_output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"[Ingestion] Fetching TripAdvisor reviews from {DATASET_URL}...")
    df_raw = pd.read_parquet(DATASET_URL)
    initial_row_count = len(df_raw)
    print(f"[Ingestion] Loaded raw parquet dataset with {initial_row_count} records.")

    # 1. Extract rating from prediction metadata
    def extract_rating(pred):
        if pred is not None and len(pred) > 0 and isinstance(pred[0], dict):
            try:
                return int(pred[0].get("label", 0))
            except (ValueError, TypeError):
                return None
        return None

    df_raw["rating"] = df_raw["prediction"].apply(extract_rating)
    df_raw = df_raw.rename(columns={"text": "review_text"})

    # Save a slice of raw data if not already saved
    if not raw_output_path.exists():
        df_raw[["review_text", "rating"]].to_csv(raw_output_path, index=False)
        print(f"[Ingestion] Saved raw copy to {raw_output_path}")

    # 2. Schema Validation & Missing Value Handling
    missing_text_count = int(df_raw["review_text"].isna().sum())
    missing_rating_count = int(df_raw["rating"].isna().sum())

    df_clean = df_raw.dropna(subset=["review_text", "rating"]).copy()
    df_clean["rating"] = df_clean["rating"].astype(int)

    # 3. Duplicate Removal
    duplicate_count = int(df_clean.duplicated(subset=["review_text"]).sum())
    df_clean = df_clean.drop_duplicates(subset=["review_text"]).copy()

    # 4. Text Quality Filters
    df_clean["review_length"] = df_clean["review_text"].astype(str).str.len()
    df_clean = df_clean[df_clean["review_length"] >= 20].copy()

    # 5. Rating-to-Sentiment Mapping
    # Standard Academic 3-Class Mapping:
    # 1 - 2 stars -> negative
    # 3 stars     -> neutral
    # 4 - 5 stars -> positive
    def map_rating_to_sentiment(r: int) -> str:
        if r in (1, 2):
            return "negative"
        elif r == 3:
            return "neutral"
        elif r in (4, 5):
            return "positive"
        return "neutral"

    df_clean["sentiment"] = df_clean["rating"].apply(map_rating_to_sentiment)

    # 6. Balanced Sampling to prevent majority-class bias
    # Rating distribution is typically 4-5 heavy; we balance negative, neutral, and positive classes
    df_neg = df_clean[df_clean["sentiment"] == "negative"]
    df_neu = df_clean[df_clean["sentiment"] == "neutral"]
    df_pos = df_clean[df_clean["sentiment"] == "positive"]

    n_samples = min(target_samples_per_class, len(df_neg), len(df_neu), len(df_pos))
    print(f"[Ingestion] Balancing classes to {n_samples} samples per sentiment class...")

    sampled_neg = df_neg.sample(n=n_samples, random_state=42)
    sampled_neu = df_neu.sample(n=n_samples, random_state=42)
    sampled_pos = df_pos.sample(n=n_samples, random_state=42)

    df_balanced = pd.concat([sampled_neg, sampled_neu, sampled_pos]).sample(frac=1.0, random_state=42).reset_index(drop=True)

    # 7. Compute Quality & Statistical Metrics
    rating_distribution = df_balanced["rating"].value_counts().to_dict()
    sentiment_distribution = df_balanced["sentiment"].value_counts().to_dict()
    lengths = df_balanced["review_length"]

    quality_metrics = {
        "dataset_name": "TripAdvisor Hotel & Tourism Reviews Benchmark",
        "dataset_source": "argilla/tripadvisor-hotel-reviews (Hugging Face)",
        "license": "CC-BY-NC-4.0",
        "raw_total_reviews": initial_row_count,
        "missing_reviews_handled": missing_text_count,
        "missing_ratings_handled": missing_rating_count,
        "duplicate_reviews_removed": duplicate_count,
        "processed_samples_count": len(df_balanced),
        "sentiment_mapping": {
            "ratings_1_2": "negative",
            "rating_3": "neutral",
            "ratings_4_5": "positive"
        },
        "sentiment_distribution": {k: int(v) for k, v in sentiment_distribution.items()},
        "rating_distribution": {int(k): int(v) for k, v in rating_distribution.items()},
        "text_statistics": {
            "average_character_length": round(float(lengths.mean()), 1),
            "median_character_length": round(float(lengths.median()), 1),
            "min_character_length": int(lengths.min()),
            "max_character_length": int(lengths.max())
        }
    }

    # Save processed dataset
    df_balanced[["review_text", "rating", "sentiment"]].to_csv(processed_output_path, index=False)
    print(f"[Ingestion] Saved processed dataset ({len(df_balanced)} rows) to {processed_output_path}")

    # Save dataset quality report
    with open(metrics_output_path, "w", encoding="utf-8") as f:
        json.dump(quality_metrics, f, indent=2)
    print(f"[Ingestion] Saved dataset quality metrics to {metrics_output_path}")

    return df_balanced, quality_metrics

if __name__ == "__main__":
    download_and_ingest_dataset()
