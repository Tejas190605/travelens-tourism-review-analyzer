# DEPLOYMENT_GUIDE.md — Free Cloud Hosting & Deployment Guide

**System Name:** TRAVELENS — Tourism Destination Review Analyzer  
**Recommended Free Cloud Provider:** Render ([render.com](https://render.com))  
**Target Architecture:**
- **Frontend:** Render Free Static Site (React 18 / Vite SPA)
- **Backend:** Render Free Web Service (FastAPI / Uvicorn ASGI)
- **Database:** Auto-Seeded SQLite (Zero-Configuration Demo) OR Free External PostgreSQL (Neon / Supabase)

---

## 1. Cloud Architecture & Free-Tier Trade-Offs

| Architecture Layer | Service Type | Free Tier Quota | Behavior & Limitations | Handling Strategy |
| :--- | :--- | :--- | :--- | :--- |
| **Frontend SPA** | Render Static Site | 100 GB/month bandwidth | Permanent HTTPS, fast global CDN, always awake | Includes `_redirects` for React Router deep linking |
| **Backend API** | Render Web Service | 512 MB RAM, 0.1 CPU | Inactive services sleep after 15 minutes; cold start takes ~30–50s | Warmup sequence preloads ML artifacts into memory on boot |
| **Data Storage** | SQLite (Self-Healing) | Included in web service container | Ephemeral disk resets on container redeploy | **Automatic Startup Seeding:** Backend auto-populates all 54 destinations and 629 reviews if database is fresh |
| **Persistent DB (Optional)** | External Cloud PostgreSQL (Neon / Supabase) | Free tier available | Fully persistent relational database | Set `DATABASE_URL=postgresql://...` in backend environment |

---

## 2. Deployment Method 1: Render Blueprint (Recommended, 1-Click)

The repository includes a production-ready `render.yaml` file configured for both frontend and backend.

### Steps:
1. Log in to [dashboard.render.com](https://dashboard.render.com).
2. Click **New +** $\rightarrow$ select **Blueprint**.
3. Connect your GitHub account and select repository: `travelens-tourism-review-analyzer`.
4. Render will detect `render.yaml` and display the two configured services:
   - `travelens-backend` (Python Web Service)
   - `travelens-frontend` (Static Site)
5. Click **Apply**.
6. Render will automatically build the backend, link its URL to the frontend's `VITE_API_BASE_URL`, and build the static site.

---

## 3. Deployment Method 2: Manual Dashboard Setup (Step-by-Step)

If you prefer configuring the services individually via the Render UI:

### Step 3.1: Deploy Backend Web Service
1. In Render Dashboard, click **New +** $\rightarrow$ **Web Service**.
2. Select your repository `travelens-tourism-review-analyzer`.
3. Configure settings:
   - **Name:** `travelens-backend`
   - **Region:** Any (e.g. Oregon, Frankfurt, or Singapore)
   - **Branch:** `main`
   - **Root Directory:** `backend`
   - **Runtime:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - **Instance Type:** `Free`
4. In **Environment Variables**, add:
   - `ENVIRONMENT` = `production`
   - `DEBUG` = `false`
   - `SECRET_KEY` = (Click "Generate" or enter a secure 32-character string)
   - `ALLOWED_ORIGINS` = `*`
   - `DATABASE_URL` = `sqlite:///./travelens.db`
5. Click **Create Web Service**.
6. Wait 2–3 minutes for the build to finish. Once live, copy your backend URL (e.g. `https://travelens-backend.onrender.com`).
7. Verify by opening `https://travelens-backend.onrender.com/api/health` in your browser (should return `{"status":"ok"}`).

---

### Step 3.2: Deploy Frontend Static Site
1. In Render Dashboard, click **New +** $\rightarrow$ **Static Site**.
2. Select your repository `travelens-tourism-review-analyzer`.
3. Configure settings:
   - **Name:** `travelens-frontend`
   - **Branch:** `main`
   - **Root Directory:** `frontend`
   - **Build Command:** `npm install && npm run build`
   - **Publish Directory:** `dist`
4. In **Environment Variables**, add:
   - `VITE_API_BASE_URL` = `https://travelens-backend.onrender.com` (Your deployed backend URL from Step 3.1)
5. In **Redirects / Rewrites** (or rely on `public/_redirects` already in the repo):
   - Type: `Rewrite`
   - Source: `/*`
   - Destination: `/index.html`
6. Click **Create Static Site**.
7. Once deployed (~1 minute), Render will assign your permanent public URL (e.g. `https://travelens-frontend.onrender.com`).

---

## 4. Post-Deployment Live Verification Checklist

Once both services are deployed, test the live application:

- [ ] **Home Page:** Open `https://travelens-frontend.onrender.com`. Verify hero banner and featured cards load.
- [ ] **Catalog & Filters:** Navigate to `/explore`. Search for `"Jaipur"` and filter by `"Heritage"` / `"Budget"`.
- [ ] **Destination Profile:** Open `/destination/1`. Verify 9-aspect radar chart, sentiment donut, and review cards display data.
- [ ] **Interactive NLP Review Analyzer:** Submit a custom sentence (e.g. *"The beach was lovely but hotel food was overpriced"*). Verify real-time aspect polarity detection.
- [ ] **Personalized Trip Planner:** Go to `/plan`. Move priority sliders (e.g. Cleanliness = 5, Price = 4) and verify ranked matches with trade-offs.
- [ ] **Destination Benchmarking:** Go to `/compare`. Select two destinations and verify side-by-side aspect differentials.
- [ ] **Authentication & Bookmarking:** Register a test account or log in as `traveler@travelens.com` (`userpassword123`) and bookmark a destination.
- [ ] **Direct URL Refresh:** Refresh on `/destination/1` or `/explore` to confirm `_redirects` prevents 404 errors.

---

## 5. Cold-Start Notice for Evaluators / Teachers

> [!NOTE]
> Because Render free-tier web services sleep after 15 minutes of inactivity, the very first request to the backend after a dormant period may take **30 to 50 seconds** while the container boots up and warms the ML models. Subsequent requests will respond in under **50 ms**.
