import React, { useState, useEffect } from 'react';
import { useSearchParams, Link } from 'react-router-dom';
import { 
  Star, 
  Trash2, 
  ArrowRight,
  Share2, 
  Bookmark, 
  Check, 
  MapPin, 
  AlertTriangle, 
  ThumbsUp,
  Scale
} from 'lucide-react';
import { getDestinations, getDestinationById, getDestinationAnalytics, saveDestination, tokenStorage } from '../services/api';
import DestinationImage from '../components/DestinationImage';
import { formatDailyBudgetInr, normaliseBudgetTier } from '../utils/currencyFormatter';

const ALL_ASPECTS = [
  'Attractions',
  'Food',
  'Cleanliness',
  'Price',
  'Crowd',
  'Safety',
  'Transport',
  'Accommodation',
  'Hospitality'
];

export default function Compare() {
  const [searchParams, setSearchParams] = useSearchParams();
  const [allDestinations, setAllDestinations] = useState([]);
  const [selectedIds, setSelectedIds] = useState([]);
  const [destinationsData, setDestinationsData] = useState([]);
  const [analyticsData, setAnalyticsData] = useState({});
  const [loading, setLoading] = useState(true);
  const [copiedLink, setCopiedLink] = useState(false);

  const initialParamsRef = React.useRef({
    dests: searchParams.get('dests'),
    destA: searchParams.get('destA'),
    destB: searchParams.get('destB')
  });

  // Load destination catalog
  useEffect(() => {
    getDestinations()
      .then((dests) => {
        setAllDestinations(dests);
        const paramIds = initialParamsRef.current.dests;
        const paramA = initialParamsRef.current.destA;
        const paramB = initialParamsRef.current.destB;
        
        let initialIds = [];
        if (paramIds) {
          initialIds = paramIds.split(',').map(Number).filter(n => !isNaN(n));
        } else if (paramA && paramB) {
          initialIds = [Number(paramA), Number(paramB)];
        } else if (paramA) {
          initialIds = [Number(paramA), dests[1]?.id].filter(Boolean);
        } else if (dests.length >= 2) {
          initialIds = [dests[0].id, dests[1].id];
        }

        setSelectedIds(initialIds.slice(0, 4));
        setLoading(false);
      })
      .catch((err) => {
        console.error(err);
        setLoading(false);
      });
  }, []);

  // Fetch full details and analytics for all selected destinations
  useEffect(() => {
    if (selectedIds.length === 0) return;

    setSearchParams({ dests: selectedIds.join(',') }, { replace: true });

    Promise.all(
      selectedIds.map((id) =>
        Promise.all([getDestinationById(id), getDestinationAnalytics(id)]).then(([dest, an]) => ({
          dest,
          an,
        }))
      )
    )
      .then((results) => {
        setDestinationsData(results.map((r) => r.dest));
        const anMap = {};
        results.forEach((r) => {
          anMap[r.dest.id] = r.an;
        });
        setAnalyticsData(anMap);
      })
      .catch((err) => {
        console.error('Error fetching comparison data:', err);
      });
  }, [selectedIds, setSearchParams]);

  const handleAddDestination = (idToAdd) => {
    const numId = Number(idToAdd);
    if (!numId || selectedIds.includes(numId)) return;
    if (selectedIds.length >= 4) {
      alert('You can compare up to 4 destinations at a time.');
      return;
    }
    setSelectedIds([...selectedIds, numId]);
  };

  const handleRemoveDestination = (idToRemove) => {
    if (selectedIds.length <= 2) {
      alert('Comparison requires at least 2 destinations.');
      return;
    }
    setSelectedIds(selectedIds.filter((id) => id !== idToRemove));
  };

  const handleShare = () => {
    navigator.clipboard.writeText(window.location.href);
    setCopiedLink(true);
    setTimeout(() => setCopiedLink(false), 2500);
  };

  const handleSave = async (id) => {
    const token = tokenStorage.get();
    if (!token) {
      alert('Please sign in to save destinations to your shortlist.');
      return;
    }
    try {
      await saveDestination(id);
      alert('Destination saved to your shortlist!');
    } catch (err) {
      alert(err.message || 'Could not save destination.');
    }
  };

  if (loading) {
    return (
      <main className="app-container" style={{ padding: 'var(--space-4xl) 0' }}>
        <div className="state-box">
          <div className="spinner"></div>
          <p style={{ marginTop: '16px' }}>Loading destination comparison...</p>
        </div>
      </main>
    );
  }

  return (
    <main style={{ padding: 'var(--space-2xl) 0 var(--space-4xl)' }}>
      <div className="app-container">
        {/* Header */}
        <header style={{ marginBottom: 'var(--space-2xl)', textAlign: 'center' }}>
          <span style={{ textTransform: 'uppercase', fontSize: '0.8rem', letterSpacing: '0.12em', color: 'var(--color-terracotta)', fontWeight: 700 }}>
            Side-by-Side Evaluation
          </span>
          <h1 style={{ marginTop: '6px', marginBottom: '10px', fontSize: 'clamp(2.2rem, 3.8vw, 3rem)' }}>
            Compare Destinations
          </h1>
          <p style={{ maxWidth: '680px', margin: '0 auto', fontSize: '1.08rem', color: 'var(--color-slate-600)', lineHeight: 1.6 }}>
            Evaluate places side by side across visitor ratings, daily budgets in INR, ideal stay durations, best seasons, and review feedback to decide what suits you best.
          </p>
        </header>

        {/* Comparison Control Toolbar */}
        <div 
          style={{
            display: 'flex',
            flexWrap: 'wrap',
            justifyContent: 'space-between',
            alignItems: 'center',
            backgroundColor: 'var(--color-white)',
            padding: 'var(--space-lg) var(--space-xl)',
            borderRadius: 'var(--radius-lg)',
            border: '1px solid var(--color-sand-200)',
            boxShadow: 'var(--shadow-subtle)',
            marginBottom: 'var(--space-2xl)',
            gap: 'var(--space-md)'
          }}
        >
          {/* Add Dropdown */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', flexWrap: 'wrap' }}>
            <label htmlFor="add-dest-select" style={{ fontSize: '0.9rem', fontWeight: 600, color: 'var(--color-slate-800)' }}>
              Add a Place to Compare:
            </label>
            <select
              id="add-dest-select"
              onChange={(e) => {
                if (e.target.value) {
                  handleAddDestination(e.target.value);
                  e.target.value = '';
                }
              }}
              style={{ padding: '8px 14px', borderRadius: 'var(--radius-md)', border: '1px solid var(--color-sand-200)', fontSize: '0.9rem' }}
            >
              <option value="">Select a destination...</option>
              {allDestinations
                .filter((d) => !selectedIds.includes(d.id))
                .map((d) => (
                  <option key={d.id} value={d.id}>
                    {d.name} ({d.country})
                  </option>
                ))}
            </select>
            <span style={{ fontSize: '0.82rem', color: 'var(--color-slate-500)' }}>
              (Comparing {selectedIds.length} of max 4)
            </span>
          </div>

          {/* Share Link */}
          <button
            onClick={handleShare}
            className="btn btn-secondary"
            style={{ fontSize: '0.88rem', padding: '8px 14px', display: 'inline-flex', alignItems: 'center', gap: '6px' }}
          >
            {copiedLink ? <Check size={16} color="var(--color-olive)" /> : <Share2 size={16} />}
            <span>{copiedLink ? 'Link Copied!' : 'Share Comparison'}</span>
          </button>
        </div>

        {/* Factual Comparison Takeaways Banner when 2 destinations compared */}
        {destinationsData.length === 2 && (() => {
          const [dA, dB] = destinationsData;
          const anA = analyticsData[dA.id]?.aspects || {};
          const anB = analyticsData[dB.id]?.aspects || {};
          const tierRates = { 'Budget': 3200, 'Moderate': 6200, 'Luxury': 14500, 'Premium': 14500 };
          const tierA = normaliseBudgetTier(dA.budget_tier);
          const tierB = normaliseBudgetTier(dB.budget_tier);
          const rateA = tierRates[tierA] || 6200;
          const rateB = tierRates[tierB] || 6200;

          const advantagesA = [];
          const advantagesB = [];

          ALL_ASPECTS.forEach((asp) => {
            const dataA = anA[asp];
            const dataB = anB[asp];
            const scoreA = dataA?.aspect_score;
            const scoreB = dataB?.aspect_score;
            if (scoreA !== null && scoreA !== undefined && dataA?.mention_count >= 2 &&
                scoreB !== null && scoreB !== undefined && dataB?.mention_count >= 2) {
              if (scoreA - scoreB >= 8) advantagesA.push(`${asp} (${scoreA} vs ${scoreB})`);
              else if (scoreB - scoreA >= 8) advantagesB.push(`${asp} (${scoreB} vs ${scoreA})`);
            }
          });

          return (
            <div 
              style={{
                backgroundColor: 'var(--color-white)',
                borderRadius: 'var(--radius-lg)',
                border: '1px solid var(--color-sand-200)',
                padding: 'var(--space-xl)',
                marginBottom: 'var(--space-2xl)',
                boxShadow: 'var(--shadow-subtle)'
              }}
            >
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px' }}>
                <Scale size={20} color="var(--color-terracotta)" />
                <h3 style={{ margin: 0, fontSize: '1.25rem' }}>Comparison Takeaways: {dA.name} vs {dB.name}</h3>
              </div>
              <p style={{ fontSize: '0.88rem', color: 'var(--color-slate-600)', marginBottom: 'var(--space-md)' }}>
                Factual differences based on verified review consensus and indicative daily budgets. Neither place is universally superior; choose based on your preferred travel balance.
              </p>

              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '12px' }}>
                {/* Budget Comparison */}
                <div style={{ padding: '12px 14px', backgroundColor: 'var(--color-sand-50)', borderRadius: 'var(--radius-md)', border: '1px solid var(--color-sand-200)', fontSize: '0.88rem' }}>
                  <strong style={{ display: 'block', color: 'var(--color-slate-900)', marginBottom: '4px' }}>Estimated Daily Cost:</strong>
                  {rateA < rateB ? (
                    <span style={{ color: 'var(--color-olive)', fontWeight: 600 }}>
                      ✓ {dA.name} is ~₹{(rateB - rateA).toLocaleString('en-IN')}/day lower (~₹{rateA.toLocaleString('en-IN')} vs ~₹{rateB.toLocaleString('en-IN')}).
                    </span>
                  ) : rateB < rateA ? (
                    <span style={{ color: 'var(--color-olive)', fontWeight: 600 }}>
                      ✓ {dB.name} is ~₹{(rateA - rateB).toLocaleString('en-IN')}/day lower (~₹{rateB.toLocaleString('en-IN')} vs ~₹{rateA.toLocaleString('en-IN')}).
                    </span>
                  ) : (
                    <span style={{ color: 'var(--color-slate-700)' }}>
                      Both places share the {tierA} price bracket (~₹{rateA.toLocaleString('en-IN')} / person / day).
                    </span>
                  )}
                </div>

                {/* Aspect Advantages */}
                <div style={{ padding: '12px 14px', backgroundColor: 'var(--color-sand-50)', borderRadius: 'var(--radius-md)', border: '1px solid var(--color-sand-200)', fontSize: '0.88rem' }}>
                  <strong style={{ display: 'block', color: 'var(--color-slate-900)', marginBottom: '4px' }}>Dimension Strengths:</strong>
                  {advantagesA.length > 0 || advantagesB.length > 0 ? (
                    <ul style={{ margin: 0, paddingLeft: '18px', color: 'var(--color-slate-800)', display: 'flex', flexDirection: 'column', gap: '3px' }}>
                      {advantagesA.length > 0 && (
                        <li><strong>{dA.name}:</strong> Higher satisfaction in {advantagesA.join(', ')}</li>
                      )}
                      {advantagesB.length > 0 && (
                        <li><strong>{dB.name}:</strong> Higher satisfaction in {advantagesB.join(', ')}</li>
                      )}
                    </ul>
                  ) : (
                    <span style={{ color: 'var(--color-slate-600)' }}>
                      Both destinations receive comparable satisfaction across reviewed travel dimensions.
                    </span>
                  )}
                </div>
              </div>
            </div>
          );
        })()}

        {/* Side-by-Side Comparison Matrix */}
        <div style={{ overflowX: 'auto', paddingBottom: 'var(--space-xl)' }}>
          <div 
            style={{ 
              display: 'grid', 
              gridTemplateColumns: `repeat(${destinationsData.length}, minmax(280px, 1fr))`, 
              gap: 'var(--space-xl)',
              minWidth: destinationsData.length * 280
            }}
          >
            {destinationsData.map((dest) => {
              const an = analyticsData[dest.id];
              const destAspects = an?.aspects || {};
              const inrDaily = formatDailyBudgetInr(dest.indicative_daily_budget, dest.budget_tier);
              const displayTier = normaliseBudgetTier(dest.budget_tier);

              // Top positive aspects
              const topStrengths = Object.entries(destAspects)
                .filter(([, d]) => d.aspect_score >= 65 && d.mention_count >= 2)
                .sort((a, b) => b[1].aspect_score - a[1].aspect_score)
                .slice(0, 2);

              // Top caveats
              const topCaveats = Object.entries(destAspects)
                .filter(([, d]) => d.aspect_score <= 50 && d.mention_count >= 2)
                .sort((a, b) => a[1].aspect_score - b[1].aspect_score)
                .slice(0, 2);

              return (
                <div 
                  key={dest.id}
                  style={{
                    backgroundColor: 'var(--color-white)',
                    borderRadius: 'var(--radius-lg)',
                    border: '1px solid var(--color-sand-200)',
                    boxShadow: 'var(--shadow-card)',
                    display: 'flex',
                    flexDirection: 'column',
                    overflow: 'hidden'
                  }}
                >
                  {/* Image & Remove header */}
                  <div style={{ position: 'relative', height: '200px' }}>
                    <DestinationImage
                      src={dest.image_url}
                      alt={dest.name}
                      category={dest.category}
                      style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                    />
                    <button
                      onClick={() => handleRemoveDestination(dest.id)}
                      title="Remove from comparison"
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

                  {/* Destination Info */}
                  <div style={{ padding: 'var(--space-xl)', flex: 1, display: 'flex', flexDirection: 'column' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '4px', color: 'var(--color-terracotta)', fontSize: '0.8rem', fontWeight: 700, textTransform: 'uppercase', marginBottom: '4px' }}>
                      <MapPin size={14} />
                      <span>{dest.state_or_region ? `${dest.state_or_region}, ${dest.country}` : dest.country}</span>
                    </div>

                    <h2 style={{ fontSize: '1.45rem', marginBottom: '8px' }}>
                      <Link to={`/destinations/${dest.id}`} style={{ color: 'inherit', textDecoration: 'none' }}>
                        {dest.name}
                      </Link>
                    </h2>

                    {/* Rating & Reviews */}
                    <div style={{ display: 'flex', alignItems: 'center', gap: '6px', marginBottom: 'var(--space-lg)' }}>
                      <Star size={16} fill="var(--color-terracotta)" color="var(--color-terracotta)" />
                      <strong style={{ fontSize: '1.05rem', color: 'var(--color-slate-900)' }}>
                        {dest.average_rating ? Number(dest.average_rating).toFixed(1) : '4.5'}
                      </strong>
                      <span style={{ fontSize: '0.85rem', color: 'var(--color-slate-500)' }}>
                        ({dest.total_reviews} reviews)
                      </span>
                    </div>

                    {/* Key Attributes Strip */}
                    <div style={{ borderTop: '1px solid var(--color-sand-200)', borderBottom: '1px solid var(--color-sand-200)', padding: '14px 0', display: 'flex', flexDirection: 'column', gap: '10px', fontSize: '0.88rem', marginBottom: 'var(--space-lg)' }}>
                      <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                        <span style={{ color: 'var(--color-slate-500)' }}>Indicative Budget:</span>
                        <strong style={{ color: 'var(--color-slate-900)' }}>{inrDaily}</strong>
                      </div>
                      <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                        <span style={{ color: 'var(--color-slate-500)' }}>Budget Tier:</span>
                        <span className="badge" style={{ backgroundColor: 'var(--color-sand-100)', color: 'var(--color-slate-800)', fontSize: '0.75rem', fontWeight: 600 }}>{displayTier}</span>
                      </div>
                      <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                        <span style={{ color: 'var(--color-slate-500)' }}>Recommended Stay:</span>
                        <strong style={{ color: 'var(--color-slate-800)' }}>{dest.recommended_duration || '3–4 days'}</strong>
                      </div>
                      <div style={{ display: 'flex', justifyContent: 'space-between' }}>
                        <span style={{ color: 'var(--color-slate-500)' }}>Best Season:</span>
                        <strong style={{ color: 'var(--color-slate-800)' }}>{dest.best_season?.split('(')[0] || 'Oct–Mar'}</strong>
                      </div>
                    </div>

                    {/* What Visitors Love */}
                    <div style={{ marginBottom: 'var(--space-md)' }}>
                      <span style={{ fontSize: '0.8rem', color: 'var(--color-olive)', fontWeight: 700, textTransform: 'uppercase', display: 'flex', alignItems: 'center', gap: '4px', marginBottom: '6px' }}>
                        <ThumbsUp size={14} />
                        <span>What Visitors Praise:</span>
                      </span>
                      {topStrengths.length > 0 ? (
                        <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px' }}>
                          {topStrengths.map(([asp, d]) => (
                            <span key={asp} className="badge badge-positive" style={{ fontSize: '0.78rem' }}>
                              {asp}: {d.aspect_score}/100
                            </span>
                          ))}
                        </div>
                      ) : (
                        <p style={{ fontSize: '0.82rem', color: 'var(--color-slate-500)', margin: 0, fontStyle: 'italic' }}>
                          Consistent, balanced feedback.
                        </p>
                      )}
                    </div>

                    {/* What to Watch Out For */}
                    <div style={{ marginBottom: 'var(--space-lg)' }}>
                      <span style={{ fontSize: '0.8rem', color: 'var(--color-crimson)', fontWeight: 700, textTransform: 'uppercase', display: 'flex', alignItems: 'center', gap: '4px', marginBottom: '6px' }}>
                        <AlertTriangle size={14} />
                        <span>Watch Out For:</span>
                      </span>
                      {topCaveats.length > 0 ? (
                        <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px' }}>
                          {topCaveats.map(([asp, d]) => (
                            <span key={asp} className="badge badge-negative" style={{ fontSize: '0.78rem' }}>
                              {asp}: {d.aspect_score}/100
                            </span>
                          ))}
                        </div>
                      ) : (
                        <p style={{ fontSize: '0.82rem', color: 'var(--color-slate-500)', margin: 0, fontStyle: 'italic' }}>
                          No significant caveats recorded.
                        </p>
                      )}
                    </div>

                    {/* 9 Dimensions Complete Scorecard */}
                    <div style={{ borderTop: '1px solid var(--color-sand-200)', paddingTop: '12px', marginBottom: 'var(--space-xl)' }}>
                      <span style={{ fontSize: '0.8rem', color: 'var(--color-slate-500)', fontWeight: 700, textTransform: 'uppercase', display: 'block', marginBottom: '8px' }}>
                        All 9 Dimension Scores:
                      </span>
                      <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                        {ALL_ASPECTS.map((asp) => {
                          const data = destAspects[asp];
                          const score = data?.aspect_score;
                          const hasData = score !== null && score !== undefined && data?.mention_count >= 2;
                          return (
                            <div key={asp} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontSize: '0.82rem' }}>
                              <span style={{ color: 'var(--color-slate-700)' }}>{asp}</span>
                              <span 
                                title={data?.mention_count ? `${data.mention_count} reviews discuss ${asp}` : 'Limited mentions'}
                                style={{ 
                                  fontWeight: 600, 
                                  color: hasData 
                                    ? (score >= 65 ? 'var(--color-olive)' : score <= 48 ? 'var(--color-crimson)' : 'var(--color-amber)') 
                                    : 'var(--color-slate-400)',
                                  fontSize: hasData ? '0.82rem' : '0.75rem'
                                }}
                              >
                                {hasData ? `${score}/100` : 'Limited feedback'}
                              </span>
                            </div>
                          );
                        })}
                      </div>
                    </div>

                    {/* CTAs */}
                    <div style={{ marginTop: 'auto', display: 'flex', flexDirection: 'column', gap: '8px' }}>
                      <Link 
                        to={`/destinations/${dest.id}`} 
                        className="btn btn-primary"
                        style={{ width: '100%', justifyContent: 'center', padding: '10px', fontSize: '0.9rem' }}
                      >
                        <span>View Full Guide</span>
                        <ArrowRight size={14} />
                      </Link>

                      <button
                        onClick={() => handleSave(dest.id)}
                        className="btn btn-secondary"
                        style={{ width: '100%', justifyContent: 'center', padding: '9px', fontSize: '0.88rem' }}
                      >
                        <Bookmark size={15} />
                        <span>Save to Shortlist</span>
                      </button>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </main>
  );
}
