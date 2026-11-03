const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const html = require('fs').readFileSync(process.argv[2], 'utf8');
  const doc = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body>' + html + '</body></html>';
  const p = await b.newPage({ viewport: { width: 695, height: 1000 }, colorScheme: 'light' });
  const errs = [];
  p.on('pageerror', e => errs.push('pageerror: ' + e.message));
  p.on('console', m => { if (m.type() === 'error') errs.push('console: ' + m.text()); });
  await p.emulateMedia({ media: 'print', colorScheme: 'light' });
  await p.setContent(doc, { waitUntil: 'networkidle', timeout: 90000 });
  await p.evaluate(async () => {
    document.querySelectorAll('details').forEach(d => d.open = true);
    if (window.MathJax && MathJax.startup) await MathJax.startup.promise;
    await document.fonts.ready;
  });
  await p.waitForTimeout(2500);
  const info = await p.evaluate(() => ({ sw: document.documentElement.scrollWidth, svgs: document.querySelectorAll('.chart svg').length, mjx: document.querySelectorAll('mjx-container').length, fonts: [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family).filter((v, i, a) => a.indexOf(v) === i) }));
  console.log(JSON.stringify(info));
  await p.pdf({ path: process.argv[3], preferCSSPageSize: true, printBackground: true, displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: '<div style="font-family: Arial, sans-serif; font-size:8px; color:#667; width:100%; padding:0 13mm; display:flex; justify-content:space-between;"><span>Review notes on Kritov, Clifford Geometry and Mass Relations, v13 · 3 November 2026</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>' });
  console.log(errs.join('\n') || 'no errors');
  await b.close();
})();
