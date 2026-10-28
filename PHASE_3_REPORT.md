# TRAVELENS — Phase 3 Implementation Report
**ASTMA Analytics Engine: Legitimate Data Ingestion, Model Improvement & Analytical Services**

**Date:** October 2026  
**Status:** COMPLETE  
**Project:** TRAVELENS — Tourism Destination Review Analyzer  
**Workspace:** `c:\Users\tejas\Tourism Review`  

---

## 1. Dataset Source

* **Dataset Name:** TripAdvisor Hotel & Tourism Reviews Benchmark (`tripadvisor-hotel-reviews`)
* **Repository / Provider:** Hugging Face Hub (`argilla/tripadvisor-hotel-reviews`)
* **Provenance:** Publicly available real-world travel and accommodation reviews originally collected from TripAdvisor, curated and published by Argilla as an open text-classification benchmark.
* **Access Method:** Downloaded and validated through automated ingestion pipeline (`backend/app/ml/ingestion.py`).

---

## 2. Dataset License and Usage Information

* **License:** Creative Commons Attribution-NonCommercial 4.0 International (**CC-BY-NC-4.0**)
* **Permitted Usage:** Academic research, non-commercial educational benchmarking, and software engineering development.
* **Ethical Compliance:** Zero live scraping performed; zero violation of platform terms of service. Text data is pre-existing, static, and anonymized.

---

## 3. Dataset Size and Distribution

* **Raw Total Reviews in Upstream Corpus:** 20,491 records
* **Filtered & Balanced Working Dataset:** 6,000 records
* **Class Balance:** Exact 1:1:1 stratification across all three sentiment classes:
  * **Negative:** 2,000 samples (33.3%)
  * **Neutral:** 2,000 samples (33.3%)
  * **Positive:** 2,000 samples (33.3%)
* **Text Length Characteristics:**
  * Mean Review Length: **767.9 characters**
  * Median Review Length: **568.5 characters**
  * Minimum Length: 47 characters
  * Maximum Length: 13,501 characters

---

## 4. Data Cleaning Pipeline

Executed programmatically in [backend/app/ml/ingestion.py](file:///c:/Users/tejas/Tourism%20Review/backend/app/ml/ingestion.py):
1. **Schema Validation:** Verified existence and validity of review text and star rating metadata.
2. **Missing Value Resolution:** Zero missing values tolerated; rows missing either field dropped.
3. **Deduplication:** Duplicate review strings filtered using hash-based deduplication.
4. **Noise Floor Filter:** Enforced minimum length threshold ($\ge 20$ characters) to reject empty or truncated entries.
5. **Class Equalization:** Downsampled the over-represented 5-star majority to match negative and neutral counts, completely eliminating majority-class learning bias.
6. **Artifact Storage:**
   * Raw dataset copy: `backend/data/raw/tripadvisor_reviews_raw.csv`
   * Cleaned balanced dataset: `backend/data/processed/tripadvisor_reviews_processed.csv`
   * Data quality report: `backend/models/dataset_metrics.json`

---

## 5. Sentiment Label Mapping

Rating metadata normalized to 3 discrete target classes according to standard academic sentiment thresholds:

$$\text{Sentiment}(r) = \begin{cases} 
\text{Negative} & \text{if } r \in \{1, 2\} \\ 
\text{Neutral} & \text{if } r = 3 \\ 
\text{Positive} & \text{if } r \in \{4, 5\} 
\end{cases}$$

### Class Distribution After Ingestion:
* **Negative (1–2 Stars):** 2,000 reviews (880 1-star, 1,120 2-star)
* **Neutral (3 Stars):** 2,000 reviews (2,000 3-star)
* **Positive (4–5 Stars):** 2,000 reviews (798 4-star, 1,202 5-star)
* **Total:** 6,000 reviews

---

## 6. Baseline Model (Phase 2 Review)

* **Architecture:** TF-IDF (1,2) + Multinomial Logistic Regression ($C=1.0$)
* **Training Corpus:** 150 development samples (50 positive, 50 neutral, 50 negative)
* **Train / Test Split:** 120 train / 30 test
* **Baseline Performance:**
  * Accuracy: **60.00%**
  * Macro Precision: **0.6071**
  * Macro Recall: **0.6000**
  * Macro F1-Score: **0.5926**
* **Limitation:** Sample sparsity caused high variance and limited feature coverage on nuanced vocabulary. Preserved in `backend/models/baseline_metrics.json`.

---

## 7. Improved Model Architecture & Validation Strategy

* **Architecture:** N-Gram TF-IDF Vectorizer + Multinomial Logistic Regression ($L_2$ Regularization)
* **Training Dataset:** 6,000 balanced TripAdvisor travel reviews
* **Stratified Split:**
  * Training Split: 4,800 samples (80%)
  * Held-Out Test Split: 1,200 samples (20%)
* **Hyperparameter Selection (5-Fold Stratified Cross-Validation on Training Split):**
  * *Config 1 (Unigrams, $C=1.0$, min_df=3):* Mean CV Macro F1 = 0.7327
  * *Config 2 (Unigrams + Bigrams, $C=1.0$, min_df=3, max_features=8000):* **Mean CV Macro F1 = 0.7384 (Selected)**
  * *Config 3 (Unigrams + Bigrams, $C=2.0$, min_df=2, max_features=10000):* Mean CV Macro F1 = 0.7331

---

## 8. Actual Empirical Evaluation Metrics

Evaluated **once** on the 1,200 held-out test samples (400 negative, 400 neutral, 400 positive):

| Metric | Phase 2 Baseline (150 samples) | Phase 3 Improved (6,000 samples) | Absolute Delta |
| :--- | :--- | :--- | :--- |
| **Accuracy** | **0.6000 (60.00%)** | **0.7450 (74.50%)** | **+0.1450 (+14.50%)** |
| **Macro Precision** | **0.6071** | **0.7467** | **+0.1396 (+13.96%)** |
| **Macro Recall** | **0.6000** | **0.7450** | **+0.1450 (+14.50%)** |
| **Macro F1-Score** | **0.5926** | **0.7458** | **+0.1532 (+15.32%)** |
| **Weighted F1-Score**| **0.5926** | **0.7458** | **+0.1532 (+15.32%)** |

---

## 9. Confusion Matrix Analysis

Test Split Confusion Matrix (1,200 samples, 400 per class):

$$\begin{array}{c|ccc}
\text{Actual \ Predicted} & \textbf{Negative} & \textbf{Neutral} & \textbf{Positive} \\
\hline
\textbf{Negative (400)} & 315 & 75 & 10 \\
\textbf{Neutral (400)}  & 79 & 260 & 61 \\
\textbf{Positive (400)} & 5 & 76 & 319 \\
\end{array}$$

### Empirical Observations:
1. **Minimal Extreme Confusion:** Only 10 negative reviews were misclassified as positive (2.5%), and only 5 positive reviews were misclassified as negative (1.25%).
2. **Neutral Nuance:** The majority of misclassifications occur adjacent to the neutral category (e.g., 75 negative classified as neutral, 76 positive classified as neutral), reflecting typical linguistic subjectivity in 3-star borderline reviews.
3. **Artifact Persistence:** Serialized to [backend/models/confusion_matrix.json](file:///c:/Users/tejas/Tourism%20Review/backend/models/confusion_matrix.json) and [backend/models/baseline_comparison.json](file:///c:/Users/tejas/Tourism%20Review/backend/models/baseline_comparison.json).

---

## 10. ASTMA Preprocessing Pipeline

Implemented in [backend/app/ml/preprocessing.py](file:///c:/Users/tejas/Tourism%20Review/backend/app/ml/preprocessing.py):
1. **Text Cleaning & Contraction Expansion:** Replaces `wasn't` $\rightarrow$ `was not`, `can't` $\rightarrow$ `cannot`.
2. **Case Normalization:** Unicode lowercasing.
3. **Sentence / Clause Segmentation:** Breaks reviews at punctuation boundaries and contrastive conjunctions (`but`, `however`, `although`).
4. **Token Extraction:** Regex word-boundary tokenization (`\b[a-zA-Z]{2,}\b`) eliminating trailing punctuation.
5. **Sentiment Negation Preservation:** Stopword filter removes non-discriminative English words while strictly preserving critical negation modifiers (`not`, `never`, `barely`, `hardly`, `scarcely`, `without`, `cannot`).
6. **Domain Lemmatization:** Inflection normalization for plurals and verb tenses.

---

## 11. Aspect Extraction Methodology

Implemented in [backend/app/services/aspects.py](file:///c:/Users/tejas/Tourism%20Review/backend/app/services/aspects.py):
* **9 Defined Tourism Aspects:** `Attractions`, `Food`, `Cleanliness`, `Price`, `Crowd`, `Safety`, `Transport`, `Accommodation`, `Hospitality`.
* **Clause-Level Polarity Isolation:** Each sentence/clause is analyzed independently to prevent cross-aspect sentiment pollution.
* **Inherent Tourism Cues:**
  * Words like *"crowded"*, *"packed"*, *"chaotic"* inherently penalize the `Crowd` aspect unless negated.
  * Words like *"serene"*, *"quiet"*, *"peaceful"* reward the `Crowd` aspect.
* **Verified Verification Test Cases:**
  * *Case 1:* `"The beach was beautiful but the area was extremely crowded."`
    * `Attractions` $\rightarrow$ **Positive** (score: 1.0, keyword: `beach`)
    * `Crowd` $\rightarrow$ **Negative** (score: -1.0, keyword: `crowded`)
  * *Case 2:* `"The food was excellent but the hotel room was dirty."`
    * `Food` $\rightarrow$ **Positive** (score: 1.0, keyword: `food`)
    * `Cleanliness` $\rightarrow$ **Negative** (score: -1.0, keyword: `dirty`)
    * `Accommodation` $\rightarrow$ **Negative** (score: -1.0, keyword: `hotel`, `room`)

---

## 12. Keyword Extraction Service

Implemented in [backend/app/services/keywords.py](file:///c:/Users/tejas/Tourism%20Review/backend/app/services/keywords.py):
* **Dual-Level Extraction:**
  * *Review-Level:* Extracts salient keyphrases from a single submitted text.
  * *Destination-Level:* Extracts corpus-level salient keywords aggregated across all reviews for a destination in the database.
* **Scoring & Frequency:** Uses sublinear TF-IDF weighting combined with token occurrence frequency counting (`Counter`).
* **Noise Suppression:** Custom blacklist eliminates generic non-informative tourism stopwords (`hotel`, `place`, `day`, `stayed`, `trip`).

---

## 13. Destination-Level Analytics Service

Implemented in [backend/app/services/analytics.py](file:///c:/Users/tejas/Tourism%20Review/backend/app/services/analytics.py):
* **Database Aggregation:** Directly queries database `destinations`, `reviews`, and `review_aspects` tables without hardcoded data.
* **Calculated Metrics:**
  * Total review count
  * Average rating (1–5)
  * Sentiment percentage breakdown: Positive %, Neutral %, Negative % (summing to 100%)
  * Granular Aspect Breakdown: For each of the 9 aspects, computes mention count, positive count, neutral count, negative count, and normalized aspect score ($0–100$):
    $$\text{Aspect Score} = \left(\frac{N_{\text{pos}} + 0.5 \times N_{\text{neu}}}{N_{\text{total}}}\right) \times 100$$

---

## 14. Sentiment Trend Analysis Service

Implemented in [backend/app/services/analytics.py](file:///c:/Users/tejas/Tourism%20Review/backend/app/services/analytics.py):
* **Chronological Aggregation:** Groups reviews by Year-Month (`YYYY-MM`) based on verified review dates.
* **Outputs:** Monthly review count, monthly Positive %, Neutral %, and Negative %.
* **Transparency Guardrail:** If reviews lack dates, returns `trend_available: false` rather than inventing synthetic timelines.

---

## 15. API Additions

All endpoints implemented and verified under `/api`:

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/analysis/model-metrics` | Returns active model evaluation metrics, baseline comparison, and dataset quality stats |
| `GET` | `/api/destinations/{id}/analytics` | Returns database-computed destination review count, rating, sentiment %, and 9-aspect scores |
| `GET` | `/api/destinations/{id}/trends` | Returns chronological monthly sentiment distribution trends |
| `GET` | `/api/destinations/{id}/keywords` | Returns top TF-IDF keywords and frequencies across destination reviews |
| `GET` | `/api/destinations/{id}/reviews` | Enhanced with `rating` query filter (`?rating=5`) alongside `sentiment` and `aspect` |
| `POST`| `/api/analyze-review` | Live sandbox returning sentiment, confidence, probabilities, detected aspects, keywords, and latency in ms |

---

## 16. Test Suite and Execution Results

* **Runner:** `pytest 9.1.1` on Python 3.14.3
* **Total Tests Executed:** **46 test cases** across 12 modules
* **Execution Time:** **3.13 seconds**
* **Result:** **46 PASSED, 0 FAILED (100% Pass Rate)**
* **Coverage Scope:** Data ingestion schema, rating-to-sentiment mapping, ML model inference, aspect extraction (both test cases), negation scoping, destination aggregation, sentiment trends, destination keywords, review filtering by rating/aspect/sentiment, auth flows, and model metrics API.

---

## 17. Inference Performance Verification

Benchmarked over 50 consecutive inference cycles on the complete ASTMA pipeline (cleaning + TF-IDF vectorization + Logistic Regression inference + 9-aspect extraction + TF-IDF keyword extraction):
* **Average Inference Latency:** **3.94 ms**
* **Minimum Latency:** 2.77 ms
* **Maximum Latency:** 5.84 ms
* **P95 Latency:** 5.23 ms
* **Conclusion:** Sub-5ms execution guarantees instantaneous, flicker-free responsiveness in the interactive UI sandbox.

---

## 18. ASTMA Syllabus Academic Mapping

| ASTMA Syllabus Concept | Implementation in TRAVELENS Phase 3 |
| :--- | :--- |
| **Text Mining** | Extraction of hidden patterns, aspect mentions, and keyphrase clusters from unstructured travel reviews. |
| **Text Preprocessing** | Contraction expansion, HTML stripping, lowercasing, regex tokenization, negation-preserving stopword filtering, and lemmatization. |
| **Natural Language Processing (NLP)** | Sentence and clause boundary detection, dependency-inspired negation scoping, and aspect seed lexicon matching. |
| **Sentiment Analysis** | 3-class sentiment categorization (Positive, Neutral, Negative) at both whole-review and aspect-clause levels. |
| **Sentiment Prediction** | Multinomial Logistic Regression model using sublinear TF-IDF features, predicting classes with calibrated probability distributions. |
| **Keyword Extraction** | Statistical term-frequency inverse-document-frequency (TF-IDF) extraction returning ranked keyphrases with document frequency. |
| **Precision** | Actual test macro precision: **0.7467** (measures reliability of positive/neutral/negative predictions). |
| **Recall** | Actual test macro recall: **0.7450** (measures proportion of actual sentiment instances retrieved). |
| **Information Visualization Readiness** | Structured JSON outputs (aspect scores, radar vectors, monthly trends, stacked sentiment percentages) ready for rendering in the Phase 4/5 React UI. |

---

## 19. Known Limitations

1. **Aspect Model Type:** Aspects are extracted using maintainable, rule-based lexical matching rather than deep-learning sequence labeling (e.g., BERT-NER). This was a deliberate architectural choice to ensure full explainability during academic viva defense and maintain sub-5ms CPU latency.
2. **Neutral Sentiment Ambiguity:** As evident in the confusion matrix, neutral reviews carry natural linguistic ambiguity where subjective 3-star reviews mix minor praise and minor complaints.

---

*Phase 3 ASTMA Analytics Engine is complete, tested, and validated.*
