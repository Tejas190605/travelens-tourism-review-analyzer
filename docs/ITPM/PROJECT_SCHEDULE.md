# PROJECT_SCHEDULE.md — Project Schedule & PERT/CPM Analysis

**Project Name:** TRAVELENS — Tourism Destination Review Analyzer  
**Academic Module:** IT Project Management (ITPM)  
**Methodology:** Program Evaluation and Review Technique (PERT) & Critical Path Method (CPM)  
**Timeline Nature:** Reconstructed Academic Engineering Schedule (Working Days)  
*Note: All durations represent planned and reconstructed academic working days; historical values are clearly identified as estimates.*

---

## 1. Project Activity & Schedule Network Table

| Activity ID | Activity Description | Immediate Predecessors | Optimistic ($o$) | Most Likely ($m$) | Pessimistic ($p$) | Expected Time ($T_E$) | Variance ($\sigma^2$) | Deliverable |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **A** | Problem Formulation & Feasibility Study | — | 2 | 3 | 5 | **3.17** | 0.25 | Feasibility Report |
| **B** | Requirements Elicitation & Blueprint | A | 3 | 4 | 7 | **4.33** | 0.44 | `PROJECT_BLUEPRINT.md` |
| **C** | Architecture Design & System Modeling | B | 2 | 3 | 5 | **3.17** | 0.25 | Architecture Specs |
| **D** | Backend Scaffolding & Database Engine | C | 3 | 5 | 8 | **5.17** | 0.69 | `backend/app/db/` & DB Seed |
| **E** | ASTMA Data Ingestion & Preprocessing | D | 2 | 3 | 6 | **3.33** | 0.44 | Cleaned 6,000 Dataset |
| **F** | TF-IDF & Logistic Regression Model Training | E | 3 | 4 | 7 | **4.33** | 0.44 | `sentiment_classifier.joblib` |
| **G** | 9-Aspect Semantic Extraction Engine | E | 2 | 4 | 6 | **4.00** | 0.44 | `aspect_extractor.py` |
| **H** | REST API Endpoints & Analytics Services | F, G | 3 | 4 | 6 | **4.17** | 0.25 | 12 REST Endpoints |
| **I** | Frontend Scaffolding & Design System | C | 2 | 3 | 5 | **3.17** | 0.25 | Vite + Vanilla CSS |
| **J** | Core Frontend UI Views (Explore, Details) | H, I | 4 | 6 | 9 | **6.17** | 0.69 | React Detail & Charts |
| **K** | User Features (Auth, Saved, Recommend) | J | 3 | 5 | 8 | **5.17** | 0.69 | Rec Wizard & JWT State |
| **L** | Integration Hardening & Lifespan Pre-warming | K | 2 | 3 | 5 | **3.17** | 0.25 | Sub-20ms Latency |
| **M** | Quality Assurance Testing (Pytest Suite) | L | 2 | 3 | 6 | **3.33** | 0.44 | 50 Passing Tests |
| **N** | Security Audit & OWASP Verification | L | 2 | 3 | 5 | **3.17** | 0.25 | `SECURITY_AUDIT.md` |
| **O** | Final Academic Documentation & Viva Package | M, N | 3 | 4 | 7 | **4.33** | 0.44 | `README.md` & Submission Package |

---

## 2. PERT Mathematical Calculations

The PERT Expected Duration ($T_E$) and Task Variance ($\sigma^2$) are calculated according to the standard beta distribution:

$$T_E = \frac{o + 4m + p}{6}$$
$$\sigma^2 = \left(\frac{p - o}{6}\right)^2$$

### Critical Path Method (CPM) Forward & Backward Pass Analysis

```
Network Paths from Initiation (A) to Project Closure (O):
Path 1: A -> B -> C -> I -> J -> K -> L -> M -> O
Path 2: A -> B -> C -> D -> E -> F -> H -> J -> K -> L -> M -> O  [CRITICAL PATH]
Path 3: A -> B -> C -> D -> E -> G -> H -> J -> K -> L -> M -> O
Path 4: A -> B -> C -> D -> E -> F -> H -> J -> K -> L -> N -> O
```

### Path Length Summary
- **Path 1 (via Frontend Scaffolding I):**
  $3.17 + 4.33 + 3.17 + 3.17 + 6.17 + 5.17 + 3.17 + 3.33 + 4.33 = \mathbf{36.00\text{ days}}$
- **Path 2 (via ML Training F & QA M):**
  $3.17 + 4.33 + 3.17 + 5.17 + 3.33 + 4.33 + 4.17 + 6.17 + 5.17 + 3.17 + 3.33 + 4.33 = \mathbf{44.52\text{ days}}$
- **Path 3 (via Aspect Engine G & QA M):**
  $3.17 + 4.33 + 3.17 + 5.17 + 3.33 + 4.00 + 4.17 + 6.17 + 5.17 + 3.17 + 3.33 + 4.33 = \mathbf{44.19\text{ days}}$
- **Path 4 (via Security Audit N):**
  $3.17 + 4.33 + 3.17 + 5.17 + 3.33 + 4.33 + 4.17 + 6.17 + 5.17 + 3.17 + 3.17 + 4.33 = \mathbf{44.36\text{ days}}$

---

## 3. Critical Path Identification

$$\mathbf{\text{Critical Path: }} \mathbf{A \rightarrow B \rightarrow C \rightarrow D \rightarrow E \rightarrow F \rightarrow H \rightarrow J \rightarrow K \rightarrow L \rightarrow M \rightarrow O}$$

- **Total Critical Path Duration ($T_{\text{CP}}$):** **44.52 working days** ($\approx 9$ academic calendar weeks).
- **Critical Path Variance ($\sigma^2_{\text{CP}}$):**
  $$\sigma^2_{\text{CP}} = 0.25 + 0.44 + 0.25 + 0.69 + 0.44 + 0.44 + 0.25 + 0.69 + 0.69 + 0.25 + 0.44 + 0.44 = \mathbf{5.27}$$
- **Critical Path Standard Deviation ($\sigma_{\text{CP}}$):**
  $$\sigma_{\text{CP}} = \sqrt{5.27} \approx \mathbf{2.30\text{ working days}}$$

### Schedule Probability Analysis
To determine the probability of completing the project within a target deadline $T_D = 48\text{ working days}$:
$$Z = \frac{T_D - T_{\text{CP}}}{\sigma_{\text{CP}}} = \frac{48 - 44.52}{2.30} = \frac{3.48}{2.30} \approx +1.51$$
From standard normal distribution tables, $P(Z \le 1.51) \approx \mathbf{93.4\%}$ probability of on-time completion within planned academic deadlines.

---

## 4. Float / Slack Analysis

| Activity | Early Start (ES) | Early Finish (EF) | Late Start (LS) | Late Finish (LF) | Total Float ($TF = LS - ES$) | Critical? |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **A** | 0.00 | 3.17 | 0.00 | 3.17 | **0.00** | **YES** |
| **B** | 3.17 | 7.50 | 3.17 | 7.50 | **0.00** | **YES** |
| **C** | 7.50 | 10.67 | 7.50 | 10.67 | **0.00** | **YES** |
| **D** | 10.67 | 15.84 | 10.67 | 15.84 | **0.00** | **YES** |
| **E** | 15.84 | 19.17 | 15.84 | 19.17 | **0.00** | **YES** |
| **F** | 19.17 | 23.50 | 19.17 | 23.50 | **0.00** | **YES** |
| **G** | 19.17 | 23.17 | 19.50 | 23.50 | **0.33** | NO |
| **H** | 23.50 | 27.67 | 23.50 | 27.67 | **0.00** | **YES** |
| **I** | 10.67 | 13.84 | 24.50 | 27.67 | **13.83** | NO |
| **J** | 27.67 | 33.84 | 27.67 | 33.84 | **0.00** | **YES** |
| **K** | 33.84 | 39.01 | 33.84 | 39.01 | **0.00** | **YES** |
| **L** | 39.01 | 42.18 | 39.01 | 42.18 | **0.00** | **YES** |
| **M** | 42.18 | 45.51 | 42.18 | 45.51 | **0.00** | **YES** |
| **N** | 42.18 | 45.35 | 42.34 | 45.51 | **0.16** | NO |
| **O** | 45.51 | 49.84 | 45.51 | 49.84 | **0.00** | **YES** |
