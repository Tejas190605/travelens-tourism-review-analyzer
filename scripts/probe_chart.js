const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ channel: 'chrome', headless: true });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  await page.goto('http://localhost:5173/destinations/1', { waitUntil: 'networkidle' });
  await page.waitForTimeout(2000);

  const surfaces = await page.$$eval('.recharts-surface', (els) =>
    els.map((e) => ({
      tagName: e.tagName,
      width: e.getAttribute('width'),
      height: e.getAttribute('height'),
      clientWidth: e.clientWidth,
      clientHeight: e.clientHeight,
      parentClass: e.parentElement ? e.parentElement.className : null,
      parentTag: e.parentElement ? e.parentElement.tagName : null,
    }))
  );
  console.log('All .recharts-surface:', JSON.stringify(surfaces, null, 2));

  const wrapper = await page.$eval('.recharts-wrapper', (e) => ({
    width: e.clientWidth,
    height: e.clientHeight,
    style: e.getAttribute('style'),
  })).catch((e) => e.message);
  console.log('Recharts wrapper:', wrapper);

  await browser.close();
})();
