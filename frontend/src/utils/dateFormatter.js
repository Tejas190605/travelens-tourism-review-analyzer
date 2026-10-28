/**
 * Unambiguous British English date formatting utility.
 * Formats ISO date strings into "DD Mon YYYY" (e.g. "25 Oct 2025", "7 Feb 2026").
 */
export function formatBritishDate(dateStr) {
  if (!dateStr) return 'Curated Observation';
  const d = new Date(dateStr);
  if (isNaN(d.getTime())) return String(dateStr);
  const day = d.getDate();
  const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  const month = months[d.getMonth()];
  const year = d.getFullYear();
  return `${day} ${month} ${year}`;
}
