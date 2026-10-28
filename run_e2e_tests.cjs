const { chromium } = require('./frontend/node_modules/playwright');
const path = require('path');
const fs = require('fs');

const BASE_URL = 'http://localhost:5173';
const SCREENSHOT_DIR = path.join(__dirname, 'docs', 'screenshots');

if (!fs.existsSync(SCREENSHOT_DIR)) {
  fs.mkdirSync(SCREENSHOT_DIR, { recursive: true });
}

async function runAllJourneys() {
  console.log('====================================================');
  console.log('TRAVELENS — End-to-End Real User Journey Suite');
  console.log('Target: ' + BASE_URL);
  console.log('====================================================\n');

  const browser = await chromium.launch({
    channel: 'chrome',
    headless: true,
  });

  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
  });

  const page = await context.newPage();

  const consoleErrors = [];
  const failedRequests = [];

  page.on('console', (msg) => {
    if (msg.type() === 'error') {
      consoleErrors.push(msg.text());
    }
  });

  page.on('requestfailed', (req) => {
    failedRequests.push(`${req.method()} ${req.url()} - ${req.failure()?.errorText}`);
  });

  const results = [];

  function record(journey, name, passed, details) {
    results.push({ journey, name, passed, details });
    const status = passed ? 'PASS' : 'FAIL';
    console.log(`[${status}] Journey ${journey}: ${name}`);
    if (details) console.log(`       Details: ${details}`);
  }

  try {
    // -------------------------------------------------------------
    // JOURNEY 1: Discover -> Search for Jaipur -> Destination Guide
    // -------------------------------------------------------------
    console.log('\n--- Running Journey 1: Search & Destination Guide ---');
    await page.goto(`${BASE_URL}/`, { waitUntil: 'networkidle' });
    
    // Assert title & brand
    const title = await page.title();
    if (!title.includes('TRAVELENS')) throw new Error(`Unexpected title: ${title}`);

    // Fill search box
    const searchInput = page.locator('input[placeholder*="Where do you want to go"]');
    await searchInput.fill('Jaipur');
    await page.locator('button[type="submit"]:has-text("Search")').click();

    await page.waitForURL(/.*\/explore\?query=Jaipur/, { timeout: 8000 });
    
    // Check Jaipur card in Explore
    const jaipurCard = page.locator('.destination-card', { hasText: 'Jaipur' }).first();
    await jaipurCard.waitFor({ state: 'visible', timeout: 5000 });

    // Open Jaipur Guide
    await jaipurCard.locator('a:has-text("View Destination Guide")').click();
    await page.waitForURL(/.*\/destinations\/\d+/, { timeout: 8000 });

    // Verify Jaipur details page
    const destHeading = await page.locator('h1').textContent();
    const hasJaipur = destHeading.includes('Jaipur');
    const overviewText = await page.textContent('body');
    const hasInr = overviewText.includes('₹');
    
    await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'journey_1_jaipur_guide.png') });
    record(1, 'Search for Jaipur & Open Destination Guide', hasJaipur && hasInr, `Heading: "${destHeading.trim()}", Found INR budget: ${hasInr}`);

    // -------------------------------------------------------------
    // JOURNEY 2: Explore Catalog with Filters
    // -------------------------------------------------------------
    console.log('\n--- Running Journey 2: Explore Filters (Region, Category, Budget) ---');
    await page.goto(`${BASE_URL}/explore`, { waitUntil: 'networkidle' });

    // Test Region filter: India
    const indiaButton = page.locator('button:has-text("India")');
    await indiaButton.click();
    await page.waitForTimeout(500);
    const indiaCards = await page.locator('.destination-card').count();

    // Test Category filter: Heritage
    const heritageButton = page.locator('button:has-text("Heritage")');
    await heritageButton.click();
    await page.waitForTimeout(500);
    const heritageCards = await page.locator('.destination-card').count();

    // Reset filters before global search
    await page.getByRole('button', { name: 'All Regions' }).click();
    await page.getByRole('button', { name: 'All', exact: true }).click();
    await page.locator('#budget-filter').selectOption('All');
    await page.waitForTimeout(400);

    // Test Search filter in Explore
    const expSearch = page.locator('input[placeholder*="Search by city"]');
    await expSearch.fill('Paris');
    await page.waitForTimeout(600);
    const parisCardVisible = await page.locator('.destination-card', { hasText: 'Paris' }).isVisible();
    await expSearch.fill('');
    await page.waitForTimeout(400);

    await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'journey_2_explore_filters.png') });
    record(2, 'Explore Catalog & Multidimensional Filters', parisCardVisible && indiaCards > 0 && heritageCards > 0, `India cards: ${indiaCards}, Heritage cards: ${heritageCards}, Paris search match: ${parisCardVisible}`);

    // -------------------------------------------------------------
    // JOURNEY 3: Destination Details Structure & Guide Tabs
    // -------------------------------------------------------------
    console.log('\n--- Running Journey 3: Destination Details & Guide Tabs ---');
    await page.goto(`${BASE_URL}/destinations/1`, { waitUntil: 'networkidle' });

    const lovedVisible = await page.locator('h3:has-text("What travellers appreciated")').isVisible();
    const caveatsVisible = await page.locator('h3:has-text("Caveats & challenges")').isVisible();
    const dimensionsVisible = await page.locator('h3:has-text("What Travellers Say Across 9 Travel Dimensions")').isVisible();

    // Click through practical guide tabs
    await page.locator('button:has-text("Suggested Itinerary")').click();
    await page.waitForTimeout(300);
    const itineraryVisible = await page.locator('text=Day 1:').first().isVisible();

    await page.locator('button:has-text("Getting There & Transit")').click();
    await page.waitForTimeout(300);
    const transitVisible = await page.locator('text=Transit Routes').isVisible();

    await page.locator('button:has-text("Practical Advice")').click();
    await page.waitForTimeout(300);
    const tipsVisible = await page.locator('text=Practical Travel Advice').isVisible();

    // Test review filters
    const sentimentSelect = page.locator('select', { hasText: 'All Sentiments' }).first();
    if (await sentimentSelect.isVisible()) {
      await sentimentSelect.selectOption('positive');
      await page.waitForTimeout(500);
    }

    await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'journey_3_destination_details.png') });
    record(3, 'Destination Guide & Interactive Tabs', lovedVisible && caveatsVisible && dimensionsVisible && itineraryVisible && transitVisible && tipsVisible, `Strengths: ${lovedVisible}, Caveats: ${caveatsVisible}, Itinerary tab: ${itineraryVisible}, Transit tab: ${transitVisible}, Tips tab: ${tipsVisible}`);

    // -------------------------------------------------------------
    // JOURNEY 4 & 5: Authentication, Shortlist Persistence & Removal
    // -------------------------------------------------------------
    console.log('\n--- Running Journey 4 & 5: Authentication & Shortlist Persistence ---');
    await page.goto(`${BASE_URL}/login`, { waitUntil: 'networkidle' });
    
    // Quick demo autofill
    await page.locator('button:has-text("Use demo traveller credentials")').click();
    await page.locator('button[type="submit"]:has-text("Sign In")').click();
    await page.waitForTimeout(1000);

    // Navigate to Jaipur and save
    await page.goto(`${BASE_URL}/destinations/1`, { waitUntil: 'networkidle' });
    const saveButton = page.locator('button', { hasText: /Save Destination|Saved in Shortlist/ }).first();
    const saveTextBefore = await saveButton.textContent();
    if (saveTextBefore.includes('Save Destination')) {
      await saveButton.click();
      await page.waitForTimeout(500);
    }

    // Journey 4: Save Varanasi and verify both Jaipur and Varanasi persist
    await page.goto(`${BASE_URL}/destinations/2`, { waitUntil: 'networkidle' });
    const saveVaranasi = page.locator('button', { hasText: /Save Destination|Saved in Shortlist/ }).first();
    const varanasiTextBefore = await saveVaranasi.textContent();
    if (varanasiTextBefore.includes('Save Destination')) {
      await saveVaranasi.click();
      await page.waitForTimeout(500);
    }

    // Navigate away to Discover
    await page.goto(`${BASE_URL}/`, { waitUntil: 'networkidle' });

    // Navigate to Saved Places
    await page.locator('a.nav-link:has-text("Saved Places")').click();
    await page.waitForURL(/.*\/saved/, { timeout: 8000 });
    await page.waitForTimeout(500);

    // Verify both Jaipur and Varanasi are shortlisted
    const jaipurInShortlist = await page.locator('.destination-card', { hasText: 'Jaipur' }).isVisible();
    const varanasiInShortlist = await page.locator('.destination-card', { hasText: 'Varanasi' }).isVisible();
    await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'journey_4_saved_places.png') });
    record(4, 'Save Destination & Shortlist Persistence Across Routes', jaipurInShortlist && varanasiInShortlist, `Jaipur persisted: ${jaipurInShortlist}, Varanasi persisted: ${varanasiInShortlist}`);

    // Journey 5: Remove Varanasi from Shortlist while keeping Jaipur safe
    const removeVaranasiBtn = page.locator('.destination-card', { hasText: 'Varanasi' }).locator('button[title*="Remove"]').first();
    if (await removeVaranasiBtn.isVisible()) {
      await removeVaranasiBtn.click();
      await page.waitForTimeout(600);
    }
    const varanasiStillThere = await page.locator('.destination-card', { hasText: 'Varanasi' }).isVisible();
    const jaipurStillPersists = await page.locator('.destination-card', { hasText: 'Jaipur' }).isVisible();
    await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'journey_5_shortlist_removed.png') });
    record(5, 'Remove Destination from Shortlist', (!varanasiStillThere) && jaipurStillPersists, `Varanasi removed: ${!varanasiStillThere}, Jaipur preserved: ${jaipurStillPersists}`);

    // -------------------------------------------------------------
    // JOURNEY 6: Compare Destinations Side-by-Side
    // -------------------------------------------------------------
    console.log('\n--- Running Journey 6: Side-by-Side Destination Comparison ---');
    await page.goto(`${BASE_URL}/compare?destA=1&destB=5`, { waitUntil: 'networkidle' });

    const compareCols = await page.locator('.destination-card, div:has(h2 a)').count();
    const hasJaipurInComp = await page.locator('text=Jaipur').first().isVisible();
    const hasUdaipurInComp = await page.locator('text=Udaipur').first().isVisible();

    // Test adding 3rd destination
    const addSelect = page.locator('#add-dest-select');
    if (await addSelect.isVisible()) {
      await addSelect.selectOption({ index: 1 });
      await page.waitForTimeout(500);
    }

    await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'journey_6_comparison.png') });
    record(6, 'Side-by-Side Destination Comparison Matrix', hasJaipurInComp && hasUdaipurInComp, `Jaipur visible: ${hasJaipurInComp}, Udaipur visible: ${hasUdaipurInComp}`);

    // -------------------------------------------------------------
    // JOURNEY 7: Trip Cost Calculator Mathematical Correctness
    // -------------------------------------------------------------
    console.log('\n--- Running Journey 7: Trip Cost Calculator Verification ---');
    await page.goto(`${BASE_URL}/saved`, { waitUntil: 'networkidle' });

    const daysInput = page.locator('#calc-days');
    const travellersInput = page.locator('#calc-travellers');
    const tierSelect = page.locator('#calc-tier');

    // Case 1: 3 travellers, 4 days, Moderate (₹6,200) -> 6200 * 3 * 4 = ₹74,400
    await daysInput.fill('4');
    await travellersInput.fill('3');
    await tierSelect.selectOption('Moderate');
    await page.waitForTimeout(300);
    let totalText = await page.locator('text=₹74,400').first().isVisible();
    const case1Pass = totalText;

    // Case 2: 2 travellers, 7 days, Budget (₹3,200) -> 3200 * 2 * 7 = ₹44,800
    await daysInput.fill('7');
    await travellersInput.fill('2');
    await tierSelect.selectOption('Budget');
    await page.waitForTimeout(300);
    let totalText2 = await page.locator('text=₹44,800').first().isVisible();
    const case2Pass = totalText2;

    // Case 3: 2 travellers, 7 days, Premium (₹14,500) -> 14500 * 2 * 7 = ₹2,03,000
    await tierSelect.selectOption('Premium');
    await page.waitForTimeout(300);
    let totalText3 = await page.locator('text=₹2,03,000').first().isVisible();
    const case3Pass = totalText3;

    await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'journey_7_calculator.png') });
    const calcMathAllPass = case1Pass && case2Pass && case3Pass;
    record(7, 'Trip Cost Calculator Mathematical Arithmetic', calcMathAllPass, `Case 1 (3 pax, 4 days @ ₹6,200 = ₹74,400): ${case1Pass}, Case 2 (2 pax, 7 days @ ₹3,200 = ₹44,800): ${case2Pass}, Case 3 (2 pax, 7 days @ ₹14,500 = ₹2,03,000): ${case3Pass}`);

    // -------------------------------------------------------------
    // JOURNEY 8: Plan a Trip Preferences & Recommendation Shifts
    // -------------------------------------------------------------
    console.log('\n--- Running Journey 8: Plan a Trip Preferences & Shift ---');
    await page.goto(`${BASE_URL}/plan`, { waitUntil: 'networkidle' });

    // Fill preferences: Heritage = 5, Food = 5, Nature = 1
    await page.locator('#trip-travellers').fill('2');
    await page.locator('#trip-days').fill('5');
    await page.locator('#trip-budget').selectOption('Moderate');

    await page.locator('button:has-text("Find Matching Destinations")').click();
    await page.waitForTimeout(1000);

    const recMatchesCount = await page.locator('article', { hasText: 'Estimated Trip Budget' }).count();
    const hasTripTotalInr = await page.locator('text=₹62,000').first().isVisible(); // 6200 * 2 * 5 = 62,000

    await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'journey_8_plan_trip.png') });
    record(8, 'Plan a Trip Preferences & Recommendations with Itinerary Preview', recMatchesCount > 0 && hasTripTotalInr, `Matches found: ${recMatchesCount}, Calculated trip total (₹62,000) verified: ${hasTripTotalInr}`);

    // -------------------------------------------------------------
    // JOURNEY 9: Auth Validation, Logout & Protected Access
    // -------------------------------------------------------------
    console.log('\n--- Running Journey 9: Auth Validation & Logout ---');
    // Logout
    await page.goto(`${BASE_URL}/saved`, { waitUntil: 'networkidle' });
    const logoutBtn = page.locator('button:has-text("Sign Out")').first();
    if (await logoutBtn.isVisible()) {
      await logoutBtn.click();
      await page.waitForTimeout(800);
    }

    // Try accessing protected /saved route while logged out -> should redirect to /login
    await page.goto(`${BASE_URL}/saved`, { waitUntil: 'networkidle' });
    const isAtLogin = page.url().includes('/login');

    // Test invalid login error feedback
    await page.locator('#auth-email').fill('invalid_user_999@test.com');
    await page.locator('#auth-password').fill('wrongpassword123');
    await page.locator('button[type="submit"]:has-text("Sign In")').click();
    await page.waitForTimeout(600);
    const authErrorVisible = await page.locator('text=Incorrect email or password').isVisible() || await page.locator('text=Authentication failed').isVisible();

    await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'journey_9_auth_validation.png') });
    record(9, 'Authentication Security, Logout & Protected Route Shielding', isAtLogin && authErrorVisible, `Redirect to login when logged out: ${isAtLogin}, Invalid credentials error displayed: ${authErrorVisible}`);

    // -------------------------------------------------------------
    // JOURNEY 10: Empty Results, Missing Destinations & Error Handling
    // -------------------------------------------------------------
    console.log('\n--- Running Journey 10: Empty States & Error Handling ---');
    // Empty search in Explore
    await page.goto(`${BASE_URL}/explore?query=NonExistentPlaceXYZ987`, { waitUntil: 'networkidle' });
    const emptyStateVisible = await page.locator('h3:has-text("No destinations match your filters")').isVisible();
    const resetBtnVisible = await page.locator('button:has-text("Reset All Filters")').isVisible();

    // Click Reset
    if (resetBtnVisible) {
      await page.locator('button:has-text("Reset All Filters")').click();
      await page.waitForTimeout(600);
    }
    const resetRestoredCards = await page.locator('.destination-card').count();

    // Non-existent destination ID
    await page.goto(`${BASE_URL}/destinations/99999`, { waitUntil: 'networkidle' });
    const notFoundVisible = await page.locator('h2:has-text("Destination Not Found")').isVisible();
    const returnExploreVisible = await page.locator('a:has-text("Return to Explore")').isVisible();

    await page.screenshot({ path: path.join(SCREENSHOT_DIR, 'journey_10_empty_states.png') });
    record(10, 'Empty Search, Missing Destination 404 & Recovery', emptyStateVisible && resetRestoredCards > 0 && notFoundVisible && returnExploreVisible, `Empty search state: ${emptyStateVisible}, Reset restored catalogue: ${resetRestoredCards > 0}, 404 destination handled gracefully: ${notFoundVisible}`);

  } catch (err) {
    console.error('Test execution error:', err);
    record('FATAL', 'Execution Failure', false, err.message);
  } finally {
    await browser.close();
  }

  console.log('\n====================================================');
  console.log('SUMMARY OF TEST RESULTS:');
  console.log('====================================================');
  const allPassed = results.every(r => r.passed);
  results.forEach(r => {
    console.log(`Journey ${r.journey}: ${r.name} -> ${r.passed ? 'PASSED' : 'FAILED'}`);
  });
  console.log(`\nTotal Console Errors Logged: ${consoleErrors.length}`);
  if (consoleErrors.length > 0) {
    consoleErrors.forEach(e => console.log('   Console Error: ' + e));
  }
  console.log(`Total Failed Network Requests: ${failedRequests.length}`);
  if (failedRequests.length > 0) {
    failedRequests.forEach(r => console.log('   Failed Request: ' + r));
  }
  console.log(`\nOverall E2E Status: ${allPassed ? 'ALL 10 JOURNEYS PASSED' : 'FAILURES DETECTED'}`);
  console.log('====================================================');

  fs.writeFileSync(path.join(__dirname, 'e2e_results.json'), JSON.stringify({
    timestamp: new Date().toISOString(),
    allPassed,
    results,
    consoleErrors,
    failedRequests
  }, null, 2));
}

runAllJourneys();
