import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { 
  Star, 
  MapPin, 
  ThumbsUp, 
  AlertTriangle, 
  ArrowLeft,
  Calendar,
  Bookmark,
  BookmarkCheck,
  Compass,
  Clock,
  IndianRupee,
  Bus,
  ShieldCheck,
  Sparkles,
  CheckCircle,
  MessageSquare,
  ThumbsDown,
  Flag,
  X
} from 'lucide-react';
import { formatBritishDate } from '../utils/dateFormatter';
import { formatDailyBudgetInr, normaliseBudgetTier } from '../utils/currencyFormatter';
import { 
  getDestinationById, 
  getDestinationAnalytics, 
  getDestinationKeywords, 
  getDestinationReviews,
  getSavedStatus,
  saveDestination,
  removeSavedDestination,
  getDestinations,
  submitIssueReport,
  tokenStorage
} from '../services/api';
import DestinationImage from '../components/DestinationImage';

const ASPECTS_LIST = ['All', 'Attractions', 'Food', 'Cleanliness', 'Price', 'Crowd', 'Safety', 'Transport', 'Accommodation', 'Hospitality'];

export default function DestinationDetails() {
  const { id } = useParams();
  const [destination, setDestination] = useState(null);
  const [analytics, setAnalytics] = useState(null);
  const [keywords, setKeywords] = useState([]);
  const [reviews, setReviews] = useState([]);
  const [alternatives, setAlternatives] = useState([]);

  // Guide tab selection: 'attractions' | 'itinerary' | 'transport' | 'tips'
  const [activeGuideTab, setActiveGuideTab] = useState('attractions');

  // Review filters state
  const [sentimentFilter, setSentimentFilter] = useState('All');
  const [ratingFilter, setRatingFilter] = useState('All');
  const [aspectFilter, setAspectFilter] = useState('All');
  const [isSaved, setIsSaved] = useState(false);
  const [saveLoading, setSaveLoading] = useState(false);

  // User feedback and reporting state
  const [feedbackGiven, setFeedbackGiven] = useState(() => {
    try {
      return localStorage.getItem(`travelens_feedback_${id}`) || null;
    } catch {
      return null;
    }
  });
  const [showReportModal, setShowReportModal] = useState(false);
  const [reportSubmitted, setReportSubmitted] = useState(false);
  const [reportCategory, setReportCategory] = useState('Outdated price or opening hours');
  const [reportComment, setReportComment] = useState('');
  const [reportEmail, setReportEmail] = useState('');
  const [reportSubmitting, setReportSubmitting] = useState(false);
  const [reportError, setReportError] = useState(null);

  const [loading, setLoading] = useState(true);
  const [reviewsLoading, setReviewsLoading] = useState(false);
  const [error, setError] = useState(null);


  useEffect(() => {
    Promise.all([
      getDestinationById(id),
      getDestinationAnalytics(id),
      getDestinationKeywords(id, 10),
    ])
      .then(([destData, analyticsData, keywordsData]) => {
        setDestination(destData);
        setAnalytics(analyticsData);
        setKeywords(keywordsData);
        setLoading(false);

        // Fetch alternatives with similar category or region
        getDestinations()
          .then((all) => {
            if (Array.isArray(all)) {
              const currentId = Number(id);
              const matches = all.filter(d => d.id !== currentId && (d.category === destData.category || d.region === destData.region));
              const fallbacks = all.filter(d => d.id !== currentId);
              setAlternatives(matches.length >= 2 ? matches.slice(0, 3) : fallbacks.slice(0, 3));
            }
          })
          .catch(() => {});
      })
      .catch((err) => {
        setError(err.message || 'Failed to load destination details.');
        setLoading(false);
      });

    // Check saved status
    getSavedStatus(id)
      .then((res) => setIsSaved(res.is_saved))
      .catch(() => setIsSaved(false));
  }, [id]);

  const handleSubmitReport = async (e) => {
    if (e) e.preventDefault();
    setReportSubmitting(true);
    setReportError(null);
    try {
      await submitIssueReport({
        destination_id: Number(id),
        issue_type: reportCategory,
        comment: reportComment.trim() || undefined,
        contact_email: reportEmail.trim() || undefined,
      });
      setReportSubmitted(true);
      setReportSubmitting(false);
    } catch (err) {
      setReportError(err.message || 'Failed to submit report. Please try again.');
      setReportSubmitting(false);
    }
  };


  // Fetch reviews based on active filters
  useEffect(() => {
    if (!destination) return;
    
    getDestinationReviews(id, {
      sentiment: sentimentFilter !== 'All' ? sentimentFilter : null,
      rating: ratingFilter !== 'All' ? Number(ratingFilter) : null,
      aspect: aspectFilter !== 'All' ? aspectFilter : null,
    })
      .then((data) => {
        setReviews(data || []);
        setReviewsLoading(false);
      })
      .catch((err) => {
        console.error('Error fetching filtered reviews:', err);
        setReviewsLoading(false);
      });
  }, [id, destination, sentimentFilter, ratingFilter, aspectFilter]);

  const handleToggleSave = async () => {
    const token = tokenStorage.get();
    if (!token) {
      alert('Please sign in to save destinations to your shortlist.');
      return;
    }

    setSaveLoading(true);
    try {
      if (isSaved) {
        await removeSavedDestination(id);
        setIsSaved(false);
      } else {
        await saveDestination(id);
        setIsSaved(true);
      }
    } catch (err) {
      alert(err.message || 'Could not update shortlist.');
    } finally {
      setSaveLoading(false);
    }
  };

  if (loading) {
    return (
      <main className="app-container" style={{ padding: 'var(--space-4xl) 0' }}>
        <div className="state-box">
          <div className="spinner"></div>
          <p style={{ marginTop: '16px' }}>Loading destination guide...</p>
        </div>
      </main>
    );
  }

  if (error || !destination) {
    return (
      <main className="app-container" style={{ padding: 'var(--space-4xl) 0' }}>
        <div className="state-box">
          <h2 style={{ color: 'var(--color-crimson)', marginBottom: '8px' }}>Destination Not Found</h2>
          <p style={{ color: 'var(--color-slate-600)', marginBottom: '20px' }}>{error || 'Unable to load destination data.'}</p>
          <Link to="/explore" className="btn btn-primary">Return to Explore</Link>
        </div>
      </main>
    );
  }

  // Parse guide fields safely
  let attractionsList = [];
  try {
    attractionsList = destination.attractions ? JSON.parse(destination.attractions) : [];
  } catch {
    attractionsList = destination.attractions ? destination.attractions.split(',').map(s => s.trim()) : [];
  }

  let activitiesList = [];
  try {
    activitiesList = destination.activities ? JSON.parse(destination.activities) : [];
  } catch {
    activitiesList = destination.activities ? destination.activities.split(',').map(s => s.trim()) : [];
  }

  // Analytics extraction
  const aspects = analytics?.aspects || {};
  const aspectEntries = Object.entries(aspects);
  const totalReviewsCount = destination.total_reviews || 0;

  // Filter top positive vs top concern aspects
  const lovedAspects = aspectEntries
    .filter(([, d]) => d.aspect_score !== null && d.aspect_score >= 65 && d.mention_count >= 2)
    .sort((a, b) => b[1].aspect_score - a[1].aspect_score)
    .slice(0, 3);

  const concernAspects = aspectEntries
    .filter(([, d]) => d.aspect_score !== null && d.aspect_score <= 48 && d.mention_count >= 2)
    .sort((a, b) => a[1].aspect_score - b[1].aspect_score)
    .slice(0, 3);

  const dailyBudgetInr = formatDailyBudgetInr(destination.indicative_daily_budget, destination.budget_tier);
  const displayBudgetTier = normaliseBudgetTier(destination.budget_tier);

  return (
    <main style={{ paddingBottom: 'var(--space-4xl)' }}>
      {/* Editorial Breadcrumb */}
      <div className="app-container" style={{ padding: 'var(--space-md) 0' }}>
        <Link to="/explore" style={{ display: 'inline-flex', alignItems: 'center', gap: '8px', fontSize: '0.9rem', color: 'var(--color-slate-600)', textDecoration: 'none', fontWeight: 500 }}>
          <ArrowLeft size={16} />
          <span>Back to All Destinations</span>
        </Link>
      </div>

      {/* A. Destination Introduction: Hero Photo, Name, Location & Overview */}
      <section style={{ backgroundColor: 'var(--color-sand-50)', borderBottom: '1px solid var(--color-sand-200)', padding: 'var(--space-lg) 0 var(--space-3xl)' }}>
        <div className="app-container">
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(340px, 1fr))', gap: 'var(--space-2xl)', alignItems: 'center' }}>
            {/* Visual Photography */}
            <div style={{ position: 'relative', height: '420px', borderRadius: 'var(--radius-lg)', overflow: 'hidden', boxShadow: 'var(--shadow-card)' }}>
              <DestinationImage 
                src={destination.image_url} 
                alt={destination.name}
                category={destination.category}
                style={{ width: '100%', height: '100%', objectFit: 'cover' }}
              />
              <div style={{ position: 'absolute', top: '16px', right: '16px', display: 'flex', gap: '8px' }}>
                <span className="badge badge-category" style={{ backgroundColor: 'rgba(255,255,255,0.95)', color: 'var(--color-slate-900)', fontWeight: 600 }}>
                  {destination.category}
                </span>
                {destination.region && (
                  <span className="badge" style={{ backgroundColor: 'var(--color-slate-900)', color: '#FFFFFF', fontWeight: 600 }}>
                    {destination.region}
                  </span>
                )}
              </div>
            </div>

            {/* Destination Metadata & Actions */}
            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px', color: 'var(--color-terracotta)', fontWeight: 700, fontSize: '0.88rem', textTransform: 'uppercase', letterSpacing: '0.06em', marginBottom: '8px' }}>
                <MapPin size={16} />
                <span>
                  {destination.state_or_region ? `${destination.state_or_region}, ${destination.country}` : destination.country}
                </span>
              </div>

              <h1 style={{ fontSize: 'clamp(2.3rem, 4vw, 3.4rem)', marginBottom: '14px', lineHeight: 1.15 }}>
                {destination.name}
              </h1>
              
              <p style={{ fontSize: '1.08rem', color: 'var(--color-slate-700)', lineHeight: 1.65, marginBottom: 'var(--space-xl)' }}>
                {destination.description}
              </p>

              <div style={{ display: 'flex', alignItems: 'center', gap: 'var(--space-md)', flexWrap: 'wrap' }}>
                <button
                  onClick={handleToggleSave}
                  disabled={saveLoading}
                  className={isSaved ? "btn btn-primary" : "btn btn-secondary"}
                  style={{ padding: '12px 22px', display: 'inline-flex', alignItems: 'center', gap: '8px', fontSize: '0.95rem' }}
                >
                  {isSaved ? <BookmarkCheck size={18} /> : <Bookmark size={18} />}
                  <span>{isSaved ? "Saved in Shortlist" : "Save Destination"}</span>
                </button>

                <Link
                  to={`/compare?destA=${destination.id}`}
                  className="btn btn-secondary"
                  style={{ padding: '12px 20px', display: 'inline-flex', alignItems: 'center', gap: '8px', fontSize: '0.95rem' }}
                >
                  <Compass size={18} />
                  <span>Compare Place</span>
                </Link>

                <Link
                  to={`/plan`}
                  className="btn btn-secondary"
                  style={{ padding: '12px 20px', display: 'inline-flex', alignItems: 'center', gap: '8px', fontSize: '0.95rem' }}
                >
                  <Calendar size={18} />
                  <span>Plan a Trip</span>
                </Link>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Overview Strip: Rating, Reviews, Best Season, Duration, INR Budget */}
      <section style={{ backgroundColor: 'var(--color-white)', borderBottom: '1px solid var(--color-sand-200)', padding: 'var(--space-xl) 0' }}>
        <div className="app-container">
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(210px, 1fr))', gap: 'var(--space-xl)' }}>
            {/* Rating & Reviews */}
            <div style={{ display: 'flex', alignItems: 'flex-start', gap: '12px' }}>
              <div style={{ width: '42px', height: '42px', borderRadius: 'var(--radius-md)', backgroundColor: 'var(--color-sand-100)', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>
                <Star size={22} fill="var(--color-terracotta)" color="var(--color-terracotta)" />
              </div>
              <div>
                <span style={{ fontSize: '0.75rem', textTransform: 'uppercase', letterSpacing: '0.06em', color: 'var(--color-slate-400)', fontWeight: 700, display: 'block' }}>
                  Visitor Rating
                </span>
                <div style={{ display: 'flex', alignItems: 'baseline', gap: '6px', marginTop: '2px' }}>
                  <span style={{ fontSize: '1.4rem', fontWeight: 700, color: 'var(--color-slate-900)' }}>
                    {destination.average_rating > 0 ? Number(destination.average_rating).toFixed(1) : '4.5'}
                  </span>
                  <span style={{ fontSize: '0.85rem', color: 'var(--color-slate-500)' }}>
                    ({totalReviewsCount} reviews)
                  </span>
                </div>
                <span style={{ fontSize: '0.74rem', color: 'var(--color-olive)', fontWeight: 600, display: 'block', marginTop: '3px' }}>
                  Verified 2024–2026 Corpus
                </span>
              </div>
            </div>

            {/* Best Season */}
            <div style={{ display: 'flex', alignItems: 'flex-start', gap: '12px' }}>
              <div style={{ width: '42px', height: '42px', borderRadius: 'var(--radius-md)', backgroundColor: 'var(--color-sand-100)', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>
                <Calendar size={22} color="var(--color-terracotta)" />
              </div>
              <div>
                <span style={{ fontSize: '0.75rem', textTransform: 'uppercase', letterSpacing: '0.06em', color: 'var(--color-slate-400)', fontWeight: 700, display: 'block' }}>
                  Best Season
                </span>
                <span style={{ fontSize: '1rem', fontWeight: 600, color: 'var(--color-slate-900)', display: 'block', marginTop: '2px' }}>
                  {destination.best_season || 'October to March'}
                </span>
              </div>
            </div>

            {/* Recommended Duration */}
            <div style={{ display: 'flex', alignItems: 'flex-start', gap: '12px' }}>
              <div style={{ width: '42px', height: '42px', borderRadius: 'var(--radius-md)', backgroundColor: 'var(--color-sand-100)', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>
                <Clock size={22} color="var(--color-olive)" />
              </div>
              <div>
                <span style={{ fontSize: '0.75rem', textTransform: 'uppercase', letterSpacing: '0.06em', color: 'var(--color-slate-400)', fontWeight: 700, display: 'block' }}>
                  Recommended Stay
                </span>
                <span style={{ fontSize: '1rem', fontWeight: 600, color: 'var(--color-slate-900)', display: 'block', marginTop: '2px' }}>
                  {destination.recommended_duration || '3–4 days'}
                </span>
              </div>
            </div>

            {/* INR Budget Tier & Daily Estimate */}
            <div style={{ display: 'flex', alignItems: 'flex-start', gap: '12px' }}>
              <div style={{ width: '42px', height: '42px', borderRadius: 'var(--radius-md)', backgroundColor: 'var(--color-sand-100)', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>
                <IndianRupee size={22} color="var(--color-terracotta)" />
              </div>
              <div>
                <span style={{ fontSize: '0.75rem', textTransform: 'uppercase', letterSpacing: '0.06em', color: 'var(--color-slate-400)', fontWeight: 700, display: 'block' }}>
                  Estimated Daily Budget
                </span>
                <span style={{ fontSize: '1rem', fontWeight: 700, color: 'var(--color-slate-900)', display: 'block', marginTop: '2px' }}>
                  {dailyBudgetInr}
                </span>
                <span style={{ fontSize: '0.8rem', color: 'var(--color-slate-500)' }}>
                  Tier: {displayBudgetTier}
                </span>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* B. The Traveller's Perspective: Strengths, Challenges, Aspects & Most Discussed Topics */}
      <section style={{ padding: 'var(--space-3xl) 0', borderBottom: '1px solid var(--color-sand-200)' }}>
        <div className="app-container">
          <div style={{ marginBottom: 'var(--space-2xl)' }}>
            <span style={{ textTransform: 'uppercase', fontSize: '0.8rem', letterSpacing: '0.12em', color: 'var(--color-terracotta)', fontWeight: 700 }}>
              The Traveller's Perspective
            </span>
            <h2 style={{ fontSize: '2rem', marginTop: '4px', marginBottom: '8px' }}>
              What visiting {destination.name} is really like
            </h2>
            <p style={{ fontSize: '1.05rem', color: 'var(--color-slate-600)', maxWidth: '780px' }}>
              We analyse what travellers write about their journeys, highlighting both the most appreciated experiences and honest caveats.
            </p>
          </div>

          {/* What Travellers Liked vs What Travellers Found Challenging */}
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: 'var(--space-xl)', marginBottom: 'var(--space-3xl)' }}>
            {/* What Travellers Appreciated */}
            <div 
              style={{
                backgroundColor: 'var(--color-white)',
                padding: 'var(--space-xl)',
                borderRadius: 'var(--radius-lg)',
                border: '1px solid var(--color-sand-200)',
                borderTop: '4px solid var(--color-olive)',
                boxShadow: 'var(--shadow-subtle)'
              }}
            >
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: 'var(--space-md)', color: 'var(--color-olive)' }}>
                <ThumbsUp size={22} />
                <h3 style={{ fontSize: '1.25rem', color: 'var(--color-slate-900)', margin: 0 }}>What travellers appreciated</h3>
              </div>
              <p style={{ fontSize: '0.92rem', color: 'var(--color-slate-600)', marginBottom: 'var(--space-md)' }}>
                Consistent strengths praised by visitors in reviews of {destination.name}:
              </p>
              {lovedAspects.length > 0 ? (
                <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '10px', padding: 0, margin: 0 }}>
                  {lovedAspects.map(([asp, d]) => (
                    <li key={asp} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '10px 14px', backgroundColor: 'var(--color-olive-light)', borderRadius: 'var(--radius-md)' }}>
                      <span style={{ fontWeight: 600, color: 'var(--color-slate-900)' }}>{asp}</span>
                      <span style={{ fontWeight: 600, color: 'var(--color-olive)', fontSize: '0.88rem' }}>
                        {d.sentiment.positive_pct}% positive feedback
                      </span>
                    </li>
                  ))}
                </ul>
              ) : (
                <p style={{ fontStyle: 'italic', fontSize: '0.9rem', color: 'var(--color-slate-500)', margin: 0 }}>
                  Visitors report a balanced overall experience without prominent positive outliers.
                </p>
              )}
            </div>

            {/* Common Concerns / Challenges */}
            <div 
              style={{
                backgroundColor: 'var(--color-white)',
                padding: 'var(--space-xl)',
                borderRadius: 'var(--radius-lg)',
                border: '1px solid var(--color-sand-200)',
                borderTop: '4px solid var(--color-crimson)',
                boxShadow: 'var(--shadow-subtle)'
              }}
            >
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: 'var(--space-md)', color: 'var(--color-crimson)' }}>
                <AlertTriangle size={22} />
                <h3 style={{ fontSize: '1.25rem', color: 'var(--color-slate-900)', margin: 0 }}>Caveats & challenges</h3>
              </div>
              <p style={{ fontSize: '0.92rem', color: 'var(--color-slate-600)', marginBottom: 'var(--space-md)' }}>
                Bottlenecks, crowds, or recurring challenges mentioned in reviews:
              </p>
              {concernAspects.length > 0 ? (
                <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '10px', padding: 0, margin: 0 }}>
                  {concernAspects.map(([asp, d]) => (
                    <li key={asp} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '10px 14px', backgroundColor: 'var(--color-crimson-light)', borderRadius: 'var(--radius-md)' }}>
                      <span style={{ fontWeight: 600, color: 'var(--color-slate-900)' }}>{asp}</span>
                      <span style={{ fontWeight: 600, color: 'var(--color-crimson)', fontSize: '0.88rem' }}>
                        {d.sentiment.negative_pct}% mentions note challenges
                      </span>
                    </li>
                  ))}
                </ul>
              ) : (
                <p style={{ fontStyle: 'italic', fontSize: '0.9rem', color: 'var(--color-slate-500)', margin: 0 }}>
                  No severe recurrent visitor concerns recorded for this destination.
                </p>
              )}
            </div>
          </div>

          {/* Aspect Scorecard: What Travellers Say About */}
          <div style={{ marginBottom: 'var(--space-3xl)' }}>
            <div style={{ marginBottom: 'var(--space-lg)' }}>
              <h3 style={{ fontSize: '1.5rem', marginBottom: '6px' }}>What Travellers Say Across 9 Travel Dimensions</h3>
              <p style={{ fontSize: '0.95rem', color: 'var(--color-slate-600)', margin: 0 }}>
                Every score indicates traveller satisfaction in written reviews. Dimensions with limited mentions are clearly labeled.
              </p>
            </div>

            <div 
              style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
                gap: 'var(--space-md)'
              }}
            >
              {aspectEntries.map(([aspName, data]) => {
                const hasData = data.mention_count >= 2 && data.aspect_score !== null;
                const score = data.aspect_score;
                const isPositive = score >= 65;
                const isConcern = score <= 48;
                const color = !hasData 
                  ? 'var(--color-slate-500)' 
                  : isPositive 
                  ? 'var(--color-olive)' 
                  : isConcern 
                  ? 'var(--color-crimson)' 
                  : 'var(--color-amber)';
                const bgLight = !hasData
                  ? 'var(--color-sand-100)'
                  : isPositive 
                  ? 'var(--color-olive-light)' 
                  : isConcern 
                  ? 'var(--color-crimson-light)' 
                  : 'var(--color-amber-light)';

                return (
                  <div 
                    key={aspName}
                    style={{
                      backgroundColor: 'var(--color-white)',
                      padding: 'var(--space-lg)',
                      borderRadius: 'var(--radius-md)',
                      border: '1px solid var(--color-sand-200)',
                      display: 'flex',
                      flexDirection: 'column',
                      justifyContent: 'space-between',
                      gap: '12px'
                    }}
                  >
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: '8px' }}>
                      <div>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '6px', flexWrap: 'wrap' }}>
                          <span style={{ fontWeight: 700, fontSize: '1.02rem', color: 'var(--color-slate-900)' }}>
                            {aspName}
                          </span>
                          {hasData && data.mention_count < 10 && (
                            <span 
                              style={{ 
                                fontSize: '0.72rem', 
                                fontWeight: 600, 
                                color: '#92400E', 
                                backgroundColor: '#FEF3C7', 
                                padding: '2px 7px', 
                                borderRadius: '4px',
                                border: '1px solid #FDE68A'
                              }}
                            >
                              Limited data (&lt; 10 mentions)
                            </span>
                          )}
                          {hasData && data.sentiment.positive_pct >= 20 && data.sentiment.negative_pct >= 20 && (
                            <span 
                              style={{ 
                                fontSize: '0.72rem', 
                                fontWeight: 600, 
                                color: '#78350F', 
                                backgroundColor: '#FDE68A', 
                                padding: '2px 7px', 
                                borderRadius: '4px'
                              }}
                            >
                              Mixed Feedback
                            </span>
                          )}
                        </div>
                        <span style={{ fontSize: '0.8rem', color: 'var(--color-slate-500)', display: 'block', marginTop: '2px' }}>
                          {data.mention_count >= 10
                            ? `Strong consensus (${data.mention_count} aspect mentions)`
                            : data.mention_count >= 2
                            ? `Moderate consensus (${data.mention_count} aspect mentions)`
                            : data.mention_count > 0
                            ? `Sparse evidence (${data.mention_count} aspect mention)`
                            : 'Not enough review data'}
                        </span>
                      </div>

                      <span 
                        style={{ 
                          fontWeight: 700, 
                          fontSize: hasData ? '0.92rem' : '0.8rem', 
                          color, 
                          backgroundColor: bgLight, 
                          padding: '4px 10px', 
                          borderRadius: 'var(--radius-sm)' 
                        }}
                      >
                        {hasData ? `${score} / 100` : 'Not enough review data'}
                      </span>
                    </div>

                    {/* Progress Bar */}
                    <div className="aspect-bar-track" style={{ height: '7px' }}>
                      {hasData ? (
                        <div 
                          className="aspect-bar-fill" 
                          style={{ width: `${score}%`, backgroundColor: color }}
                        />
                      ) : (
                        <div style={{ width: '100%', height: '100%', backgroundColor: 'var(--color-sand-200)' }} />
                      )}
                    </div>

                    {/* Feedback summary */}
                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.8rem', color: 'var(--color-slate-500)' }}>
                      {hasData ? (
                        <>
                          <span style={{ color: 'var(--color-olive)', fontWeight: 600 }}>{data.sentiment.positive_pct}% Positive</span>
                          <span>{data.sentiment.neutral_pct}% Neutral</span>
                          <span style={{ color: 'var(--color-crimson)', fontWeight: 600 }}>{data.sentiment.negative_pct}% Critical</span>
                        </>
                      ) : (
                        <span style={{ fontStyle: 'italic' }}>Insufficient feedback to establish reliable consensus</span>
                      )}
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

          {/* Most Discussed Topics */}
          <div>
            <h3 style={{ fontSize: '1.35rem', marginBottom: '8px' }}>Most Discussed Topics</h3>
            <p style={{ fontSize: '0.92rem', color: 'var(--color-slate-600)', marginBottom: 'var(--space-md)' }}>
              Top themes and recurring phrases highlighted by travellers visiting {destination.name}:
            </p>
            
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px' }}>
              {keywords.length > 0 ? (
                keywords.map((kw, idx) => (
                  <span 
                    key={kw.keyword}
                    className="badge"
                    style={{
                      backgroundColor: idx < 3 ? 'var(--color-sand-100)' : 'var(--color-white)',
                      color: 'var(--color-slate-900)',
                      border: '1px solid var(--color-sand-200)',
                      padding: '8px 14px',
                      fontSize: '0.88rem',
                      fontWeight: idx < 3 ? 700 : 500
                    }}
                  >
                    {kw.keyword}
                    {kw.frequency && (
                      <span style={{ fontSize: '0.8rem', color: 'var(--color-terracotta)', marginLeft: '6px', fontWeight: 700 }}>
                        ×{kw.frequency}
                      </span>
                    )}
                  </span>
                ))
              ) : (
                <p style={{ color: 'var(--color-slate-400)', fontSize: '0.9rem' }}>Review topics compiled from visitor corpus.</p>
              )}
            </div>
          </div>

          {/* Review Summary Feedback & Integrity Strip */}
          <div 
            style={{
              marginTop: 'var(--space-2xl)',
              padding: 'var(--space-md) var(--space-xl)',
              backgroundColor: 'var(--color-sand-50)',
              borderRadius: 'var(--radius-md)',
              border: '1px solid var(--color-sand-200)',
              display: 'flex',
              flexWrap: 'wrap',
              justifyContent: 'space-between',
              alignItems: 'center',
              gap: 'var(--space-md)'
            }}
          >
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px', flexWrap: 'wrap' }}>
              <span style={{ fontSize: '0.88rem', fontWeight: 600, color: 'var(--color-slate-800)' }}>
                Was this review summary helpful?
              </span>
              {feedbackGiven ? (
                <span style={{ fontSize: '0.85rem', color: 'var(--color-olive)', fontWeight: 600, display: 'inline-flex', alignItems: 'center', gap: '4px' }}>
                  <CheckCircle size={15} /> Thank you for your feedback! ({feedbackGiven === 'yes' ? 'Helpful' : 'Needs improvement'})
                </span>
              ) : (
                <div style={{ display: 'flex', gap: '8px' }}>
                  <button
                    type="button"
                    onClick={() => {
                      setFeedbackGiven('yes');
                      try { localStorage.setItem(`travelens_feedback_${id}`, 'yes'); } catch {}
                    }}
                    className="btn btn-secondary"
                    style={{ padding: '4px 12px', fontSize: '0.82rem', display: 'inline-flex', alignItems: 'center', gap: '4px' }}
                  >
                    <ThumbsUp size={14} color="var(--color-olive)" />
                    <span>Yes</span>
                  </button>
                  <button
                    type="button"
                    onClick={() => {
                      setFeedbackGiven('no');
                      try { localStorage.setItem(`travelens_feedback_${id}`, 'no'); } catch {}
                    }}
                    className="btn btn-secondary"
                    style={{ padding: '4px 12px', fontSize: '0.82rem', display: 'inline-flex', alignItems: 'center', gap: '4px' }}
                  >
                    <ThumbsDown size={14} color="var(--color-crimson)" />
                    <span>No</span>
                  </button>
                </div>
              )}
            </div>

            <button
              type="button"
              onClick={() => {
                setShowReportModal(true);
                setReportSubmitted(false);
              }}
              style={{
                background: 'none',
                border: 'none',
                fontSize: '0.82rem',
                color: 'var(--color-slate-500)',
                textDecoration: 'underline',
                cursor: 'pointer',
                display: 'inline-flex',
                alignItems: 'center',
                gap: '4px'
              }}
            >
              <Flag size={13} />
              <span>Report incorrect information</span>
            </button>
          </div>
        </div>
      </section>

      {/* C. Practical Travel Guide: Attractions, Itinerary, Transit, Advice */}
      <section style={{ padding: 'var(--space-3xl) 0', backgroundColor: 'var(--color-sand-50)', borderBottom: '1px solid var(--color-sand-200)' }}>
        <div className="app-container">
          <div style={{ marginBottom: 'var(--space-lg)' }}>
            <span style={{ textTransform: 'uppercase', fontSize: '0.8rem', letterSpacing: '0.12em', color: 'var(--color-terracotta)', fontWeight: 700 }}>
              Practical Travel Guide
            </span>
            <h2 style={{ fontSize: '2rem', marginTop: '4px', marginBottom: '6px' }}>
              Itinerary, Sights & Practical Logistics
            </h2>
            <p style={{ fontSize: '1.02rem', color: 'var(--color-slate-600)', margin: 0 }}>
              Curated travel recommendations and tips to help you make the most of your trip.
            </p>
          </div>

          {/* Guide Tabs */}
          <div style={{ display: 'flex', gap: '8px', borderBottom: '2px solid var(--color-sand-200)', marginBottom: 'var(--space-xl)', flexWrap: 'wrap' }}>
            <button
              onClick={() => setActiveGuideTab('attractions')}
              style={{
                padding: '12px 20px',
                border: 'none',
                background: 'none',
                borderBottom: activeGuideTab === 'attractions' ? '3px solid var(--color-terracotta)' : '3px solid transparent',
                fontWeight: activeGuideTab === 'attractions' ? 700 : 500,
                color: activeGuideTab === 'attractions' ? 'var(--color-slate-900)' : 'var(--color-slate-600)',
                cursor: 'pointer',
                fontSize: '0.95rem'
              }}
            >
              Attractions & Experiences
            </button>
            <button
              onClick={() => setActiveGuideTab('itinerary')}
              style={{
                padding: '12px 20px',
                border: 'none',
                background: 'none',
                borderBottom: activeGuideTab === 'itinerary' ? '3px solid var(--color-terracotta)' : '3px solid transparent',
                fontWeight: activeGuideTab === 'itinerary' ? 700 : 500,
                color: activeGuideTab === 'itinerary' ? 'var(--color-slate-900)' : 'var(--color-slate-600)',
                cursor: 'pointer',
                fontSize: '0.95rem'
              }}
            >
              Suggested Itinerary
            </button>
            <button
              onClick={() => setActiveGuideTab('transport')}
              style={{
                padding: '12px 20px',
                border: 'none',
                background: 'none',
                borderBottom: activeGuideTab === 'transport' ? '3px solid var(--color-terracotta)' : '3px solid transparent',
                fontWeight: activeGuideTab === 'transport' ? 700 : 500,
                color: activeGuideTab === 'transport' ? 'var(--color-slate-900)' : 'var(--color-slate-600)',
                cursor: 'pointer',
                fontSize: '0.95rem'
              }}
            >
              Getting There & Transit
            </button>
            <button
              onClick={() => setActiveGuideTab('tips')}
              style={{
                padding: '12px 20px',
                border: 'none',
                background: 'none',
                borderBottom: activeGuideTab === 'tips' ? '3px solid var(--color-terracotta)' : '3px solid transparent',
                fontWeight: activeGuideTab === 'tips' ? 700 : 500,
                color: activeGuideTab === 'tips' ? 'var(--color-slate-900)' : 'var(--color-slate-600)',
                cursor: 'pointer',
                fontSize: '0.95rem'
              }}
            >
              Practical Advice
            </button>
          </div>

          {/* Tab 1: Attractions & Experiences */}
          {activeGuideTab === 'attractions' && (
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: 'var(--space-lg)' }}>
              <div style={{ backgroundColor: '#FFFFFF', padding: 'var(--space-xl)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--color-sand-200)', boxShadow: 'var(--shadow-subtle)' }}>
                <h3 style={{ fontSize: '1.25rem', marginBottom: 'var(--space-md)', display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <Sparkles size={18} color="var(--color-terracotta)" />
                  Top Attractions
                </h3>
                {attractionsList.length > 0 ? (
                  <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '10px', padding: 0, margin: 0 }}>
                    {attractionsList.map((attr, idx) => (
                      <li key={idx} style={{ display: 'flex', alignItems: 'center', gap: '12px', padding: '12px 14px', backgroundColor: 'var(--color-sand-50)', borderRadius: 'var(--radius-md)' }}>
                        <span style={{ width: '24px', height: '24px', borderRadius: '50%', backgroundColor: 'var(--color-terracotta)', color: '#FFF', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '0.8rem', fontWeight: 700, flexShrink: 0 }}>
                          {idx + 1}
                        </span>
                        <span style={{ fontWeight: 600, color: 'var(--color-slate-900)' }}>{attr}</span>
                      </li>
                    ))}
                  </ul>
                ) : (
                  <p style={{ color: 'var(--color-slate-500)', margin: 0 }}>Curated sights available in destination summary.</p>
                )}
              </div>

              <div style={{ backgroundColor: '#FFFFFF', padding: 'var(--space-xl)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--color-sand-200)', boxShadow: 'var(--shadow-subtle)' }}>
                <h3 style={{ fontSize: '1.25rem', marginBottom: 'var(--space-md)', display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <Compass size={18} color="var(--color-olive)" />
                  Must-Do Experiences
                </h3>
                {activitiesList.length > 0 ? (
                  <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '10px', padding: 0, margin: 0 }}>
                    {activitiesList.map((act, idx) => (
                      <li key={idx} style={{ display: 'flex', alignItems: 'flex-start', gap: '12px', padding: '12px 14px', backgroundColor: 'var(--color-olive-light)', borderRadius: 'var(--radius-md)' }}>
                        <CheckCircle size={18} color="var(--color-olive)" style={{ marginTop: '2px', flexShrink: 0 }} />
                        <span style={{ fontSize: '0.92rem', color: 'var(--color-slate-900)', lineHeight: 1.5 }}>{act}</span>
                      </li>
                    ))}
                  </ul>
                ) : (
                  <p style={{ color: 'var(--color-slate-500)', margin: 0 }}>Check review feedback above for popular activities.</p>
                )}
              </div>
            </div>
          )}

          {/* Tab 2: Suggested Itinerary */}
          {activeGuideTab === 'itinerary' && (
            <div style={{ backgroundColor: '#FFFFFF', padding: 'var(--space-2xl)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--color-sand-200)', boxShadow: 'var(--shadow-subtle)' }}>
              <h3 style={{ fontSize: '1.35rem', marginBottom: 'var(--space-md)' }}>
                Suggested Travel Plan ({destination.recommended_duration || '3–4 days'})
              </h3>
              {destination.suggested_itinerary ? (
                <div style={{ display: 'flex', flexDirection: 'column', gap: '14px' }}>
                  {destination.suggested_itinerary.split(/(?=Day \d+:)/).filter(s => s.trim()).map((dayStr, idx) => (
                    <div key={idx} style={{ padding: '16px 20px', backgroundColor: 'var(--color-sand-50)', borderRadius: 'var(--radius-md)', borderLeft: '4px solid var(--color-terracotta)' }}>
                      <p style={{ margin: 0, fontSize: '0.98rem', color: 'var(--color-slate-800)', lineHeight: 1.6 }}>
                        {dayStr.trim()}
                      </p>
                    </div>
                  ))}
                </div>
              ) : (
                <p style={{ color: 'var(--color-slate-600)', margin: 0 }}>
                  You can personalize your day-by-day plan using Plan a Trip.
                </p>
              )}
            </div>
          )}

          {/* Tab 3: Getting There & Transit */}
          {activeGuideTab === 'transport' && (
            <div style={{ backgroundColor: '#FFFFFF', padding: 'var(--space-2xl)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--color-sand-200)', boxShadow: 'var(--shadow-subtle)' }}>
              <h3 style={{ fontSize: '1.35rem', marginBottom: 'var(--space-md)', display: 'flex', alignItems: 'center', gap: '8px' }}>
                <Bus size={22} color="var(--color-slate-700)" />
                Transit Routes, Airports & Local Mobility
              </h3>
              <p style={{ fontSize: '1.05rem', color: 'var(--color-slate-700)', lineHeight: 1.7, marginBottom: 'var(--space-md)' }}>
                {destination.transport_info || 'Accessible by domestic and international flights, railway hubs, and regional highway networks.'}
              </p>
              <div style={{ padding: '14px 18px', backgroundColor: 'var(--color-sand-100)', borderRadius: 'var(--radius-md)', fontSize: '0.92rem', color: 'var(--color-slate-700)' }}>
                <strong>Transport Advice:</strong> Check the Transport dimension in the review scorecard above to review visitor satisfaction regarding walking, cabs, and transit links.
              </div>
            </div>
          )}

          {/* Tab 4: Practical Advice & Etiquette */}
          {activeGuideTab === 'tips' && (
            <div style={{ backgroundColor: '#FFFFFF', padding: 'var(--space-2xl)', borderRadius: 'var(--radius-lg)', border: '1px solid var(--color-sand-200)', boxShadow: 'var(--shadow-subtle)' }}>
              <h3 style={{ fontSize: '1.35rem', marginBottom: 'var(--space-md)', display: 'flex', alignItems: 'center', gap: '8px' }}>
                <ShieldCheck size={22} color="var(--color-olive)" />
                Practical Travel Advice & Safety Notes
              </h3>
              <p style={{ fontSize: '1.05rem', color: 'var(--color-slate-700)', lineHeight: 1.7, marginBottom: 'var(--space-md)' }}>
                {destination.practical_tips || 'Respect cultural customs and modest dress etiquette in heritage monuments and places of worship. Book passes in advance during peak season.'}
              </p>
              <div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap', marginTop: 'var(--space-md)' }}>
                <span className="badge" style={{ backgroundColor: 'var(--color-sand-100)', color: 'var(--color-slate-800)', padding: '6px 14px', fontSize: '0.88rem' }}>
                  Safety: Assessed by travellers
                </span>
                <span className="badge" style={{ backgroundColor: 'var(--color-sand-100)', color: 'var(--color-slate-800)', padding: '6px 14px', fontSize: '0.88rem' }}>
                  Daily Budget: {dailyBudgetInr}
                </span>
              </div>
            </div>
          )}
        </div>
      </section>

      {/* D. Visitor Reviews: Authentic Reviews with Star Ratings, Sentiment & Aspect Tags */}
      <section style={{ padding: 'var(--space-3xl) 0', borderBottom: '1px solid var(--color-sand-200)' }}>
        <div className="app-container">
          <div style={{ marginBottom: 'var(--space-xl)' }}>
            <span style={{ textTransform: 'uppercase', fontSize: '0.8rem', letterSpacing: '0.12em', color: 'var(--color-terracotta)', fontWeight: 700 }}>
              Traveller Voices
            </span>
            <h2 style={{ fontSize: '2rem', marginTop: '4px', marginBottom: '6px' }}>
              Visitor Reviews ({totalReviewsCount})
            </h2>
            <p style={{ fontSize: '1.02rem', color: 'var(--color-slate-600)', margin: 0 }}>
              Read direct traveller feedback. Filter by sentiment, star rating, or specific tourism aspect.
            </p>
          </div>

          {/* Filter Ribbon */}
          <div 
            style={{
              display: 'flex',
              flexWrap: 'wrap',
              gap: 'var(--space-md)',
              backgroundColor: 'var(--color-white)',
              padding: 'var(--space-md) var(--space-lg)',
              borderRadius: 'var(--radius-md)',
              border: '1px solid var(--color-sand-200)',
              marginBottom: 'var(--space-xl)',
              alignItems: 'center'
            }}
          >
            {/* Sentiment Filter */}
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <span style={{ fontSize: '0.88rem', color: 'var(--color-slate-700)', fontWeight: 600 }}>Sentiment:</span>
              <select 
                value={sentimentFilter} 
                onChange={(e) => setSentimentFilter(e.target.value)}
                style={{ padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--color-sand-200)', fontSize: '0.88rem' }}
              >
                <option value="All">All Sentiments</option>
                <option value="positive">Positive</option>
                <option value="neutral">Neutral</option>
                <option value="negative">Negative</option>
                <option value="mixed">Mixed Reviews</option>
              </select>
            </div>

            {/* Star Rating Filter */}
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <span style={{ fontSize: '0.88rem', color: 'var(--color-slate-700)', fontWeight: 600 }}>Star Rating:</span>
              <select 
                value={ratingFilter} 
                onChange={(e) => setRatingFilter(e.target.value)}
                style={{ padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--color-sand-200)', fontSize: '0.88rem' }}
              >
                <option value="All">All Stars</option>
                <option value="5">5 Stars</option>
                <option value="4">4 Stars</option>
                <option value="3">3 Stars</option>
                <option value="2">2 Stars</option>
                <option value="1">1 Star</option>
              </select>
            </div>

            {/* Aspect Filter */}
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <span style={{ fontSize: '0.88rem', color: 'var(--color-slate-700)', fontWeight: 600 }}>Aspect:</span>
              <select 
                value={aspectFilter} 
                onChange={(e) => setAspectFilter(e.target.value)}
                style={{ padding: '8px 12px', borderRadius: 'var(--radius-sm)', border: '1px solid var(--color-sand-200)', fontSize: '0.88rem' }}
              >
                {ASPECTS_LIST.map((asp) => (
                  <option key={asp} value={asp}>{asp}</option>
                ))}
              </select>
            </div>

            <button 
              onClick={() => { setSentimentFilter('All'); setRatingFilter('All'); setAspectFilter('All'); }}
              className="btn btn-ghost"
              style={{ fontSize: '0.85rem', padding: '6px 12px', marginLeft: 'auto' }}
            >
              Reset Filters
            </button>
          </div>

          {/* Reviews List */}
          {reviewsLoading ? (
            <div className="state-box">
              <div className="spinner"></div>
              <p style={{ marginTop: '12px' }}>Filtering reviews...</p>
            </div>
          ) : reviews.length === 0 ? (
            <div className="state-box">
              <MessageSquare size={36} className="state-box-icon" style={{ color: 'var(--color-terracotta)', marginBottom: '10px' }} />
              <h3>No reviews match your selected filters</h3>
              <p style={{ marginTop: '4px', color: 'var(--color-slate-600)' }}>Try adjusting the sentiment or aspect dropdowns above.</p>
            </div>
          ) : (
            <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-md)' }}>
              {reviews.map((rev) => {
                const sentimentType = rev.sentiment || (rev.rating >= 4 ? 'positive' : rev.rating === 3 ? 'neutral' : 'negative');
                const isPos = sentimentType === 'positive';
                const isNeg = sentimentType === 'negative';
                const sentimentBadge = isPos ? 'badge-positive' : isNeg ? 'badge-negative' : 'badge-neutral';

                return (
                  <article 
                    key={rev.id} 
                    style={{
                      backgroundColor: 'var(--color-white)',
                      padding: 'var(--space-xl)',
                      borderRadius: 'var(--radius-md)',
                      border: '1px solid var(--color-sand-200)',
                      boxShadow: 'var(--shadow-subtle)'
                    }}
                  >
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px', flexWrap: 'wrap', gap: '8px' }}>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '10px', flexWrap: 'wrap' }}>
                        {/* Star Rating */}
                        <div style={{ display: 'flex', color: 'var(--color-terracotta)', alignItems: 'center', gap: '2px' }}>
                          {[...Array(rev.rating || 5)].map((_, i) => (
                            <Star key={i} size={15} fill="currentColor" />
                          ))}
                          <span style={{ fontWeight: 700, marginLeft: '4px', fontSize: '0.92rem', color: 'var(--color-slate-800)' }}>
                            {rev.rating}.0
                          </span>
                        </div>

                        {/* Sentiment Badge */}
                        <span className={`badge ${sentimentBadge}`} style={{ fontSize: '0.8rem', textTransform: 'capitalize' }}>
                          {sentimentType}
                        </span>

                        {/* Mixed Sentiment Badge */}
                        {rev.is_mixed && (
                          <span className="badge" style={{ fontSize: '0.8rem', backgroundColor: '#FEF3C7', color: '#92400E', border: '1px solid #FDE68A', fontWeight: 600 }}>
                            Mixed Feedback
                          </span>
                        )}
                      </div>

                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                        <span style={{ fontSize: '0.82rem', color: 'var(--color-slate-500)' }}>
                          {formatBritishDate(rev.review_date)}
                        </span>
                      </div>
                    </div>

                    <p style={{ color: 'var(--color-slate-800)', fontSize: '1rem', lineHeight: 1.65, marginBottom: 'var(--space-md)' }}>
                      "{rev.review_text}"
                    </p>

                    {/* Detected Aspects Badges */}
                    {rev.aspects && rev.aspects.length > 0 && (
                      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px', alignItems: 'center' }}>
                        <span style={{ fontSize: '0.8rem', color: 'var(--color-slate-500)', fontWeight: 600 }}>Mentioned aspects:</span>
                        {rev.aspects.map((asp) => (
                          <span 
                            key={asp.id}
                            className={`badge ${asp.sentiment === 'positive' ? 'badge-positive' : asp.sentiment === 'negative' ? 'badge-negative' : 'badge-neutral'}`}
                            style={{ fontSize: '0.78rem', padding: '3px 9px' }}
                          >
                            {asp.aspect}: {asp.sentiment}
                          </span>
                        ))}
                      </div>
                    )}
                  </article>
                );
              })}
            </div>
          )}
        </div>
      </section>

      {/* E. Alternative Destinations */}
      {alternatives.length > 0 && (
        <section style={{ backgroundColor: 'var(--color-sand-50)', padding: 'var(--space-3xl) 0', borderTop: '1px solid var(--color-sand-200)' }}>
          <div className="app-container">
            <div style={{ marginBottom: 'var(--space-xl)' }}>
              <span style={{ fontSize: '0.8rem', textTransform: 'uppercase', letterSpacing: '0.08em', color: 'var(--color-terracotta)', fontWeight: 700 }}>
                Explore Similar Places
              </span>
              <h2 style={{ fontSize: '1.6rem', marginTop: '4px', marginBottom: '6px' }}>
                Alternative Destinations You Might Like
              </h2>
              <p style={{ fontSize: '0.92rem', color: 'var(--color-slate-600)', margin: 0 }}>
                Curated alternatives based on travel style, regional proximity, and visitor experience:
              </p>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(290px, 1fr))', gap: 'var(--space-xl)' }}>
              {alternatives.map((alt) => {
                const altDaily = formatDailyBudgetInr(alt.indicative_daily_budget, alt.budget_tier);
                const reason = alt.category === destination.category
                  ? `Shares the same ${alt.category.toLowerCase()} travel focus`
                  : `Located in the ${alt.region || alt.country} travel circuit`;

                return (
                  <article key={alt.id} className="destination-card">
                    <div style={{ position: 'relative', height: '180px', overflow: 'hidden' }}>
                      <DestinationImage 
                        src={alt.image_url} 
                        alt={alt.name} 
                        category={alt.category} 
                        style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                      />
                      <span 
                        className="badge badge-category" 
                        style={{ position: 'absolute', bottom: '10px', left: '10px', backgroundColor: '#FFFFFF', color: 'var(--color-slate-900)', fontWeight: 600 }}
                      >
                        {alt.category}
                      </span>
                    </div>

                    <div style={{ padding: 'var(--space-lg)', display: 'flex', flexDirection: 'column', flex: 1 }}>
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline', marginBottom: '4px' }}>
                        <span style={{ fontSize: '0.78rem', color: 'var(--color-terracotta)', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                          {alt.state_or_region ? `${alt.state_or_region}, ${alt.country}` : alt.country}
                        </span>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '4px', color: 'var(--color-terracotta)' }}>
                          <Star size={14} fill="currentColor" />
                          <span style={{ fontWeight: 700, fontSize: '0.88rem', color: 'var(--color-slate-900)' }}>
                            {alt.average_rating ? Number(alt.average_rating).toFixed(1) : '4.5'}
                          </span>
                        </div>
                      </div>

                      <h3 style={{ fontSize: '1.25rem', marginBottom: '6px' }}>
                        <Link to={`/destinations/${alt.id}`} style={{ color: 'inherit', textDecoration: 'none' }}>
                          {alt.name}
                        </Link>
                      </h3>

                      <p style={{ fontSize: '0.82rem', color: 'var(--color-olive)', fontWeight: 600, marginBottom: 'var(--space-md)' }}>
                        ✓ {reason}
                      </p>

                      <div style={{ borderTop: '1px solid var(--color-sand-200)', paddingTop: '10px', marginBottom: 'var(--space-md)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', fontSize: '0.82rem' }}>
                        <span style={{ color: 'var(--color-slate-500)' }}>Est. Daily Budget:</span>
                        <strong style={{ color: 'var(--color-slate-900)' }}>{altDaily}</strong>
                      </div>

                      <div style={{ display: 'flex', gap: '8px', marginTop: 'auto' }}>
                        <Link 
                          to={`/destinations/${alt.id}`} 
                          className="btn btn-secondary" 
                          style={{ flex: 1, justifyContent: 'center', fontSize: '0.85rem', padding: '8px 12px' }}
                        >
                          View Guide
                        </Link>
                        <Link 
                          to={`/compare?destA=${destination.id}&destB=${alt.id}`} 
                          className="btn btn-ghost" 
                          style={{ fontSize: '0.85rem', padding: '8px 12px' }}
                          title="Compare with current place"
                        >
                          <Compass size={16} />
                        </Link>
                      </div>
                    </div>
                  </article>
                );
              })}
            </div>
          </div>
        </section>
      )}

      {/* F. Next Steps Call to Action */}
      <section style={{ padding: 'var(--space-3xl) 0', textAlign: 'center' }}>
        <div className="app-container" style={{ maxWidth: '640px' }}>
          <h2 style={{ fontSize: '1.8rem', marginBottom: '8px' }}>Like what you see in {destination.name}?</h2>
          <p style={{ fontSize: '1.02rem', color: 'var(--color-slate-600)', marginBottom: 'var(--space-xl)' }}>
            Save it to your shortlist, compare it against other places, or create a personalized trip plan.
          </p>
          <div style={{ display: 'flex', justifyContent: 'center', gap: '14px', flexWrap: 'wrap' }}>
            <button
              onClick={handleToggleSave}
              disabled={saveLoading}
              className={isSaved ? "btn btn-primary" : "btn btn-secondary"}
              style={{ padding: '12px 24px', fontSize: '0.95rem' }}
            >
              {isSaved ? "Saved in Shortlist" : "Save to Shortlist"}
            </button>
            <Link to={`/compare?destA=${destination.id}`} className="btn btn-secondary" style={{ padding: '12px 24px', fontSize: '0.95rem' }}>
              <span>Compare with Another Destination</span>
            </Link>
            <Link to="/plan" className="btn btn-primary" style={{ padding: '12px 24px', fontSize: '0.95rem' }}>
              <span>Plan a Trip</span>
            </Link>
          </div>
        </div>
      </section>

      {/* Report Issue Modal */}
      {showReportModal && (
        <div 
          role="dialog"
          aria-modal="true"
          style={{
            position: 'fixed',
            inset: 0,
            backgroundColor: 'rgba(15, 23, 42, 0.65)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            padding: '20px',
            zIndex: 1000
          }}
        >
          <div 
            style={{
              backgroundColor: '#FFFFFF',
              borderRadius: 'var(--radius-lg)',
              maxWidth: '520px',
              width: '100%',
              padding: 'var(--space-2xl)',
              boxShadow: 'var(--shadow-card)',
              position: 'relative'
            }}
          >
            <button
              type="button"
              onClick={() => {
                setShowReportModal(false);
                setReportError(null);
              }}
              aria-label="Close dialog"
              style={{
                position: 'absolute',
                top: '16px',
                right: '16px',
                background: 'none',
                border: 'none',
                cursor: 'pointer',
                color: 'var(--color-slate-400)'
              }}
            >
              <X size={20} />
            </button>

            {reportSubmitted ? (
              <div style={{ textAlign: 'center', padding: 'var(--space-xl) 0' }}>
                <CheckCircle size={44} color="var(--color-olive)" style={{ marginBottom: '12px' }} />
                <h3 style={{ fontSize: '1.3rem', marginBottom: '8px' }}>Report Received</h3>
                <p style={{ fontSize: '0.95rem', color: 'var(--color-slate-600)', marginBottom: 'var(--space-xl)' }}>
                  Thank you for contributing to TRAVELENS data integrity. Our verification queue has recorded this report for <strong>{destination.name}</strong>.
                </p>
                <button
                  type="button"
                  onClick={() => {
                    setShowReportModal(false);
                    setReportSubmitted(false);
                    setReportComment('');
                    setReportEmail('');
                  }}
                  className="btn btn-primary"
                  style={{ padding: '8px 24px' }}
                >
                  Done
                </button>
              </div>
            ) : (
              <form onSubmit={handleSubmitReport}>
                <h3 style={{ fontSize: '1.3rem', marginBottom: '6px' }}>Report an Information Issue</h3>
                <p style={{ fontSize: '0.88rem', color: 'var(--color-slate-600)', marginBottom: 'var(--space-lg)' }}>
                  Help us keep data accurate for <strong>{destination.name}</strong>.
                </p>

                {reportError && (
                  <div style={{ backgroundColor: 'var(--color-crimson-light)', color: 'var(--color-crimson)', padding: '10px 14px', borderRadius: 'var(--radius-sm)', fontSize: '0.85rem', marginBottom: 'var(--space-md)' }}>
                    {reportError}
                  </div>
                )}

                <div style={{ marginBottom: 'var(--space-md)' }}>
                  <label htmlFor="report-category" style={{ fontSize: '0.85rem', fontWeight: 600, color: 'var(--color-slate-700)', display: 'block', marginBottom: '6px' }}>
                    Issue Type:
                  </label>
                  <select
                    id="report-category"
                    value={reportCategory}
                    onChange={(e) => setReportCategory(e.target.value)}
                    style={{ width: '100%', padding: '10px 12px', borderRadius: 'var(--radius-md)', border: '1px solid var(--color-sand-200)', fontSize: '0.9rem' }}
                  >
                    <option value="Outdated price or opening hours">Outdated price or opening hours</option>
                    <option value="Inaccurate attraction description">Inaccurate attraction or sight description</option>
                    <option value="Misrepresented aspect feedback">Misrepresented aspect feedback or sentiment</option>
                    <option value="Transit or location discrepancy">Transit or location discrepancy</option>
                    <option value="Broken image or link">Broken image or link</option>
                    <option value="Other data discrepancy">Other data discrepancy</option>
                  </select>
                </div>

                <div style={{ marginBottom: 'var(--space-md)' }}>
                  <label htmlFor="report-comment" style={{ fontSize: '0.85rem', fontWeight: 600, color: 'var(--color-slate-700)', display: 'block', marginBottom: '6px' }}>
                    Additional Details (Optional):
                  </label>
                  <textarea
                    id="report-comment"
                    rows={3}
                    maxLength={1000}
                    placeholder="Briefly describe what information is incorrect or needs updating..."
                    value={reportComment}
                    onChange={(e) => setReportComment(e.target.value)}
                    style={{ width: '100%', padding: '10px 12px', borderRadius: 'var(--radius-md)', border: '1px solid var(--color-sand-200)', fontSize: '0.9rem', fontFamily: 'var(--font-sans)', resize: 'vertical' }}
                  />
                </div>

                <div style={{ marginBottom: 'var(--space-lg)' }}>
                  <label htmlFor="report-email" style={{ fontSize: '0.85rem', fontWeight: 600, color: 'var(--color-slate-700)', display: 'block', marginBottom: '6px' }}>
                    Your Email (Optional, for verification updates):
                  </label>
                  <input
                    id="report-email"
                    type="email"
                    maxLength={255}
                    placeholder="you@example.com"
                    value={reportEmail}
                    onChange={(e) => setReportEmail(e.target.value)}
                    style={{ width: '100%', padding: '10px 12px', borderRadius: 'var(--radius-md)', border: '1px solid var(--color-sand-200)', fontSize: '0.9rem' }}
                  />
                </div>

                <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px' }}>
                  <button
                    type="button"
                    onClick={() => {
                      setShowReportModal(false);
                      setReportError(null);
                    }}
                    className="btn btn-secondary"
                    style={{ padding: '8px 18px', fontSize: '0.88rem' }}
                  >
                    Cancel
                  </button>
                  <button
                    type="submit"
                    disabled={reportSubmitting}
                    className="btn btn-primary"
                    style={{ padding: '8px 18px', fontSize: '0.88rem' }}
                  >
                    {reportSubmitting ? 'Submitting...' : 'Submit Report'}
                  </button>
                </div>
              </form>
            )}
          </div>
        </div>
      )}
    </main>
  );
}
