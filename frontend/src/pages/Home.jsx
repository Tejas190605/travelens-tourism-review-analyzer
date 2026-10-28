import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Search, Compass, ArrowRight, Star, IndianRupee, Sparkles, X } from 'lucide-react';
import { getDestinations } from '../services/api';
import DestinationImage from '../components/DestinationImage';
import { formatDailyBudgetInr } from '../utils/currencyFormatter';

const CURATED_COLLECTIONS = [
  { id: 'all', label: 'All Curated', filter: () => true },
  { id: 'heritage', label: 'Heritage & Culture', filter: (d) => d.category === 'Heritage' || d.category === 'Cultural' },
  { id: 'nature', label: 'Nature Escapes', filter: (d) => d.category === 'Nature' },
  { id: 'coastal', label: 'Coastal Breaks', filter: (d) => d.category === 'Coastal' || d.category === 'Island' },
  { id: 'weekend', label: 'Weekend Getaways', filter: (d) => (d.recommended_duration && d.recommended_duration.includes('2') || d.recommended_duration?.includes('3')) },
  { id: 'urban', label: 'Urban & Art', filter: (d) => d.category === 'Urban' }
];

const SEARCH_SUGGESTIONS = ['Jaipur', 'Varanasi', 'Goa', 'Munnar', 'Florence', 'Paris'];

export default function Home() {
  const [destinations, setDestinations] = useState([]);
  const [activeCollection, setActiveCollection] = useState('all');
  const [searchQuery, setSearchQuery] = useState('');
  const [showWalkthrough, setShowWalkthrough] = useState(() => {
    try {
      return localStorage.getItem('travelens_walkthrough_dismissed') !== 'true';
    } catch {
      return true;
    }
  });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleDismissWalkthrough = () => {
    setShowWalkthrough(false);
    try {
      localStorage.setItem('travelens_walkthrough_dismissed', 'true');
    } catch {}
  };


  useEffect(() => {
    getDestinations()
      .then((data) => {
        // Guarantee deduplication by unique destination id
        const unique = Array.from(new Map(data.map((d) => [d.id, d])).values());
        setDestinations(unique);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message || 'Unable to load destinations.');
        setLoading(false);
      });
  }, []);

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    if (searchQuery.trim()) {
      navigate(`/explore?query=${encodeURIComponent(searchQuery.trim())}`);
    } else {
      navigate('/explore');
    }
  };

  const handleSuggestionClick = (name) => {
    navigate(`/explore?query=${encodeURIComponent(name)}`);
  };

  // Filter curated destinations according to active collection
  const currentCollectionConfig = CURATED_COLLECTIONS.find(c => c.id === activeCollection) || CURATED_COLLECTIONS[0];
  const filteredFeatured = destinations.filter(currentCollectionConfig.filter).slice(0, 6);

  return (
    <main>
      {/* 1. Immersive Editorial Hero Section */}
      <section 
        style={{
          position: 'relative',
          minHeight: '76vh',
          display: 'flex',
          alignItems: 'center',
          backgroundColor: '#192024',
          color: '#FFFFFF',
          overflow: 'hidden'
        }}
      >
        {/* Background Photography with Natural Contrast */}
        <div 
          style={{
            position: 'absolute',
            inset: 0,
            backgroundImage: 'url("https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?q=80&w=1920&auto=format&fit=crop")',
            backgroundSize: 'cover',
            backgroundPosition: 'center 40%',
            opacity: 0.38,
            filter: 'contrast(1.08)'
          }}
        />

        {/* Soft Vignette Gradient */}
        <div 
          style={{
            position: 'absolute',
            inset: 0,
            background: 'linear-gradient(to top, rgba(25, 32, 36, 0.95) 0%, rgba(25, 32, 36, 0.45) 55%, rgba(25, 32, 36, 0.8) 100%)'
          }}
        />

        <div className="app-container" style={{ position: 'relative', zIndex: 10, padding: 'var(--space-4xl) var(--space-lg)' }}>
          <div style={{ maxWidth: '820px' }}>
            <span 
              className="badge" 
              style={{ 
                backgroundColor: 'rgba(194, 94, 56, 0.3)', 
                color: '#EFE6D4', 
                border: '1px solid rgba(194, 94, 56, 0.5)',
                marginBottom: 'var(--space-md)',
                fontSize: '0.85rem',
                letterSpacing: '0.04em',
                fontWeight: 600
              }}
            >
              TRAVELENS — Find places worth travelling for.
            </span>

            <h1 style={{ color: '#FFFFFF', marginBottom: 'var(--space-md)', fontWeight: 600, fontSize: 'clamp(2.5rem, 5vw, 3.8rem)', lineHeight: 1.15 }}>
              Discover destinations as<br />
              <span style={{ fontStyle: 'italic', fontWeight: 400, color: '#E8DFC8', fontFamily: 'var(--font-serif)' }}>
                travellers truly see them.
              </span>
            </h1>

            <p style={{ color: '#D8DFE3', fontSize: '1.18rem', lineHeight: 1.65, marginBottom: 'var(--space-xl)', maxWidth: '720px' }}>
              Discover destinations, understand what visitors say about food, safety, crowds and more, and plan your trip with transparent budget estimates.
            </p>

            {/* Central Search Box */}
            <form 
              onSubmit={handleSearchSubmit}
              style={{
                display: 'flex',
                alignItems: 'center',
                backgroundColor: '#FFFFFF',
                borderRadius: 'var(--radius-md)',
                padding: '6px 8px 6px 18px',
                maxWidth: '640px',
                marginBottom: 'var(--space-md)',
                boxShadow: '0 10px 30px rgba(0,0,0,0.3)'
              }}
            >
              <Search size={20} color="var(--color-slate-400)" style={{ flexShrink: 0, marginRight: '10px' }} />
              <input 
                type="text" 
                placeholder="Where do you want to go? (e.g. Jaipur, Munnar, Goa, Paris)..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                style={{
                  border: 'none',
                  outline: 'none',
                  width: '100%',
                  fontSize: '1rem',
                  fontFamily: 'var(--font-sans)',
                  color: 'var(--color-slate-900)'
                }}
              />
              <button type="submit" className="btn btn-primary" style={{ padding: '12px 24px', fontSize: '0.95rem' }}>
                Search
              </button>
            </form>

            {/* Quick Suggestions */}
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap', marginBottom: 'var(--space-2xl)', fontSize: '0.9rem', color: '#B6C3C9' }}>
              <span>Popular places:</span>
              {SEARCH_SUGGESTIONS.map((city) => (
                <button
                  key={city}
                  type="button"
                  onClick={() => handleSuggestionClick(city)}
                  style={{
                    background: 'none',
                    border: 'none',
                    color: '#E8DFC8',
                    textDecoration: 'underline',
                    cursor: 'pointer',
                    fontSize: '0.9rem'
                  }}
                >
                  {city}
                </button>
              ))}
            </div>

            {/* Action Buttons */}
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: 'var(--space-md)' }}>
              <Link to="/explore" className="btn btn-primary" style={{ padding: '13px 26px', fontSize: '1rem' }}>
                <span>Explore Destinations</span>
                <ArrowRight size={18} />
              </Link>
              <Link to="/plan" className="btn btn-outline" style={{ borderColor: '#E8DFC8', color: '#FFFFFF', padding: '13px 24px', fontSize: '1rem' }}>
                <span>Plan a Trip</span>
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* Dismissible 3-Step Walkthrough Banner */}
      {showWalkthrough && (
        <section style={{ backgroundColor: 'var(--color-sand-100)', borderBottom: '1px solid var(--color-sand-200)', padding: 'var(--space-xl) 0' }}>
          <div className="app-container">
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 'var(--space-md)' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                <Compass size={18} color="var(--color-terracotta)" />
                <span style={{ fontSize: '0.85rem', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.06em', color: 'var(--color-slate-800)' }}>
                  How TRAVELENS Helps You Plan Confidently
                </span>
              </div>
              <button
                type="button"
                onClick={handleDismissWalkthrough}
                aria-label="Dismiss walkthrough banner"
                style={{
                  background: 'none',
                  border: 'none',
                  cursor: 'pointer',
                  color: 'var(--color-slate-500)',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '4px',
                  fontSize: '0.82rem',
                  padding: '4px 8px'
                }}
              >
                <span>Dismiss</span>
                <X size={16} />
              </button>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))', gap: 'var(--space-md)' }}>
              <div style={{ backgroundColor: '#FFFFFF', padding: '14px 16px', borderRadius: 'var(--radius-md)', border: '1px solid var(--color-sand-200)' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '6px' }}>
                  <span style={{ display: 'inline-flex', alignItems: 'center', justifyContent: 'center', width: '22px', height: '22px', borderRadius: '50%', backgroundColor: 'var(--color-terracotta)', color: '#FFFFFF', fontSize: '0.75rem', fontWeight: 700 }}>1</span>
                  <strong style={{ fontSize: '0.92rem', color: 'var(--color-slate-900)' }}>Search & Discover</strong>
                </div>
                <p style={{ margin: 0, fontSize: '0.82rem', color: 'var(--color-slate-600)', lineHeight: 1.45 }}>
                  Find destinations across India and global hubs with filtering by geography, travel style, and budget tiers.
                </p>
              </div>

              <div style={{ backgroundColor: '#FFFFFF', padding: '14px 16px', borderRadius: 'var(--radius-md)', border: '1px solid var(--color-sand-200)' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '6px' }}>
                  <span style={{ display: 'inline-flex', alignItems: 'center', justifyContent: 'center', width: '22px', height: '22px', borderRadius: '50%', backgroundColor: 'var(--color-terracotta)', color: '#FFFFFF', fontSize: '0.75rem', fontWeight: 700 }}>2</span>
                  <strong style={{ fontSize: '0.92rem', color: 'var(--color-slate-900)' }}>Understand Review Consensus</strong>
                </div>
                <p style={{ margin: 0, fontSize: '0.82rem', color: 'var(--color-slate-600)', lineHeight: 1.45 }}>
                  Review 9 dimensions (Food, Safety, Cleanliness, Price, etc.) with transparent mention counts and honest caveats.
                </p>
              </div>

              <div style={{ backgroundColor: '#FFFFFF', padding: '14px 16px', borderRadius: 'var(--radius-md)', border: '1px solid var(--color-sand-200)' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '6px' }}>
                  <span style={{ display: 'inline-flex', alignItems: 'center', justifyContent: 'center', width: '22px', height: '22px', borderRadius: '50%', backgroundColor: 'var(--color-terracotta)', color: '#FFFFFF', fontSize: '0.75rem', fontWeight: 700 }}>3</span>
                  <strong style={{ fontSize: '0.92rem', color: 'var(--color-slate-900)' }}>Plan & Compare with Transparent Costs</strong>
                </div>
                <p style={{ margin: 0, fontSize: '0.82rem', color: 'var(--color-slate-600)', lineHeight: 1.45 }}>
                  Simulate realistic trip budgets in Indian Rupees, compare places side-by-side, and save favorites to your shortlist.
                </p>
              </div>
            </div>
          </div>
        </section>
      )}

      {/* 2. Curated Destination Discovery Section */}
      <section style={{ padding: 'var(--space-3xl) 0 var(--space-4xl)' }}>
        <div className="app-container">
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-end', marginBottom: 'var(--space-xl)', flexWrap: 'wrap', gap: '16px' }}>
            <div>
              <span style={{ textTransform: 'uppercase', fontSize: '0.8rem', letterSpacing: '0.12em', color: 'var(--color-terracotta)', fontWeight: 700 }}>
                Curated Collections
              </span>
              <h2 style={{ marginTop: '6px', marginBottom: '6px', fontSize: 'clamp(1.8rem, 3vw, 2.3rem)' }}>
                Handpicked places for your next journey
              </h2>
              <p style={{ color: 'var(--color-slate-600)', margin: 0, fontSize: '1.02rem' }}>
                Every destination backed by authentic visitor reviews, verified strengths, and realistic INR daily budgets.
              </p>
            </div>
            <Link to="/explore" style={{ display: 'inline-flex', alignItems: 'center', gap: '6px', fontWeight: 600, color: 'var(--color-slate-900)', fontSize: '0.95rem' }}>
              <span>View all {destinations.length} destinations</span>
              <ArrowRight size={16} />
            </Link>
          </div>

          {/* Collection Filter Tabs */}
          <div style={{ display: 'flex', gap: '8px', overflowX: 'auto', paddingBottom: '8px', marginBottom: 'var(--space-xl)' }}>
            {CURATED_COLLECTIONS.map((col) => {
              const active = activeCollection === col.id;
              return (
                <button
                  key={col.id}
                  onClick={() => setActiveCollection(col.id)}
                  style={{
                    backgroundColor: active ? 'var(--color-slate-900)' : 'var(--color-sand-100)',
                    color: active ? '#FFFFFF' : 'var(--color-slate-800)',
                    border: '1px solid var(--color-sand-200)',
                    borderRadius: 'var(--radius-full)',
                    padding: '8px 18px',
                    fontSize: '0.9rem',
                    fontWeight: active ? 600 : 500,
                    cursor: 'pointer',
                    whiteSpace: 'nowrap',
                    transition: 'all 0.15s ease'
                  }}
                >
                  {col.label}
                </button>
              );
            })}
          </div>

          {/* Destination Grid */}
          {loading ? (
            <div className="state-box">
              <div className="spinner"></div>
              <p style={{ marginTop: '12px' }}>Loading destinations...</p>
            </div>
          ) : error ? (
            <div className="state-box">
              <p style={{ color: 'var(--color-crimson)', marginBottom: '12px' }}>{error}</p>
              <button onClick={() => window.location.reload()} className="btn btn-secondary">Retry</button>
            </div>
          ) : (
            <div className="destination-grid">
              {filteredFeatured.map((dest) => {
                const inrDaily = formatDailyBudgetInr(dest.indicative_daily_budget, dest.budget_tier);

                return (
                  <article key={dest.id} className="destination-card">
                    {/* Destination Photograph */}
                    <div style={{ position: 'relative', height: '230px', overflow: 'hidden' }}>
                      <DestinationImage
                        src={dest.image_url} 
                        alt={dest.name}
                        category={dest.category}
                        style={{ width: '100%', height: '100%' }}
                      />
                      <span 
                        className="badge badge-category" 
                        style={{ position: 'absolute', top: '12px', right: '12px', backdropFilter: 'blur(4px)', backgroundColor: 'rgba(255,255,255,0.95)', fontWeight: 600 }}
                      >
                        {dest.category}
                      </span>
                    </div>

                    {/* Card Content */}
                    <div style={{ padding: 'var(--space-lg)', display: 'flex', flexDirection: 'column', flex: 1 }}>
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', marginBottom: '6px' }}>
                        <span style={{ fontSize: '0.8rem', color: 'var(--color-terracotta)', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                          {dest.state_or_region ? `${dest.state_or_region}, ${dest.country}` : dest.country}
                        </span>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '4px', color: 'var(--color-terracotta)' }}>
                          <Star size={15} fill="currentColor" />
                          <span style={{ fontWeight: 700, fontSize: '0.95rem', color: 'var(--color-slate-900)' }}>
                            {dest.average_rating > 0 ? Number(dest.average_rating).toFixed(1) : '4.5'}
                          </span>
                          <span style={{ fontSize: '0.8rem', color: 'var(--color-slate-500)' }}>
                            ({dest.total_reviews})
                          </span>
                        </div>
                      </div>

                      <h3 style={{ fontSize: '1.35rem', marginBottom: '8px' }}>
                        <Link to={`/destinations/${dest.id}`} style={{ color: 'inherit', textDecoration: 'none' }}>
                          {dest.name}
                        </Link>
                      </h3>

                      <p style={{ fontSize: '0.92rem', color: 'var(--color-slate-600)', marginBottom: 'var(--space-md)', flex: 1, display: '-webkit-box', WebkitLineClamp: 3, WebkitBoxOrient: 'vertical', overflow: 'hidden', lineHeight: 1.55 }}>
                        {dest.description}
                      </p>

                      {/* Daily Budget in INR */}
                      <div style={{ borderTop: '1px solid var(--color-sand-200)', paddingTop: '10px', marginBottom: 'var(--space-md)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontSize: '0.88rem' }}>
                        <span style={{ color: 'var(--color-slate-500)' }}>Indicative budget:</span>
                        <strong style={{ color: 'var(--color-slate-900)' }}>{inrDaily}</strong>
                      </div>

                      <Link 
                        to={`/destinations/${dest.id}`} 
                        className="btn btn-secondary" 
                        style={{ width: '100%', justifyContent: 'space-between', padding: '10px 16px', fontSize: '0.9rem' }}
                      >
                        <span>View Destination Guide</span>
                        <ArrowRight size={16} />
                      </Link>
                    </div>
                  </article>
                );
              })}
            </div>
          )}
        </div>
      </section>

      {/* 3. The Traveller's Advantage: Why Real Reviews Matter */}
      <section 
        style={{ 
          backgroundColor: 'var(--color-sand-100)', 
          borderTop: '1px solid var(--color-sand-200)',
          borderBottom: '1px solid var(--color-sand-200)',
          padding: 'var(--space-4xl) 0'
        }}
      >
        <div className="app-container">
          <div style={{ maxWidth: '720px', margin: '0 auto var(--space-3xl)', textAlign: 'center' }}>
            <span style={{ textTransform: 'uppercase', fontSize: '0.8rem', letterSpacing: '0.12em', color: 'var(--color-terracotta)', fontWeight: 700 }}>
              The TRAVELENS Advantage
            </span>
            <h2 style={{ marginTop: '6px', marginBottom: '12px', fontSize: 'clamp(1.8rem, 3vw, 2.4rem)' }}>
              Know before you go
            </h2>
            <p style={{ fontSize: '1.08rem', color: 'var(--color-slate-700)', lineHeight: 1.65 }}>
              Planning travel should not feel like gambling on an average star rating. We look at the details that define real trips.
            </p>
          </div>

          <div 
            style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(auto-fit, minmax(290px, 1fr))',
              gap: 'var(--space-xl)'
            }}
          >
            {/* Advantage 1 */}
            <div 
              style={{
                backgroundColor: 'var(--color-white)',
                padding: 'var(--space-2xl)',
                borderRadius: 'var(--radius-lg)',
                border: '1px solid var(--color-sand-200)',
                boxShadow: 'var(--shadow-subtle)'
              }}
            >
              <div 
                style={{
                  width: '46px',
                  height: '46px',
                  borderRadius: '10px',
                  backgroundColor: 'var(--color-olive-light)',
                  color: 'var(--color-olive)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  marginBottom: 'var(--space-md)'
                }}
              >
                <Compass size={24} />
              </div>
              <h3 style={{ fontSize: '1.25rem', marginBottom: '8px' }}>9 Travel Dimensions</h3>
              <p style={{ fontSize: '0.95rem', color: 'var(--color-slate-600)', lineHeight: 1.6 }}>
                Every review is checked for feedback on food, cleanliness, attractions, pricing, crowds, safety, transit, stays, and local hospitality.
              </p>
            </div>

            {/* Advantage 2 */}
            <div 
              style={{
                backgroundColor: 'var(--color-white)',
                padding: 'var(--space-2xl)',
                borderRadius: 'var(--radius-lg)',
                border: '1px solid var(--color-sand-200)',
                boxShadow: 'var(--shadow-subtle)'
              }}
            >
              <div 
                style={{
                  width: '46px',
                  height: '46px',
                  borderRadius: '10px',
                  backgroundColor: 'var(--color-amber-light)',
                  color: 'var(--color-amber)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  marginBottom: 'var(--space-md)'
                }}
              >
                <Sparkles size={24} />
              </div>
              <h3 style={{ fontSize: '1.25rem', marginBottom: '8px' }}>Both Sides of the Story</h3>
              <p style={{ fontSize: '0.95rem', color: 'var(--color-slate-600)', lineHeight: 1.6 }}>
                We clearly separate what visitors loved from recurring headaches—so you can enjoy the highlights and prepare for the trade-offs.
              </p>
            </div>

            {/* Advantage 3 */}
            <div 
              style={{
                backgroundColor: 'var(--color-white)',
                padding: 'var(--space-2xl)',
                borderRadius: 'var(--radius-lg)',
                border: '1px solid var(--color-sand-200)',
                boxShadow: 'var(--shadow-subtle)'
              }}
            >
              <div 
                style={{
                  width: '46px',
                  height: '46px',
                  borderRadius: '10px',
                  backgroundColor: 'var(--color-terracotta-light)',
                  color: 'var(--color-terracotta)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  marginBottom: 'var(--space-md)'
                }}
              >
                <IndianRupee size={24} />
              </div>
              <h3 style={{ fontSize: '1.25rem', marginBottom: '8px' }}>Transparent INR Budgets</h3>
              <p style={{ fontSize: '0.95rem', color: 'var(--color-slate-600)', lineHeight: 1.6 }}>
                Realistic estimates per person per day in Indian Rupees, with practical calculators to budget your complete trip with confidence.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* 4. Bottom Trip Planning Call-to-Action */}
      <section style={{ padding: 'var(--space-4xl) 0', textAlign: 'center' }}>
        <div className="app-container" style={{ maxWidth: '680px' }}>
          <h2 style={{ fontSize: '2.2rem', marginBottom: '12px' }}>Ready to plan your next getaway?</h2>
          <p style={{ fontSize: '1.08rem', color: 'var(--color-slate-600)', lineHeight: 1.6, marginBottom: 'var(--space-xl)' }}>
            Tell us your travel style, budget, and trip duration. We’ll match you with the best destinations and provide a suggested day-by-day plan.
          </p>
          <div style={{ display: 'flex', justifyContent: 'center', gap: '14px', flexWrap: 'wrap' }}>
            <Link to="/plan" className="btn btn-primary" style={{ padding: '14px 32px', fontSize: '1.02rem' }}>
              <span>Plan a Trip</span>
              <ArrowRight size={18} />
            </Link>
            <Link to="/explore" className="btn btn-secondary" style={{ padding: '14px 28px', fontSize: '1.02rem' }}>
              <span>Browse All Destinations</span>
            </Link>
          </div>
        </div>
      </section>
    </main>
  );
}
