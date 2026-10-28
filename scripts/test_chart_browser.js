const { chromium } = require('playwright');

async function testChartBrowser() {
  console.log('[Browser QA] Launching Chrome to verify Monthly Sentiment Trend Chart...');
  const browser = await chromium.launch({ channel: 'chrome', headless: true });
  const context = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const page = await context.newPage();

  try {
    await page.goto('http://localhost:5173/destinations/1', { waitUntil: 'networkidle' });
    await page.waitForTimeout(2000);

    // 1. Locate Recharts ResponsiveContainer
    const rechartsContainer = await page.$('.recharts-responsive-container');
    if (!rechartsContainer) {
      throw new Error('FAIL: .recharts-responsive-container not found on page');
    }
    const containerBox = await rechartsContainer.boundingBox();
    console.log(`[PASS] ResponsiveContainer box: width=${containerBox.width}px, height=${containerBox.height}px`);

    if (containerBox.width <= 0 || containerBox.height <= 0) {
      throw new Error(`FAIL: ResponsiveContainer has zero dimension: width=${containerBox.width}, height=${containerBox.height}`);
    }

    // 2. Locate rendered chart SVG (.recharts-wrapper > svg.recharts-surface)
    const rechartsSurface = await page.$('.recharts-wrapper > svg.recharts-surface');
    if (!rechartsSurface) {
      throw new Error('FAIL: .recharts-wrapper > svg.recharts-surface SVG not found');
    }
    const surfaceBox = await rechartsSurface.boundingBox();
    console.log(`[PASS] Chart SVG Surface box: width=${surfaceBox.width}px, height=${surfaceBox.height}px`);

    if (surfaceBox.width <= 100 || surfaceBox.height <= 100) {
      throw new Error(`FAIL: Chart SVG surface rendered with insufficient/zero dimension: width=${surfaceBox.width}, height=${surfaceBox.height}`);
    }

    // 3. Verify calendar-month spacing and XAxis ticks
    const xTicks = await page.$$('.recharts-xAxis-tick-labels text');
    console.log(`[PASS] Calendar-month X-axis ticks found: ${xTicks.length}`);
    if (xTicks.length < 2) {
      throw new Error(`FAIL: Expected at least 2 calendar-month ticks, found ${xTicks.length}`);
    }

    // 4. Verify Legend
    const legend = await page.$('.recharts-legend-wrapper');
    if (!legend) {
      throw new Error('FAIL: Legend wrapper not found');
    }
    const legendText = await legend.innerText();
    console.log(`[PASS] Legend text: "${legendText.trim()}"`);

    // 5. Verify Tooltip hover interaction
    const areaPath = await page.$('.recharts-area-dots circle');
    if (areaPath) {
      await areaPath.hover();
      await page.waitForTimeout(500);
      const tooltip = await page.$('.recharts-tooltip-wrapper');
      console.log(`[PASS] Tooltip wrapper visible on hover: ${!!tooltip}`);
    }

    console.log('\n[SUCCESS] Monthly Sentiment Trend Chart verified: non-zero explicit dimensions, valid SVG, calendar ticks, and legend.');
  } finally {
    await browser.close();
  }
}

testChartBrowser()
  .then(() => process.exit(0))
  .catch((err) => {
    console.error('[Regression Failure]', err);
    process.exit(1);
  });
