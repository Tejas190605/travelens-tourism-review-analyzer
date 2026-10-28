import React, { useState, useEffect } from 'react';
import { useSearchParams, Link } from 'react-router-dom';
import { Search, Star, ArrowRight, IndianRupee, Compass, X } from 'lucide-react';
import { getDestinations } from '../services/api';
import DestinationImage from '../components/DestinationImage';
import { formatDailyBudgetInr, normaliseBudgetTier } from '../utils/currencyFormatter';

const CATEGORIES = ['All', 'Heritage', 'Nature', 'Coastal', 'Cultural', 'Island', 'Urban', 'Adventure'];
const REGIONS = ['All', 'India', 'Europe', 'Asia', 'Americas', 'Middle East', 'Africa', 'Oceania'];
const BUDGET_TIERS = ['All', 'Budget', 'Moderate', 'Premium'];

export default function Explore() {
  const [searchParams, setSearchParams] = useSearchParams();
  const initialQuery = searchParams.get('query') || '';
  const initialCategory = searchParams.get('category') || 'All';
  const initialRegion = searchParams.get('region') || 'All';

  const [query, setQuery] = useState(initialQuery);
  const [selectedCategory, setSelectedCategory] = useState(initialCategory);
  const [selectedRegion, setSelectedRegion] = useState(initialRegion);
  const [selectedBudget, setSelectedBudget] = useState('All');
  const [sortBy, setSortBy] = useState('rating');
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 12;

  const [destinations, setDestinations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Map 'Premium' UI label to 'Luxury' database tier expected by backend
    const apiBudgetTier = selectedBudget === 'Premium' ? 'Luxury' : selectedBudget;

    getDestinations({ 
      query, 
      category: selectedCategory,
      region: selectedRegion,
      budget_tier: apiBudgetTier,
      sort_by: sortBy
    })
      .then((data) => {
        // Guarantee deduplication by unique destination id
        const unique = Array.from(new Map(data.map((item) => [item.id, item])).values());
        setDestinations(unique);
        setCurrentPage(1);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message || 'Unable to load destinations.');
        setLoading(false);
      });
  }, [query, selectedCategory, selectedRegion, selectedBudget, sortBy]);

  const handleCategoryClick = (cat) => {
    setSelectedCategory(cat);
    const newParams = new URLSearchParams(searchParams);
    if (cat === 'All') newParams.delete('category');
    else newParams.set('category', cat);
    setSearchParams(newParams);
  };

  const handleRegionClick = (reg) => {
    setSelectedRegion(reg);
    const newParams = new URLSearchParams(searchParams);
    if (reg === 'All') newParams.delete('region');
    else newParams.set('region', reg);
    setSearchParams(newParams);
  };

  // Pagination calculation
  const totalPages = Math.ceil(destinations.length / itemsPerPage) || 1;
  const paginatedDestinations = destinations.slice(
    (currentPage - 1) * itemsPerPage,
    currentPage * itemsPerPage
  );

  return (
    <main style={{ padding: 'var(--space-2xl) 0 var(--space-4xl)' }}>
      <div className="app-container">
        {/* Header */}
        <header style={{ marginBottom: 'var(--space-2xl)' }}>
          <span style={{ textTransform: 'uppercase', fontSize: '0.8rem', letterSpacing: '0.12em', color: 'var(--color-terracotta)', fontWeight: 700 }}>
            Curated Directory
          </span>
          <h1 style={{ marginTop: '6px', marginBottom: '10px' }}>Explore Destinations</h1>
          <p style={{ maxWidth: '720px', fontSize: '1.05rem', color: 'var(--color-slate-600)', lineHeight: 1.6 }}>
            Browse through 50+ curated destinations across India and international gateways. Every location features aspect-level review analysis, authentic visitor feedback, and verified travel guidance.
          </p>
        </header>

        {/* Search & Filter Toolbar */}
        <div 
          style={{
            display: 'flex',
            flexDirection: 'column',
            gap: 'var(--space-md)',
            backgroundColor: 'var(--color-white)',
            padding: 'var(--space-xl)',
            borderRadius: 'var(--radius-lg)',
            border: '1px solid var(--color-sand-200)',
            boxShadow: 'var(--shadow-subtle)',
            marginBottom: 'var(--space-2xl)'
          }}
        >
          {/* Top row: search & dropdowns */}
          <div style={{ display: 'flex', gap: 'var(--space-md)', flexWrap: 'wrap', alignItems: 'center' }}>
            <div style={{ position: 'relative', flex: 1, minWidth: '280px' }}>
              <Search size={18} color="var(--color-slate-400)" style={{ position: 'absolute', left: '16px', top: '50%', transform: 'translateY(-50%)', pointerEvents: 'none' }} />
              <input 
                type="text" 
                placeholder="Search by city, country, region, or sights..."
                value={query}
                onChange={(e) => {
                  setQuery(e.target.value);
                  const p = new URLSearchParams(searchParams);
                  if (e.target.value) p.set('query', e.target.value);
                  else p.delete('query');
                  setSearchParams(p);
                }}
                style={{
                  width: '100%',
                  padding: query ? '12px 42px 12px 46px' : '12px 16px 12px 46px',
                  borderRadius: 'var(--radius-md)',
                  border: '1px solid var(--color-sand-200)',
                  fontSize: '0.95rem',
                  fontFamily: 'var(--font-sans)',
                  color: 'var(--color-slate-900)',
                  backgroundColor: 'var(--color-sand-50)',
                  outline: 'none'
                }}
              />
              {query && (
                <button
                  type="button"
                  aria-label="Clear search"
                  onClick={() => {
                    setQuery('');
                    const p = new URLSearchParams(searchParams);
                    p.delete('query');
                    setSearchParams(p);
                  }}
                  style={{
                    position: 'absolute',
                    right: '12px',
                    top: '50%',
                    transform: 'translateY(-50%)',
                    background: 'none',
                    border: 'none',
                    padding: '4px',
                    cursor: 'pointer',
                    color: 'var(--color-slate-400)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    borderRadius: '50%'
                  }}
                >
                  <X size={16} />
                </button>
              )}
            </div>

            {/* Budget Selector */}
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <label htmlFor="budget-filter" style={{ fontSize: '0.85rem', color: 'var(--color-slate-600)', fontWeight: 600 }}>
                Budget Tier:
              </label>
              <select 
                id="budget-filter"
                value={selectedBudget} 
                onChange={(e) => setSelectedBudget(e.target.value)}
                style={{
                  padding: '11px 14px',
                  borderRadius: 'var(--radius-md)',
                  border: '1px solid var(--color-sand-200)',
                  backgroundColor: 'var(--color-sand-50)',
                  color: 'var(--color-slate-900)',
                  fontSize: '0.9rem',
                  fontWeight: 500,
                  cursor: 'pointer'
                }}
              >
                {BUDGET_TIERS.map(b => (
                  <option key={b} value={b}>{b === 'All' ? 'All Budget Tiers' : b}</option>
                ))}
              </select>
            </div>

            {/* Sort Selector */}
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <label htmlFor="sort-filter" style={{ fontSize: '0.85rem', color: 'var(--color-slate-600)', fontWeight: 600 }}>
                Sort By:
              </label>
              <select 
                id="sort-filter"
                value={sortBy} 
                onChange={(e) => setSortBy(e.target.value)}
                style={{
                  padding: '11px 14px',
                  borderRadius: 'var(--radius-md)',
                  border: '1px solid var(--color-sand-200)',
                  backgroundColor: 'var(--color-sand-50)',
                  color: 'var(--color-slate-900)',
                  fontSize: '0.9rem',
                  fontWeight: 500,
                  cursor: 'pointer'
                }}
              >
                <option value="rating">Highest Star Rating</option>
                <option value="reviews">Most Reviewed</option>
                <option value="name">Alphabetical (A–Z)</option>
              </select>
            </div>
          </div>

          {/* Region Tabs */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap', paddingTop: '6px' }}>
            <span style={{ fontSize: '0.85rem', color: 'var(--color-slate-600)', fontWeight: 700, minWidth: '70px' }}>Region:</span>
            {REGIONS.map((reg) => {
              const active = selectedRegion === reg;
              return (
                <button
                  key={reg}
                  type="button"
                  onClick={() => handleRegionClick(reg)}
                  style={{
                    backgroundColor: active ? 'var(--color-slate-900)' : 'var(--color-sand-100)',
                    color: active ? '#FFFFFF' : 'var(--color-slate-800)',
                    border: '1px solid var(--color-sand-200)',
                    borderRadius: 'var(--radius-full)',
                    padding: '6px 14px',
                    fontSize: '0.85rem',
                    fontWeight: active ? 600 : 500,
                    cursor: 'pointer',
                    transition: 'all 0.15s ease'
                  }}
                >
                  {reg === 'All' ? 'All Regions' : reg}
                </button>
              );
            })}
          </div>

          {/* Category Tabs */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap' }}>
            <span style={{ fontSize: '0.85rem', color: 'var(--color-slate-600)', fontWeight: 700, minWidth: '70px' }}>Category:</span>
            {CATEGORIES.map((cat) => {
              const active = selectedCategory === cat;
              return (
                <button
                  key={cat}
                  type="button"
                  onClick={() => handleCategoryClick(cat)}
                  style={{
                    backgroundColor: active ? 'var(--color-terracotta)' : 'var(--color-white)',
                    color: active ? '#FFFFFF' : 'var(--color-slate-800)',
                    border: '1px solid var(--color-sand-200)',
                    borderRadius: 'var(--radius-full)',
                    padding: '6px 14px',
                    fontSize: '0.85rem',
                    fontWeight: active ? 600 : 500,
                    cursor: 'pointer',
                    transition: 'all 0.15s ease'
                  }}
                >
                  {cat}
                </button>
              );
            })}
          </div>
        </div>

        {/* Results Counter */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 'var(--space-lg)' }}>
          <span style={{ fontSize: '0.95rem', color: 'var(--color-slate-600)' }}>
            Showing <strong>{destinations.length}</strong> catalogued destinations
          </span>
          {totalPages > 1 && (
            <span style={{ fontSize: '0.85rem', color: 'var(--color-slate-500)' }}>
              Page {currentPage} of {totalPages}
            </span>
          )}
        </div>

        {/* Loading State */}
        {loading ? (
          <div className="state-box" style={{ padding: 'var(--space-4xl) var(--space-xl)' }}>
            <div className="spinner"></div>
            <p style={{ marginTop: '16px', color: 'var(--color-slate-600)' }}>Loading verified destinations...</p>
          </div>
        ) : error ? (
          <div className="state-box" style={{ padding: 'var(--space-4xl) var(--space-xl)' }}>
            <p style={{ color: 'var(--color-crimson)', fontWeight: 600 }}>{error}</p>
          </div>
        ) : destinations.length === 0 ? (
          <div className="state-box" style={{ padding: 'var(--space-4xl) var(--space-xl)' }}>
            <Compass size={40} className="state-box-icon" style={{ color: 'var(--color-terracotta)', marginBottom: '12px' }} />
            <h3 style={{ marginBottom: '6px' }}>No destinations match your filters</h3>
            <p style={{ maxWidth: '440px', margin: '0 auto 20px', color: 'var(--color-slate-600)', fontSize: '0.95rem' }}>
              Try clearing search terms or selecting 'All' for region, category, and budget tiers.
            </p>
            <button 
              onClick={() => { setQuery(''); setSelectedCategory('All'); setSelectedRegion('All'); setSelectedBudget('All'); }}
              className="btn btn-primary"
            >
              Reset All Filters
            </button>
          </div>
        ) : (
          <>
            {/* Destination Grid */}
            <div className="destination-grid" style={{ marginBottom: 'var(--space-2xl)' }}>
              {paginatedDestinations.map((dest) => {
                let attractionsSnippet = [];
                try {
                  attractionsSnippet = dest.attractions ? JSON.parse(dest.attractions).slice(0, 2) : [];
                } catch {
                  attractionsSnippet = dest.attractions ? dest.attractions.split(',').slice(0, 2) : [];
                }

                const dailyInrStr = formatDailyBudgetInr(dest.indicative_daily_budget, dest.budget_tier);
                const displayBudgetTier = normaliseBudgetTier(dest.budget_tier);

                return (
                  <article key={dest.id} className="destination-card">
                    <div style={{ position: 'relative', height: '220px', overflow: 'hidden' }}>
                      <DestinationImage 
                        src={dest.image_url} 
                        alt={dest.name}
                        category={dest.category}
                        style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                      />
                      <div style={{ position: 'absolute', top: '12px', right: '12px', display: 'flex', gap: '6px' }}>
                        <span className="badge badge-category" style={{ backgroundColor: '#FFFFFF', color: 'var(--color-slate-900)', fontWeight: 600 }}>
                          {dest.category}
                        </span>
                        {dest.region && (
                          <span className="badge" style={{ backgroundColor: 'var(--color-slate-900)', color: '#FFFFFF', fontSize: '0.75rem', fontWeight: 600 }}>
                            {dest.region}
                          </span>
                        )}
                      </div>
                    </div>

                    <div className="destination-card-body" style={{ display: 'flex', flexDirection: 'column', flex: 1, padding: 'var(--space-lg)' }}>
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', marginBottom: '6px' }}>
                        <span style={{ fontSize: '0.8rem', color: 'var(--color-terracotta)', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                          {dest.state_or_region ? `${dest.state_or_region}, ${dest.country}` : dest.country}
                        </span>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '4px', color: 'var(--color-terracotta)' }}>
                          <Star size={15} fill="currentColor" />
                          <span style={{ fontWeight: 700, fontSize: '0.92rem', color: 'var(--color-slate-900)' }}>
                            {dest.average_rating > 0 ? Number(dest.average_rating).toFixed(1) : 'N/A'}
                          </span>
                          <span style={{ fontSize: '0.8rem', color: 'var(--color-slate-500)' }}>
                            ({dest.total_reviews} {dest.total_reviews === 1 ? 'review' : 'reviews'})
                          </span>
                        </div>
                      </div>

                      <h3 style={{ fontSize: '1.25rem', marginBottom: '8px', lineHeight: 1.3 }}>
                        <Link to={`/destinations/${dest.id}`} style={{ color: 'inherit', textDecoration: 'none' }}>
                          {dest.name}
                        </Link>
                      </h3>

                      <p style={{ fontSize: '0.92rem', color: 'var(--color-slate-600)', lineHeight: 1.55, marginBottom: 'var(--space-md)', flex: 1 }}>
                        {dest.description && dest.description.length > 115 
                          ? `${dest.description.slice(0, 115)}...` 
                          : dest.description}
                      </p>

                      {/* Travel Quick Info in INR */}
                      <div 
                        style={{ 
                          display: 'flex', 
                          flexDirection: 'column', 
                          gap: '6px', 
                          fontSize: '0.85rem', 
                          color: 'var(--color-slate-600)', 
                          marginBottom: 'var(--space-md)', 
                          borderTop: '1px solid var(--color-sand-200)', 
                          paddingTop: '10px' 
                        }}
                      >
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                          <span style={{ display: 'inline-flex', alignItems: 'center', gap: '4px' }}>
                            <IndianRupee size={13} color="var(--color-olive)" />
                            <strong>{dailyInrStr}</strong>
                          </span>
                          <span className="badge" style={{ backgroundColor: 'var(--color-sand-100)', color: 'var(--color-slate-800)', fontSize: '0.75rem', fontWeight: 600 }}>
                            {displayBudgetTier}
                          </span>
                        </div>
                        {dest.recommended_duration && (
                          <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.82rem', color: 'var(--color-slate-500)' }}>
                            <span>Recommended:</span>
                            <span style={{ fontWeight: 500, color: 'var(--color-slate-800)' }}>{dest.recommended_duration}</span>
                          </div>
                        )}
                        {attractionsSnippet.length > 0 && (
                          <div style={{ whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis', fontSize: '0.8rem', color: 'var(--color-slate-500)' }}>
                            Key Sights: {attractionsSnippet.join(', ')}
                          </div>
                        )}
                      </div>

                      <Link 
                        to={`/destinations/${dest.id}`} 
                        className="btn btn-secondary"
                        style={{ width: '100%', justifyContent: 'center', gap: '6px', fontSize: '0.88rem', padding: '9px 14px' }}
                      >
                        <span>View Destination Guide</span>
                        <ArrowRight size={14} />
                      </Link>
                    </div>
                  </article>
                );
              })}
            </div>

            {/* Pagination Controls */}
            {totalPages > 1 && (
              <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', gap: '8px', marginTop: 'var(--space-xl)' }}>
                <button
                  onClick={() => setCurrentPage(prev => Math.max(prev - 1, 1))}
                  disabled={currentPage === 1}
                  className="btn btn-secondary"
                  style={{ padding: '8px 16px', fontSize: '0.88rem' }}
                >
                  Previous
                </button>

                {[...Array(totalPages)].map((_, i) => {
                  const pageNum = i + 1;
                  const isActive = currentPage === pageNum;
                  return (
                    <button
                      key={pageNum}
                      onClick={() => setCurrentPage(pageNum)}
                      className="badge"
                      style={{
                        backgroundColor: isActive ? 'var(--color-terracotta)' : 'var(--color-white)',
                        color: isActive ? '#FFFFFF' : 'var(--color-slate-800)',
                        border: '1px solid var(--color-sand-200)',
                        padding: '7px 13px',
                        fontSize: '0.9rem',
                        fontWeight: isActive ? 700 : 500,
                        cursor: 'pointer'
                      }}
                    >
                      {pageNum}
                    </button>
                  );
                })}

                <button
                  onClick={() => setCurrentPage(prev => Math.min(prev + 1, totalPages))}
                  disabled={currentPage === totalPages}
                  className="btn btn-secondary"
                  style={{ padding: '8px 16px', fontSize: '0.88rem' }}
                >
                  Next
                </button>
              </div>
            )}
          </>
        )}
      </div>
    </main>
  );
}
