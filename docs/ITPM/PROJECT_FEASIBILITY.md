# PROJECT_FEASIBILITY.md — Project Feasibility Study

**Project Name:** TRAVELENS — Tourism Destination Review Analyzer  
**Academic Module:** IT Project Management (ITPM)  
**Evaluation Standard:** TELOS Feasibility Framework (Technical, Economic, Legal, Operational, Schedule)  

---

## 1. Executive Feasibility Summary

The objective of the TRAVELENS project was to evaluate the technical and operational viability of building an Aspect-Sentiment Tourism Mining & Analytics (ASTMA) platform. Conventional tourism websites present aggregate star ratings that obscure critical trade-offs (e.g. a destination with a 4.5-star rating may have outstanding cultural attractions but severe overcrowding or excessive pricing). TRAVELENS demonstrates the feasibility of decomposing natural language tourist feedback into 9 explainable tourism dimensions using a decoupled 3-tier enterprise architecture.

---

## 2. TELOS Feasibility Analysis

### 2.1 Technical Feasibility (Rating: HIGH / ACHIEVABLE)
- **Requirement:** High-speed text processing, sentiment inference, and interactive visualization without specialized GPU hardware.
- **Evaluation:**
  - **Machine Learning:** Evaluated deep learning transformer models (BERT/RoBERTa) vs classical TF-IDF with Multinomial Logistic Regression. Selected TF-IDF + Logistic Regression due to CPU feasibility, deterministic reproducibility, low RAM footprint, and sub-10ms inference latency.
  - **Backend Layer:** FastAPI (Python 3.10+) provides native asynchronous handling, Pydantic v2 data contract validation, and ASGI lifespan event hooks.
  - **Frontend Layer:** React 18 SPA coupled with Vite delivers rapid build times and responsive rendering through Recharts without heavy commercial UI framework overhead.
  - **Verdict:** Fully feasible using widely available, open-source enterprise libraries.

### 2.2 Economic Feasibility (Rating: HIGH / ZERO-BUDGET)
- **Expenditure Constraints:** Student academic project conducted with $0 external funding.
- **Resource Allocation:**
  - Database: Open-source SQLite (development) and PostgreSQL (production).
  - Web Server & Tools: Node.js, Python, Vite, and Git are completely open-source.
  - Hosting/Infrastructure: Runs locally on standard commodity developer workstations.
- **Verdict:** Highly economically feasible with zero licensing or subscription liabilities.

### 2.3 Legal & Ethical Feasibility (Rating: COMPLIANT)
- **Data Compliance:** Commercial scraping of live consumer review platforms (e.g. TripAdvisor, Google Maps) violates platform Terms of Service (ToS) and risks intellectual property infringement.
- **Mitigation:** Utilized the static, pre-existing, and anonymized **TripAdvisor Hotel & Tourism Reviews Benchmark Dataset** published by Argilla on Hugging Face under the **Creative Commons Attribution-NonCommercial 4.0 International (CC-BY-NC-4.0)** license.
- **Academic Disclaimers:** Explicit disclaimers prominently embedded in site footers and about pages declaring independent educational research status with zero affiliation to TripAdvisor LLC.
- **Verdict:** Fully compliant with academic integrity, copyright, and data privacy standards.

### 2.4 Operational Feasibility (Rating: HIGH / USER-CENTRIC)
- **User Personas:** Independent travelers, vacation planners, and academic evaluators seeking granular insights rather than generic 5-star ratings.
- **Usability:** System requires zero technical knowledge from users. Sliders (1–5) and search boxes provide intuitive inputs, while radar charts and badges convey complex multi-dimensional sentiment metrics instantly.
- **Verdict:** High operational utility and adoption potential.

### 2.5 Schedule Feasibility (Rating: ACHIEVABLE ACADEMIC TIMELINE)
- **Lifecycle:** Structured across 6 sequential milestones spanning 6 development sprints.
- **Milestone Gating:** Strict phase exit criteria ensured no premature frontend development occurred before the database and ML engines were verified.
- **Verdict:** Project was delivered within planned academic milestones.
