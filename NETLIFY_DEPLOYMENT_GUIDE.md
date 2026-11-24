# NETLIFY_DEPLOYMENT_GUIDE.md — Deploying TRAVELENS Frontend on Netlify

**System Name:** TRAVELENS — Tourism Destination Review Analyzer & Trip Planner  
**Repository:** `https://github.com/Tejas190605/travelens-tourism-review-analyzer`  
**Frontend Stack:** React 18, Vite, React Router DOM, Recharts, Lucide Icons  
**Target Platform:** Netlify ([app.netlify.com](https://app.netlify.com)) — Free Tier  

---

## 1. Architecture Overview

TRAVELENS uses a decoupled architecture:
* **Frontend:** Deployed to **Netlify** as a high-performance static SPA with global edge CDN, automatic HTTPS, and instant Git continuous deployment.
* **Backend:** Deployed to a Python ASGI hosting platform (such as **Render Free Web Service**) running FastAPI, SQLite self-healing database, and Scikit-learn ML models.
* **Communication:** Frontend talks to backend via REST APIs configured dynamically through `VITE_API_BASE_URL`.

---

## 2. Netlify Configuration Specification

The repository includes a dedicated `netlify.toml` file at the root:

```toml
[build]
  base = "frontend"
  publish = "dist"
  command = "npm run build"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

Additionally, `frontend/public/_redirects` contains:
```text
/*    /index.html   200
```
This ensures that direct URL navigation (e.g. refreshing `/explore` or opening `/destination/1` directly) routes cleanly through React Router without 404 errors.

---

## 3. Step-by-Step Deployment Instructions

### Step 1: Sign in to Netlify
1. Go to [app.netlify.com](https://app.netlify.com).
2. Click **Log in** $\rightarrow$ select **GitHub** to sign in with your GitHub account (`Tejas190605`).

### Step 2: Import the Existing GitHub Repository
1. In the Netlify Team Overview dashboard, click **Add new site** $\rightarrow$ **Import an existing project**.
2. Select **GitHub** as your Git provider.
3. If prompted, authorize Netlify to access your repositories.
4. Search for and select: `travelens-tourism-review-analyzer`.

### Step 3: Configure Build & Deploy Settings
Netlify will auto-detect settings from `netlify.toml`. Verify the following fields:
* **Branch to deploy:** `main`
* **Base directory:** `frontend`
* **Build command:** `npm run build`
* **Publish directory:** `frontend/dist` (or `dist` when base is set to `frontend`)

### Step 4: Configure Environment Variables
1. In the same deployment setup screen (or under **Site configuration** $\rightarrow$ **Environment variables**):
2. Click **Add a variable** or **New variable**.
3. Set:
   * **Key:** `VITE_API_BASE_URL`
   * **Value:** Your live backend URL (e.g. `https://travelens-backend.onrender.com`).
     *(Note: Do not append `/api` at the end; the frontend service automatically appends `/api` to endpoints.)*

### Step 5: Deploy the Site
1. Click **Deploy travelens-tourism-review-analyzer** (or **Deploy site**).
2. Netlify will provision a container, run `npm install`, execute `vite build`, and publish your application.
3. In ~1 minute, your site will be live with a permanent HTTPS URL (e.g. `https://travelens-review.netlify.app`).

### Step 6: Customize Your Site Name (Optional)
1. Go to **Site configuration** $\rightarrow$ **General** $\rightarrow$ **Site details**.
2. Click **Change site name**.
3. Enter a custom subdomain (e.g. `travelens` $\rightarrow$ `https://travelens.netlify.app`).

---

## 4. Backend Connection & CORS Setup

Ensure your backend permits requests from your Netlify domain:
1. In your backend hosting provider (e.g. Render Dashboard $\rightarrow$ Environment Variables):
2. Set `ALLOWED_ORIGINS`:
   * Value: `https://<your-site-name>.netlify.app,http://localhost:5173` (or `*`).
3. If using Render free tier, verify backend health:
   * Open `https://<your-backend-service>.onrender.com/api/health` in your browser.
   * Expected response: `{"status":"ok","app":"TRAVELENS API","version":"1.0.0","environment":"production"}`.

---

## 5. Post-Deployment Verification Checklist

Once your Netlify site is live, open the URL and test each feature:

- [ ] **1. Homepage:** Hero banner, navigation bar, and destination cards load with images and star ratings.
- [ ] **2. Explore Page (`/explore`):** Search for a destination (e.g. *"Jaipur"*), filter by category (*"Heritage"*), and filter by region (*"India"* / *"International"*).
- [ ] **3. Destination Details (`/destination/1`):** 9-aspect radar chart renders, sentiment donut renders, and review explorer displays paginated reviews.
- [ ] **4. Real-Time NLP Review Analyzer (`/destination/1`):** Submit a custom review in the interactive form. Verify that aspect clauses and predicted sentiment appear with confidence scores.
- [ ] **5. Personalized Recommendations (`/plan`):** Adjust 1–5 priority sliders for Cleanliness, Price, and Attractions. Verify ranked destination matches with explainable trade-offs.
- [ ] **6. Destination Comparison (`/compare`):** Select two destinations. Verify the 9-aspect comparative bar charts and difference takeaways render.
- [ ] **7. Authentication (`/login`):** Log in with demo account (`traveler@travelens.com` / `userpassword123`) or register a new user. Verify token stored and profile displayed.
- [ ] **8. Saved Destinations (`/saved`):** Bookmark a destination and confirm it appears in the user profile.
- [ ] **9. Direct URL Refresh:** Refresh the browser while on `/explore` or `/destination/1`. Confirm the page reloads cleanly without a 404 error.
- [ ] **10. Browser Console:** Open Developer Tools (F12) $\rightarrow$ Console. Confirm there are no critical CORS errors or unhandled network exceptions.
