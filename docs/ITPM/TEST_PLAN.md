# TEST_PLAN.md — Master Software Test Plan

**Project Name:** TRAVELENS — Tourism Destination Review Analyzer  
**Academic Module:** IT Project Management (ITPM)  
**Standard:** IEEE 829 Software Test Documentation Standard  
**Test Suite Status:** 50/50 AUTOMATED TESTS PASSING (100% PASS RATE)  

---

## 1. Test Strategy & Scope

The Master Test Plan establishes a multi-tiered verification methodology ensuring all functional features, machine learning inferences, security controls, and responsive user interfaces are rigorously validated.

### 1.1 In-Scope Test Categories
- **Unit Testing:** Individual verification of NLP preprocessor, TF-IDF vectorizer, Logistic Regression classifier, password hashing, and token generation.
- **Integration Testing:** API route controllers communicating with application services, database ORM sessions, and serialized model binaries.
- **Security Testing:** Probing for SQL injection, unauthorized endpoint access, role enforcement, and token tampering.
- **End-to-End (E2E) Browser Testing:** User journey execution through the React frontend using the Antigravity Browser Agent.
- **Performance & Latency Profiling:** Measurement of cold-start vs steady-state model inference and HTTP round-trip latencies.
- **Cross-Viewport Responsive Testing:** Layout verification on Desktop (1440px), Tablet (768px), and Mobile (390px).

---

## 2. Test Levels & Execution Environment

| Test Level | Tooling / Framework | Target Component | Execution Environment |
| :--- | :--- | :--- | :--- |
| **Unit & Integration** | `pytest 8.3+`, `httpx`, `TestClient` | Backend services, ML pipeline, API routes | Python 3.10+, SQLite in-memory test database |
| **Security Probes** | Automated Python test scripts | SQL injection, JWT validation, RBAC | Local ASGI server (`http://127.0.0.1:8000`) |
| **Frontend Production Build** | Vite v5 / v8 bundler | React 18 SPA, JavaScript modules, Vanilla CSS | Node.js v18+, NPM |
| **End-to-End (E2E)** | Antigravity Autonomous Browser Agent | Complete user workflow across UI views | Chromium headless browser |
| **Mathematical Recount** | SQLite CLI & Python direct queries | Aggregate destination analytics & percentages | Local SQLite database file |

---

## 3. Test Entry and Exit Criteria

### 3.1 Entry Criteria
- Source code formatted and free of syntax errors.
- Pre-trained ML model binaries (`sentiment_classifier.joblib`, `tfidf_vectorizer.joblib`) present in `backend/models/`.
- Seed database initialized with destination and review records.
- Backend server and frontend development/build environments initialized.

### 3.2 Exit Criteria (All Met for Phase 6/7)
- 100% passing rate on the 50 automated pytest cases ($0\text{ failures}$).
- Clean production build with $0\text{ bundling errors}$.
- 12 out of 12 live API endpoints verified with expected HTTP status codes.
- Zero Critical or High security vulnerabilities.
- Complete browser journey completed without console errors.

---

## 4. Test Execution Summary

```
================================================================================
Test Category             Total Cases   Passed   Failed   Pass Rate
================================================================================
Backend API & Routing          12         12        0       100.0%
Authentication & Security      10         10        0       100.0%
ASTMA NLP & ML Engine          14         14        0       100.0%
Recommendation Engine           6          6        0       100.0%
Saved Destinations              5          5        0       100.0%
Database & Cascade Deletes      3          3        0       100.0%
--------------------------------------------------------------------------------
TOTAL AUTOMATED TESTS          50         50        0       100.0%
================================================================================
Browser E2E Multi-Viewport      1          1        0       100.0%
Live HTTP API Boundary Suite   12         12        0       100.0%
================================================================================
```
