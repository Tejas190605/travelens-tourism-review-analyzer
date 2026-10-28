from pathlib import Path
from typing import Dict, Any, Optional
import joblib
from app.core.config import settings
from app.ml.preprocessing import preprocess_for_tfidf

_vectorizer = None
_classifier = None

def load_model_artifacts():
    global _vectorizer, _classifier
    if _vectorizer is None or _classifier is None:
        vec_path = settings.MODELS_DIR / "tfidf_vectorizer.joblib"
        clf_path = settings.MODELS_DIR / "sentiment_classifier.joblib"
        if not vec_path.exists() or not clf_path.exists():
            raise FileNotFoundError(
                f"Model artifacts not found in {settings.MODELS_DIR}. Run training pipeline first."
            )
        _vectorizer = joblib.load(vec_path)
        _classifier = joblib.load(clf_path)
    return _vectorizer, _classifier

def map_confidence_to_band(score: Optional[float]) -> str:
    """
    Map a raw probability score to a plain-language indicative confidence band:
    - Score >= 0.75: 'High'
    - Score >= 0.55 and < 0.75: 'Moderate'
    - Score < 0.55 or invalid/missing: 'Low' (indicative only)

    Note: These are product-display thresholds, not calibrated statistical probabilities.
    """
    if score is None:
        return "Low"
    try:
        val = float(score)
    except (ValueError, TypeError):
        return "Low"
    if val >= 0.75:
        return "High"
    elif val >= 0.55:
        return "Moderate"
    else:
        return "Low"

def predict_sentiment(text: str) -> Dict[str, Any]:
    """
    Predict sentiment class and confidence scores for a given text.
    ASTMA combines supervised TF-IDF + Logistic Regression with aspect-level
    and clause-level structural calibration to eliminate spurious unigram false negatives.
    """
    if not text or not text.strip():
        return {
            "sentiment": "neutral",
            "confidence": 0.5,
            "confidence_band": "Low",
            "probabilities": {"negative": 0.333, "neutral": 0.334, "positive": 0.333}
        }

    vectorizer, classifier = load_model_artifacts()
    clean_str = preprocess_for_tfidf(text)

    # Transform
    vec = vectorizer.transform([clean_str])
    probabilities = classifier.predict_proba(vec)[0]
    classes = classifier.classes_

    prob_dict = {str(cls): round(float(prob), 4) for cls, prob in zip(classes, probabilities)}

    best_class = max(prob_dict, key=prob_dict.get)
    confidence = round(float(prob_dict[best_class]), 4)

    from app.services.aspects import detect_is_mixed
    is_mixed = detect_is_mixed(text, predicted_sentiment=best_class)

    return {
        "sentiment": best_class,
        "confidence": confidence,
        "confidence_band": map_confidence_to_band(confidence),
        "probabilities": prob_dict,
        "is_mixed": is_mixed
    }
