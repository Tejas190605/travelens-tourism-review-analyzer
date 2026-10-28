# TRAVELENS — Final B.Tech Project Report & Evaluation Dossier

**Degree:** Bachelor of Technology (B.Tech) in Computer Science & Engineering / Information Technology  
**Project Title:** TRAVELENS — Tourism Destination Review Analyzer & Consumer Trip Planner  
**Curriculum Alignment:** Enterprise Systems (ES) | Natural Language Processing & Machine Learning (ASTMA) | IT Project Management (ITPM)  
**Submission Date:** October 2026  
**System Status:** Fully Implemented, Verified, and Submission-Ready  

---

## Abstract

Online tourism platforms predominantly summarize destination quality through single scalar star ratings (e.g., 4.2 out of 5 stars). Such aggregate metrics obscure significant experiential trade-offs: a location may possess magnificent cultural attractions and world-class dining while suffering from severe overcrowding, unhygienic facilities, inflated taxi rates, or personal safety concerns. Prospective travelers experience cognitive overload when manually parsing hundreds of unstructured reviews to extract specific dimensional attributes relevant to their individual priorities.

**TRAVELENS** is an enterprise-grade tourism review intelligence platform and consumer trip planner designed to address this fundamental problem. Built on a strictly decoupled 3-tier architecture—comprising a React 18 Single-Page Application (SPA), a FastAPI asynchronous REST service, and an SQLAlchemy 2.0 relational data layer—TRAVELENS implements **Aspect-Sentiment Tourism Mining & Analytics (ASTMA)**. The engine combines sublinear TF-IDF numerical vectorization, a multinomial Logistic Regression classifier with calibrated probability estimation, and a clause-level 9-dimension aspect extractor with context-window negation handling.

Evaluated on a balanced 1,200-sample test split from the standardized TripAdvisor Hotel & Tourism Reviews Benchmark Dataset, the system achieves an empirical accuracy of **74.50%** and a macro F1-score of **0.7458** (+41.17% over random chance baseline) with steady-state inference latency under **5 milliseconds**. Furthermore, TRAVELENS integrates multi-criteria preference-weighted destination recommendations, side-by-side comparison matrices, multi-tenant bookmark isolation, and verified Indian Rupee (INR) trip budget estimation. The system is verified by **67 passing automated backend tests**, **0 frontend linter warnings across 18 files**, **10 comprehensive Playwright end-to-end user journeys**, and **12 deep verification checks**.

---

## 1. Introduction & Motivation

### 1.1 The Fallacy of the Aggregate Star Rating
In modern e-tourism, travelers rely heavily on online customer reviews to plan trips and allocate financial resources. However, conventional travel discovery services present consumer feedback primarily through arithmetic mean star ratings (1 to 5 stars). This collapse of multidimensional human experience into a scalar metric presents severe limitations:
1. **Masking of Critical Bottlenecks:** A destination with a 4.2/5 rating may feature awe-inspiring historical architecture (5/5) while suffering from rampant pickpocketing (1/5) or exorbitant local transport costs (2/5).
2. **Cognitive Fatigue:** Travelers must manually filter through dozens of pages of repetitive or conflicting feedback to determine whether a destination fits their specific constraints (e.g., budget limits, family safety, or crowd tolerance).
3. **Absence of Explainability:** Traditional ranking engines frequently prioritize popularity or sponsored placements without detailing why a location matches an individual's travel style.

### 1.2 Objectives of TRAVELENS
1. **Granular Aspect Extraction:** Decompose unstructured natural language reviews into 9 core tourism dimensions: *Attractions, Food, Cleanliness, Price, Crowd, Safety, Transport, Accommodation, and Hospitality*.
2. **Robust Sentiment Classification:** Implement a fast, interpretable supervised classifier distinguishing Positive, Neutral, and Negative sentiments with syntactic negation support.
3. **Consumer-Oriented Trip Planning:** Provide an intuitive, transparent interface with realistic Indian Rupee (INR) daily budget tiers, day-by-day suggested itineraries, and mathematical cost estimators.
4. **Architectural Decoupling:** Enforce strict separation between the React presentation layer, FastAPI application tier, and SQLAlchemy data layer.
5. **Quality Assurance & Verification:** Maintain verifiable test coverage, zero database corruption during automated testing, and responsive cross-device usability.

---

## 2. Theoretical Background & Literature Survey

### 2.1 Aspect-Based Sentiment Analysis (ABSA)
Sentiment analysis has evolved from document-level and sentence-level polarity classification into fine-grained Aspect-Based Sentiment Analysis (ABSA). In tourism research, reviews are characterized by co-occurring attributes evaluated with contrasting polarities in a single sentence (e.g., *"The palace was magnificent, but the entrance ticket was a total rip-off"*).

ABSA involves two core sub-tasks:
- **Aspect Category Detection (ACD):** Identifying whether a sentence or clause references a predefined dimension.
- **Aspect Category Polarity (ACP):** Determining the sentiment polarity expressed toward that specific dimension.

### 2.2 Algorithmic Selection: TF-IDF + Logistic Regression vs. Deep Transformers
While large language models (BERT, RoBERTa) achieve marginal accuracy gains on NLP benchmarks, they impose severe constraints in production:
- **Inference Latency:** BERT models require 150–400 ms per sentence on commodity CPU hardware, whereas sublinear TF-IDF + Logistic Regression executes in **3–5 ms**.
- **Model Footprint:** Transformer weights exceed 400 MB in memory, while our serialized model binaries take **~1.2 MB** on disk.
- **Explainability:** Logistic Regression coefficients provide transparent log-odds for every token, ensuring that decisions can be academically defended and audited.

---

## 3. System Architecture & Engineering Design

### 3.1 Decoupled 3-Tier Enterprise Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    TIER 1: PRESENTATION                     │
│  React 18 SPA (Vite) | Vanilla CSS Design Tokens | Clean UX │
│  Routes: / (Discover), /explore, /destinations/:id,         │
│          /plan, /compare, /saved, /about, /login            │
└──────────────────────────────┬──────────────────────────────┘
                               │ HTTP REST / JSON
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                TIER 2: APPLICATION & LOGIC                  │
│  FastAPI (ASGI) | Python 3.10+ | Pydantic v2 Schemas        │
│  ├── Routers: /api/destinations, /api/reviews, /api/auth    │
│  ├── Services: Analytics, Recommendations, Aspects, Keywords│
│  └── ASTMA ML Engine: Vectorizer, Classifier, Negation Logic│
└──────────────────────────────┬──────────────────────────────┘
                               │ SQLAlchemy 2.0 ORM
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                     TIER 3: DATA LAYER                      │
│  Relational Database (SQLite in Dev / PostgreSQL in Prod)   │
│  Tables: destinations, reviews, review_aspects,             │
│          users, saved_destinations, user_preferences        │
│  Model Binaries: tfidf_vectorizer.joblib, classifier.joblib │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Design Patterns Applied
- **Model-View-Controller (MVC):** Data models in SQLAlchemy, views in React SPA, controllers in FastAPI routers.
- **Dependency Injection:** Database sessions (`get_db`) and user authentication (`get_current_user`) injected into endpoints cleanly.
- **Lifespan Warmup Pattern:** ASGI lifespan hook loads ML model binaries into RAM at startup, eliminating cold-start latency for user requests.

---

## 4. ASTMA Natural Language Processing Pipeline

### 4.1 Pipeline Workflow
1. **Text Normalization:**
   - Case folding to lowercase.
   - Contraction expansion (`wasn't` $\rightarrow$ `was not`, `can't` $\rightarrow$ `cannot`).
   - Removal of HTML tags and special characters.
2. **Clause Segmentation & Negation Binding:**
   - Sentences segmented by conjunctions (`but`, `however`, `although`, `yet`) and punctuation.
   - Negation words (`not`, `never`, `hardly`, `scarcely`, `barely`) preserved to invert polarities within a 3-token window.
3. **Numerical Vectorization:**
   - Sublinear term-frequency scaling: $\text{tf-idf}(t, d) = (1 + \log(\text{tf}(t, d))) \times \log\left(\frac{1 + N}{1 + \text{df}(t)}\right) + 1$.
   - N-gram range: unigrams and bigrams (`(1, 2)`).
   - Maximum features: 8,000.
4. **Supervised Classification:**
   - Multinomial Logistic Regression with $L_2$ penalty and balanced class weights.
   - Softmax calibrated probability estimation across Negative, Neutral, and Positive classes.
5. **Aspect-Level Clause Extraction:**
   - Domain lexicons across the 9 dimensions.
   - Polarity assignment with negation flipping.
   - Mixed review detection (`is_mixed = True` when positive and negative aspects co-occur).

---

## 5. Relational Database Schema & Entities

The relational database architecture is defined in `backend/app/db/models.py`:

| Table Name | Primary Key | Foreign Keys | Key Attributes & Constraints |
|---|---|---|---|
| `users` | `id` (int) | None | `email` (unique index), `password_hash` (bcrypt), `role` (`user`/`admin`), `created_at` |
| `destinations` | `id` (int) | None | `name`, `country`, `region`, `category`, `image_url`, `indicative_daily_budget`, `budget_tier`, `recommended_duration`, `best_season`, `suggested_itinerary` |
| `reviews` | `id` (int) | `destination_id` $\rightarrow$ `destinations.id` | `review_text`, `rating` (`CHECK 1 <= rating <= 5`), `sentiment`, `predicted_sentiment`, `prediction_confidence`, `is_mixed` |
| `review_aspects` | `id` (int) | `review_id` $\rightarrow$ `reviews.id` | `aspect` (indexed), `sentiment`, `score`, `created_at` |
| `saved_destinations` | `id` (int) | `user_id` $\rightarrow$ `users.id`, `destination_id` $\rightarrow$ `destinations.id` | Cascading deletion, isolated per user |
| `user_preferences` | `id` (int) | `user_id` $\rightarrow$ `users.id` | `category`, `weight` (1.0 to 5.0) |

---

## 6. Verification, Testing & Quality Assurance

### 6.1 Testing Methodology & Statistics
Automated verification was executed across four rigorous testing tiers:

```
┌─────────────────────────────────────────────────────────────┐
│ 1. BACKEND PYTEST SUITE                                     │
│    • 67 passed tests in 22.14s (100% pass rate)             │
│    • Covered: API routes, ML preprocessing, aspect negation,│
│      multi-user authorization, database cascades.           │
├─────────────────────────────────────────────────────────────┤
│ 2. FRONTEND LINT & CODE QUALITY                             │
│    • 0 warnings and 0 errors on 18 files (oxlint)           │
│    • Clean module-level purity and reactive dependencies.   │
├─────────────────────────────────────────────────────────────┤
│ 3. FRONTEND PRODUCTION BUILD                                │
│    • 1,921 modules transformed in 495ms (Vite v8.3.4)       │
│    • Dist bundle: index.html (1.13 KB), CSS (8.15 KB),      │
│      JS (394 KB / 109 KB gzip).                             │
├─────────────────────────────────────────────────────────────┤
│ 4. PLAYWRIGHT END-TO-END BROWSER AUTOMATION                 │
│    • 10/10 Consumer Journeys Passed (run_e2e_tests.cjs)     │
│    • 12/12 Deep Verification Checks Passed                  │
│      (verify_deep_e2e.cjs)                                  │
│    • 0 failed network requests.                             │
└─────────────────────────────────────────────────────────────┘
```

### 6.2 Representative ML Inference Validation
Direct execution on representative user inputs confirmed accurate classification:
- **Positive:** *"The Amber Fort in Jaipur was breathtaking! The tour guide was very friendly and courteous, and the local street food was delicious and fresh."*  
  $\rightarrow$ `sentiment: positive (56.7%)`, aspects: `Attractions (positive)`, `Hospitality (positive)`, `Food (positive)`.
- **Negative:** *"The hotel room was filthy and unhygienic with a foul odor. The staff was extremely rude and unhelpful, and the taxi fares were exorbitant and overpriced."*  
  $\rightarrow$ `sentiment: negative (85.6%)`, aspects: `Cleanliness (negative)`, `Accommodation (negative)`, `Hospitality (negative)`, `Price (negative)`, `Transport (negative)`.
- **Mixed:** *"The palaces and architecture were magnificent and stunning, but the entry tickets were overpriced and the area was terribly crowded."*  
  $\rightarrow$ `is_mixed: True`, aspects: `Attractions (positive)`, `Crowd (negative)`, `Price (negative)`.

---

## 7. User Manual & Demonstration Guide

### 7.1 Key Routes & User Capabilities
1. **Discover Home (`/`):** Instant destination search, curated category pills, and travel philosophy.
2. **Explore Directory (`/explore`):** 54 destinations filterable by Region (India, Europe, Asia), Category (Heritage, Nature, Coastal), and Budget Tier (Budget, Moderate, Luxury) in Indian Rupees.
3. **Destination Guide (`/destinations/:id`):** Strengths vs Caveats analysis, 9-aspect scorecard, interactive logistics tabs (Itinerary, Best Time, Transit, Tips), and verified visitor reviews.
4. **Plan a Trip (`/plan`):** Preference-weighted multi-attribute utility recommendations with day-by-day suggested itineraries and trip budget arithmetic.
5. **Compare Places (`/compare`):** Side-by-side benchmarking of two destinations across ratings, daily rates, seasons, and dimension scores.
6. **Saved Places (`/saved`):** Personal shortlist with multi-tenant isolation and mathematical trip cost calculator in INR.
7. **About (`/about`):** Empirical machine learning metrics and explanation of the 9 travel dimensions.

### 7.2 Pre-Configured Test Accounts
- **Traveler Account:** `traveler@travelens.com` / `userpassword123` (Contains persistent Jaipur shortlist bookmark)
- **Admin Account:** `admin@travelens.com` / `adminpassword123`

---

## 8. Viva Voce Defense Summary

| Common Examiner Question | TRAVELENS Engineering Defense |
|---|---|
| **Why not use deep learning (BERT/LLMs)?** | TF-IDF + Logistic Regression achieves 74.5% accuracy with sub-5ms CPU latency and 1.2 MB disk footprint, avoiding high GPU costs and server cold starts. |
| **How is multi-user security enforced?** | Passwords hashed with 12-round bcrypt; stateless HS256 JWT tokens; all bookmark queries filter strictly by `user_id == current_user.id`. |
| **How is database integrity maintained?** | Database foreign keys enforce cascade deletes; automated tests execute on isolated test databases to prevent polluting production data. |
| **What is the mathematical basis for recommendations?** | Multi-Attribute Utility Theory (MAUT): normalized dot product between user priority weights (1–5) and review-derived aspect scores (0–100). |
| **How are budgets calculated?** | Indian Rupee (INR) arithmetic: $\text{Daily Budget} \times \text{Number of Travellers} \times \text{Duration (Days)}$ with standard inclusion transparency. |

---

## 9. Conclusion & Future Work

TRAVELENS successfully demonstrates how Aspect-Based Sentiment Analysis and enterprise software engineering can transform raw, unstructured consumer feedback into an actionable, transparent travel discovery and planning product.

### Future Enhancements:
1. **Multilingual NLP:** Incorporate multilingual transformer embeddings (XLM-RoBERTa) to parse international reviews across Hindi, French, and Spanish.
2. **Cloud PostgreSQL Migration:** Transition from SQLite to managed PostgreSQL with connection pooling for enterprise concurrency.
3. **Active Learning Feedback Loop:** Allow users to submit corrections on misclassified clauses to iteratively improve model precision over time.
