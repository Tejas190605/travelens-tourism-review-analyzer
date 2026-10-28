# FINAL_METRICS_VERIFICATION.md — Empirical Data & Model Verification Audit

**Project:** TRAVELENS — Tourism Destination Review Analyzer  
**Academic Module:** Aspect-Sentiment Tourism Mining & Analytics (ASTMA)  
**Evaluation Date:** October 2026  
**Auditor:** Final Quality Assurance & Academic Validation Verification  
**Status:** DEFINITIVE EMPIRICAL RECORD (SOURCE OF TRUTH)

---

## 1. Executive Summary & Resolution of Test-Set Discrepancy

During the cross-phase audit between Phase 3, Phase 5, Phase 6, and earlier draft notes, an apparent test-set size discrepancy was identified:
- **Phase 3 Report (`PHASE_3_REPORT.md`)** and backend model files documented **1,200 held-out test samples** (out of a 6,000-sample balanced dataset).
- **Certain sections in Phase 6 drafts** noted **720 test samples**.

### Root Cause Analysis & Empirical Verification
An exhaustive inspection of the actual physical model artifacts on disk:
- `backend/models/model_metrics.json`
- `backend/models/confusion_matrix.json`
- `backend/models/baseline_comparison.json`
- `backend/models/dataset_metrics.json`
- `backend/app/ml/train.py`

proves conclusively that **1,200 test samples** is the **actual, measured, and verified evaluation configuration**.

The "720" figure originated in a preliminary working draft during initial sample-size exploration ($3,600 \times 0.20 = 720$) prior to finalizing the full 6,000 balanced dataset ($6,000 \times 0.20 = 1,200$). That preliminary draft figure was inadvertently cited in select summary tables in Phase 6 documentation.

**Definitive Source of Truth:**  
The serialized model artifacts in [backend/models/model_metrics.json](file:///c:/Users/tejas/Tourism%20Review/backend/models/model_metrics.json) and [backend/models/confusion_matrix.json](file:///c:/Users/tejas/Tourism%20Review/backend/models/confusion_matrix.json), alongside [PHASE_3_REPORT.md](file:///c:/Users/tejas/Tourism%20Review/PHASE_3_REPORT.md), represent the **unambiguous, empirical source of truth** for all academic submissions and evaluations.

---

## 2. Definitive Verified Dataset Metrics

| Parameter | Measured Value | Data Provenance / Verification File |
| :--- | :--- | :--- |
| **Upstream Raw Dataset** | **20,491 reviews** | `backend/data/raw/tripadvisor_reviews_raw.csv` |
| **Dataset Source** | TripAdvisor Hotel & Tourism Reviews Benchmark | Hugging Face: `argilla/tripadvisor-hotel-reviews` |
| **Licensing** | CC-BY-NC-4.0 | Creative Commons Attribution-NonCommercial 4.0 |
| **Processed Balanced Corpus** | **6,000 reviews** | `backend/data/processed/tripadvisor_reviews_processed.csv` |
| **Sampling Strategy** | Exact 1:1:1 Stratified Balance | Downsampled positive majority to prevent class bias |
| **Class Distribution (Total)** | • Negative (1–2 Stars): **2,000** (33.33%)<br>• Neutral (3 Stars): **2,000** (33.33%)<br>• Positive (4–5 Stars): **2,000** (33.33%) | `backend/models/dataset_metrics.json` |
| **Train / Test Split Ratio** | 80% Train / 20% Held-Out Test | Stratified by sentiment class (`random_state=42`) |
| **Actual Training Set Size** | **4,800 samples** | Exactly 1,600 per class |
| **Actual Test Set Size** | **1,200 samples** | Exactly 400 per class |
| **Text Character Statistics** | Mean: **767.9 chars**, Median: **568.5 chars**, Min: 47, Max: 13,501 | `backend/models/dataset_metrics.json` |

---

## 3. Verified Model Architecture & Hyperparameters

The model architecture was selected via 5-fold stratified cross-validation on the 4,800 training samples without touching the test set:

```json
{
  "name": "Config_2_Unigrams_Bigrams_C1.0",
  "ngram_range": [1, 2],
  "min_df": 3,
  "max_features": 8000,
  "C": 1.0,
  "class_weight": "balanced",
  "sublinear_tf": true,
  "solver": "lbfgs"
}
```

### 5-Fold Cross-Validation Performance on Training Split
- **Config 1 (Unigrams, $C=1.0$, max_feat=5000):** Mean CV Macro F1 = $0.7327 \pm 0.0105$
- **Config 2 (Unigrams + Bigrams, $C=1.0$, max_feat=8000):** **Mean CV Macro F1 = $0.7384 \pm 0.0125$ (Selected)**
- **Config 3 (Unigrams + Bigrams, $C=2.0$, max_feat=10000):** Mean CV Macro F1 = $0.7331 \pm 0.0103$

---

## 4. Final Empirical Test-Set Metrics (1,200 Samples)

Evaluated exactly once on the 1,200 held-out test samples:

| Metric | Measured Value | Percentage / Calculation |
| :--- | :---: | :--- |
| **Accuracy** | **0.7450** | **74.50%** (894 correct out of 1,200 total) |
| **Macro Precision** | **0.7467** | Average of unweighted per-class precisions |
| **Macro Recall** | **0.7450** | Average of unweighted per-class recalls |
| **Macro F1-Score** | **0.7458** | Harmonic mean of Macro Precision and Macro Recall |
| **Weighted Precision** | **0.7467** | Class-weighted precision (identical due to exact balance) |
| **Weighted Recall** | **0.7450** | Class-weighted recall (identical due to exact balance) |
| **Weighted F1-Score** | **0.7458** | Class-weighted F1-Score |

---

## 5. Final Confusion Matrix (1,200 Test Samples)

From `backend/models/confusion_matrix.json`:

$$\begin{array}{c|ccc|c}
\textbf{Actual \ Predicted} & \textbf{Negative} & \textbf{Neutral} & \textbf{Positive} & \textbf{Total} \\
\hline
\textbf{Negative (Actual)} & \mathbf{315} & 75 & 10 & 400 \\
\textbf{Neutral (Actual)}  & 79 & \mathbf{260} & 61 & 400 \\
\textbf{Positive (Actual)} & 5 & 76 & \mathbf{319} & 400 \\
\hline
\textbf{Total Predicted}   & 399 & 411 & 390 & \mathbf{1,200}
\end{array}$$

### Per-Class Performance Breakdown
1. **Negative Class (400 samples):**
   - True Positives: 315 | False Positives: 84 ($79 + 5$) | False Negatives: 85 ($75 + 10$)
   - Class Precision: $\frac{315}{399} = 0.7895$ (78.95%)
   - Class Recall: $\frac{315}{400} = 0.7875$ (78.75%)
   - Class F1-Score: $0.7885$
2. **Neutral Class (400 samples):**
   - True Positives: 260 | False Positives: 151 ($75 + 76$) | False Negatives: 140 ($79 + 61$)
   - Class Precision: $\frac{260}{411} = 0.6326$ (63.26%)
   - Class Recall: $\frac{260}{400} = 0.6500$ (65.00%)
   - Class F1-Score: $0.6412$
3. **Positive Class (400 samples):**
   - True Positives: 319 | False Positives: 71 ($10 + 61$) | False Negatives: 81 ($5 + 76$)
   - Class Precision: $\frac{319}{390} = 0.8179$ (81.79%)
   - Class Recall: $\frac{319}{400} = 0.7975$ (79.75%)
   - Class F1-Score: $0.8076$

### Macro-Averages:
- $\text{Macro Precision} = \frac{0.7895 + 0.6326 + 0.8179}{3} = \mathbf{0.7467}$
- $\text{Macro Recall} = \frac{0.7875 + 0.6500 + 0.7975}{3} = \mathbf{0.7450}$
- $\text{Macro F1} = \frac{0.7885 + 0.6412 + 0.8076}{3} = \mathbf{0.7458}$

**Empirical Insight for Academic Viva:**  
Polarity discrimination between extreme classes (Negative vs Positive) is exceptionally strong: only 10 negatives are misclassified as positive ($2.5\%$), and only 5 positives are misclassified as negative ($1.25\%$). As is standard in natural language processing of 3-star reviews, the neutral class exhibits boundary overlap due to inherently mixed sentiments (e.g., *"The location was great but the room was small"*).

---

## 6. Baseline vs Final Model Comparison

| Evaluation Metric | Phase 2 Baseline (150 samples) | Phase 3 Final (6,000 samples) | Absolute Improvement |
| :--- | :---: | :---: | :---: |
| **Training Samples** | 120 | **4,800** | $+4,680$ samples |
| **Test Samples** | 30 | **1,200** | $+1,170$ samples |
| **Accuracy** | 60.00% | **74.50%** | **+14.50%** |
| **Macro Precision** | 0.6071 | **0.7467** | **+0.1396** |
| **Macro Recall** | 0.6000 | **0.7450** | **+0.1450** |
| **Macro F1-Score** | 0.5926 | **0.7458** | **+0.1532** |

---

## 7. Final Verification Sign-Off

This document stands as the definitive, immutable empirical record of the TRAVELENS ASTMA machine learning evaluation. All numbers match the serialized `.json` artifacts in `backend/models/` to 4 decimal places.
