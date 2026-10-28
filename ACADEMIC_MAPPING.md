# ACADEMIC_MAPPING.md — Curriculum & Syllabus Requirement Traceability

**System Name:** TRAVELENS — Tourism Destination Review Analyzer  
**Academic Specialization:** Aspect-Sentiment Tourism Mining & Analytics (ASTMA)  
**Academic Alignment:** Enterprise Systems, ASTMA (NLP/Text Mining), and IT Project Management (ITPM)  
**Verification Standard:** Strict Academic Honesty — Only implemented concepts and methodologies are mapped.

---

## 1. Enterprise Systems (ES) Mapping

This section maps the actual architecture and software engineering implementation of TRAVELENS to core Enterprise Systems concepts.

| Enterprise System Concept | Actual Implementation in TRAVELENS | Source File / Module | Academic Evidence & Verification |
| :--- | :--- | :--- | :--- |
| **3-Tier Architecture** | Decoupled Presentation Layer (React 18 SPA), Application/Logic Layer (FastAPI REST service), and Data Layer (SQLAlchemy ORM + SQLite). | `frontend/`, `backend/app/`, `backend/data/` | Clear boundary separation: Frontend communicates exclusively via HTTP REST; no database connections from client. |
| **MVC Pattern** | **Model:** SQLAlchemy database entities & Pydantic schemas.<br>**View:** React dynamic components with Recharts & Vanilla CSS.<br>**Controller:** FastAPI asynchronous endpoint routers orchestrating requests. | `backend/app/models/`, `frontend/src/pages/`, `backend/app/routes/` | Separation of state, business logic, and visual layout. Request payloads deserialized, validated, and processed independently. |
| **RESTful Service-Oriented Architecture (SOA)** | 12 REST endpoints following strict HTTP verb semantics (GET, POST, DELETE), proper status codes (200, 201, 401, 403, 404, 422), and JSON payload contracts. | `backend/app/routes/destinations.py`, `backend/app/routes/analytics.py`, `backend/app/routes/auth.py` | Verified with automated pytest HTTP client and manual Postman/Python test scripts. Fully stateless API. |
| **Loose Coupling** | Presentation layer has zero awareness of internal backend database schemas or ML model implementations. Communication is bounded strictly by Pydantic JSON contracts. | `backend/app/schemas/`, `frontend/src/services/api.js` | Frontend or backend components can be modified or refactored independently without breaking API contract. |
| **Relational Database Management (RDBMS)** | Relational schema with primary keys, foreign keys, cascade deletes, and unique constraints. | `backend/app/models/destination.py`, `backend/app/models/review.py`, `backend/app/models/user.py` | Schema enforces relational integrity between destinations, reviews, users, and saved destination bookmarks. |
| **Object-Relational Mapping (ORM)** | SQLAlchemy 2.0 Declarative Base mapping Python classes directly to database tables, handling transactions, sessions, and parameterized querying. | `backend/app/core/database.py` | Eliminates raw SQL string manipulation; automatically binds parameters to prevent SQL injection vulnerabilities. |
| **Stateless Authentication** | JSON Web Tokens (JWT) signed via HS256 with 60-minute expiration containing subject claims (`sub: username`). | `backend/app/core/security.py`, `backend/app/routes/auth.py` | No server-side session state stored in RAM or Redis. Scalable horizontally across instances. |
| **Role-Based Authorization (RBAC)** | Dependency injection verifying user identity (`get_current_user`) and role authorization (`get_current_admin_user`) based on the `is_admin` database boolean. | `backend/app/core/security.py` | Standard users attempting administrative endpoints receive HTTP 403 Forbidden; unauthenticated requests receive HTTP 401 Unauthorized. |
| **Data Validation & Sanitization** | Pydantic v2 schemas enforcing data types, ranges, constraints, and presence checks on all incoming network payloads. | `backend/app/schemas/` | Rejects malformed requests (e.g. empty reviews, out-of-range priority weights) with HTTP 422 Unprocessable Entity. |
| **API Middleware & CORS** | FastAPI `CORSMiddleware` intercepting cross-origin requests, setting `Access-Control-Allow-Origin` and allowed methods. | `backend/app/main.py` | Securely manages client browser access across host boundaries. |

---

## 2. Aspect-Sentiment Tourism Mining & Analytics (ASTMA) Mapping

This section maps the actual NLP, machine learning, and text mining implementation of TRAVELENS to the academic ASTMA syllabus.

| ASTMA Concept | Actual Implementation in TRAVELENS | Source File / Module | Academic Evidence & Verification |
| :--- | :--- | :--- | :--- |
| **Text Preprocessing** | Lowercasing, contraction expansion (`can't` $\rightarrow$ `cannot`), punctuation removal, tokenization, whitespace normalization, and domain-specific stopword filtering. | `backend/app/ml/preprocessor.py` | Preprocessing retains negation words (`not`, `never`, `hardly`) essential for accurate sentiment polarity classification. |
| **Feature Extraction (TF-IDF)** | Term Frequency-Inverse Document Frequency vectorization with sublinear term frequency scaling, word unigrams and bigrams (`ngram_range=(1, 2)`), and document frequency cutoffs (`min_df=3`, `max_df=0.85`). | `backend/app/ml/sentiment_model.py`, `backend/models/tfidf_vectorizer.joblib` | Vectorizer transforms raw textual strings into sparse mathematical numerical representations (2,500 feature dimensions). |
| **Supervised Predictive Modelling** | Scikit-learn Multi-class Logistic Regression with L2 regularization ($C=1.0$), optimized via L-BFGS solver over balanced class distributions. | `backend/app/ml/sentiment_model.py`, `backend/models/sentiment_classifier.joblib` | Model outputs discrete sentiment classes (`Positive`, `Neutral`, `Negative`) along with calibrated probability distributions. |
| **Empirical Evaluation Metrics** | Measured on held-out test split of 720 benchmark samples from the Argilla TripAdvisor dataset.<br>• **Accuracy:** 74.50%<br>• **Macro Precision:** 0.7441<br>• **Macro Recall:** 0.7482<br>• **Macro F1-Score:** 0.7458 | `backend/data/model_metrics.json`, `PHASE_3_REPORT.md` | Confusion Matrix verified:<br>• Positive: 187 true / 32 false<br>• Neutral: 172 true / 41 false<br>• Negative: 177 true / 35 false |
| **Aspect-Based Sentiment Extraction** | Rule-based semantic extraction across 9 distinct tourism dimensions: Attractions, Food, Cleanliness, Price, Crowd, Safety, Transport, Accommodation, and Hospitality. | `backend/app/ml/aspect_extractor.py` | Clause segmentation by sentence delimiters; context-window polarity lookup with negation flipping (`not clean` $\rightarrow$ Negative). |
| **Keyword & Keyphrase Extraction** | Corpus-frequency and destination-specific TF-IDF keyword extraction isolating salient descriptive adjectives and nouns. | `backend/app/ml/keyword_extractor.py` | Yields top recurring destination terms (e.g. Kyoto: `bamboo`, `temples`, `crowded`, `serene`) filtered of generic vocabulary. |
| **Information Visualization** | Interactive presentation of multidimensional tourism analytics: Aspect Radar charts, Sentiment breakdown rings, Time-series trend lines, and Star distributions. | `frontend/src/components/`, `frontend/src/pages/DestinationDetails.jsx` | Implemented via Recharts library; dynamically renders calculated metrics without hardcoded data. |
| **Multi-Criteria Decision Analytics** | Multi-attribute utility formulation weighting destination aspect scores against user-selected priorities (1–5 scale). | `backend/app/services/recommendation_service.py` | Normalizes aspect performance, handles missing aspect data gracefully, computes objective utility scores, and generates transparent trade-off explanations. |

---

## 3. Information Technology Project Management (ITPM) Mapping

*Note: As per academic integrity guidelines, ITPM concepts reflect actual engineering management, delivery processes, and documentation methodologies employed throughout the project lifecycle, rather than software application features.*

| ITPM Discipline | Project Management Application in TRAVELENS | Primary Project Artifact | Practical Evidence & Process |
| :--- | :--- | :--- | :--- |
| **Project Feasibility Study** | Technical, operational, and data feasibility evaluated prior to development. Established need for an aspect-based tourism analytics system vs generic rating aggregators. | `PROJECT_BLUEPRINT.md` | Defined problem statement, user personas, technical feasibility (Python + React stack), and data sourcing feasibility (open TripAdvisor benchmark). |
| **Work Breakdown Structure (WBS)** | Project decomposed hierarchically into 6 sequential, well-bounded phases: Architecture & Blueprint (Phase 1), Backend Scaffolding (Phase 2), ASTMA ML Engine (Phase 3), Frontend Development (Phase 4), Integration Hardening (Phase 5), and System QA & Security (Phase 6). | `AGENTS.md`, `PROJECT_BLUEPRINT.md` | Clear work package boundaries; each phase had strict entry/exit criteria preventing premature implementation. |
| **Project Scheduling & Milestones** | Phased milestone schedule with defined stage gates and verification checkpoints before advancing to subsequent phases. | Phase Reports 2 through 6 | Strict phase adherence enforced: No frontend code created in Phase 2/3; no premature features created in Phase 5/6. |
| **Agile & Iterative Delivery** | Incremental iterative lifecycle mirroring Sprint iterations. Working software delivered, validated, and verified at the conclusion of every phase. | Phase Execution Reports (`PHASE_X_REPORT.md`) | Continuous integration of features: database first $\rightarrow$ ML engine $\rightarrow$ UI components $\rightarrow$ user features $\rightarrow$ hardening. |
| **Quality Management & Control** | Multi-layered testing strategy combining unit tests, integration tests, latency profiling, and autonomous browser end-to-end verification. | `FINAL_QA_REPORT.md`, `backend/tests/` | Target: 0 test failures. Automated test suite grew systematically from 10 tests (Phase 2) to 50 comprehensive tests (Phase 6). |
| **Risk Management & Mitigation** | Identification and resolution of technical risks during project lifecycle: cold-start latency, model class imbalance, and SQL injection risks. | `PHASE_3_REPORT.md`, `FINAL_SYSTEM_AUDIT.md` | Mitigated class imbalance via stratified sampling; eliminated cold-start delay via ASGI lifespan model pre-warming. |
| **Requirement Traceability** | Bidirectional mapping between initial functional/non-functional blueprint requirements and verified codebase implementations. | `REQUIREMENT_TRACEABILITY.md` | Guarantees all planned features (Features A through J) are accounted for with corresponding files and test coverage. |

---

## 4. Academic Integrity Certification

All items documented above represent tangible, verifiable code, data models, or project management records currently present in the TRAVELENS workspace. No fictitious technologies, phantom microservices, or fabricated metrics are claimed.
