import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { Compass, ArrowRight, IndianRupee, MapPin, Users, Clock, Bookmark, BookmarkCheck, Star } from 'lucide-react';
import { getRecommendations, saveDestination, removeSavedDestination, tokenStorage } from '../services/api';
import DestinationImage from '../components/DestinationImage';
import { formatInr, normaliseBudgetTier, DAILY_BUDGET_RATES, calculateTripTotalInr } from '../utils/currencyFormatter';

const REGIONS = ['All', 'India', 'Europe', 'Asia', 'Americas', 'Middle East', 'Africa', 'Oceania'];


const TRAVEL_STYLES = [
  { key: 'heritage', label: 'Heritage & History', desc: 'Monuments, architecture, and cultural depths' },
  { key: 'food', label: 'Food & Culinary Culture', desc: 'Authentic local dining and street food' },
  { key: 'nature', label: 'Nature & Scenery', desc: 'Mountains, verdant hills, and outdoor trails' },
  { key: 'peace', label: 'Peace & Relaxation', desc: 'Low crowds, serene ambiance, and gentle pacing' },
  { key: 'safety', label: 'High Safety & Comfort', desc: 'Well-rated cleanliness, secure stays, and transit' },
  { key: 'budget', label: 'Value for Money', desc: 'Economical dining, transit, and fair entry passes' }
];

export default function Recommend() {
  // Trip Preferences Form State
  const [travellers, setTravellers] = useState(2);
  const [days, setDays] = useState(5);
  const [budgetTier, setBudgetTier] = useState('Moderate');
  const [regionFilter, setRegionFilter] = useState('All');

  // Priorities weights (1-5 scale)
  const [priorities, setPriorities] = useState({
    heritage: 5,
    food: 4,
    nature: 4,
    peace: 3,
    safety: 4,
    budget: 3
  });

  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [savedStatus, setSavedStatus] = useState({});

  const handleSliderChange = (key, val) => {
    setPriorities((prev) => ({
      ...prev,
      [key]: parseInt(val, 10),
    }));
  };

  const handlePlanSubmit = async (e) => {
    if (e) e.preventDefault();
    setLoading(true);
    setError(null);

    const apiBudget = budgetTier === 'Premium' ? 'Luxury' : (budgetTier !== 'All' ? budgetTier : null);

    const payload = {
      heritage: priorities.heritage,
      food: priorities.food,
      adventure: priorities.nature,
      relaxation: priorities.peace,
      family: priorities.safety,
      budget: priorities.budget,
      region_filter: regionFilter !== 'All' ? regionFilter : null,
      budget_filter: apiBudget,
    };

    try {
      const data = await getRecommendations(payload, 6);
      setResults(data.recommendations || []);
      setLoading(false);
    } catch (err) {
      setError(err.message || 'Unable to compute trip recommendations. Please ensure backend is running.');
      setLoading(false);
    }
  };

  const handleToggleSave = async (destId) => {
    const token = tokenStorage.get();
    if (!token) {
      alert('Please sign in to save destinations to your shortlist.');
      return;
    }

    const current = !!savedStatus[destId];
    try {
      if (current) {
        await removeSavedDestination(destId);
        setSavedStatus(prev => ({ ...prev, [destId]: false }));
      } else {
        await saveDestination(destId);
        setSavedStatus(prev => ({ ...prev, [destId]: true }));
      }
    } catch (err) {
      alert(err.message || 'Could not update bookmark.');
    }
  };

  return (
    <main style={{ padding: 'var(--space-2xl) 0 var(--space-4xl)' }}>
      <div className="app-container" style={{ maxWidth: '1060px' }}>
        {/* Header */}
        <header style={{ textAlign: 'center', marginBottom: 'var(--space-2xl)' }}>
          <span style={{ textTransform: 'uppercase', fontSize: '0.8rem', letterSpacing: '0.12em', color: 'var(--color-terracotta)', fontWeight: 700 }}>
            Trip Planning & Personalisation
          </span>
          <h1 style={{ marginTop: '6px', marginBottom: '10px', fontSize: 'clamp(2.2rem, 3.8vw, 3rem)' }}>
            Plan a Trip
          </h1>
          <p style={{ maxWidth: '700px', margin: '0 auto', fontSize: '1.08rem', color: 'var(--color-slate-600)', lineHeight: 1.6 }}>
            Set your budget, number of travellers, and travel priorities. We match your style with verified visitor reviews and calculate indicative INR budgets with suggested day-by-day itineraries.
          </p>
        </header>

        {/* 1. Interactive Trip Builder Form */}
        <section 
          style={{
            backgroundColor: 'var(--color-white)',
            padding: 'var(--space-2xl)',
            borderRadius: 'var(--radius-lg)',
            border: '1px solid var(--color-sand-200)',
            boxShadow: 'var(--shadow-card)',
            marginBottom: 'var(--space-3xl)'
          }}
        >
          {/* Trip Scope Row: Travellers, Days, Budget Tier, Region */}
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: 'var(--space-lg)', paddingBottom: 'var(--space-xl)', borderBottom: '1px solid var(--color-sand-200)', marginBottom: 'var(--space-xl)' }}>
            {/* Travellers */}
            <div>
              <label htmlFor="trip-travellers" style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '0.88rem', fontWeight: 600, color: 'var(--color-slate-800)', marginBottom: '6px' }}>
                <Users size={16} color="var(--color-terracotta)" />
                <span>Travellers:</span>
              </label>
              <input
                id="trip-travellers"
                type="number"
                min="1"
                max="20"
                value={travellers}
                onChange={(e) => {
                  const val = parseInt(e.target.value, 10);
                  setTravellers(isNaN(val) ? 1 : Math.max(1, Math.min(20, val)));
                }}
                style={{ width: '100%', padding: '10px 12px', borderRadius: 'var(--radius-md)', border: '1px solid var(--color-sand-200)', fontSize: '0.95rem' }}
              />
            </div>

            {/* Days */}
            <div>
              <label htmlFor="trip-days" style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '0.88rem', fontWeight: 600, color: 'var(--color-slate-800)', marginBottom: '6px' }}>
                <Clock size={16} color="var(--color-olive)" />
                <span>Trip Duration (Days):</span>
              </label>
              <input
                id="trip-days"
                type="number"
                min="1"
                max="60"
                value={days}
                onChange={(e) => {
                  const val = parseInt(e.target.value, 10);
                  setDays(isNaN(val) ? 1 : Math.max(1, Math.min(60, val)));
                }}
                style={{ width: '100%', padding: '10px 12px', borderRadius: 'var(--radius-md)', border: '1px solid var(--color-sand-200)', fontSize: '0.95rem' }}
              />
            </div>

            {/* Budget Tier */}
            <div>
              <label htmlFor="trip-budget" style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '0.88rem', fontWeight: 600, color: 'var(--color-slate-800)', marginBottom: '6px' }}>
                <IndianRupee size={16} color="var(--color-terracotta)" />
                <span>Budget Category:</span>
              </label>
              <select
                id="trip-budget"
                value={budgetTier}
                onChange={(e) => setBudgetTier(e.target.value)}
                style={{ width: '100%', padding: '10px 12px', borderRadius: 'var(--radius-md)', border: '1px solid var(--color-sand-200)', fontSize: '0.95rem' }}
              >
                <option value="All">Any Budget</option>
                <option value="Budget">Budget (~₹3,200/day)</option>
                <option value="Moderate">Moderate (~₹6,200/day)</option>
                <option value="Premium">Premium (~₹14,500/day)</option>
              </select>
            </div>

            {/* Region */}
            <div>
              <label htmlFor="trip-region" style={{ display: 'flex', alignItems: 'center', gap: '6px', fontSize: '0.88rem', fontWeight: 600, color: 'var(--color-slate-800)', marginBottom: '6px' }}>
                <MapPin size={16} color="var(--color-slate-600)" />
                <span>Region:</span>
              </label>
              <select
                id="trip-region"
                value={regionFilter}
                onChange={(e) => setRegionFilter(e.target.value)}
                style={{ width: '100%', padding: '10px 12px', borderRadius: 'var(--radius-md)', border: '1px solid var(--color-sand-200)', fontSize: '0.95rem' }}
              >
                {REGIONS.map(r => (
                  <option key={r} value={r}>{r === 'All' ? 'All Global Regions' : r}</option>
                ))}
              </select>
            </div>
          </div>

          {/* Travel Style Weights */}
          <div style={{ marginBottom: 'var(--space-xl)' }}>
            <h3 style={{ fontSize: '1.25rem', marginBottom: '4px' }}>What matters most to you?</h3>
            <p style={{ fontSize: '0.92rem', color: 'var(--color-slate-600)', marginBottom: 'var(--space-lg)' }}>
              Adjust these preferences to find destinations that align with your travel style:
            </p>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(290px, 1fr))', gap: 'var(--space-lg) var(--space-2xl)' }}>
              {TRAVEL_STYLES.map(({ key, label, desc }) => {
                const val = priorities[key];
                return (
                  <div key={key} style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline' }}>
                      <span style={{ fontWeight: 600, color: 'var(--color-slate-900)', fontSize: '0.95rem' }}>{label}</span>
                      <span style={{ fontSize: '0.82rem', fontWeight: 700, color: val >= 4 ? 'var(--color-terracotta)' : 'var(--color-slate-600)' }}>
                        {val === 5 ? 'Essential (5/5)' : val === 4 ? 'Important (4/5)' : val === 3 ? 'Moderate (3/5)' : 'Low priority'}
                      </span>
                    </div>
                    <p style={{ fontSize: '0.82rem', color: 'var(--color-slate-500)', margin: 0 }}>{desc}</p>
                    <input
                      type="range"
                      min="1"
                      max="5"
                      step="1"
                      value={val}
                      onChange={(e) => handleSliderChange(key, e.target.value)}
                      style={{ width: '100%', accentColor: 'var(--color-terracotta)', cursor: 'pointer', marginTop: '4px' }}
                    />
                  </div>
                );
              })}
            </div>
          </div>

          {/* Find Matches CTA */}
          <div style={{ textAlign: 'center', borderTop: '1px solid var(--color-sand-200)', paddingTop: 'var(--space-xl)' }}>
            <button
              onClick={handlePlanSubmit}
              disabled={loading}
              className="btn btn-primary"
              style={{ padding: '14px 40px', fontSize: '1.02rem', display: 'inline-flex', alignItems: 'center', gap: '8px' }}
            >
              <Compass size={20} />
              <span>{loading ? 'Finding Best Matches...' : 'Find Matching Destinations'}</span>
            </button>
          </div>
        </section>

        {/* Error Notification */}
        {error && (
          <div className="state-box" style={{ borderColor: 'var(--color-crimson)', marginBottom: 'var(--space-xl)' }}>
            <p style={{ color: 'var(--color-crimson)', fontWeight: 600 }}>{error}</p>
          </div>
        )}

        {/* Loading Spinner */}
        {loading && (
          <div className="state-box" style={{ padding: 'var(--space-4xl) var(--space-xl)' }}>
            <div className="spinner"></div>
            <p style={{ marginTop: '16px', color: 'var(--color-slate-600)' }}>Analysing verified destination reviews for your criteria...</p>
          </div>
        )}

        {/* 2. Recommended Destination Matches */}
        {results && !loading && (
          <section>
            <div style={{ marginBottom: 'var(--space-xl)' }}>
              <span style={{ textTransform: 'uppercase', fontSize: '0.8rem', letterSpacing: '0.12em', color: 'var(--color-terracotta)', fontWeight: 700 }}>
                Matched Destinations
              </span>
              <h2 style={{ fontSize: '1.9rem', marginTop: '4px', marginBottom: '6px' }}>
                Recommended Places for Your {days}-Day Trip
              </h2>
              <p style={{ fontSize: '1rem', color: 'var(--color-slate-600)' }}>
                Destinations matching your preferences, with calculated total INR estimates and suggested itineraries.
              </p>
            </div>

            {results.length === 0 ? (
              <div className="state-box" style={{ padding: 'var(--space-4xl) var(--space-xl)' }}>
                <Compass size={40} className="state-box-icon" style={{ color: 'var(--color-terracotta)', marginBottom: '12px' }} />
                <h3>No destinations matched these specific criteria</h3>
                <p style={{ maxWidth: '440px', margin: '0 auto 16px', color: 'var(--color-slate-600)' }}>
                  Try broadening your region or selecting 'Any Budget'.
                </p>
                <button
                  type="button"
                  onClick={() => {
                    setRegionFilter('All');
                    setBudgetTier('All');
                    handlePlanSubmit();
                  }}
                  className="btn btn-secondary"
                  style={{ fontSize: '0.9rem', padding: '8px 18px' }}
                >
                  Reset Region & Budget Filters
                </button>
              </div>
            ) : (
              <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-2xl)' }}>
                {results.map((item) => {
                  const normalized = normaliseBudgetTier(item.budget_tier);
                  const ratePerPerson = DAILY_BUDGET_RATES[normalized]?.rate || 6200;
                  const totalEstimate = calculateTripTotalInr(ratePerPerson, travellers, days);

                  let itineraryDays = [];
                  if (item.suggested_itinerary) {
                    itineraryDays = item.suggested_itinerary.split(/(?=Day \d+:)/).filter(s => s.trim()).slice(0, 3);
                  }

                  // Explainable match reasons from top_matches or fallback reasons
                  const matchFactors = (item.top_matches && item.top_matches.length > 0)
                    ? item.top_matches
                    : (item.reasons || []);

                  const isSaved = !!savedStatus[item.destination_id];

                  return (
                    <article
                      key={item.destination_id}
                      style={{
                        backgroundColor: 'var(--color-white)',
                        borderRadius: 'var(--radius-lg)',
                        border: '1px solid var(--color-sand-200)',
                        boxShadow: 'var(--shadow-card)',
                        overflow: 'hidden'
                      }}
                    >
                      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))' }}>
                        {/* Destination Photo */}
                        <div style={{ position: 'relative', minHeight: '280px' }}>
                          <DestinationImage
                            src={item.image_url}
                            alt={item.name}
                            category={item.category}
                            style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                          />
                          <span 
                            className="badge badge-category"
                            style={{ position: 'absolute', top: '14px', right: '14px', backgroundColor: '#FFFFFF', color: 'var(--color-slate-900)', fontWeight: 600 }}
                          >
                            {item.category}
                          </span>
                        </div>

                        {/* Destination Info & Calculated Budget */}
                        <div style={{ padding: 'var(--space-2xl)', display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
                          <div>
                            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', marginBottom: '4px' }}>
                              <span style={{ fontSize: '0.82rem', color: 'var(--color-terracotta)', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                                {item.state_or_region ? `${item.state_or_region}, ${item.country}` : item.country}
                              </span>
                              <div style={{ display: 'flex', alignItems: 'center', gap: '4px', color: 'var(--color-terracotta)' }}>
                                <Star size={15} fill="currentColor" />
                                <span style={{ fontWeight: 700, fontSize: '0.95rem', color: 'var(--color-slate-900)' }}>
                                  {item.average_rating ? Number(item.average_rating).toFixed(1) : '4.5'}
                                </span>
                                <span style={{ fontSize: '0.8rem', color: 'var(--color-slate-500)' }}>
                                  ({item.total_reviews} reviews)
                                </span>
                              </div>
                            </div>

                            <h3 style={{ fontSize: '1.6rem', marginBottom: '8px' }}>
                              <Link to={`/destinations/${item.destination_id}`} style={{ color: 'inherit', textDecoration: 'none' }}>
                                {item.name}
                              </Link>
                            </h3>

                            <p style={{ fontSize: '0.95rem', color: 'var(--color-slate-600)', lineHeight: 1.55, marginBottom: 'var(--space-lg)' }}>
                              {item.description}
                            </p>

                            {/* Transparent Trip Cost Calculation in INR with Inclusions & Exclusions */}
                            <div style={{ backgroundColor: 'var(--color-sand-50)', padding: '16px', borderRadius: 'var(--radius-md)', border: '1px solid var(--color-sand-200)', marginBottom: 'var(--space-lg)' }}>
                              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', marginBottom: '4px' }}>
                                <span style={{ fontSize: '0.82rem', textTransform: 'uppercase', letterSpacing: '0.05em', color: 'var(--color-slate-500)', fontWeight: 700 }}>
                                  Estimated Trip Budget (INR)
                                </span>
                                <strong style={{ fontSize: '1.35rem', color: 'var(--color-slate-900)' }}>
                                  {formatInr(totalEstimate)}
                                </strong>
                              </div>
                              <p style={{ margin: '0 0 6px 0', fontSize: '0.82rem', color: 'var(--color-slate-600)' }}>
                                {formatInr(ratePerPerson)}/person/day × {travellers} traveller{travellers > 1 ? 's' : ''} × {days} days.
                              </p>
                              <div style={{ fontSize: '0.76rem', color: 'var(--color-slate-500)', display: 'flex', flexDirection: 'column', gap: '2px', borderTop: '1px dashed var(--color-sand-300)', paddingTop: '6px' }}>
                                <span><strong style={{ color: 'var(--color-olive)' }}>✓ Includes:</strong> Accommodation, daily dining, local transit & sightseeing entry.</span>
                                <span><strong style={{ color: 'var(--color-slate-600)' }}>✕ Excludes:</strong> Long-distance flights, visa fees & discretionary shopping.</span>
                              </div>
                            </div>

                            {/* Why it matches (Explainable match factors) */}
                            {matchFactors.length > 0 && (
                              <div style={{ marginBottom: '12px' }}>
                                <span style={{ fontSize: '0.82rem', color: 'var(--color-olive)', fontWeight: 700, textTransform: 'uppercase', display: 'block', marginBottom: '4px' }}>
                                  Why It Fits Your Travel Style:
                                </span>
                                <ul style={{ listStyle: 'none', padding: 0, margin: 0, display: 'flex', flexDirection: 'column', gap: '4px' }}>
                                  {matchFactors.slice(0, 3).map((r, i) => (
                                    <li key={i} style={{ display: 'flex', alignItems: 'flex-start', gap: '8px', fontSize: '0.9rem', color: 'var(--color-slate-800)' }}>
                                      <span style={{ color: 'var(--color-olive)', fontWeight: 700 }}>✓</span>
                                      <span>{r}</span>
                                    </li>
                                  ))}
                                </ul>
                              </div>
                            )}

                            {/* Trade-offs to consider */}
                            {item.trade_offs && item.trade_offs.length > 0 && (
                              <div style={{ marginBottom: 'var(--space-md)' }}>
                                <span style={{ fontSize: '0.82rem', color: 'var(--color-crimson)', fontWeight: 700, textTransform: 'uppercase', display: 'block', marginBottom: '4px' }}>
                                  Honest Caveats to Keep in Mind:
                                </span>
                                <ul style={{ listStyle: 'none', padding: 0, margin: 0, display: 'flex', flexDirection: 'column', gap: '4px' }}>
                                  {item.trade_offs.slice(0, 2).map((to, i) => (
                                    <li key={i} style={{ display: 'flex', alignItems: 'flex-start', gap: '8px', fontSize: '0.88rem', color: 'var(--color-slate-700)' }}>
                                      <span style={{ color: 'var(--color-crimson)', fontWeight: 700 }}>•</span>
                                      <span>{to}</span>
                                    </li>
                                  ))}
                                </ul>
                              </div>
                            )}

                            {/* Data-Driven Summary Explanation */}
                            {item.explanation && (
                              <p style={{ fontSize: '0.82rem', color: 'var(--color-slate-600)', backgroundColor: 'var(--color-sand-100)', padding: '8px 12px', borderRadius: 'var(--radius-sm)', margin: '0 0 var(--space-md) 0' }}>
                                <strong>Assessment:</strong> {item.explanation}
                              </p>
                            )}
                          </div>

                          {/* Action Buttons */}
                          <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap', borderTop: '1px solid var(--color-sand-200)', paddingTop: 'var(--space-md)' }}>
                            <Link 
                              to={`/destinations/${item.destination_id}`} 
                              className="btn btn-primary"
                              style={{ padding: '10px 18px', fontSize: '0.9rem' }}
                            >
                              <span>View Destination Guide</span>
                              <ArrowRight size={16} />
                            </Link>

                            <button
                              onClick={() => handleToggleSave(item.destination_id)}
                              className="btn btn-secondary"
                              style={{ padding: '10px 16px', fontSize: '0.9rem', display: 'inline-flex', alignItems: 'center', gap: '6px' }}
                            >
                              {isSaved ? <BookmarkCheck size={16} /> : <Bookmark size={16} />}
                              <span>{isSaved ? 'Saved' : 'Save to Shortlist'}</span>
                            </button>

                            <Link
                              to={`/compare?destA=${item.destination_id}`}
                              className="btn btn-ghost"
                              style={{ padding: '10px 14px', fontSize: '0.9rem' }}
                            >
                              <span>Compare Place</span>
                            </Link>
                          </div>
                        </div>
                      </div>

                      {/* Day-by-Day Itinerary Preview Accordion/Snippet */}
                      {itineraryDays.length > 0 && (
                        <div style={{ borderTop: '1px solid var(--color-sand-200)', backgroundColor: 'var(--color-sand-50)', padding: 'var(--space-lg) var(--space-2xl)' }}>
                          <span style={{ fontSize: '0.82rem', fontWeight: 700, textTransform: 'uppercase', color: 'var(--color-slate-500)', display: 'block', marginBottom: '8px' }}>
                            Suggested Itinerary Preview:
                          </span>
                          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '12px' }}>
                            {itineraryDays.map((dStr, idx) => (
                              <div key={idx} style={{ padding: '10px 14px', backgroundColor: '#FFFFFF', borderRadius: 'var(--radius-sm)', border: '1px solid var(--color-sand-200)', fontSize: '0.88rem', color: 'var(--color-slate-800)' }}>
                                {dStr.trim()}
                              </div>
                            ))}
                          </div>
                        </div>
                      )}
                    </article>
                  );
                })}
              </div>
            )}
          </section>
        )}
      </div>
    </main>
  );
}
