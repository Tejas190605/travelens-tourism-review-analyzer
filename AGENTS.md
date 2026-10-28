# AGENTS.md — TRAVELENS Development Guidelines

## Project Overview
- **System Name:** TRAVELENS — Tourism Destination Review Analyzer
- **Tech Stack:**
  - Backend: Python 3.10+, FastAPI, Pydantic v2, SQLAlchemy 2.x, Alembic, SQLite (dev) / PostgreSQL (prod).
  - NLP/ML: Scikit-learn (TF-IDF + Logistic Regression), Spacy / NLTK, Joblib.
  - Frontend: React 18 SPA (Vite), Vanilla CSS design system.

## Architectural Constraints
1. **Strict Decoupling:**
   - Presentation (React SPA), Application (FastAPI REST API), and Data (SQLAlchemy / Serialized ML models) layers must remain strictly decoupled.
   - Frontend accesses backend exclusively through REST endpoints (`/api/...`).
2. **Phase Adherence:**
   - Always implement current phase only. Never build premature UI or backend features belonging to future phases.
3. **Data Integrity:**
   - Never fabricate or hard-code fake metrics.
   - Datasets must be clearly labeled as seed/development data unless originating from verified real-world sources.
4. **Security & Secrets:**
   - Never commit `.env` or plaintext passwords.
   - Use bcrypt password hashing and stateless JWT bearer tokens.
5. **Testing & Verification:**
   - Every phase must be verified with executable automated tests (`pytest`) and live HTTP requests.
