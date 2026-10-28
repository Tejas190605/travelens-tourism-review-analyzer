# SCREENSHOT_CHECKLIST.md — Academic Report Screenshot Compilation Guide

**Project Name:** TRAVELENS — Tourism Destination Review Analyzer  
**Purpose:** Guide for capturing verified visual artifacts for academic project reports, thesis submissions, and presentation slide decks.  
*Note: All screenshots must be captured from the live running application (`http://localhost:5173`). Do not create or use fabricated mockups.*

---

## 1. Master Screenshot Capture Checklist

| # | View / Feature | URL Route | Key Visual Elements to Include | Recommended Aspect Ratio | Status |
| :-: | :--- | :--- | :--- | :-: | :-: |
| **1** | **Landing Page / Hero** | `/` | Hero headline *"See the destination through travellers' eyes"*, search bar, live system counter, curated destination cards. | 16:9 Desktop (1920×1080) | `[ ] Ready to capture` |
| **2** | **Explore Catalog** | `/explore` | Search query input, category filter buttons (`All`, `Cultural`, `Nature`, `Urban`), destination card grid with star ratings. | 16:9 Desktop (1920×1080) | `[ ] Ready to capture` |
| **3** | **Destination Hero Header** | `/destination/1` | Destination title (*"Kyoto, Japan"*), country badge, category tag, descriptive summary, bookmark button. | 16:9 Desktop (1920×1080) | `[ ] Ready to capture` |
| **4** | **9-Aspect Radar Analytics** | `/destination/1` | Interactive Recharts multi-axis Radar Chart displaying all 9 aspect scores (Attractions, Food, Cleanliness, Price, etc.). | 16:9 Desktop (1920×1080) | `[ ] Ready to capture` |
| **5** | **Sentiment Breakdown Ring** | `/destination/1` | Recharts Donut/Ring chart displaying exact percentage distribution (Positive, Neutral, Negative) and total review count. | 16:9 Desktop (1920×1080) | `[ ] Ready to capture` |
| **6** | **Review Explorer & Filters** | `/destination/1#reviews` | Star rating filter buttons (1–5), sentiment filter badges, paginated review cards with highlighted aspect tags. | 16:9 Desktop (1920×1080) | `[ ] Ready to capture` |
| **7** | **Analyze Review Input** | `/analyze` | Textarea form with custom user review input and the *"Analyze Review"* action button. | 16:9 Desktop (1920×1080) | `[ ] Ready to capture` |
| **8** | **Analyze Review ASTMA Result**| `/analyze` | Polarity result card (Positive/Neutral/Negative badge, confidence bar, color-coded aspect tags, salient keywords). | 16:9 Desktop (1920×1080) | `[ ] Ready to capture` |
| **9** | **Destination Comparison** | `/compare` | Side-by-side dropdown selectors (Kyoto vs Banff), comparative aspect bar chart, and trade-off summary cards. | 16:9 Desktop (1920×1080) | `[ ] Ready to capture` |
| **10**| **Recommendation Wizard** | `/recommend` | 1-to-5 aspect priority sliders, *"Generate Recommendations"* button, ranked destination cards with explainable trade-off text. | 16:9 Desktop (1920×1080) | `[ ] Ready to capture` |
| **11**| **User Authentication / Login**| `/login` | Editorial login form with email, password fields, security badges, and link to register. | 16:9 Desktop (1920×1080) | `[ ] Ready to capture` |
| **12**| **Saved Destinations Profile** | `/profile` | User greeting, saved destinations grid, remove bookmark action buttons, and session logout trigger. | 16:9 Desktop (1920×1080) | `[ ] Ready to capture` |
| **13**| **About & Model Metrics Table**| `/about` | Technical architecture diagram, verified model evaluation metrics table (74.5% accuracy), and CC-BY-NC-4.0 dataset attribution. | 16:9 Desktop (1920×1080) | `[ ] Ready to capture` |
| **14**| **Mobile Responsive Layout** | `/explore` & `/destination/1` | Single-column fluid layout on mobile viewport (390×844 px), mobile navigation menu, touch targets. | 9:16 Mobile (iPhone 14) | `[ ] Ready to capture` |

---

## 2. Capture Guidelines for Defense Slides
- **Resolution:** Capture at minimum 1080p ($1920 \times 1080$) for desktop views.
- **Clean Browser Profile:** Use browser developer tools with scrollbars visible and devtools docks hidden.
- **Pre-Recorded Action Artifact:** The autonomous browser walkthrough recording is already preserved in:
  `C:\Users\tejas\.gemini\antigravity-ide\brain\5b704259-905e-4910-ada8-765640ff99b2\final_qa_journey_1791487667075.webp`.
