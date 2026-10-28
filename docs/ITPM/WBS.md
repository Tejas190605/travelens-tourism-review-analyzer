# WBS.md — Work Breakdown Structure (WBS)

**Project Name:** TRAVELENS — Tourism Destination Review Analyzer  
**Academic Module:** IT Project Management (ITPM)  
**Standard:** Project Management Institute (PMI) WBS Decomposition Standards  
**Scope:** Complete 100% Rule Decomposition of Actual Project Work Packages  

---

## 1. Hierarchical Work Breakdown Structure

```
1.0 TRAVELENS Project Delivery
│
├── 1.1 Project Initiation & Feasibility
│   ├── 1.1.1 Problem formulation & stakeholder identification
│   ├── 1.1.2 TELOS feasibility assessment
│   └── 1.1.3 Dataset selection & CC-BY-NC-4.0 licensing verification
│
├── 1.2 Requirements Engineering & Specification
│   ├── 1.2.1 Functional requirement elicitation (Features A–J)
│   ├── 1.2.2 Non-functional requirement formulation (Decoupling, performance, security)
│   ├── 1.2.3 IEEE 830 system specification document (PROJECT_BLUEPRINT.md)
│   └── 1.2.4 Information architecture & wireframe definition
│
├── 1.3 System & Software Architecture Design
│   ├── 1.3.1 Decoupled 3-tier architectural decomposition
│   ├── 1.3.2 RESTful API contract & JSON schema specification
│   ├── 1.3.3 Relational database schema & ER modeling
│   └── 1.3.4 Security & authentication architecture design (Bcrypt + JWT)
│
├── 1.4 Backend Foundation & Database Development (Phase 2)
│   ├── 1.4.1 FastAPI application scaffolding & configuration management
│   ├── 1.4.2 SQLAlchemy 2.0 ORM entity declaration & migrations
│   ├── 1.4.3 Database seeding with curated destinations & reviews
│   └── 1.4.4 Initial baseline sentiment engine & unit test suite
│
├── 1.5 ASTMA Analytics & Machine Learning Engine (Phase 3)
│   ├── 1.5.1 Automated data cleaning, validation & class equalization pipeline
│   ├── 1.5.2 NLP text preprocessing (contractions, segmentation, negation preservation)
│   ├── 1.5.3 TF-IDF feature engineering & 5-fold cross-validation hyperparameter search
│   ├── 1.5.4 Model training, serialization & baseline comparison (74.5% test accuracy)
│   ├── 1.5.5 9-Aspect semantic clause extraction engine & negation inversion
│   └── 1.5.6 Corpus-level TF-IDF keyword extraction service
│
├── 1.6 Frontend Presentation Layer Development (Phase 4)
│   ├── 1.6.1 React 18 SPA scaffolding with Vite
│   ├── 1.6.2 Editorial Vanilla CSS design system & typography setup
│   ├── 1.6.3 Navigation bar, footer, and responsive layout foundations
│   ├── 1.6.4 Home & Explore catalog views
│   ├── 1.6.5 Destination Details view with Recharts (Radar, Sentiment, Trends)
│   └── 1.6.6 Custom Review Analyzer & Compare views
│
├── 1.7 User Features & System Integration Hardening (Phase 5)
│   ├── 1.7.1 Multi-criteria weighted recommendation wizard
│   ├── 1.7.2 User authentication UI, React AuthContext & persistent sessions
│   ├── 1.7.3 Saved destinations bookmarking & profile management
│   ├── 1.7.4 Performance optimization & ASGI lifespan model pre-warming
│   └── 1.7.5 Comprehensive responsive layout adaptation (Desktop/Tablet/Mobile)
│
├── 1.8 Quality Assurance & Testing (Phase 6)
│   ├── 1.8.1 Automated backend pytest suite implementation (50 passing tests)
│   ├── 1.8.2 Manual HTTP endpoint verification & boundary testing
│   ├── 1.8.3 End-to-end browser user journey validation via Antigravity Agent
│   ├── 1.8.4 Data recount verification (SQLite vs API mathematical integrity)
│   └── 1.8.5 Accessibility and cross-viewport responsive audit
│
├── 1.9 Security & Compliance Audit (Phase 6)
│   ├── 1.9.1 Bcrypt password hashing & salt round verification
│   ├── 1.9.2 JWT expiration, signature verification & tampered token handling
│   ├── 1.9.3 Role-based authorization & administrative endpoint guards
│   ├── 1.9.4 SQL injection resistance testing via ORM parameter binding
│   └── 1.9.5 Secrets exclusion & .gitignore validation
│
└── 1.10 Academic Documentation, Traceability & Viva Preparation (Phase 7)
    ├── 1.10.1 Empirical metrics verification & test discrepancy resolution
    ├── 1.10.2 Comprehensive Project README & technical manual
    ├── 1.10.3 Formal architecture, DFD, ER, Use Case & Sequence diagrams
    ├── 1.10.4 ITPM documentation package (WBS, Schedule, PERT/CPM, Risk, Sprints)
    ├── 1.10.5 Requirement traceability matrix & test cases catalog
    └── 1.10.6 Viva examination questions, answers & user demo script
```

---

## 2. WBS Dictionary (Sample Work Packages)

| WBS Code | Work Package Name | Assigned Responsibility | Primary Deliverable | Acceptance Criteria |
| :---: | :--- | :--- | :--- | :--- |
| **1.4.2** | SQLAlchemy ORM Models | Backend Engineer | `backend/app/db/models.py` | Relational tables created with foreign keys and cascade delete rules. |
| **1.5.3** | TF-IDF & Model Selection | ML Engineer | `backend/app/ml/train.py` | 5-fold CV macro F1 computed; best hyperparameter set selected without test leakage. |
| **1.5.5** | 9-Aspect Extraction Engine | NLP Engineer | `backend/app/ml/aspect_extractor.py` | All 9 aspects extracted with correct negation handling (`not clean` $\rightarrow$ Negative). |
| **1.6.5** | Destination Analytics UI | Frontend Engineer | `frontend/src/pages/DestinationDetails.jsx` | Radar, sentiment ring, and trends accurately render backend data. |
| **1.7.4** | Model Pre-Warming | System Architect | `backend/app/main.py` (`lifespan`) | First-request latency reduced to steady-state sub-20ms. |
| **1.8.1** | Pytest Automation | QA Lead | `backend/tests/` | 50/50 automated test cases pass with zero failures. |
