# DEPLOYMENT_API_FIX_REPORT.md — Frontend-to-Backend API Resolution Fix

**System Name:** TRAVELENS — Tourism Destination Review Analyzer & Trip Planner  
**Repository:** `https://github.com/Tejas190605/travelens-tourism-review-analyzer`  
**Date:** 24 November 2026  
**Status:** **ROOT CAUSE DIAGNOSED, FIXED, COMPILED & COMMITTED**  

---

## 1. Original Failure Cause (Root Cause Analysis)

### Symptom:
The deployed frontend at `https://travelens-frontend.onrender.com` displayed:
- *"Showing 0 catalogued destinations"*
- Browser console: *"Failed to fetch"*

### Root Cause Diagnosis:
1. In `render.yaml`, the frontend static site previously referenced the backend via:
   ```yaml
   envVars:
     - key: VITE_API_BASE_URL
       fromService:
         type: web
         name: travelens-backend
         property: host
   ```
2. In Render's Blueprint implementation, `property: host` does **not** provide the public HTTPS domain (`travelens-backend.onrender.com`). Instead, it evaluated to the internal container service name: `travelens-backend`.
3. In `index-Cr1HTHgr.js` (inspected directly on the live deployed site):
   ```javascript
   Si = "travelens-backend";
   Si = "https://" + Si; // evaluated to "https://travelens-backend/api"
   ```
4. When visitors opened `https://travelens-frontend.onrender.com` in their web browsers, client-side JavaScript attempted to fetch:
   ```text
   GET https://travelens-backend/api/destinations
   ```
5. Because `travelens-backend` is an internal Docker hostname that exists only within Render's private virtual network, public internet DNS failed to resolve it (`ERR_NAME_NOT_RESOLVED`), resulting in `"Failed to fetch"`.

---

## 2. Actual Live Backend Verification

Before making frontend changes, the backend public endpoint was directly tested using live HTTPS requests:

* **Backend Health Check:**
  `GET https://travelens-backend.onrender.com/api/health`
  * Status: `200 OK`
  * Response: `{"status": "ok", "app": "TRAVELENS API", "version": "1.0.0", "environment": "production"}`
* **Backend Destinations Endpoint:**
  `GET https://travelens-backend.onrender.com/api/destinations`
  * Status: `200 OK`
  * Output: **54 active destinations** returned with full ratings, images, and aspect metadata (Sample item: *Jaipur*).

**Verdict:** The backend database, models, and endpoints were 100% healthy; the issue was entirely the client-side API target URL.

---

## 3. Changes Made to Fix the Issue

### 3.1 Fixed Render Blueprint (`render.yaml`)
Replaced the internal `property: host` injection with the verified public HTTPS URL:
```yaml
  # -------------------------------------------------------------
  # 2. TRAVELENS Frontend Static Site (React 18 / Vite)
  # -------------------------------------------------------------
  - type: web
    name: travelens-frontend
    runtime: static
    rootDir: frontend
    buildCommand: npm install && npm run build
    staticPublishPath: dist
    routes:
      - type: rewrite
        source: /*
        destination: /index.html
    envVars:
      - key: VITE_API_BASE_URL
        value: https://travelens-backend.onrender.com
```

### 3.2 Frontend Production Environment Template (`frontend/.env.production`)
Added `frontend/.env.production` (whitelisted in `.gitignore`):
```ini
VITE_API_BASE_URL=https://travelens-backend.onrender.com
```
This provides double redundancy so that Vite builds automatically compile the public backend URL into the production bundle even if platform environment variable injection is delayed.

### 3.3 Robust Client API Service Normalizer (`frontend/src/services/api.js`)
Enhanced the API base URL resolver to handle all possible URL formats, prevent duplicate `/api` path segments, and strip accidental trailing slashes:
```javascript
let RAW_BASE = (import.meta.env.VITE_API_BASE_URL || '').trim();
if (RAW_BASE) {
  if (!RAW_BASE.startsWith('http://') && !RAW_BASE.startsWith('https://') && !RAW_BASE.startsWith('/')) {
    RAW_BASE = `https://${RAW_BASE}`;
  }
  RAW_BASE = RAW_BASE.replace(/\/+$/, '');
  // Prevent duplicating /api if already supplied in VITE_API_BASE_URL
  if (RAW_BASE.endsWith('/api')) {
    RAW_BASE = RAW_BASE.slice(0, -4);
  }
}
const API_BASE = RAW_BASE ? `${RAW_BASE}/api` : '/api';
```

### 3.4 Production CORS Configuration (`backend/app/main.py`)
Configured explicit origin matching for the deployed frontend alongside preview regex support, eliminating wildcard (`*`) origin conflicts with authenticated/credentialed requests:
```python
DEFAULT_ORIGINS = [
    "https://travelens-frontend.onrender.com",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:3000",
]
raw_origins = [o.strip() for o in settings.ALLOWED_ORIGINS.split(",") if o.strip()]
cors_origins = list(dict.fromkeys(DEFAULT_ORIGINS + [o for o in raw_origins if o != "*"]))

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins if cors_origins else ["*"],
    allow_origin_regex=r"https://.*\.onrender\.com",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 4. Verification & Production Bundle Inspection

* **Frontend Linter:** `oxlint` reported **0 errors, 0 warnings** across all 18 files.
* **Frontend Production Build:** `vite build` completed in 374ms.
* **Bundle Inspection:** Audited the newly generated bundle (`frontend/dist/assets/index-CJXPoQic.js`):
  ```javascript
  N = "https://travelens-backend.onrender.com";
  ```
  Confirmed that the public HTTPS URL is directly compiled into the client bundle.
* **Backend Test Suite:** Executed `pytest backend/tests -v`.  
  **Result:** **78 / 78 passed (100%)** with zero failures.

---

## 5. Live URLs for Testing

| Service | Public URL | Description |
| :--- | :--- | :--- |
| **Frontend SPA** | `https://travelens-frontend.onrender.com` | React 18 production user interface |
| **Backend API** | `https://travelens-backend.onrender.com` | FastAPI ASGI REST service |
| **Backend Health** | `https://travelens-backend.onrender.com/api/health` | System health check (`200 OK`) |
| **Destinations API** | `https://travelens-backend.onrender.com/api/destinations` | 54 destinations with reviews & aspect profiles |
| **Swagger API Docs** | `https://travelens-backend.onrender.com/docs` | Interactive OpenAPI documentation |
