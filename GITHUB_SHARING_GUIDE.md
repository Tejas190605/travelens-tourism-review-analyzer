# GITHUB_SHARING_GUIDE.md — Project Sharing & Collaboration Guide

**System Name:** TRAVELENS — Tourism Destination Review Analyzer & Trip Planner  
**Repository Target Name:** `travelens-tourism-review-analyzer`  
**Default Branch:** `main`  
**Recommended Visibility:** Private (until approved for public visibility)  

---

## 1. Connecting the Local Repository to GitHub

The local repository is completely initialized, audited, and committed on branch `main` with 0 exposed secrets and clean exclusions.

### Step 1: Create the Empty Repository on GitHub
1. Log in to your GitHub account ([github.com](https://github.com)).
2. Click **New Repository** (or visit [github.com/new](https://github.com/new)).
3. **Repository name:** `travelens-tourism-review-analyzer`
4. **Description:** `Aspect-Sentiment Tourism Mining & Analytics (ASTMA) Enterprise Platform`
5. **Visibility:** Select **Private** (recommended while under academic grading).
6. **Important:** Do **NOT** check "Add a README file", "Add .gitignore", or "Choose a license" (leave it completely empty).
7. Click **Create repository**.

### Step 2: Push Your Local Repository
In your local PowerShell terminal (`C:\Users\tejas\Tourism Review`), run:
```powershell
git remote add origin https://github.com/Tejas190605/travelens-tourism-review-analyzer.git
git push -u origin main
```
*Note: Windows Git Credential Manager will authenticate using your GitHub account (`Tejas190605`).*

---

## 2. How to Share with Your College Teacher

### Option A: Invite as a Private Collaborator (Best for Private Repos)
1. Open your repository on GitHub: `https://github.com/Tejas190605/travelens-tourism-review-analyzer`
2. Navigate to **Settings** $\rightarrow$ **Collaborators** (in the left sidebar).
3. Click **Add people**.
4. Enter your teacher's GitHub username or email address.
5. Click **Add <username> to this repository**.
6. Your teacher will receive an email invitation to view and clone the repository securely without making the code public to the internet.

### Option B: Make the Repository Public (When Approved)
If your college or teacher requires a public submission link:
1. Go to **Settings** $\rightarrow$ scroll down to the **Danger Zone**.
2. Click **Change visibility** $\rightarrow$ **Change to public**.
3. Confirm by typing the repository name.
4. The link `https://github.com/Tejas190605/travelens-tourism-review-analyzer` will now be directly viewable by anyone.

### Option C: Share via Standalone ZIP Distribution
If your evaluator prefers a direct archive submission:
1. In your repository on GitHub, click the green **<> Code** button.
2. Select **Download ZIP**.
3. All source code, models, datasets, and documentation are bundled into a single `.zip` file without local `.venv`, database binaries, or node_modules.

---

## 3. How Another Developer / Student Runs the Project

### Prerequisites
- **Python 3.10+**
- **Node.js 18+** & NPM

### Step-by-Step Setup Instructions

#### 1. Clone the Repository
```bash
git clone https://github.com/Tejas190605/travelens-tourism-review-analyzer.git
cd travelens-tourism-review-analyzer
```

#### 2. Backend Setup & Database Seeding
```bash
cd backend

# Create and activate virtual environment
python -m venv .venv

# Windows:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the 78 automated tests
python -m pytest tests -v

# Seed the SQLite demo database (54 destinations, 629 reviews)
python scripts/seed_db.py

# Start the FastAPI server
uvicorn app.main:app --reload --port 8000
```
Backend API will be active at `http://127.0.0.1:8000` with Swagger docs at `http://127.0.0.1:8000/docs`.

#### 3. Frontend Setup
In a new terminal window:
```bash
cd frontend

# Install dependencies
npm install

# Run frontend linter and build check
npm run lint
npm run build

# Start Vite development server
npm run dev
```
Open `http://localhost:5173` in your browser.

---

## 4. Normal Git Workflow for Future Updates

Whenever you make improvements to the project:
```powershell
# 1. Check changed files
git status

# 2. Stage specific files
git add <filename>  # e.g. git add README.md

# 3. Commit with a descriptive message
git commit -m "Describe what was added or updated"

# 4. Push to GitHub
git push
```
