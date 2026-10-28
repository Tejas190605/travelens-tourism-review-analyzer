# DFD_DIAGRAMS.md — Data Flow Diagrams (Level 0 and Level 1)

**System Name:** TRAVELENS — Tourism Destination Review Analyzer  
**Standard:** Yourdon & Coad / Gane & Sarson DFD Methodology  
**Verification:** Reflects actual data entities, inputs, transformations, and outputs.

---

## 1. DFD Level 0 — Context Diagram

The Level 0 context diagram defines the boundary of the TRAVELENS system, external entities (User/Traveler and Administrator), and primary data exchanges.

```mermaid
graph LR
    User["Traveler / User (External Entity)"]
    Admin["System Administrator (External Entity)"]
    System(("(0.0) TRAVELENS System<br>Tourism Destination Review Analyzer"))

    %% User Interactions
    User -->|"Search Queries, Destination Selection"| System
    User -->|"Unstructured Review Text"| System
    User -->|"Aspect Priority Weights (1-5)"| System
    User -->|"Auth Credentials (Register/Login)"| System
    User -->|"Save/Remove Bookmark Requests"| System

    System -->|"Destination Cards, Catalog Metadata"| User
    System -->|"Aspect Radar, Sentiment Distribution, Trends"| User
    System -->|"Review Sentiment, Aspect Polarity, Confidence"| User
    System -->|"Ranked Destination Recommendations & Trade-offs"| User
    System -->|"Stateless JWT Token & Profile Data"| User

    %% Admin Interactions
    Admin -->|"Admin Credentials"| System
    System -->|"System Health & Telemetry"| Admin
```

---

## 2. DFD Level 1 — Detailed System Data Flow

The Level 1 DFD decomposes process `0.0` into the five core subsystems, data stores, and internal information flows.

```mermaid
graph TD
    User["Traveler / User"]
    
    subgraph DataStores["Data Stores"]
        DS_Dest[("D1: Destinations")]
        DS_Rev[("D2: Reviews")]
        DS_User[("D3: Users")]
        DS_Saved[("D4: Saved Destinations")]
        DS_Models[("D5: ML Model Artifacts")]
    end

    subgraph Processes["Processes"]
        P1["1.0 Authenticate & Manage Session"]
        P2["2.0 Destination Catalog & Exploration"]
        P3["3.0 Compute Destination Analytics"]
        P4["4.0 Process & Mine Review (ASTMA)"]
        P5["5.0 Multi-Criteria Recommendation Engine"]
    end

    %% Flow 1: Auth
    User -->|"Login / Register Details"| P1
    P1 <-->|"Read/Write User Credentials & Hash"| DS_User
    P1 -->|"JWT Bearer Token"| User
    P1 -->|"Validated User Identity"| P5
    User -->|"Bookmark Destination Request"| P1
    P1 <-->|"Store / Delete Bookmark"| DS_Saved

    %% Flow 2: Explore
    User -->|"Search Query, Filter Filters"| P2
    P2 <-->|"Fetch Destinations Metadata"| DS_Dest
    P2 -->|"Filtered Destination Cards"| User

    %% Flow 3: Analytics
    User -->|"Select Destination ID"| P3
    P3 <-->|"Fetch Reviews & Star Ratings"| DS_Rev
    P3 -->|"Aggregated Radar Metrics, Trends, Sentiment Ring"| User

    %% Flow 4: ASTMA Real-time Mining
    User -->|"Custom Review Text"| P4
    DS_Models -->|"Load TF-IDF & Classifier"| P4
    P4 -->|"Preprocess $\rightarrow$ Vectorize $\rightarrow$ Classify $\rightarrow$ Extract Aspects"| P4
    P4 -->|"Sentiment, Confidence, 9-Aspect Polarity Tags"| User

    %% Flow 5: Recommendation
    User -->|"Priority Sliders (1-5 for 9 Aspects)"| P5
    P5 <-->|"Fetch All Destination Aspect Scores"| DS_Rev
    P5 -->|"Normalized Utility Scores & Trade-off Explanation"| User
```

---

## 3. Data Dictionary Summary

| Data Element | Type / Format | Origin | Destination Store / Process | Description |
| :--- | :--- | :--- | :--- | :--- |
| `review_text` | String (Text) | User / Benchmark | Process 4.0 / D2 | Raw tourist review string. |
| `aspect_priorities` | Dict[str, int] | User | Process 5.0 | User importance weights (1–5) across 9 dimensions. |
| `sentiment_label` | String (`positive`, `neutral`, `negative`) | Process 4.0 | D2 / Response | Predicted polarity label from Logistic Regression. |
| `confidence` | Float (0.0 to 1.0) | Process 4.0 | Response | Calibrated probability of the winning sentiment class. |
| `utility_score` | Float (0.0 to 100.0) | Process 5.0 | Response | Weighted multi-attribute score for recommended destination. |
| `jwt_token` | Base64 URL-encoded string | Process 1.0 | User Client | Stateless authentication token containing `sub` claim. |
