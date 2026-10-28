import json
import os
from pathlib import Path
from typing import Dict, Any, Tuple
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)
import joblib

from app.core.config import settings
from app.ml.preprocessing import preprocess_for_tfidf

def evaluate_configurations(X_train: pd.Series, y_train: pd.Series) -> Dict[str, Any]:
    """
    Evaluates candidate TF-IDF + Logistic Regression configurations via 5-fold cross-validation
    on the training split to select the optimal model without touching the held-out test set.
    """
    candidates = [
        {
            "name": "Config_1_Unigrams_C1.0",
            "ngram_range": (1, 1),
            "min_df": 3,
            "max_features": 5000,
            "C": 1.0,
            "class_weight": "balanced"
        },
        {
            "name": "Config_2_Unigrams_Bigrams_C1.0",
            "ngram_range": (1, 2),
            "min_df": 3,
            "max_features": 8000,
            "C": 1.0,
            "class_weight": "balanced"
        },
        {
            "name": "Config_3_Unigrams_Bigrams_C2.0",
            "ngram_range": (1, 2),
            "min_df": 2,
            "max_features": 10000,
            "C": 2.0,
            "class_weight": "balanced"
        }
    ]

    print("[ASTMA Model Selection] Running 5-fold cross validation across candidate configurations...")
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    best_config = None
    best_cv_f1 = -1.0
    cv_results = []

    for cand in candidates:
        vec = TfidfVectorizer(
            ngram_range=cand["ngram_range"],
            min_df=cand["min_df"],
            max_features=cand["max_features"],
            sublinear_tf=True
        )
        X_vec = vec.fit_transform(X_train)
        clf = LogisticRegression(
            C=cand["C"],
            solver="lbfgs",
            class_weight=cand["class_weight"],
            max_iter=1000,
            random_state=42
        )
        scores = cross_val_score(clf, X_vec, y_train, cv=skf, scoring="f1_macro")
        mean_f1 = float(scores.mean())
        std_f1 = float(scores.std())
        cand_result = {
            "name": cand["name"],
            "mean_cv_f1_macro": round(mean_f1, 4),
            "std_cv_f1_macro": round(std_f1, 4),
            "params": cand
        }
        cv_results.append(cand_result)
        print(f"  -> {cand['name']}: Mean CV Macro F1 = {mean_f1:.4f} (+/- {std_f1:.4f})")

        if mean_f1 > best_cv_f1:
            best_cv_f1 = mean_f1
            best_config = cand

    print(f"[ASTMA Model Selection] Best configuration selected: {best_config['name']} (CV F1: {best_cv_f1:.4f})")
    return {"best_config": best_config, "cv_results": cv_results}

def train_sentiment_model(
    data_path: Path = None,
    output_dir: Path = None,
    random_state: int = 42
) -> Dict[str, Any]:
    """
    Trains the ASTMA sentiment classifier on legitimate travel review data,
    computes test metrics, and exports artifacts and baseline comparison.
    """
    if data_path is None:
        # Check if processed TripAdvisor dataset exists, else fallback to raw
        processed_path = settings.DATA_DIR / "processed" / "tripadvisor_reviews_processed.csv"
        if processed_path.exists():
            data_path = processed_path
        else:
            data_path = settings.DATA_DIR / "raw" / "tourism_sentiment_training.csv"

    if output_dir is None:
        output_dir = settings.MODELS_DIR

    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"[ASTMA Trainer] Loading training dataset from: {data_path}")
    df = pd.read_csv(data_path)
    df = df.dropna(subset=["review_text", "sentiment"]).copy()
    total_samples = len(df)
    class_distribution = df["sentiment"].value_counts().to_dict()

    print(f"[ASTMA Trainer] Total samples: {total_samples}")
    print(f"[ASTMA Trainer] Class distribution: {class_distribution}")

    # Text Preprocessing
    print("[ASTMA Trainer] Preprocessing text corpus with ASTMA pipeline...")
    df["clean_text"] = df["review_text"].apply(preprocess_for_tfidf)

    X = df["clean_text"]
    y = df["sentiment"]

    # Stratified Train/Test split (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=random_state,
        stratify=y
    )

    print(f"[ASTMA Trainer] Train samples: {len(X_train)}, Test samples: {len(X_test)}")

    # Model configuration search on training set
    selection_results = evaluate_configurations(X_train, y_train)
    best_params = selection_results["best_config"]

    # Fit final TF-IDF on all training data
    vectorizer = TfidfVectorizer(
        ngram_range=best_params["ngram_range"],
        min_df=best_params["min_df"],
        max_features=best_params["max_features"],
        sublinear_tf=True
    )
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # Fit final classifier
    classifier = LogisticRegression(
        C=best_params["C"],
        solver="lbfgs",
        class_weight=best_params["class_weight"],
        max_iter=1000,
        random_state=random_state
    )
    classifier.fit(X_train_vec, y_train)

    # Evaluate ONCE on held-out test set
    y_pred = classifier.predict(X_test_vec)
    labels = sorted(list(y.unique()))

    acc = float(accuracy_score(y_test, y_pred))
    prec_macro = float(precision_score(y_test, y_pred, average="macro", zero_division=0))
    rec_macro = float(recall_score(y_test, y_pred, average="macro", zero_division=0))
    f1_macro = float(f1_score(y_test, y_pred, average="macro", zero_division=0))
    prec_weighted = float(precision_score(y_test, y_pred, average="weighted", zero_division=0))
    rec_weighted = float(recall_score(y_test, y_pred, average="weighted", zero_division=0))
    f1_weighted = float(f1_score(y_test, y_pred, average="weighted", zero_division=0))

    cm = confusion_matrix(y_test, y_pred, labels=labels).tolist()

    # Load baseline metrics if available
    baseline_path = output_dir / "baseline_metrics.json"
    baseline_metrics = None
    if baseline_path.exists():
        with open(baseline_path, "r", encoding="utf-8") as f:
            baseline_metrics = json.load(f)

    metrics = {
        "model_architecture": f"TF-IDF {best_params['ngram_range']} + Multinomial Logistic Regression (C={best_params['C']})",
        "dataset_source": "TripAdvisor Hotel & Tourism Reviews Benchmark (argilla/tripadvisor-hotel-reviews)",
        "total_sample_count": total_samples,
        "training_sample_count": len(X_train),
        "test_sample_count": len(X_test),
        "class_distribution": class_distribution,
        "labels": labels,
        "selected_hyperparameters": best_params,
        "cross_validation_results": selection_results["cv_results"],
        "accuracy": round(acc, 4),
        "precision_macro": round(prec_macro, 4),
        "recall_macro": round(rec_macro, 4),
        "f1_score_macro": round(f1_macro, 4),
        "precision_weighted": round(prec_weighted, 4),
        "recall_weighted": round(rec_weighted, 4),
        "f1_score_weighted": round(f1_weighted, 4),
        "confusion_matrix": cm,
    }

    # Baseline comparison
    comparison = {
        "metric": ["Accuracy", "Macro Precision", "Macro Recall", "Macro F1-Score"],
        "baseline_phase_2": [
            baseline_metrics.get("accuracy", 0.60) if baseline_metrics else 0.60,
            baseline_metrics.get("precision_macro", 0.6071) if baseline_metrics else 0.6071,
            baseline_metrics.get("recall_macro", 0.60) if baseline_metrics else 0.60,
            baseline_metrics.get("f1_score_macro", 0.5926) if baseline_metrics else 0.5926,
        ],
        "improved_phase_3": [
            round(acc, 4),
            round(prec_macro, 4),
            round(rec_macro, 4),
            round(f1_macro, 4)
        ],
        "delta": [
            round(acc - (baseline_metrics.get("accuracy", 0.60) if baseline_metrics else 0.60), 4),
            round(prec_macro - (baseline_metrics.get("precision_macro", 0.6071) if baseline_metrics else 0.6071), 4),
            round(rec_macro - (baseline_metrics.get("recall_macro", 0.60) if baseline_metrics else 0.60), 4),
            round(f1_macro - (baseline_metrics.get("f1_score_macro", 0.5926) if baseline_metrics else 0.5926), 4)
        ]
    }

    # Save artifacts
    vec_path = output_dir / "tfidf_vectorizer.joblib"
    clf_path = output_dir / "sentiment_classifier.joblib"
    metrics_path = output_dir / "model_metrics.json"
    cm_path = output_dir / "confusion_matrix.json"
    comp_path = output_dir / "baseline_comparison.json"

    joblib.dump(vectorizer, vec_path)
    joblib.dump(classifier, clf_path)

    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    with open(cm_path, "w", encoding="utf-8") as f:
        json.dump({"labels": labels, "matrix": cm}, f, indent=2)

    with open(comp_path, "w", encoding="utf-8") as f:
        json.dump(comparison, f, indent=2)

    print("\n" + "=" * 65)
    print("ASTMA IMPROVED MODEL TRAINING & EVALUATION REPORT")
    print("=" * 65)
    print(f"Accuracy:           {acc:.4f} ({acc*100:.2f}%)")
    print(f"Precision (macro):  {prec_macro:.4f}")
    print(f"Recall (macro):     {rec_macro:.4f}")
    print(f"F1-score (macro):   {f1_macro:.4f}")
    print(f"Confusion Matrix:   {cm}")
    print(f"Labels:             {labels}")
    print("\nBASELINE VS IMPROVED COMPARISON:")
    print(f"Accuracy:           {comparison['baseline_phase_2'][0]}  ->  {comparison['improved_phase_3'][0]}  ({comparison['delta'][0]:+.4f})")
    print(f"Macro Precision:    {comparison['baseline_phase_2'][1]}  ->  {comparison['improved_phase_3'][1]}  ({comparison['delta'][1]:+.4f})")
    print(f"Macro Recall:       {comparison['baseline_phase_2'][2]}  ->  {comparison['improved_phase_3'][2]}  ({comparison['delta'][2]:+.4f})")
    print(f"Macro F1-Score:     {comparison['baseline_phase_2'][3]}  ->  {comparison['improved_phase_3'][3]}  ({comparison['delta'][3]:+.4f})")
    print("=" * 65 + "\n")

    return metrics

if __name__ == "__main__":
    train_sentiment_model()
