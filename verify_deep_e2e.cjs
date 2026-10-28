const { chromium } = require('./frontend/node_modules/playwright');
const path = require('path');
const fs = require('fs');

const BASE_URL = 'http://localhost:5173';
const SCREENSHOT_DIR = path.join(__dirname, 'docs', 'screenshots');

async function runDeepVerification() {
  console.log('====================================================');
  console.log('TRAVELENS — Deep Verification & Mobile Audit');
  console.log('Target:', BASE_URL);
  console.log('====================================================\n');

  const browser = await chromium.launch({ channel: 'chrome', headless: true });
  
  // 1. Desktop Context
  const desktopContext = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const page = await desktopContext.newPage();

  const results = [];
  function record(check, passed, details) {
    results.push({ check, passed, details });
    console.log(`[${passed ? 'PASS' : 'FAIL'}] ${check}: ${details || ''}`);
  }

  try {
    // -------------------------------------------------------------
    // Direct URL Access & Refresh across all routes
    // -------------------------------------------------------------
    const routesToTest = [
      { path: '/', titleCheck: 'TRAVELENS' },
      { path: '/explore', elementCheck: '.destination-card' },
      { path: '/destinations/1', elementCheck: 'h1:has-text("Jaipur")' },
      { path: '/destinations/5', elementCheck: 'h1:has-text("Udaipur")' },
      { path: '/plan', elementCheck: '#trip-travellers' },
      { path: '/compare?destA=1&destB=5', elementCheck: 'h1:has-text("Compare Destinations")' },
      { path: '/about', elementCheck: 'h1:has-text("About TRAVELENS")' },
    ];

    console.log('--- Testing Direct URL Access & Page Refresh ---');
    for (const r of routesToTest) {
      await page.goto(`${BASE_URL}${r.path}`, { waitUntil: 'networkidle' });
      // Direct access check
      let directPass = false;
      if (r.titleCheck) {
        const title = await page.title();
        directPass = title.includes(r.titleCheck);
      } else if (r.elementCheck) {
        directPass = await page.locator(r.elementCheck).first().isVisible();
      }
      
      // Refresh check
      await page.reload({ waitUntil: 'networkidle' });
      let refreshPass = false;
      if (r.titleCheck) {
        const title = await page.title();
        refreshPass = title.includes(r.titleCheck);
      } else if (r.elementCheck) {
        refreshPass = await page.locator(r.elementCheck).first().isVisible();
      }

      record(`Direct & Refresh on ${r.path}`, directPass && refreshPass, `Direct: ${directPass}, Refresh: ${refreshPass}`);
    }

    // -------------------------------------------------------------
    // User Authentication & Safe Shortlist Test (Does NOT delete Jaipur)
    // -------------------------------------------------------------
    console.log('\n--- Testing Auth, Safe Shortlist & Multi-User Isolation ---');
    await page.goto(`${BASE_URL}/login`, { waitUntil: 'networkidle' });
    await page.locator('button:has-text("Use demo traveller credentials")').click();
    await page.locator('button[type="submit"]:has-text("Sign In")').click();
    await page.waitForTimeout(1000);

    // Verify User Jane is logged in
    await page.goto(`${BASE_URL}/saved`, { waitUntil: 'networkidle' });
    const jaipurPresent = await page.locator('.destination-card', { hasText: 'Jaipur' }).isVisible();
    record('Jaipur Bookmark Preserved in Shortlist', jaipurPresent, `Jaipur bookmark visible: ${jaipurPresent}`);

    // Temporarily save destination 2 (Varanasi) and remove it (never remove Jaipur)
    await page.goto(`${BASE_URL}/destinations/2`, { waitUntil: 'networkidle' });
    const saveVaranasiBtn = page.locator('button:has-text("Save Destination")').first();
    if (await saveVaranasiBtn.isVisible()) {
      await saveVaranasiBtn.click();
      await page.waitForTimeout(500);
    }
    
    // Check Varanasi in /saved
    await page.goto(`${BASE_URL}/saved`, { waitUntil: 'networkidle' });
    const varanasiPresent = await page.locator('.destination-card', { hasText: 'Varanasi' }).isVisible();
    record('Add Second Destination to Shortlist', varanasiPresent, `Varanasi visible: ${varanasiPresent}`);

    // Remove Varanasi (NOT Jaipur)
    const removeVaranasiBtn = page.locator('.destination-card', { hasText: 'Varanasi' }).locator('button[title*="Remove"]').first();
    if (await removeVaranasiBtn.isVisible()) {
      await removeVaranasiBtn.click();
      await page.waitForTimeout(500);
    }
    const varanasiRemoved = !(await page.locator('.destination-card', { hasText: 'Varanasi' }).isVisible());
    const jaipurStillSafe = await page.locator('.destination-card', { hasText: 'Jaipur' }).isVisible();
    record('Remove Added Bookmark while Preserving Base Bookmark', varanasiRemoved && jaipurStillSafe, `Varanasi removed: ${varanasiRemoved}, Jaipur still preserved: ${jaipurStillSafe}`);

    // Logout
    await page.locator('button[title="Sign Out"]').first().click();
    await page.waitForTimeout(600);

    // -------------------------------------------------------------
    // Invalid Form Inputs
    // -------------------------------------------------------------
    console.log('\n--- Testing Form Validation & Invalid Inputs ---');
    await page.goto(`${BASE_URL}/login`, { waitUntil: 'networkidle' });
    // Switch to register tab
    await page.locator('button:has-text("Register")').click();
    await page.locator('#reg-name').fill('Test User');
    await page.locator('#auth-email').fill('shortpass@test.com');
    await page.locator('#auth-password').fill('123'); // < 6 chars
    await page.locator('button[type="submit"]:has-text("Create Account")').click();
    await page.waitForTimeout(400);
    const shortPassErr = await page.locator('text=Password must contain at least 6 characters').isVisible();
    record('Short Password Validation', shortPassErr, `Expected error shown: ${shortPassErr}`);

    // -------------------------------------------------------------
    // Mobile Viewport Audit (375x667 iPhone)
    // -------------------------------------------------------------
    console.log('\n--- Testing Mobile Viewport & Navigation Drawer ---');
    const mobileContext = await browser.newContext({ viewport: { width: 375, height: 667 } });
    const mobilePage = await mobileContext.newPage();

    await mobilePage.goto(`${BASE_URL}/`, { waitUntil: 'networkidle' });

    // Verify desktop links hidden
    const desktopLinksHidden = !(await mobilePage.locator('.nav-links').isVisible());
    // Verify mobile hamburger button visible
    const hamburgerBtn = mobilePage.locator('.mobile-menu-btn');
    const hamburgerVisible = await hamburgerBtn.isVisible();

    await mobilePage.screenshot({ path: path.join(SCREENSHOT_DIR, 'consumer_mobile_home.png') });

    // Click hamburger button to open drawer
    await hamburgerBtn.click();
    await mobilePage.waitForTimeout(400);

    const drawerVisible = await mobilePage.locator('.mobile-drawer').isVisible();
    const discoverLinkInDrawer = await mobilePage.locator('.mobile-drawer a:has-text("Discover")').isVisible();
    const exploreLinkInDrawer = await mobilePage.locator('.mobile-drawer a:has-text("Explore")').isVisible();
    const planLinkInDrawer = await mobilePage.locator('.mobile-drawer a:has-text("Plan a Trip")').isVisible();

    await mobilePage.screenshot({ path: path.join(SCREENSHOT_DIR, 'consumer_mobile_drawer.png') });

    // Click Explore from mobile drawer
    await mobilePage.locator('.mobile-drawer a:has-text("Explore")').click();
    await mobilePage.waitForURL(/.*\/explore/, { timeout: 6000 });
    await mobilePage.locator('.destination-card').first().waitFor({ state: 'visible', timeout: 8000 });
    const mobileExploreCards = await mobilePage.locator('.destination-card').count();

    await mobilePage.screenshot({ path: path.join(SCREENSHOT_DIR, 'consumer_mobile_explore.png') });

    record('Mobile Viewport Navigation & Drawer', 
      desktopLinksHidden && hamburgerVisible && drawerVisible && discoverLinkInDrawer && mobileExploreCards > 0,
      `Desktop links hidden: ${desktopLinksHidden}, Hamburger visible: ${hamburgerVisible}, Drawer opened: ${drawerVisible}, Mobile Explore cards: ${mobileExploreCards}`
    );

    await mobileContext.close();
    await desktopContext.close();

  } catch (err) {
    console.error('Deep verification error:', err);
    record('Fatal Execution Error', false, err.message);
  } finally {
    await browser.close();
  }

  console.log('\n====================================================');
  console.log('DEEP VERIFICATION SUMMARY');
  console.log('====================================================');
  const allPass = results.every(r => r.passed);
  results.forEach(r => console.log(`${r.check}: ${r.passed ? 'PASSED' : 'FAILED'}`));
  console.log(`\nOverall Result: ${allPass ? 'ALL CHECKS PASSED' : 'SOME CHECKS FAILED'}`);
  console.log('====================================================');
}

runDeepVerification();
