/**
 * Indian Rupee (INR) currency and budget formatting utilities for TRAVELENS.
 * Strictly presents prices exclusively in INR (₹) with Indian numbering format.
 * Completely eliminates USD symbols, ranges, and labels.
 */

export function formatInr(amount) {
  if (amount == null || isNaN(amount)) return '₹0';
  return '₹' + Number(amount).toLocaleString('en-IN');
}

/**
 * Normalises budget tier labels to consistent: Budget, Moderate, Premium
 */
export function normaliseBudgetTier(tier) {
  if (!tier) return 'Moderate';
  const t = String(tier).trim().toLowerCase();
  if (t === 'luxury' || t === 'premium') return 'Premium';
  if (t === 'budget') return 'Budget';
  return 'Moderate';
}

/**
 * Parses any indicative budget string from backend (which may contain "$35 - $65 / ₹3,000 - ₹5,500 per day")
 * and extracts/converts exclusively into a clean INR display string: e.g. "₹3,000 – ₹5,500 / day".
 */
export function formatDailyBudgetInr(rawBudget, defaultTier = 'Moderate') {
  if (!rawBudget || typeof rawBudget !== 'string') {
    const tierDefaults = {
      Budget: '₹2,500 – ₹4,000 / day',
      Moderate: '₹4,500 – ₹7,500 / day',
      Premium: '₹9,500 – ₹18,000 / day'
    };
    return tierDefaults[normaliseBudgetTier(defaultTier)] || '₹4,500 – ₹7,500 / day';
  }

  // 1. If it already contains a ₹ range like "₹3,000 - ₹5,500 per day" or "₹3,000 - ₹5,500"
  if (rawBudget.includes('₹')) {
    const match = rawBudget.match(/₹[\d,]+(?:\s*[-–]\s*₹[\d,]+)?(?:\s*per\s*day)?/i);
    if (match) {
      let cleaned = match[0].replace(/per\s*day/i, '').trim();
      cleaned = cleaned.replace(/\s*-\s*/, ' – ');
      return `${cleaned} / day`;
    }
  }

  // 2. If it contains legacy dollar ranges like "$35 - $65"
  const usdMatch = rawBudget.match(/\$?(\d+)\s*[-–]\s*\$?(\d+)/);
  if (usdMatch) {
    const minInr = Math.round(parseInt(usdMatch[1], 10) * 85 / 100) * 100;
    const maxInr = Math.round(parseInt(usdMatch[2], 10) * 85 / 100) * 100;
    return `₹${minInr.toLocaleString('en-IN')} – ₹${maxInr.toLocaleString('en-IN')} / day`;
  }

  return rawBudget.replace(/\$/g, '₹');
}

/**
 * Standard representative daily rate per person for trip cost estimation
 */
export const DAILY_BUDGET_RATES = {
  Budget: { rate: 3200, label: 'Budget (~₹3,200 per person / day)' },
  Moderate: { rate: 6200, label: 'Moderate (~₹6,200 per person / day)' },
  Premium: { rate: 14500, label: 'Premium (~₹14,500 per person / day)' }
};

export function calculateTripTotalInr(dailyRatePerPerson, travellers = 1, days = 1) {
  const safeTravellers = Math.max(1, parseInt(travellers, 10) || 1);
  const safeDays = Math.max(1, parseInt(days, 10) || 1);
  return dailyRatePerPerson * safeTravellers * safeDays;
}
