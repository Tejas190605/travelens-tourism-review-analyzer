# RISK_REGISTER.md — Project Risk Management Matrix

**Project Name:** TRAVELENS — Tourism Destination Review Analyzer  
**Academic Module:** IT Project Management (ITPM)  
**Standard:** ISO 31000 Risk Management Framework  
**Scoring System:** Probability (1: Rare to 5: Frequent) $\times$ Impact (1: Negligible to 5: Catastrophic) = Risk Score (1–25)  

---

## 1. Risk Register & Mitigation Matrix

| Risk ID | Risk Description | Category | Prob (1–5) | Impact (1–5) | Risk Score | Preventative Mitigation Strategy | Contingency Plan | Status |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- | :--- | :---: |
| **RSK-01** | **Dataset Licensing Infringement**<br>Scraping live TripAdvisor data risks ToS violation and copyright issues. | Legal / Ethics | 4 | 5 | **20** (High) | Discard live scraping. Adopt pre-existing Hugging Face open benchmark (`argilla/tripadvisor-hotel-reviews`). | Embed clear CC-BY-NC-4.0 academic disclaimers on UI and documentation. | **CLOSED / MITIGATED** |
| **RSK-02** | **Class Imbalance in Tourism Reviews**<br>Real reviews are heavily skewed towards 5 stars, causing classifier majority bias. | ML Quality | 4 | 4 | **16** (High) | Implement automated stratified downsampling in `ingestion.py` to achieve exact 1:1:1 balance (2,000 per class). | Use `class_weight='balanced'` in Logistic Regression as secondary protection. | **CLOSED / MITIGATED** |
| **RSK-03** | **Cold-Start Model Latency**<br>First user request takes >100ms due to dynamic on-demand model loading. | Performance | 4 | 3 | **12** (Med) | Implement FastAPI `@asynccontextmanager` lifespan event pre-warming the vectorizer and classifier during startup. | Provide loading spinner in React frontend. | **CLOSED / MITIGATED** |
| **RSK-04** | **Subpar ML Model Accuracy**<br>Baseline model on small corpus (150 samples) achieved only 60.0% accuracy. | Quality | 4 | 4 | **16** (High) | Scale training dataset to 6,000 balanced benchmark samples; perform 5-fold CV to select bigram TF-IDF features. | Accept realistic empirical accuracy (74.5%) rather than fabricating inflated numbers. | **CLOSED / MITIGATED** |
| **RSK-05** | **SQL Injection Vulnerabilities**<br>User text inputs in search and review explorer could compromise database. | Security | 2 | 5 | **10** (Med) | Enforce 100% SQLAlchemy 2.0 declarative ORM parameter binding; strictly ban raw SQL string interpolation. | Database transaction rollbacks on unexpected query syntax errors. | **CLOSED / MITIGATED** |
| **RSK-06** | **Credential & Secret Leakage**<br>Accidental check-in of passwords or JWT secret keys to version control. | Security | 3 | 4 | **12** (Med) | Enforce `.gitignore` exclusion of `.env` and `*.db`; generate cryptographic pseudorandom fallback keys. | Rotate secrets immediately and invalidate active sessions. | **CLOSED / MITIGATED** |
| **RSK-07** | **Frontend/Backend Contract Mismatch**<br>Changes in API JSON schema break React component rendering. | Integration | 3 | 4 | **12** (Med) | Strict Pydantic v2 schemas for all request/response models; unified `frontend/src/services/api.js` client. | Fallback default values and graceful React error boundaries. | **CLOSED / MITIGATED** |
| **RSK-08** | **Scope Creep (Unrelated Features)**<br>Pressures to add live booking, maps, payment gateways, or deep neural networks. | Scope / Schedule | 4 | 3 | **12** (Med) | Enforce strict phase boundaries via `AGENTS.md`; prohibit out-of-scope feature development. | Relegate non-core features explicitly to academic "Future Scope". | **CLOSED / MITIGATED** |
| **RSK-09** | **Missing Aspect Data Distortion**<br>Destinations with 0 reviews for an aspect get penalized with a 0/100 score. | Data Integrity | 3 | 3 | **9** (Med) | Service returns `null` for missing aspects; UI renders `"No data yet"` instead of false 0/100 bar. | Exclude unmentioned aspects from weighted utility recommendation calculations. | **CLOSED / MITIGATED** |
| **RSK-10** | **Database Concurrency & Lockups**<br>Simultaneous write operations in SQLite during automated testing. | Technical | 2 | 3 | **6** (Low) | Configure scoped session lifecycles and WAL journal mode; design models for seamless PostgreSQL migration. | In-memory SQLite session override during automated pytest runs. | **CLOSED / MITIGATED** |

---

## 2. Risk Severity Matrix (Pre- vs Post-Mitigation)

```
        Impact ->   1 (Neg)   2 (Low)   3 (Med)   4 (High)   5 (Crit)
Prob v
5 (Freq)     |         |         |         |          |
4 (Likely)   |         |         |         | [RSK-02]*| [RSK-01]*
3 (Poss)     |         |         |         | [RSK-04]*|
2 (Unlikely) |         |         | [RSK-10]| [RSK-06]*| [RSK-05]*
1 (Rare)     |         |         |         |          |

*Note: All High and Critical risks (RSK-01, RSK-02, RSK-04, RSK-05, RSK-06) were successfully mitigated and closed during Phase 3, Phase 5, and Phase 6.*
```
