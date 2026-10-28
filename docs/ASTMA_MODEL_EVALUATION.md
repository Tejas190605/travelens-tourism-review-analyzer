# ASTMA_MODEL_EVALUATION.md — Empirical Machine Learning Evaluation Report

**Academic Subject:** Aspect-Sentiment Tourism Mining & Analytics (ASTMA)  
**Model Name:** ASTMA Sentiment Classifier (TF-IDF + Multinomial Logistic Regression)  
**Dataset:** TripAdvisor Hotel & Tourism Reviews Benchmark (`argilla/tripadvisor-hotel-reviews`)  
**Evaluation Standard:** Held-Out Empirical Test Evaluation (Zero Data Leakage)  
**Status:** DEFINITIVE FINAL EVALUATION  

---

## 1. Dataset & Sampling Strategy

- **Upstream Corpus:** 20,491 raw reviews from TripAdvisor.
- **Licensing:** Creative Commons Attribution-NonCommercial 4.0 International (**CC-BY-NC-4.0**).
- **Working Dataset:** **6,000 processed samples** downsampled with exact 1:1:1 class balance to prevent majority-class learning bias.
- **Sentiment Threshold Mapping:**
  $$\text{Sentiment}(r) = \begin{cases}
  \text{Negative} & \text{if } r \in \{1, 2\} \quad (2,000\text{ samples}) \\
  \text{Neutral} & \text{if } r = 3 \quad (2,000\text{ samples}) \\
  \text{Positive} & \text{if } r \in \{4, 5\} \quad (2,000\text{ samples})
  \end{cases}$$
- **Data Partitioning:** Stratified 80/20 train/test split:
  - **Training Split:** **4,800 samples** (1,600 Negative, 1,600 Neutral, 1,600 Positive)
  - **Held-Out Test Split:** **1,200 samples** (400 Negative, 400 Neutral, 400 Positive)

---

## 2. Feature Engineering & Model Selection

### 2.1 Text Preprocessing
1. **Contraction Normalization:** Expansion of English contractions (`wasn't` $\rightarrow$ `was not`, `can't` $\rightarrow$ `cannot`).
2. **Case Folding & Cleaning:** Lowercased regex extraction of alphabetic tokens ($\ge 2$ characters).
3. **Negation Modifier Preservation:** Stopword filter specifically preserves key sentiment negation operators (`not`, `never`, `barely`, `hardly`, `scarcely`, `without`, `cannot`).

### 2.2 Model Configuration Selection (5-Fold Stratified Cross-Validation)
Evaluated on the 4,800 training samples:

| Candidate Configuration | N-Gram Range | Min DF | Max Features | $C$ (Reg) | Mean CV Macro F1 | Std CV F1 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Config 1 (Unigrams) | (1, 1) | 3 | 5,000 | 1.0 | 0.7327 | $\pm 0.0105$ |
| **Config 2 (Unigrams + Bigrams)** | **(1, 2)** | **3** | **8,000** | **1.0** | **0.7384** | **$\pm 0.0125$ (Selected)** |
| Config 3 (Unigrams + Bigrams, $C=2.0$) | (1, 2) | 2 | 10,000 | 2.0 | 0.7331 | $\pm 0.0103$ |

---

## 3. Verified Empirical Test-Set Metrics (1,200 Held-Out Samples)

Evaluated exactly once on the 1,200 held-out test samples:

| Performance Metric | Measured Value | Standard Interpretation |
| :--- | :---: | :--- |
| **Overall Accuracy** | **74.50% (0.7450)** | 894 out of 1,200 test samples correctly classified |
| **Macro Precision** | **0.7467** | Unweighted arithmetic mean of per-class precisions |
| **Macro Recall** | **0.7450** | Unweighted arithmetic mean of per-class recalls |
| **Macro F1-Score** | **0.7458** | Harmonic mean of Macro Precision and Macro Recall |
| **Weighted F1-Score**| **0.7458** | Identical to macro due to exact class balance |

---

## 4. Confusion Matrix Analysis

From [backend/models/confusion_matrix.json](file:///c:/Users/tejas/Tourism%20Review/backend/models/confusion_matrix.json):

$$\begin{array}{c|ccc|c}
\textbf{Actual \ Predicted} & \textbf{Negative} & \textbf{Neutral} & \textbf{Positive} & \textbf{Total} \\
\hline
\textbf{Negative (Actual)} & \mathbf{315} & 75 & 10 & 400 \\
\textbf{Neutral (Actual)}  & 79 & \mathbf{260} & 61 & 400 \\
\textbf{Positive (Actual)} & 5 & 76 & \mathbf{319} & 400 \\
\hline
\textbf{Total Predicted}   & 399 & 411 & 390 & \mathbf{1,200}
\end{array}$$

### Per-Class Detailed Performance:
- **Negative Class ($N=400$):** Precision: **78.95%** | Recall: **78.75%** | F1: **0.7885**
- **Neutral Class ($N=400$):** Precision: **63.26%** | Recall: **65.00%** | F1: **0.6412**
- **Positive Class ($N=400$):** Precision: **81.79%** | Recall: **79.75%** | F1: **0.8076**

---

## 5. Academic Interpretation & Linguistic Nuance

### 5.1 Why 74.5% Accuracy is Academically Rigorous and Valuable
1. **Three-Class Formulation with 33.3% Random Chance Baseline:** Unlike binary sentiment tasks where random guessing achieves $50\%$, a balanced 3-class problem has a random baseline of $33.33\%$. An accuracy of **74.50%** represents an improvement of **$+41.17\%$ over random chance**.
2. **Extreme Class Separation ($97.5\%+$ Polarity Integrity):**
   - Out of 400 negative reviews, only 10 were misclassified as positive ($2.5\%$).
   - Out of 400 positive reviews, only 5 were misclassified as negative ($1.25\%$).
   - Severe polarity confusion is virtually non-existent ($< 2\%$).
3. **The Inherent Linguistic Ambiguity of 3-Star Reviews:**
   - 3-star reviews in real tourism corpora almost always contain mixed polarity clauses (*"The location was great, but the room was noisy and the shower leaked"*).
   - Because document-level sentiment forces a single label onto multi-faceted commentary, borderline ambiguity between Neutral and Positive/Negative is an established phenomenon across NLP literature.

---

## 6. Model Limitations

1. **Bag-of-Words Limitation:** TF-IDF n-grams capture local phrase patterns (`not clean`, `very friendly`) but lack deep semantic understanding of long-distance syntactic dependencies or sarcasm.
2. **Document-Level Granularity:** A single overall sentiment label can obscure nuanced internal clause tensions (which is why TRAVELENS couples the model with the 9-aspect rule engine).
3. **English-Only Corpus:** Trained exclusively on English benchmark reviews; multilingual tourist feedback requires translation.
