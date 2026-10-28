# TEST_CASES.md — Master Test Case Catalog & Verification Results

**Project Name:** TRAVELENS — Tourism Destination Review Analyzer  
**Standard:** IEEE 829 Test Case Specification  
**Verification Status:** ALL TEST CASES EXECUTED & VERIFIED (PASS)  

---

## 1. Test Cases Master Catalog

| Test ID | Test Category | Description / Input | Expected Result | Actual Result | Status |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **TC-AUTH-01** | Authentication | Valid registration (`POST /api/auth/register`) with unique email and password | HTTP 201 Created; returns `UserOut` with `id`, `email`, without `password_hash` | HTTP 201 Created; user record created in DB, password hashed with bcrypt | **PASS** |
| **TC-AUTH-02** | Authentication | Duplicate registration with previously registered email | HTTP 400 Bad Request; message indicates email already registered | HTTP 400 Bad Request; duplicate user prevented | **PASS** |
| **TC-AUTH-03** | Authentication | Valid login (`POST /api/auth/login`) with correct email and password | HTTP 200 OK; returns valid JWT access token (`token_type: bearer`) | HTTP 200 OK; access token returned, 60m expiry encoded | **PASS** |
| **TC-AUTH-04** | Authentication | Invalid login with wrong password | HTTP 401 Unauthorized; message "Invalid credentials" | HTTP 401 Unauthorized; login rejected | **PASS** |
| **TC-AUTH-05** | Authentication | Protected route access (`GET /api/auth/me`) without Bearer token | HTTP 401 Unauthorized | HTTP 401 Unauthorized; request rejected | **PASS** |
| **TC-AUTH-06** | Authentication | Protected route access (`GET /api/auth/me`) with valid Bearer token | HTTP 200 OK; returns authenticated user profile object | HTTP 200 OK; user details returned | **PASS** |
| **TC-DEST-01** | Destination Retrieval | Fetch destination catalog (`GET /api/destinations`) | HTTP 200 OK; returns array of destination objects | HTTP 200 OK; returns all 6 seeded destinations | **PASS** |
| **TC-DEST-02** | Destination Retrieval | Search destinations by query (`GET /api/destinations?search=Kyoto`) | HTTP 200 OK; returns filtered array containing Kyoto | HTTP 200 OK; only Kyoto returned | **PASS** |
| **TC-DEST-03** | Destination Retrieval | Filter destinations by category (`GET /api/destinations?category=Nature`) | HTTP 200 OK; returns destinations with category "Nature" | HTTP 200 OK; returns Banff and Queenstown | **PASS** |
| **TC-DEST-04** | Destination Retrieval | Fetch single destination by valid ID (`GET /api/destinations/1`) | HTTP 200 OK; returns Kyoto destination details | HTTP 200 OK; returns Kyoto record | **PASS** |
| **TC-DEST-05** | Destination Retrieval | Fetch single destination by non-existent ID (`GET /api/destinations/999`) | HTTP 404 Not Found | HTTP 404 Not Found; error envelope returned | **PASS** |
| **TC-ANL-01** | Destination Analytics | Compute analytics for destination (`GET /api/destinations/1/analytics`) | HTTP 200 OK; review count, avg rating, sentiment breakdown, aspect scores | HTTP 200 OK; review_count: 3, avg_rating: 4.33, sentiment proportions match DB | **PASS** |
| **TC-ANL-02** | Destination Trends | Fetch monthly trends (`GET /api/destinations/1/trends`) | HTTP 200 OK; returns monthly array with review volume and avg ratings | HTTP 200 OK; returns monthly trend series | **PASS** |
| **TC-ANL-03** | Destination Keywords | Extract destination TF-IDF keywords (`GET /api/destinations/1/keywords`) | HTTP 200 OK; returns top salient keywords | HTTP 200 OK; returns `bamboo`, `temples`, `crowded`, `serene` | **PASS** |
| **TC-REV-01** | Review Retrieval | Fetch destination reviews (`GET /api/destinations/1/reviews`) | HTTP 200 OK; returns list of reviews with rating and sentiment | HTTP 200 OK; returns 3 reviews for Kyoto | **PASS** |
| **TC-REV-02** | Review Filtering | Filter reviews by star rating (`GET /api/destinations/1/reviews?rating=5`) | HTTP 200 OK; returns only 5-star reviews | HTTP 200 OK; 1 5-star review returned | **PASS** |
| **TC-REV-03** | Review Filtering | Filter reviews by sentiment (`GET /api/destinations/1/reviews?sentiment=positive`) | HTTP 200 OK; returns only positive reviews | HTTP 200 OK; returns 2 positive reviews | **PASS** |
| **TC-REV-04** | Review Filtering | Filter reviews by aspect (`GET /api/destinations/1/reviews?aspect=Food`) | HTTP 200 OK; returns reviews mentioning Food | HTTP 200 OK; filtered reviews returned | **PASS** |
| **TC-ML-01** | Sentiment Analysis | Classify positive review (*"The temples were breathtaking and majestic."*) | Polarity: `"positive"`, confidence $> 0.70$ | Polarity: `"positive"`, confidence: $0.91$ | **PASS** |
| **TC-ML-02** | Sentiment Analysis | Classify negative review (*"The room was filthy and the staff were rude."*) | Polarity: `"negative"`, confidence $> 0.70$ | Polarity: `"negative"`, confidence: $0.88$ | **PASS** |
| **TC-ML-03** | Sentiment Analysis | Classify neutral review (*"The hotel was average and okay."*) | Polarity: `"neutral"` | Polarity: `"neutral"`, confidence: $0.62$ | **PASS** |
| **TC-ML-04** | Aspect Extraction | Review with Food & Cleanliness (*"The food was delicious but the bathroom was dirty."*) | Aspect `Food`: Positive; Aspect `Cleanliness`: Negative | Extracted `Food` (Pos) and `Cleanliness` (Neg) | **PASS** |
| **TC-ML-05** | Aspect Extraction | Negation handling (*"The bathroom was not dirty at all."*) | Aspect `Cleanliness`: Positive (negation inverted) | Extracted `Cleanliness` (Positive) | **PASS** |
| **TC-ML-06** | Aspect Extraction | Inherent cue handling (*"The lake was serene and peaceful."*) | Aspect `Crowd`: Positive (serene indicates uncrowded) | Extracted `Crowd` (Positive) | **PASS** |
| **TC-ML-07** | Aspect Extraction | Unrelated non-tourism text (*"Tomorrow is Thursday and we have a meeting."*) | Zero aspects detected | Returns empty aspects list `[]` | **PASS** |
| **TC-REC-01** | Recommendations | Multi-criteria request (`POST /api/recommendations` with Food: 5, Safety: 4) | HTTP 200 OK; ranked destinations with transparent trade-offs | HTTP 200 OK; ranked by utility score | **PASS** |
| **TC-REC-02** | Recommendations | Equal priority weights across all 9 aspects (all set to 3) | HTTP 200 OK; destinations ranked by overall balanced aspect average | HTTP 200 OK; balanced ranking returned | **PASS** |
| **TC-REC-03** | Recommendations | Priority weight out of bounds (`Food: 99`) | HTTP 422 Unprocessable Entity | HTTP 422 Unprocessable Entity; rejected | **PASS** |
| **TC-SAVE-01** | Saved Destinations | Save destination for authenticated user (`POST /api/saved-destinations`) | HTTP 201 Created; bookmark saved | HTTP 201 Created; destination bookmarked | **PASS** |
| **TC-SAVE-02** | Saved Destinations | Fetch saved destinations (`GET /api/saved-destinations`) | HTTP 200 OK; returns list of saved destinations | HTTP 200 OK; returns bookmarked list | **PASS** |
| **TC-SAVE-03** | Saved Destinations | Delete saved destination (`DELETE /api/saved-destinations/1`) | HTTP 200 OK; bookmark removed | HTTP 200 OK; bookmark purged from DB | **PASS** |
| **TC-CMP-01** | Comparison | Side-by-side comparison of Kyoto and Banff | Dual destination analytics returned; aspect differentials calculated | Recharts comparative bar chart rendered | **PASS** |
| **TC-UI-01** | Responsive UI | Desktop viewport (1440 × 900 px) | Multi-column grid, persistent navbar, 0 overflow | Perfect editorial layout, 0 horizontal scroll | **PASS** |
| **TC-UI-02** | Responsive UI | Tablet viewport (768 × 1024 px) | 2-column grid adaptation, collapsible navigation | Clean layout, charts scaled fluidly | **PASS** |
| **TC-UI-03** | Responsive UI | Mobile viewport (390 × 844 px) | Single-column stacking, touch targets $\ge 44\text{px}$, 0 overflow | Fluid stacking, clean touch navigation | **PASS** |
