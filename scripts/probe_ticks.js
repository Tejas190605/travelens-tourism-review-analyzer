const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ channel: 'chrome', headless: true });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await page.goto('http://localhost:5173/destinations/1', { waitUntil: 'networkidle' });
  await page.waitForTimeout(2000);

  const ticks = await page.$$eval('g.recharts-xAxis g.recharts-layer text, g.recharts-cartesian-axis-tick text, .recharts-xAxis text', (els) =>
    els.map((e) => e.textContent)
  );
  console.log('XAxis tick texts:', ticks);

  const allTexts = await page.$$eval('.recharts-wrapper svg text', (els) =>
    els.map((e) => e.textContent)
  );
  console.log('All SVG texts in chart:', allTexts);

  await browser.close();
})();
