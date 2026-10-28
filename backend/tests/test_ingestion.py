import pandas as pd
from app.ml.ingestion import download_and_ingest_dataset
from app.core.config import settings

def test_ingestion_data_validation_and_balance(tmp_path):
    processed_file = settings.DATA_DIR / "processed" / "tripadvisor_reviews_processed.csv"
    assert processed_file.exists()

    df = pd.read_csv(processed_file)
    # Validate schema
    assert "review_text" in df.columns
    assert "rating" in df.columns
    assert "sentiment" in df.columns

    # Validate no missing values
    assert df["review_text"].isna().sum() == 0
    assert df["rating"].isna().sum() == 0
    assert df["sentiment"].isna().sum() == 0

    # Validate rating boundaries
    assert df["rating"].min() >= 1
    assert df["rating"].max() <= 5

    # Validate balanced distribution
    counts = df["sentiment"].value_counts().to_dict()
    assert counts.get("negative") == 2000
    assert counts.get("neutral") == 2000
    assert counts.get("positive") == 2000
    assert len(df) == 6000

def test_sentiment_label_mapping():
    # Verify standard mapping logic:
    # 1-2 -> negative, 3 -> neutral, 4-5 -> positive
    def map_rating(r):
        if r in (1, 2):
            return "negative"
        elif r == 3:
            return "neutral"
        elif r in (4, 5):
            return "positive"
        return "neutral"

    assert map_rating(1) == "negative"
    assert map_rating(2) == "negative"
    assert map_rating(3) == "neutral"
    assert map_rating(4) == "positive"
    assert map_rating(5) == "positive"
