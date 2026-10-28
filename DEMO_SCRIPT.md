# DEMO_SCRIPT.md — TRAVELENS Final Project Demonstration Guide

**Project Name:** TRAVELENS — Tourism Destination Review Analyzer & Consumer Trip Planner  
**Presentation Audience:** Academic Faculty Examination Committee & External Evaluators (Final-Year BTech)  
**Estimated Duration:** 6 to 8 Minutes  
**Demonstrator Preparation:**
- Backend running on `http://127.0.0.1:8000` (FastAPI / Uvicorn)
- Frontend running on `http://localhost:5173` (Vite / React 18 SPA)
- Database: `backend/travelens.db` (54 destinations, 629 reviews, 3,041 aspect annotations, 2 users, 1 bookmark)

---

## 1. Demonstration Timing & Route Flow

| Step | Feature / Concept Demonstrated | Route / View | Target Duration |
| :---: | :--- | :--- | :---: |
| **1** | Project Motivation & Problem Statement | `/` (Discover Home) | 0:45 |
| **2** | Catalogue Exploration & Multidimensional Filtering | `/explore` | 0:45 |
| **3** | Deep Destination Guide & 9-Dimension Aspect Scorecard | `/destinations/1` (Jaipur) | 1:15 |
| **4** | Personalized Trip Planner & Recommendation Engine | `/plan` | 1:00 |
| **5** | Side-by-Side Destination Comparison Matrix | `/compare?destA=1&destB=5` | 0:45 |
| **6** | Authentication, Shortlist & Trip Cost Calculator | `/login` $\rightarrow$ `/saved` | 1:00 |
| **7** | About TRAVELENS & Machine Learning Provenance | `/about` | 0:45 |
| **8** | Codebase Architecture, Live Test Suite & Viva Defense | Terminal / IDE | 1:00 |
| **Total** | **Comprehensive End-to-End Evaluation Walkthrough** | | **~7:15 min** |

---

## 2. Step-by-Step Script & Narration Guide

### Step 1: Discover Home — The Problem of Scalar Star Ratings (0:00 – 0:45)
- **Action:** Open `http://localhost:5173/`. Point to the hero headline *"Discover destinations as travellers truly see them."*
- **Spoken Narration:**
  > *"Good morning, respected professors and evaluation committee members. Today I am presenting TRAVELENS, our final-year project.*  
  > *The core problem TRAVELENS addresses is the fallacy of the aggregate 5-star rating on conventional travel platforms. When a destination has an average rating of 4.2 out of 5, a traveler cannot easily tell whether that score reflects pristine cultural attractions while masking severe overcrowding, inflated taxi fares, or subpar cleanliness.*  
  > *TRAVELENS solves this through Aspect-Sentiment Tourism Mining & Analytics—decomposing natural language reviews into 9 granular tourism dimensions. Here on the Discover home page, prospective travelers see curated collections, realistic INR daily budgets, and immediate destination search without commercial advertisements or generic rating widgets."*
- **Action:** Type *"Jaipur"* into the hero search input; click the quick suggestion chip to show instant navigation.

---

### Step 2: Explore Catalogue — Multidimensional Filtering (0:45 – 1:30)
- **Action:** Click **Explore** in the navigation bar (`/explore`).
- **Demonstration Steps:**
  1. Click the **India** region filter button: observe catalogue instantly filtering to 12 Indian destinations.
  2. Click the **Heritage** category pill: observe catalogue refining to 7 heritage destinations.
  3. Change the Budget Tier dropdown to **Moderate**: observe immediate real-time filtering.
  4. Type *"Paris"* in the search input: observe instant sub-second text filtering matching Paris with French gateway metadata.
  5. Click **Reset All Filters** to restore the full 54-destination directory.
- **Spoken Narration:**
  > *"In the Explore directory, we catalog 54 diverse destinations across India and international gateways. Notice that every filter operates with zero page reloads via React 18 state management and asynchronous REST requests to our FastAPI backend. Prices are consistently formatted in Indian Rupees using Indian numbering standards, and every card reflects verifiable review statistics computed dynamically from our relational database."*

---

### Step 3: Destination Guide — 9-Dimension Aspect Scorecard (1:30 – 2:45)
- **Action:** Click **View Destination Guide** on the Jaipur card (`/destinations/1`).
- **Demonstration Steps:**
  1. Highlight the Hero banner: stay duration (`3–4 days`), best season (`October to March`), and indicative daily rate (`₹3,000 – ₹5,500 / day`).
  2. Scroll to **"What visiting Jaipur is really like"**: point out the two balanced analytical boxes:
     - **What travellers appreciated:** Cleanliness (100%), Safety (100%), Accommodation (80%).
     - **Caveats & challenges:** Crowd (40% mention challenges), Price (50% mention challenges).
  3. Scroll to **What Travellers Say Across 9 Travel Dimensions**: inspect the 9 dimension scorecards (Attractions 80/100, Food 75/100, Cleanliness 100/100, Price 41.7/100, Crowd 40/100).
  4. Demonstrate the 4 interactive guide tabs:
     - Click **Suggested Itinerary**: Day 1 Forts & Palaces, Day 2 Bazaars, Day 3 Excursions.
     - Click **Getting There & Transit**: Metro, tuk-tuk, and airport details.
     - Click **Practical Advice**: Local clothing norms and ticketing recommendations.
  5. Scroll to **Visitor Reviews**: click the **Positive** badge filter to isolate 5-star reviews; point out the extracted aspect chips (`Cleanliness: positive`, `Hospitality: positive`, `Price: negative`).
- **Spoken Narration:**
  > *"Here on the Jaipur guide, we see our aspect mining in action. Instead of a single 4.0 average, the system explicitly separates what visitors loved from recurring bottlenecks. Notice that while Attractions and Cleanliness are celebrated, Price and Crowd clearly highlight that monument entry fees and bazaar bargaining require vigilance. Furthermore, every score displays the exact number of reviews discussing it, completely preventing false perfection."*

---

### Step 4: Plan a Trip — Personalized Recommendation Engine (2:45 – 3:45)
- **Action:** Click **Plan a Trip** in the navigation bar (`/plan`).
- **Demonstration Steps:**
  1. Select **2 Travellers** and **5 Days** duration.
  2. Select Budget Tier **Moderate**.
  3. Toggle travel preferences: activate **Heritage**, **Food**, and **Nature**.
  4. Point out the top recommendation (e.g. Udaipur or Jaipur):
     - Highlight the calculated trip budget: $\text{₹6,200/day} \times 2 \times 5 = \textbf{₹62,000}$.
     - Highlight the matching rationale: *"Strong ratings for Attractions, Food, and Cleanliness"*.
     - Highlight the explicit trade-off: *"Crowds peak during festival months"*.
- **Spoken Narration:**
  > *"Our Plan a Trip engine utilizes a multi-attribute utility matching formulation. Rather than displaying sponsored placements, it computes compatibility mathematically between the user's priority weights and the empirical aspect scores derived from reviews. It also executes real-time trip budget arithmetic: calculating realistic total costs in INR based on travelers and duration, complete with an expandable day-by-day suggested itinerary."*

---

### Step 5: Compare Destinations — Side-by-Side Matrix (3:45 – 4:30)
- **Action:** Click **Compare** in the navigation bar (`/compare?destA=1&destB=5`).
- **Demonstration Steps:**
  1. Point out Destination A (**Jaipur**) and Destination B (**Udaipur**).
  2. Compare ratings (4.0 vs 4.2), review counts (11 vs 13), and INR budgets (₹3,000–₹5,500 vs ₹3,500–₹6,800).
  3. Compare dimensional scores side-by-side: Attractions (80 vs 85), Food (75 vs 80), Cleanliness (100 vs 90), and Crowd bottlenecks.
- **Spoken Narration:**
  > *"The Compare tool solves another key traveler headache: switching between tabs to weigh alternatives. Here Jaipur and Udaipur are benchmarked side-by-side across daily budgets, ideal seasons, verified strengths, and individual aspect scores, allowing travelers to make an objective, well-informed choice."*

---

### Step 6: Authentication, Shortlist & Trip Cost Calculator (4:30 – 5:30)
- **Action:** Click **Saved Places** (`/saved`). Notice the automatic login prompt.
- **Demonstration Steps:**
  1. Click **Sign In**: click the one-tap demo account autofill button (`traveler@travelens.com` / `userpassword123`) and submit.
  2. Notice instant redirect back to `/saved`.
  3. Point out Traveler Jane's persistent bookmark (**Jaipur**).
  4. Scroll down to the **Trip Cost Estimator**:
     - Change Duration to **4 days**, Travellers to **3 pax**, Budget Tier to **Moderate (~₹6,200)**.
     - Observe live calculation: $\text{3 pax} \times \text{4 days} \times \text{₹6,200} = \textbf{₹74,400}$.
  5. Demonstrate responsive navbar: open developer tools at 375px viewport (mobile), toggle the hamburger menu, show the smooth sliding drawer, and navigate to Explore.
- **Spoken Narration:**
  > *"Authentication is built using bcrypt 12-round hashing and stateless JWT bearer tokens. Notice Traveler Jane's persistent shortlist: multi-user isolation is enforced at the API layer so no user can access another user's bookmarks. The trip cost calculator performs verified mathematical arithmetic, explaining exactly what is included—accommodation, dining, transit, and sight passes."*

---

### Step 7: About TRAVELENS & Machine Learning Provenance (5:30 – 6:15)
- **Action:** Click **About** (`/about`).
- **Demonstration Steps:**
  1. Highlight the mission statement: *"Find places worth travelling for."*
  2. Review the explanation of the 9 core travel dimensions.
  3. Point out the empirical model evaluation metrics:
     - **Accuracy:** 74.5%
     - **Macro F1 Score:** 0.7458
     - **Evaluation Samples:** 1,200 annotated reviews
     - **Dataset Provenance:** Curated TripAdvisor Hotel & Tourism Reviews Benchmark Dataset (CC-BY-NC-4.0).
- **Spoken Narration:**
  > *"On our About page, we explain the foundation of TRAVELENS. Our underlying machine learning model combines a sublinear TF-IDF vectorizer with a multinomial Logistic Regression classifier and syntactic negation handling. Tested on a standardized benchmark of 1,200 samples, it achieves an empirical accuracy of 74.5% and a macro F1 score of 0.7458, providing statistically sound sentiment extraction while remaining lightweight enough to run sub-20ms inference without expensive GPU dependencies."*

---

### Step 8: Architecture, Live Verification Suite & Viva Defense (6:15 – 7:15)
- **Action:** Switch to terminal / IDE.
- **Demonstration Steps:**
  1. Show pytest suite result: `67 passed in ~22s`.
  2. Show frontend lint result: `0 warnings, 0 errors on 18 files`.
  3. Show frontend build: `built in ~500ms`.
  4. Show Playwright E2E suite result: `ALL 10 JOURNEYS PASSED` and `ALL 12 DEEP CHECKS PASSED`.
- **Spoken Narration:**
  > *"To verify enterprise software engineering standards, our project is backed by comprehensive automated testing: 67 backend unit and integration tests passing with 100% success, zero frontend linter warnings, sub-second production builds, and 22 end-to-end browser journeys automated via Playwright. The entire system adheres strictly to the 3-tier architecture, decoupled REST API principles, and zero database mutation during testing. Respected professors, we are now ready for your viva questions."*

---

## 3. Quick Reference Card for Demonstrator

| Test Account | Email: `traveler@travelens.com` | Password: `userpassword123` |
|---|---|---|
| **Admin Account** | Email: `admin@travelens.com` | Password: `adminpassword123` |
| **Backend URL** | `http://127.0.0.1:8000` | Health Check: `http://127.0.0.1:8000/api/health` |
| **Frontend URL** | `http://localhost:5173` | Build Output: `frontend/dist/` |
| **Primary Test Command** | `.\.venv\Scripts\python.exe -m pytest backend/tests -v` | 67 tests passing |
| **E2E Test Command** | `node run_e2e_tests.cjs` | 10 journeys passing |
| **Deep E2E Command** | `node verify_deep_e2e.cjs` | 12 checks passing |
