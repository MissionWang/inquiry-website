(async () => {
  const perf = window.performance.getEntriesByType("navigation")[0];
  const ttfb = perf.responseStart - perf.requestStart;
  const totalLoadTime = perf.loadEventEnd - perf.navigationStart;
  
  const title = document.title;
  const description = document.querySelector('meta[name="description"]')?.content;
  const canonical = document.querySelector('link[rel="canonical"]')?.href;
  
  // To check content-encoding: br, we might need a separate network check,
  // but we can try to find it in the navigation resource headers if available.
  // Actually, standard window.performance doesn't expose response headers.
  // I will use browser requests to see the response headers.

  return {
    title,
    description,
    canonical,
    ttfb,
    totalLoadTime
  };
})()