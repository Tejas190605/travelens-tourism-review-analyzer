# SEQUENCE_DIAGRAMS.md — System Runtime Interaction Scenarios

**System Name:** TRAVELENS — Tourism Destination Review Analyzer  
**Standard:** UML 2.5 Sequence Diagram Specification  
**Scenarios:** (A) Real-Time Review Analysis, (B) Personalized Recommendation, (C) User Login & JWT Issuance  

---

## 1. Scenario A: Analyze Review (ASTMA Pipeline)

Illustrates the end-to-end runtime lifecycle when a user submits custom review text for real-time aspect and sentiment mining.

```mermaid
sequenceDiagram
    autonumber
    actor User as Traveler / User
    participant UI as React SPA (AnalyzeReview.jsx)
    participant API as FastAPI Router (/api/analyze-review)
    participant Pre as Preprocessor (preprocessor.py)
    participant Model as Sentiment Model (sentiment_model.py)
    participant Asp as Aspect Extractor (aspect_extractor.py)
    participant KW as Keyword Extractor (keyword_extractor.py)

    User->>UI: Enters custom review text & clicks "Analyze Review"
    UI->>UI: Validates non-empty input
    UI->>API: POST /api/analyze-review { "review_text": "..." }
    
    API->>Pre: preprocess_for_tfidf(review_text)
    Pre-->>API: Cleaned normalized text (negations preserved)

    API->>Model: predict_sentiment(cleaned_text)
    Model->>Model: TF-IDF transform & Logistic Regression predict_proba()
    Model-->>API: sentiment="positive", confidence=0.88, probabilities={...}

    API->>Asp: extract_aspects(review_text)
    Asp->>Asp: Clause segmentation, lexicon match & negation check
    Asp-->>API: detected_aspects=[{"aspect": "Food", "sentiment": "positive", ...}]

    API->>KW: extract_keywords([review_text], top_n=5)
    KW-->>API: salient_keywords=["matcha", "ramen", "delightful"]

    API-->>UI: HTTP 200 OK { sentiment, confidence, aspects, keywords }
    UI->>UI: Renders Polarity Badge, Confidence Bar & Aspect Chips
    UI-->>User: Displays visual ASTMA analysis results
```

---

## 2. Scenario B: Personalized Destination Recommendation

Illustrates multi-attribute utility recommendation formulation based on user priority sliders.

```mermaid
sequenceDiagram
    autonumber
    actor User as Traveler / User
    participant UI as React SPA (Recommend.jsx)
    participant API as FastAPI Router (/api/recommendations)
    participant RecServ as Recommendation Service (recommendation_service.py)
    participant DB as SQLAlchemy / SQLite Database

    User->>UI: Adjusts priority sliders (Food: 5, Safety: 4, Crowd: 1)
    UI->>API: POST /api/recommendations { preferences: { "Food": 5, "Safety": 4, ... } }
    
    API->>RecServ: generate_recommendations(preferences, db)
    RecServ->>DB: Query all destinations and associated review aspects
    DB-->>RecServ: Destination records with reviews & calculated aspect scores

    loop For each Destination
        RecServ->>RecServ: Calculate normalized weighted utility score
        RecServ->>RecServ: Handle missing aspect dimensions gracefully
        RecServ->>RecServ: Generate transparent trade-off explanation
    end

    RecServ->>RecServ: Sort destinations descending by utility score
    RecServ-->>API: Ranked list of destination recommendation objects

    API-->>UI: HTTP 200 OK [ { destination, score, matched_aspects, tradeoff } ]
    UI->>UI: Renders Recommendation Cards & Match Percentages
    UI-->>User: Displays personalized rankings with explainable trade-offs
```

---

## 3. Scenario C: User Login & Stateless JWT Issuance

Illustrates authentication, password verification using bcrypt, and stateless token generation.

```mermaid
sequenceDiagram
    autonumber
    actor User as Traveler / User
    participant UI as React SPA (Login.jsx)
    participant AuthCtx as AuthContext (React)
    participant API as FastAPI Router (/api/auth/login)
    participant Sec as Security Engine (security.py)
    participant DB as SQLAlchemy / SQLite Database

    User->>UI: Enters email and password; clicks "Log In"
    UI->>API: POST /api/auth/login { "email": "...", "password": "..." }

    API->>DB: Query User by email
    alt User Not Found
        DB-->>API: None
        API-->>UI: HTTP 401 Unauthorized ("Invalid credentials")
        UI-->>User: Displays error notification
    else User Exists
        DB-->>API: User record (with password_hash)
        API->>Sec: verify_password(plain_password, password_hash)
        alt Password Hash Mismatch
            Sec-->>API: False
            API-->>UI: HTTP 401 Unauthorized ("Invalid credentials")
            UI-->>User: Displays error notification
        else Password Valid
            Sec-->>API: True
            API->>Sec: create_access_token(data={"sub": user.email, "role": user.role})
            Sec-->>API: Encoded HS256 JWT string (60 min expiry)
            API-->>UI: HTTP 200 OK { "access_token": "...", "token_type": "bearer", "user": {...} }
            UI->>AuthCtx: setToken(access_token) & setUser(user)
            AuthCtx->>AuthCtx: Save token to browser localStorage
            UI-->>User: Redirects to Explore / Profile view as Authenticated
        end
    end
```
