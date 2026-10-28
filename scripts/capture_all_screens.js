const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const OUT_DIR = path.resolve(__dirname, '..', 'docs', 'screenshots');
if (!fs.existsSync(OUT_DIR)) {
  fs.mkdirSync(OUT_DIR, { recursive: true });
}

async function capture() {
  console.log('[Capture] Launching Chrome browser with viewport 1440x900...');
  const browser = await chromium.launch({
    channel: 'chrome',
    headless: true,
  });

  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1,
  });

  const page = await context.newPage();

  // Helper to save screenshot
  const take = async (name, fullPage = false) => {
    const file = path.join(OUT_DIR, `${name}.png`);
    await page.waitForTimeout(600); // allow renders to settle
    await page.screenshot({ path: file, fullPage });
    const stat = fs.statSync(file);
    console.log(`[Captured] ${name}.png (${(stat.size / 1024).toFixed(1)} KB)`);
  };

  try {
    // ----------------------------------------------------
    // A. HOME PAGE
    // ----------------------------------------------------
    console.log('\n--- Section A: Home Page ---');
    await page.goto('http://localhost:5173/', { waitUntil: 'networkidle' });
    await page.waitForTimeout(1500);
    await take('01_homepage');

    // Scroll to curated cards section
    await page.evaluate(() => window.scrollBy(0, 750));
    await page.waitForTimeout(1000);
    await take('01b_homepage_cards');

    // ----------------------------------------------------
    // B. EXPLORE DESTINATIONS
    // ----------------------------------------------------
    console.log('\n--- Section B: Explore Destinations ---');
    await page.goto('http://localhost:5173/explore', { waitUntil: 'networkidle' });
    await page.waitForTimeout(1500);
    await take('02_explore_destinations');

    // Filter by India
    const indiaBtn = await page.$('button:has-text("India")');
    if (indiaBtn) {
      await indiaBtn.click();
      await page.waitForTimeout(1000);
      await take('02b_explore_india_filter');
    }

    // Filter by Europe
    const europeBtn = await page.$('button:has-text("Europe")');
    if (europeBtn) {
      await europeBtn.click();
      await page.waitForTimeout(1000);
      await take('02c_explore_intl_filter');
    }

    // ----------------------------------------------------
    // C. DESTINATION DETAILS (3 distinct categories)
    // ----------------------------------------------------
    console.log('\n--- Section C: Destination Details ---');
    // 1. Jaipur (Heritage, India - ID 1)
    await page.goto('http://localhost:5173/destinations/1', { waitUntil: 'networkidle' });
    await page.waitForTimeout(1500);
    // 1. Top hero and metadata overview
    await take('03_destination_jaipur');

    // 2. Overall Review Sentiment & What Travellers Liked / Challenging
    await page.evaluate(() => window.scrollTo(0, 580));
    await page.waitForTimeout(800);
    await take('05_destination_aspect_analysis');

    // 3. Nine Tourism Aspects Scorecard
    await page.evaluate(() => window.scrollTo(0, 1200));
    await page.waitForTimeout(800);
    await take('06_review_sentiment_analysis');

    // 4. Most Discussed Topics & Sentiment Over Time Chart
    await page.evaluate(() => window.scrollTo(0, 1850));
    await page.waitForTimeout(800);
    await take('06b_destination_reviews_cards');

    // 5. Individual Reviews Filter & Cards
    await page.evaluate(() => window.scrollTo(0, 2400));
    await page.waitForTimeout(800);
    await take('06c_review_explorer_list');

    // 6. Travel Guide Logistics & Itinerary Tab
    await page.evaluate(() => window.scrollTo(0, 3100));
    await page.waitForTimeout(600);
    const itineraryTab = await page.$('button:has-text("Suggested Itinerary")');
    if (itineraryTab) {
      await itineraryTab.click();
      await page.waitForTimeout(800);
    }
    await take('03b_destination_jaipur_itinerary');

    // 2. International Destination (Paris ID 28)
    console.log('Capturing International Destination (Paris)...');
    await page.goto('http://localhost:5173/destinations/28', { waitUntil: 'networkidle' });
    await page.waitForTimeout(1500);
    await take('04_destination_international');

    // 3. Coastal Destination (Goa ID 6)
    console.log('Capturing Coastal Destination (Goa)...');
    await page.goto('http://localhost:5173/destinations/6', { waitUntil: 'networkidle' });
    await page.waitForTimeout(1500);
    await take('04b_destination_coastal');

    // ----------------------------------------------------
    // D. DESTINATION COMPARISON
    // ----------------------------------------------------
    console.log('\n--- Section D: Destination Comparison ---');
    await page.goto('http://localhost:5173/compare?dests=1,2', { waitUntil: 'networkidle' });
    await page.waitForTimeout(1500);
    await take('07_destination_comparison');

    // Adjust priority slider and capture dynamic update
    const slider = await page.$('input[type="range"]');
    if (slider) {
      await slider.fill('1');
      await page.waitForTimeout(800);
    }
    await page.evaluate(() => window.scrollBy(0, 300));
    await page.waitForTimeout(800);
    await take('08_comparison_priority_sliders');

    // ----------------------------------------------------
    // E. PERSONALIZED RECOMMENDATIONS
    // ----------------------------------------------------
    console.log('\n--- Section E: Personalized Recommendations ---');
    await page.goto('http://localhost:5173/recommend', { waitUntil: 'networkidle' });
    await page.waitForTimeout(1000);

    // Click 'Find Matching Destinations' button
    const findBtn = await page.$('button:has-text("Find Matching Destinations")');
    if (findBtn) {
      await findBtn.click();
      await page.waitForTimeout(2500);
    }
    // Scroll down to see match cards
    await page.evaluate(() => window.scrollBy(0, 550));
    await page.waitForTimeout(1000);
    await take('09_personalized_recommendations');

    // ----------------------------------------------------
    // F. ANALYZE REVIEW (3 user specified test prompts)
    // ----------------------------------------------------
    console.log('\n--- Section F: Analyze Review ---');
    await page.goto('http://localhost:5173/analyze', { waitUntil: 'networkidle' });
    await page.waitForTimeout(1000);

    const testReviews = [
      {
        name: '10_review_analyzer_positive',
        text: 'The beaches were beautiful, the staff were friendly, and the food was excellent.',
      },
      {
        name: '11_review_analyzer_negative',
        text: 'The hotel was dirty, transport was unreliable, and everything was overpriced.',
      },
      {
        name: '12_review_analyzer_mixed',
        text: 'The monuments were breathtaking, but the queues were long and the tickets were expensive.',
      },
    ];

    for (const item of testReviews) {
      console.log(`Analyzing: "${item.text.slice(0, 45)}..."`);
      await page.goto('http://localhost:5173/analyze', { waitUntil: 'networkidle' });
      await page.waitForTimeout(800);
      await page.fill('textarea', item.text);
      await page.waitForTimeout(300);

      const submitBtn = await page.$('button:has-text("Run ASTMA Analysis"), button[type="submit"]');
      if (submitBtn) {
        await submitBtn.click();
        await page.waitForTimeout(2000);
      }

      // Scroll to view analysis output and decomposition
      await page.evaluate(() => window.scrollBy(0, 350));
      await page.waitForTimeout(800);
      await take(item.name);
    }

    // ----------------------------------------------------
    // G. AUTHENTICATION & PROFILE
    // ----------------------------------------------------
    console.log('\n--- Section G: Authentication & Profile ---');
    // Sign In page
    await page.goto('http://localhost:5173/login', { waitUntil: 'networkidle' });
    await page.waitForTimeout(1000);
    await take('13_sign_in');

    // Toggle to Register view
    const regToggle = await page.$('button:has-text("Create an Account")');
    if (regToggle) {
      await regToggle.click();
      await page.waitForTimeout(600);
      await take('13b_register');
    }

    // Log in as test user
    const travelerQuickBtn = await page.$('button:has-text("Regular Traveller")') || await page.$('button:has-text("Regular Traveler")');
    if (travelerQuickBtn) {
      await travelerQuickBtn.click();
      await page.waitForTimeout(500);
      const submitLogin = await page.$('button[type="submit"]');
      if (submitLogin) {
        await submitLogin.click();
        await page.waitForTimeout(2000);
      }
    }

    // Verify bookmark on Jaipur (ensure Jaipur is bookmarked without toggling off)
    await page.goto('http://localhost:5173/destinations/1', { waitUntil: 'networkidle' });
    await page.waitForTimeout(1000);
    const saveBtn = await page.$('button:has-text("Save to Shortlist"), button:has-text("Save Destination")');
    if (saveBtn) {
      const btnText = await saveBtn.innerText();
      if (!btnText.includes('Saved')) {
        await saveBtn.click();
        await page.waitForTimeout(1000);
      }
    }

    // Profile page
    await page.goto('http://localhost:5173/profile', { waitUntil: 'networkidle' });
    await page.waitForTimeout(1500);
    await take('14_user_profile');

    // Scroll to saved destinations & budget calculator
    await page.evaluate(() => window.scrollBy(0, 500));
    await page.waitForTimeout(1000);
    await take('15_saved_destinations');

    // ----------------------------------------------------
    // H. ABOUT & ASTMA ENGINE EVALUATION
    // ----------------------------------------------------
    console.log('\n--- Section H: About & ASTMA ---');
    await page.goto('http://localhost:5173/about', { waitUntil: 'networkidle' });
    await page.waitForTimeout(1500);
    await take('16_about_astma_workflow');

    // Scroll to model evaluation metrics & confusion matrix
    await page.evaluate(() => window.scrollBy(0, 550));
    await page.waitForTimeout(1000);
    await take('17_model_evaluation');

    console.log('\n[Done] All 22 screenshots captured successfully!');
  } catch (err) {
    console.error('[Error during capture]', err);
  } finally {
    await browser.close();
  }
}

capture();
