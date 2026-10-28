import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Bookmark, Trash2, ArrowRight, Mail, Compass, Calculator, Star } from 'lucide-react';
import { getMe, getSavedDestinations, removeSavedDestination, logoutUser, tokenStorage } from '../services/api';
import DestinationImage from '../components/DestinationImage';
import { formatInr, formatDailyBudgetInr, normaliseBudgetTier, DAILY_BUDGET_RATES, calculateTripTotalInr } from '../utils/currencyFormatter';

export default function Profile() {
  const navigate = useNavigate();
  const [user, setUser] = useState(null);
  const [savedItems, setSavedItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Trip Budget Calculator State
  const [calcDays, setCalcDays] = useState(5);
  const [calcTier, setCalcTier] = useState('Moderate');
  const [calcTravelers, setCalcTravelers] = useState(2);

  useEffect(() => {
    const token = tokenStorage.get();
    if (!token) {
      navigate('/login');
      return;
    }

    async function loadProfileData() {
      try {
        setLoading(true);
        const [userData, savedData] = await Promise.all([
          getMe(),
          getSavedDestinations(),
        ]);
        setUser(userData);
        setSavedItems(savedData || []);
        setLoading(false);
      } catch (err) {
        setError(err.message || 'Failed to load account. Please sign in again.');
        setLoading(false);
      }
    }

    loadProfileData();
  }, [navigate]);

  const handleRemove = async (destId) => {
    try {
      await removeSavedDestination(destId);
      setSavedItems((prev) => prev.filter((item) => item.destination_id !== destId));
    } catch (err) {
      alert('Could not remove bookmark: ' + err.message);
    }
  };

  const handleLogout = () => {
    logoutUser();
    navigate('/');
    window.location.reload();
  };

  // Mathematically verified INR calculator
  const normalizedTier = normaliseBudgetTier(calcTier);
  const tierConfig = DAILY_BUDGET_RATES[normalizedTier] || DAILY_BUDGET_RATES.Moderate;
  const totalTripInr = calculateTripTotalInr(tierConfig.rate, calcTravelers, calcDays);

  if (loading) {
    return (
      <main className="app-container" style={{ padding: 'var(--space-4xl) 0' }}>
        <div className="state-box">
          <div className="spinner"></div>
          <p style={{ marginTop: '16px' }}>Loading your saved places...</p>
        </div>
      </main>
    );
  }

  if (error || !user) {
    return (
      <main className="app-container" style={{ padding: 'var(--space-4xl) 0' }}>
        <div className="state-box">
          <p style={{ color: 'var(--color-crimson)', marginBottom: '16px', fontWeight: 600 }}>{error || 'Session expired.'}</p>
          <Link to="/login" className="btn btn-primary">Sign In to TRAVELENS</Link>
        </div>
      </main>
    );
  }

  const savedIdsParam = savedItems.map(item => item.destination_id).slice(0, 4).join(',');

  return (
    <main style={{ padding: 'var(--space-2xl) 0 var(--space-4xl)' }}>
      <div className="app-container" style={{ maxWidth: '1040px' }}>
        {/* Profile Card Header */}
        <section 
          style={{
            backgroundColor: 'var(--color-white)',
            borderRadius: 'var(--radius-lg)',
            border: '1px solid var(--color-sand-200)',
            padding: 'var(--space-2xl)',
            boxShadow: 'var(--shadow-card)',
            marginBottom: 'var(--space-2xl)',
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            flexWrap: 'wrap',
            gap: '20px'
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '18px' }}>
            <div 
              style={{
                width: '64px',
                height: '64px',
                borderRadius: '50%',
                backgroundColor: 'var(--color-terracotta)',
                color: '#FFFFFF',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: '1.6rem',
                fontFamily: 'var(--font-serif)',
                fontWeight: 700
              }}
            >
              {user.name ? user.name[0].toUpperCase() : 'U'}
            </div>
            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <h1 style={{ fontSize: '1.6rem', margin: 0 }}>{user.name}</h1>
                <span className="badge badge-category" style={{ fontSize: '0.75rem', fontWeight: 600 }}>
                  Traveller Account
                </span>
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '16px', marginTop: '6px', fontSize: '0.88rem', color: 'var(--color-slate-500)', flexWrap: 'wrap' }}>
                <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                  <Mail size={14} />
                  {user.email}
                </span>
                <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                  <Bookmark size={14} />
                  {savedItems.length} Shortlisted Places
                </span>
              </div>
            </div>
          </div>

          <button onClick={handleLogout} className="btn btn-secondary" style={{ fontSize: '0.9rem', padding: '9px 18px' }}>
            Sign Out
          </button>
        </section>

        {/* Shortlisted Destinations */}
        <section style={{ marginBottom: 'var(--space-3xl)' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 'var(--space-lg)', flexWrap: 'wrap', gap: '12px' }}>
            <div>
              <h2 style={{ fontSize: '1.6rem', margin: 0 }}>Shortlisted Destinations ({savedItems.length})</h2>
              <p style={{ fontSize: '0.92rem', color: 'var(--color-slate-600)', margin: '4px 0 0' }}>
                Places you have saved for upcoming trips.
              </p>
            </div>

            {savedItems.length >= 2 && (
              <Link 
                to={`/compare?dests=${savedIdsParam}`} 
                className="btn btn-primary"
                style={{ fontSize: '0.88rem', padding: '8px 16px', display: 'inline-flex', alignItems: 'center', gap: '6px' }}
              >
                <Compass size={16} />
                <span>Compare Shortlisted Places</span>
              </Link>
            )}
          </div>

          {savedItems.length === 0 ? (
            <div className="state-box" style={{ padding: 'var(--space-4xl) var(--space-xl)' }}>
              <Bookmark size={40} className="state-box-icon" style={{ color: 'var(--color-terracotta)', marginBottom: '12px' }} />
              <h3 style={{ marginBottom: '6px' }}>Your shortlist is currently empty</h3>
              <p style={{ maxWidth: '440px', margin: '0 auto 20px', color: 'var(--color-slate-600)', fontSize: '0.95rem' }}>
                Explore destinations in our curated catalogue and click "Save Destination" to build your trip shortlist.
              </p>
              <Link to="/explore" className="btn btn-primary">
                Browse Destinations
              </Link>
            </div>
          ) : (
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(290px, 1fr))', gap: 'var(--space-xl)' }}>
              {savedItems.map((item) => {
                const dest = item.destination;
                if (!dest) return null;

                const dailyInrStr = formatDailyBudgetInr(dest.indicative_daily_budget, dest.budget_tier);

                return (
                  <article key={item.destination_id} className="destination-card">
                    <div style={{ position: 'relative', height: '200px', overflow: 'hidden' }}>
                      <DestinationImage 
                        src={dest.image_url} 
                        alt={dest.name} 
                        category={dest.category} 
                        style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                      />
                      <button
                        onClick={() => handleRemove(item.destination_id)}
                        title="Remove from shortlisted places"
                        style={{
                          position: 'absolute',
                          top: '10px',
                          right: '10px',
                          background: 'rgba(255,255,255,0.92)',
                          border: 'none',
                          borderRadius: '50%',
                          width: '32px',
                          height: '32px',
                          display: 'flex',
                          alignItems: 'center',
                          justifyContent: 'center',
                          cursor: 'pointer',
                          color: 'var(--color-crimson)',
                          boxShadow: '0 2px 6px rgba(0,0,0,0.15)'
                        }}
                      >
                        <Trash2 size={16} />
                      </button>
                      <span 
                        className="badge badge-category" 
                        style={{ position: 'absolute', bottom: '10px', left: '10px', backgroundColor: '#FFFFFF', color: 'var(--color-slate-900)', fontWeight: 600 }}
                      >
                        {dest.category}
                      </span>
                    </div>

                    <div style={{ padding: 'var(--space-lg)', display: 'flex', flexDirection: 'column', flex: 1 }}>
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', marginBottom: '4px' }}>
                        <span style={{ fontSize: '0.8rem', color: 'var(--color-terracotta)', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                          {dest.state_or_region ? `${dest.state_or_region}, ${dest.country}` : dest.country}
                        </span>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '4px', color: 'var(--color-terracotta)' }}>
                          <Star size={15} fill="currentColor" />
                          <span style={{ fontWeight: 700, fontSize: '0.92rem', color: 'var(--color-slate-900)' }}>
                            {dest.average_rating ? Number(dest.average_rating).toFixed(1) : '4.5'}
                          </span>
                        </div>
                      </div>

                      <h3 style={{ fontSize: '1.3rem', marginBottom: '8px' }}>
                        <Link to={`/destinations/${dest.id}`} style={{ color: 'inherit', textDecoration: 'none' }}>
                          {dest.name}
                        </Link>
                      </h3>

                      <p style={{ fontSize: '0.9rem', color: 'var(--color-slate-600)', marginBottom: 'var(--space-md)', flex: 1, display: '-webkit-box', WebkitLineClamp: 2, WebkitBoxOrient: 'vertical', overflow: 'hidden', lineHeight: 1.5 }}>
                        {dest.description}
                      </p>

                      <div style={{ borderTop: '1px solid var(--color-sand-200)', paddingTop: '10px', marginBottom: 'var(--space-md)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontSize: '0.85rem' }}>
                        <span style={{ color: 'var(--color-slate-500)' }}>Daily budget:</span>
                        <strong style={{ color: 'var(--color-slate-900)' }}>{dailyInrStr}</strong>
                      </div>

                      <div style={{ display: 'flex', gap: '8px' }}>
                        <Link 
                          to={`/destinations/${dest.id}`} 
                          className="btn btn-secondary" 
                          style={{ flex: 1, justifyContent: 'center', fontSize: '0.88rem', padding: '8px 12px' }}
                        >
                          <span>View Guide</span>
                          <ArrowRight size={14} />
                        </Link>
                        <Link 
                          to={`/compare?destA=${dest.id}`} 
                          className="btn btn-ghost" 
                          style={{ fontSize: '0.88rem', padding: '8px 12px' }}
                          title="Compare with another place"
                        >
                          <Compass size={16} />
                        </Link>
                      </div>
                    </div>
                  </article>
                );
              })}
            </div>
          )}
        </section>

        {/* INR Trip Budget Estimator */}
        <section 
          style={{
            backgroundColor: 'var(--color-white)',
            borderRadius: 'var(--radius-lg)',
            border: '1px solid var(--color-sand-200)',
            padding: 'var(--space-2xl)',
            boxShadow: 'var(--shadow-subtle)'
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '8px' }}>
            <Calculator size={22} color="var(--color-terracotta)" />
            <h2 style={{ margin: 0, fontSize: '1.4rem' }}>Trip Cost Estimator (INR)</h2>
          </div>
          <p style={{ fontSize: '0.95rem', color: 'var(--color-slate-600)', marginBottom: 'var(--space-xl)' }}>
            Calculate estimated trip budgets in Indian Rupees based on realistic daily travel expenses.
          </p>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: 'var(--space-lg)', marginBottom: 'var(--space-xl)' }}>
            <div>
              <label htmlFor="calc-days" style={{ display: 'block', fontSize: '0.88rem', fontWeight: 600, color: 'var(--color-slate-700)', marginBottom: '6px' }}>
                Trip Duration (Days):
              </label>
              <input
                id="calc-days"
                type="number"
                min="1"
                max="60"
                value={calcDays}
                onChange={(e) => {
                  const val = parseInt(e.target.value, 10);
                  setCalcDays(isNaN(val) ? 1 : Math.max(1, Math.min(60, val)));
                }}
                style={{ width: '100%', padding: '10px 14px', borderRadius: 'var(--radius-md)', border: '1px solid var(--color-sand-200)', fontSize: '0.95rem' }}
              />
            </div>

            <div>
              <label htmlFor="calc-travellers" style={{ display: 'block', fontSize: '0.88rem', fontWeight: 600, color: 'var(--color-slate-700)', marginBottom: '6px' }}>
                Number of Travellers:
              </label>
              <input
                id="calc-travellers"
                type="number"
                min="1"
                max="20"
                value={calcTravelers}
                onChange={(e) => {
                  const val = parseInt(e.target.value, 10);
                  setCalcTravelers(isNaN(val) ? 1 : Math.max(1, Math.min(20, val)));
                }}
                style={{ width: '100%', padding: '10px 14px', borderRadius: 'var(--radius-md)', border: '1px solid var(--color-sand-200)', fontSize: '0.95rem' }}
              />
            </div>

            <div>
              <label htmlFor="calc-tier" style={{ display: 'block', fontSize: '0.88rem', fontWeight: 600, color: 'var(--color-slate-700)', marginBottom: '6px' }}>
                Budget Category:
              </label>
              <select
                id="calc-tier"
                value={calcTier}
                onChange={(e) => setCalcTier(e.target.value)}
                style={{ width: '100%', padding: '10px 14px', borderRadius: 'var(--radius-md)', border: '1px solid var(--color-sand-200)', fontSize: '0.95rem' }}
              >
                <option value="Budget">Budget (~₹3,200 / person / day)</option>
                <option value="Moderate">Moderate (~₹6,200 / person / day)</option>
                <option value="Premium">Premium (~₹14,500 / person / day)</option>
              </select>
            </div>
          </div>

          <div 
            style={{ 
              backgroundColor: 'var(--color-sand-50)', 
              padding: 'var(--space-xl)', 
              borderRadius: 'var(--radius-md)', 
              border: '1px solid var(--color-sand-200)',
              display: 'flex', 
              justifyContent: 'space-between', 
              alignItems: 'center', 
              flexWrap: 'wrap', 
              gap: '16px' 
            }}
          >
            <div>
              <span style={{ fontSize: '0.85rem', textTransform: 'uppercase', letterSpacing: '0.06em', color: 'var(--color-slate-500)', fontWeight: 700, display: 'block' }}>
                Calculated Total Trip Estimate
              </span>
              <span style={{ fontSize: '2.1rem', fontWeight: 700, color: 'var(--color-slate-900)', display: 'block', marginTop: '2px' }}>
                {formatInr(totalTripInr)}
              </span>
              <span style={{ fontSize: '0.85rem', color: 'var(--color-slate-600)' }}>
                {formatInr(tierConfig.rate)}/day × {calcTravelers} traveller{calcTravelers > 1 ? 's' : ''} × {calcDays} days.
              </span>
            </div>

            <div style={{ maxWidth: '420px', fontSize: '0.8rem', color: 'var(--color-slate-600)', lineHeight: 1.5, borderLeft: '3px solid var(--color-terracotta)', paddingLeft: '12px' }}>
              <div style={{ marginBottom: '4px' }}>
                <strong style={{ color: 'var(--color-olive)' }}>✓ Includes:</strong> Standard stay, daily meals, local transit, entry tickets.
              </div>
              <div style={{ marginBottom: '4px' }}>
                <strong style={{ color: 'var(--color-slate-600)' }}>✕ Excludes:</strong> Long-distance transport, seasonal surges, visa/insurance.
              </div>
              <span style={{ fontStyle: 'italic', color: 'var(--color-slate-500)', fontSize: '0.75rem', display: 'block' }}>
                * Indicative benchmark only. Not a live price quote or guaranteed booking rate.
              </span>
            </div>
          </div>
        </section>
      </div>
    </main>
  );
}
