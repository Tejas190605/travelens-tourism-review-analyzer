# TRAVELENS — Tourism Destination Review Analyzer

> **"See the destination through travellers' eyes."**  
> An Aspect-Sentiment Tourism Mining & Analytics (ASTMA) Enterprise Platform.

[![Backend Tests](https://img.shields.io/badge/pytest-78%2F78%20passed-brightgreen.svg)]()
[![Frontend Lint](https://img.shields.io/badge/oxlint-0%20warnings-brightgreen.svg)]()
[![Frontend Build](https://img.shields.io/badge/vite-clean%20build-brightgreen.svg)]()
[![E2E Verification](https://img.shields.io/badge/playwright-22%2F22%20passed-brightgreen.svg)]()
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-teal.svg)]()
[![React](https://img.shields.io/badge/react-18-blue.svg)]()
[![Dataset License](https://img.shields.io/badge/license-CC--BY--NC--4.0-orange.svg)]()

---

## 1. Problem Statement

Conventional tourism review websites rely on aggregate 1-to-5 star ratings that collapse rich, multifaceted traveler experiences into a single misleading average. A destination boasting a 4.5-star rating might feature world-class historical monuments while simultaneously suffering from extreme overcrowding, inflated prices, or inadequate public transportation. Consequently, prospective travelers face cognitive overload and "review fatigue," manually reading through hundreds of unstructured comments to unearth specific details relevant to their personal needs (e.g., cleanliness, safety, or budget).

---

## 2. Proposed Solution: TRAVELENS

TRAVELENS is an academic and enterprise engineering platform that bridges the gap between raw, unstructured tourist feedback and actionable decision-making. By applying **Aspect-Sentiment Tourism Mining & Analytics (ASTMA)**, TRAVELENS decomposes reviews across **9 core tourism dimensions**, computes empirical polarity metrics, isolates salient keyphrases, enables side-by-side destination comparisons, and provides an explainable multi-criteria recommendation engine tailored to user-specified priorities.

---

## 3. Key Features

- **Destination Catalog & Exploration:** Dynamic full-text search, category filtering (Cultural, Nature, Urban), and interactive cards.
- **Deep Destination Analytics:** Multi-axis 9-aspect radar charts, sentiment distribution rings, star ratings, and monthly review trends.
- **Review Explorer & Filtering:** Paginated review lists filterable by star rating (1–5), sentiment polarity (Positive, Neutral, Negative), and individual aspect tags.
- **Interactive Review Analyzer:** Real-time NLP inference form classifying custom review text, extracting aspect polarity clauses, and computing confidence scores.
- **Dual Destination Benchmarking:** Side-by-side comparative analysis of two destinations across all 9 aspect scores with differential bar charts.
- **Personalized Recommendation Wizard:** Multi-attribute utility formulation with 1–5 priority sliders for each aspect, calculating objective rankings with transparent trade-off explanations.
- **Secure Authentication & Bookmarks:** Cryptographic password hashing (bcrypt), stateless JWT bearer authentication, and a personal saved destinations dashboard.

---

## 4. Why TRAVELENS is Different

| Feature | Conventional Travel Portals | TRAVELENS Platform |
| :--- | :--- | :--- |
| **Metric Depth** | Single aggregate star average (e.g. 4.2/5) | **9-Aspect Radar Profile** (Attractions, Food, Cleanliness, Price, Crowd, Safety, Transport, Accommodation, Hospitality) |
| **Text Mining** | Unstructured comment lists | **Clause-Level Polarity Extraction with Negation Handling** |
| **Recommendations** | Sponsored listings or popularity bias | **Multi-Attribute Utility Matching with Transparent Trade-Off Explanations** |
| **Benchmarking** | Manual tab switching between destinations | **Side-by-Side Comparative Aspect Analytics** |
| **Data Integrity** | Prone to noisy zero-score penalties | **Null-Safe Missing Aspect Handling (`No data yet`)** |

---

## 5. Technology Stack

- **Presentation Layer:** React 18 SPA, Vite, Recharts (Radar, Pie, Bar, Line charts), Lucide React Icons, Vanilla CSS design tokens.
- **Application & API Layer:** Python 3.10+, FastAPI (ASGI asynchronous service), Pydantic v2 schemas.
- **Data & Storage Layer:** SQLAlchemy 2.0 ORM, SQLite (development) / PostgreSQL (production), Joblib model serialization.
- **Machine Learning & NLP:** Scikit-learn (TF-IDF vectorizer + Multinomial Logistic Regression), Regex tokenizer, Contraction expander.
- **Security & Crypto:** Passlib (bcrypt 12-round hashing), Python-Jose (stateless HS256 JWT tokens).

---

## 6. System Architecture

TRAVELENS adheres strictly to a **Decoupled 3-Tier Enterprise Architecture**:

```
[ TRAVELER / USER ]
        │
        ▼
[ TIER 1: REACT 18 SPA ] ──────────── (Vite + Recharts + Vanilla CSS)
        │
        ▼ HTTP REST / JSON contracts
[ TIER 2: FASTAPI REST SERVICE ] ──── (ASGI Async Controllers & Security)
        ├── Application Services ──── (Analytics, Recommendation, Auth)
        └── ASTMA ML Engine ───────── (TF-IDF + Logistic Regression + 9-Aspect Engine)
        │
        ▼ SQLAlchemy 2.0 ORM
[ TIER 3: DATA LAYER ] ────────────── (Relational DB & Serialized Model Artifacts)
```

### 6.1 Project Directory Structure

```text
Tourism Review/
├── backend/
│   ├── alembic/                # Database migrations
│   ├── app/
│   │   ├── api/                # FastAPI endpoint routers (destinations, reviews, etc.)
│   │   ├── core/               # Configuration, security, JWT helpers
│   │   ├── db/                 # Database connection and SQLAlchemy models
│   │   ├── ml/                 # Model training, inference, preprocessing pipeline
│   │   ├── schemas/            # Pydantic request/response validation schemas
│   │   └── services/           # Analytics, recommendation, aspect analysis
│   ├── data/                   # Raw, processed, and seed review CSV datasets
│   ├── models/                 # Serialized TF-IDF vectorizer & Logistic Regression models
│   ├── scripts/                # Database population and corpus generation scripts
│   ├── tests/                  # 78 comprehensive pytest unit and regression tests
│   ├── alembic.ini             # Alembic migration configuration
│   └── requirements.txt        # Backend Python dependencies
├── frontend/
│   ├── public/                 # Static assets
│   ├── src/
│   │   ├── components/         # Reusable UI components & navigation
│   │   ├── context/            # Auth & bookmark state providers
│   │   ├── pages/              # Views (Home, Explore, DestinationDetail, Compare, etc.)
│   │   ├── services/           # Axios/Fetch API client wrappers
│   │   └── styles/             # Modular CSS design system tokens
│   ├── package.json            # Node.js dependencies and scripts
│   └── vite.config.js          # Vite build configuration
├── docs/
│   ├── diagrams/               # Architecture and workflow diagrams
│   └── screenshots/            # Verified end-to-end user journey screenshots
├── .env.example                # Safe environment variable template
├── .gitignore                  # Security-first Git exclusion rules
├── requirements.txt            # Root Python dependencies pointer
└── README.md                   # Complete system documentation
```

---

## 7. ASTMA Methodology

The **Aspect-Sentiment Tourism Mining & Analytics (ASTMA)** pipeline processes reviews as follows:
1. **Text Preprocessing:** Contraction expansion (`wasn't` $\rightarrow$ `was not`), case normalization, punctuation filtering, and stopword removal preserving negation tokens (`not`, `never`, `cannot`).
2. **Numerical Vectorization:** Sublinear TF-IDF vectorizer extracting unigrams and bigrams (`ngram_range=(1, 2)`, 8,000 maximum features).
3. **Sentiment Classification:** Multinomial Logistic Regression with $L_2$ regularization ($C=1.0$) predicting Positive, Neutral, or Negative polarity.
4. **Aspect Extraction:** Clause-level semantic matching across 9 tourism dimensions:
   - *Attractions, Food, Cleanliness, Price, Crowd, Safety, Transport, Accommodation, Hospitality*.
5. **Negation Inversion:** Context-window parsing inverting polarity for negated clauses (e.g. *"not clean"* $\rightarrow$ Negative).
6. **Keyphrase Extraction:** Corpus-level TF-IDF extraction highlighting destination characteristics.

---

## 8. Academic Alignment

- **Enterprise Systems (ES):** 3-tier decoupling, RESTful service-oriented design, MVC pattern, ORM data mapping, stateless JWT authentication, Role-Based Access Control (RBAC).
- **Text Mining & Analytics (ASTMA):** Tokenization, feature extraction, supervised text classification, precision, recall, macro F1, confusion matrix evaluation, rule-based aspect extraction, information visualization.
- **IT Project Management (ITPM):** Feasibility study, Work Breakdown Structure (WBS), project scheduling, PERT/CPM critical path analysis, risk management matrix, agile sprint delivery, quality gates.

---

## 9. Dataset & Provenance Attribution

- **Corpus Name:** TripAdvisor Hotel & Tourism Reviews Benchmark Dataset (`argilla/tripadvisor-hotel-reviews`).
- **Repository:** Hugging Face Hub (curated and published by Argilla).
- **Licensing:** Creative Commons Attribution-NonCommercial 4.0 International (**CC-BY-NC-4.0**).
- **Scale:** 20,491 raw reviews; filtered to a balanced 6,000-sample working benchmark (2,000 positive, 2,000 neutral, 2,000 negative).
- **Academic Disclaimer:** This application is an independent educational engineering prototype developed strictly for academic evaluation. It uses a static, pre-existing research benchmark and does **not** connect live to TripAdvisor or scrape live web data. TRAVELENS is not affiliated with, endorsed by, or sponsored by TripAdvisor LLC.

---

## 10. Empirical Model Evaluation

Evaluated on the **1,200 held-out test samples** (400 per class, 80/20 train/test split):

| Evaluation Metric | Baseline (Phase 2, 150 samples) | Final Model (Phase 3, 6,000 samples) | Absolute Delta |
| :--- | :---: | :---: | :---: |
| **Accuracy** | 60.00% | **74.50%** | **+14.50%** |
| **Macro Precision** | 0.6071 | **0.7467** | **+0.1396** |
| **Macro Recall** | 0.6000 | **0.7450** | **+0.1450** |
| **Macro F1-Score** | 0.5926 | **0.7458** | **+0.1532** |

### Confusion Matrix (1,200 Test Samples):
$$\begin{array}{c|ccc}
\text{Actual \ Predicted} & \textbf{Negative} & \textbf{Neutral} & \textbf{Positive} \\
\hline
\textbf{Negative (400)} & 315 & 75 & 10 \\
\textbf{Neutral (400)}  & 79 & 260 & 61 \\
\textbf{Positive (400)} & 5 & 76 & 319 \\
\end{array}$$

*Extreme class discrimination is exceptionally high: only 10 negatives were misclassified as positive (2.5%) and only 5 positives as negative (1.25%).*

---

## 11. Installation & Setup Guide

### Prerequisites
- Python 3.10 or higher
- Node.js 18 or higher (with NPM)

### 11.1 Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create and activate virtual environment
python -m venv .venv

# On Windows (PowerShell):
.venv\Scripts\Activate.ps1
# On macOS / Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Seed the database with destinations and review corpus
python scripts/seed_db.py

# Run automated test suite (78 tests)
python -m pytest tests -v

# Start backend server (starts on http://127.0.0.1:8000)
uvicorn app.main:app --reload --port 8000
```

### 11.2 Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Run linter
npm run lint

# Build production bundle
npm run build

# Start local development server (starts on http://localhost:5173)
npm run dev
```

---

## 12. Visual Interface & Screenshots

Comprehensive UI screenshots documenting all major flows are stored in [`docs/screenshots/`](docs/screenshots/):

| View | Screenshot Preview | Description |
| :--- | :--- | :--- |
| **Home & Overview** | `docs/screenshots/01_homepage.png` | Landing view showcasing platform capabilities and featured spots |
| **Explore Destinations** | `docs/screenshots/02_explore_destinations.png` | Search, filtering by category (Cultural, Nature, Urban), and ratings |
| **Aspect Analytics** | `docs/screenshots/05_destination_aspect_analysis.png` | 9-Dimension radar chart, sentiment distribution, and breakdown |
| **Review Analyzer** | `docs/screenshots/10_review_analyzer_positive.png` | Live ML inference on custom tourist reviews with polarity clauses |
| **Destination Comparison**| `docs/screenshots/07_destination_comparison.png` | Side-by-side benchmarking of two destinations across 9 aspects |
| **Personalized Recommendations**| `docs/screenshots/09_personalized_recommendations.png` | Multi-criteria utility ranking based on 1–5 priority sliders |

---

## 13. REST API Overview

| Endpoint | Method | Auth Required | Description |
| :--- | :---: | :---: | :--- |
| `/api/health` | GET | No | System health and ML model status |
| `/api/destinations` | GET | No | List destinations with search & category filters |
| `/api/destinations/{id}` | GET | No | Get single destination profile |
| `/api/destinations/{id}/analytics`| GET | No | 9-Aspect scores, rating, sentiment distribution |
| `/api/destinations/{id}/trends` | GET | No | Monthly review volume and rating trends |
| `/api/destinations/{id}/keywords`| GET | No | TF-IDF salient destination keyphrases |
| `/api/destinations/{id}/reviews` | GET | No | Paginated reviews with rating/sentiment/aspect filter |
| `/api/analyze-review` | POST | No | Real-time ASTMA text mining and aspect inference |
| `/api/recommendations` | POST | No | Multi-criteria utility ranking based on 1–5 priorities |
| `/api/auth/register` | POST | No | User registration with bcrypt hashing |
| `/api/auth/login` | POST | No | User login issuing stateless HS256 JWT |
| `/api/auth/me` | GET | Yes | Current authenticated user profile |
| `/api/saved-destinations` | GET | Yes | List saved destinations for user |
| `/api/saved-destinations` | POST | Yes | Bookmark a destination |
| `/api/saved-destinations/{id}` | DELETE | Yes | Remove a bookmarked destination |

---

## 14. Project Limitations

1. **Static Research Benchmark:** Relies on the static Argilla TripAdvisor benchmark rather than live scraping (intentional design ensuring legal and ethical compliance).
2. **Rule-Based Aspect Extraction:** Uses domain-specific seed lexicons and clause parsing rather than heavy transformer dependency parsers (ensures sub-10ms response time on commodity CPUs).
3. **English Language Scope:** Trained and evaluated strictly on English-language travel reviews.

---

## 15. Future Scope (Planned Enhancements)

- Integration of multilingual transformer models (e.g., XLM-RoBERTa) for cross-lingual tourism review mining.
- Expansion to live verified open data APIs (e.g. OpenStreetMap metadata, approved tourism board feeds).
- Geospatial mapping integration with interactive destination boundaries.
- Continuous active-learning retraining pipelines with user feedback loops.

---

## 16. Academic Submission Details

- **Academic Project:** TRAVELENS — Tourism Destination Review Analyzer
- **Author / Candidate:** Final Year Software Engineering / Data Analytics
- **Evaluation Status:** **SUBMISSION READY (All 7 Phases Completed)**
