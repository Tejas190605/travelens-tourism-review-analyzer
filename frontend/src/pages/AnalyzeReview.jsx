import React, { useState } from 'react';
import { Send, AlertCircle, Clock, SplitSquareVertical } from 'lucide-react';
import { analyzeReviewText } from '../services/api';

const EXAMPLE_REVIEWS = [
  {
    label: 'Positive Experience',
    title: 'Heritage & Great Hospitality',
    text: 'Visiting the ancient palaces and temples was an unforgettable journey. The architecture took our breath away, local food was delicious, and the tour guides showed extraordinary hospitality throughout our stay.'
  },
  {
    label: 'Mixed Experience',
    title: 'Majestic Sights but Severe Crowds',
    text: 'The Taj Mahal was absolutely breathtaking and majestic, but the surrounding streets were dirty, entry tickets were expensive, and the overwhelming queues tested our patience.'
  },
  {
    label: 'Negative Experience',
    title: 'Cleanliness & Taxi Overcharging',
    text: 'Extremely disappointed. Public restrooms lacked basic cleanliness, taxi drivers charged exorbitant fares without meters, and aggressive vendors constantly harassed tourists.'
  },
  {
    label: 'Nuanced / Moderate',
    title: 'Decent Transit & Standard Food',
    text: 'The historical monuments were decent and well maintained. Local bus transport was acceptable though slightly crowded. Food was average for the price charged.'
  }
];

export default function AnalyzeReview() {
  const [reviewText, setReviewText] = useState('');
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleAnalyze = async (e) => {
    if (e) e.preventDefault();
    if (!reviewText.trim()) return;

    setLoading(true);
    setError(null);

    try {
      const result = await analyzeReviewText(reviewText.trim());
      setAnalysis(result);
      setLoading(false);
    } catch (err) {
      setError(err.message || 'Analysis failed. Please ensure the backend server is running.');
      setLoading(false);
    }
  };

  const handleLoadSample = (sample) => {
    setReviewText(sample.text);
    setAnalysis(null);
    setError(null);
  };

  const getSentimentDetails = (sentiment) => {
    if (sentiment === 'positive') {
      return { badge: 'badge-positive', hex: 'var(--color-olive)', bg: 'var(--color-olive-light)', label: 'Positive' };
    }
    if (sentiment === 'negative') {
      return { badge: 'badge-negative', hex: 'var(--color-crimson)', bg: 'var(--color-crimson-light)', label: 'Negative' };
    }
    return { badge: 'badge-neutral', hex: 'var(--color-amber)', bg: 'var(--color-amber-light)', label: 'Neutral' };
  };

  return (
    <main style={{ padding: 'var(--space-2xl) 0 var(--space-4xl)' }}>
      <div className="app-container" style={{ maxWidth: '960px' }}>
        {/* Page Header */}
        <header style={{ marginBottom: 'var(--space-2xl)', textAlign: 'center' }}>
          <span style={{ textTransform: 'uppercase', fontSize: '0.8rem', letterSpacing: '0.12em', color: 'var(--color-terracotta)', fontWeight: 700 }}>
            Interactive Sentiment Engine
          </span>
          <h1 style={{ marginTop: '6px', marginBottom: '10px' }}>Try a Review</h1>
          <p style={{ maxWidth: '680px', margin: '0 auto', fontSize: '1.05rem', color: 'var(--color-slate-600)', lineHeight: 1.6 }}>
            Paste any traveller review to understand its overall sentiment, detected tourism aspects, and nuanced feedback breakdown.
          </p>
        </header>

        {/* Input Card */}
        <section 
          style={{
            backgroundColor: 'var(--color-white)',
            padding: 'var(--space-xl)',
            borderRadius: 'var(--radius-lg)',
            border: '1px solid var(--color-sand-200)',
            boxShadow: 'var(--shadow-card)',
            marginBottom: 'var(--space-2xl)'
          }}
        >
          {/* Example Reviews Selector */}
          <div style={{ marginBottom: 'var(--space-lg)' }}>
            <span style={{ fontSize: '0.85rem', color: 'var(--color-slate-700)', fontWeight: 700, display: 'block', marginBottom: '10px' }}>
              Try an Example Review:
            </span>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(210px, 1fr))', gap: '10px' }}>
              {EXAMPLE_REVIEWS.map((sample, idx) => (
                <button
                  key={idx}
                  type="button"
                  onClick={() => handleLoadSample(sample)}
                  style={{
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'flex-start',
                    padding: '10px 14px',
                    borderRadius: 'var(--radius-md)',
                    border: '1px solid var(--color-sand-200)',
                    backgroundColor: 'var(--color-sand-50)',
                    cursor: 'pointer',
                    textAlign: 'left',
                    transition: 'all 0.15s ease'
                  }}
                  onMouseOver={(e) => { e.currentTarget.style.borderColor = 'var(--color-terracotta)'; }}
                  onMouseOut={(e) => { e.currentTarget.style.borderColor = 'var(--color-sand-200)'; }}
                >
                  <span style={{ fontSize: '0.75rem', color: 'var(--color-terracotta)', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                    {sample.label}
                  </span>
                  <span style={{ fontSize: '0.88rem', fontWeight: 600, color: 'var(--color-slate-900)', marginTop: '2px' }}>
                    {sample.title}
                  </span>
                </button>
              ))}
            </div>
          </div>

          <form onSubmit={handleAnalyze}>
            <div style={{ marginBottom: 'var(--space-md)' }}>
              <label htmlFor="review-textarea" style={{ fontSize: '0.9rem', color: 'var(--color-slate-700)', fontWeight: 600, display: 'block', marginBottom: '8px' }}>
                Review Text
              </label>
              <textarea
                id="review-textarea"
                rows={5}
                placeholder="Paste or write a traveller review here (e.g., 'The heritage monuments were spectacular, but the crowds and transport prices made the experience exhausting')..."
                value={reviewText}
                onChange={(e) => setReviewText(e.target.value)}
                style={{
                  width: '100%',
                  padding: '14px 16px',
                  borderRadius: 'var(--radius-md)',
                  border: '1px solid var(--color-sand-200)',
                  backgroundColor: 'var(--color-sand-50)',
                  fontSize: '1rem',
                  fontFamily: 'var(--font-sans)',
                  color: 'var(--color-slate-900)',
                  resize: 'vertical',
                  lineHeight: 1.6,
                  outline: 'none'
                }}
              />
            </div>

            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '12px' }}>
              <span style={{ fontSize: '0.82rem', color: 'var(--color-slate-500)' }}>
                {reviewText.length} characters
              </span>
              <button 
                type="submit" 
                disabled={loading || reviewText.trim().length < 5}
                className="btn btn-primary"
                style={{ padding: '12px 28px', display: 'inline-flex', alignItems: 'center', gap: '8px', fontSize: '0.95rem' }}
              >
                <span>{loading ? 'Analysing Review...' : 'Analyse Review'}</span>
                <Send size={16} />
              </button>
            </div>
          </form>
        </section>

        {/* Error Notification */}
        {error && (
          <div 
            style={{
              backgroundColor: 'var(--color-crimson-light)',
              color: 'var(--color-crimson)',
              padding: 'var(--space-md) var(--space-lg)',
              borderRadius: 'var(--radius-md)',
              marginBottom: 'var(--space-xl)',
              display: 'flex',
              alignItems: 'center',
              gap: '10px'
            }}
          >
            <AlertCircle size={20} />
            <span>{error}</span>
          </div>
        )}

        {/* Loading State */}
        {loading && (
          <div className="state-box" style={{ padding: 'var(--space-3xl) var(--space-xl)' }}>
            <div className="spinner"></div>
            <p style={{ marginTop: '16px', color: 'var(--color-slate-600)' }}>Extracting tourism aspects and calculating sentiment...</p>
          </div>
        )}

        {/* Analysis Results */}
        {analysis && !loading && (
          <section 
            style={{
              backgroundColor: 'var(--color-white)',
              borderRadius: 'var(--radius-lg)',
              border: '1px solid var(--color-sand-200)',
              boxShadow: 'var(--shadow-card)',
              overflow: 'hidden'
            }}
          >
            {/* Result Summary Bar */}
            <div 
              style={{
                backgroundColor: 'var(--color-sand-50)',
                padding: 'var(--space-xl)',
                borderBottom: '1px solid var(--color-sand-200)',
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center',
                flexWrap: 'wrap',
                gap: '16px'
              }}
            >
              <div>
                <span style={{ fontSize: '0.8rem', textTransform: 'uppercase', letterSpacing: '0.08em', color: 'var(--color-slate-500)', fontWeight: 700 }}>
                  Sentiment Detected in Review Text
                </span>
                <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginTop: '6px', flexWrap: 'wrap' }}>
                  <span 
                    className={`badge ${getSentimentDetails(analysis.sentiment).badge}`}
                    style={{ fontSize: '1.05rem', padding: '6px 16px', textTransform: 'capitalize', letterSpacing: '0.03em', fontWeight: 700 }}
                  >
                    {analysis.sentiment}
                  </span>
                  <span style={{ fontSize: '0.95rem', color: 'var(--color-slate-700)' }}>
                    Model Score: <strong>{analysis.confidence_band ? (analysis.confidence_band === 'Low' ? 'Low (indicative only)' : analysis.confidence_band) : (analysis.confidence >= 0.75 ? 'High' : analysis.confidence >= 0.55 ? 'Moderate' : 'Low (indicative only)')}</strong>
                  </span>
                  {analysis.is_mixed && (
                    <span className="badge" style={{ backgroundColor: '#FEF3C7', color: '#92400E', border: '1px solid #FDE68A', fontSize: '0.85rem', fontWeight: 600 }}>
                      Mixed Feedback Detected
                    </span>
                  )}
                </div>
                <span style={{ fontSize: '0.76rem', color: 'var(--color-slate-500)', display: 'block', marginTop: '6px' }}>
                  Indicative classification band (High ≥ 75%, Moderate 55–74%, Low &lt; 55%). Reflects model decision score, not absolute review fact.
                </span>
              </div>

              {analysis.latency_ms && (
                <div style={{ display: 'flex', alignItems: 'center', gap: '6px', color: 'var(--color-slate-500)', fontSize: '0.85rem' }}>
                  <Clock size={16} />
                  <span>Analysis Time: {analysis.latency_ms} ms</span>
                </div>
              )}
            </div>

            {/* How Each Part of the Review Is Interpreted (for Mixed / Compound reviews) */}
            {analysis.clause_analysis && analysis.clause_analysis.length > 0 && (
              <div style={{ padding: 'var(--space-xl)', borderBottom: '1px solid var(--color-sand-200)' }}>
                <h3 style={{ fontSize: '1.25rem', marginBottom: '8px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <SplitSquareVertical size={18} color="var(--color-terracotta)" />
                  How Each Part of the Review Is Interpreted
                </h3>
                <p style={{ fontSize: '0.9rem', color: 'var(--color-slate-600)', marginBottom: 'var(--space-lg)' }}>
                  Reviews combining praise and criticism are broken down into constituent clauses to assess contrasting aspects:
                </p>

                <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                  {analysis.clause_analysis.map((clause, idx) => {
                    const clColor = getSentimentDetails(clause.sentiment);
                    return (
                      <div 
                        key={idx}
                        style={{
                          display: 'flex',
                          justifyContent: 'space-between',
                          alignItems: 'center',
                          padding: '12px 16px',
                          borderRadius: 'var(--radius-md)',
                          backgroundColor: clColor.bg,
                          borderLeft: `4px solid ${clColor.hex}`,
                          gap: '12px',
                          flexWrap: 'wrap'
                        }}
                      >
                        <span style={{ fontStyle: 'italic', fontSize: '0.95rem', color: 'var(--color-slate-900)', flex: 1, minWidth: '240px' }}>
                          "{clause.clause_text}"
                        </span>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                          {clause.aspects && clause.aspects.map(asp => (
                            <span key={asp} className="badge badge-category" style={{ fontSize: '0.78rem' }}>
                              {asp}
                            </span>
                          ))}
                          <span className={`badge ${clColor.badge}`} style={{ textTransform: 'capitalize', fontSize: '0.82rem', fontWeight: 600 }}>
                            {clause.sentiment}
                          </span>
                        </div>
                      </div>
                    );
                  })}
                </div>
              </div>
            )}

            {/* Aspects Detected */}
            <div style={{ padding: 'var(--space-xl)' }}>
              <div style={{ marginBottom: 'var(--space-xl)' }}>
                <h3 style={{ fontSize: '1.25rem', marginBottom: '6px' }}>What Travellers Say About Specific Aspects</h3>
                <p style={{ fontSize: '0.9rem', color: 'var(--color-slate-600)', marginBottom: 'var(--space-md)' }}>
                  Tourism dimensions identified in this review mapped to our 9-aspect schema:
                </p>

                {analysis.detected_aspects && analysis.detected_aspects.length > 0 ? (
                  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: 'var(--space-md)' }}>
                    {analysis.detected_aspects.map((asp, idx) => {
                      const colorInfo = getSentimentDetails(asp.sentiment);
                      return (
                        <div 
                          key={idx}
                          style={{
                            padding: 'var(--space-md) var(--space-lg)',
                            borderRadius: 'var(--radius-md)',
                            border: '1px solid var(--color-sand-200)',
                            backgroundColor: 'var(--color-sand-50)'
                          }}
                        >
                          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
                            <span style={{ fontWeight: 700, color: 'var(--color-slate-900)' }}>{asp.aspect}</span>
                            <span className={`badge ${colorInfo.badge}`} style={{ textTransform: 'capitalize', fontSize: '0.8rem', fontWeight: 600 }}>
                              {asp.sentiment}
                            </span>
                          </div>
                          {asp.keywords && asp.keywords.length > 0 && (
                            <div style={{ fontSize: '0.8rem', color: 'var(--color-slate-500)', marginTop: '4px' }}>
                              Keywords: {asp.keywords.join(', ')}
                            </div>
                          )}
                        </div>
                      );
                    })}
                  </div>
                ) : (
                  <p style={{ color: 'var(--color-slate-500)', fontStyle: 'italic', fontSize: '0.92rem' }}>
                    No specific tourism aspects detected. The review discusses general experience without mentioning named attractions, food, prices, or transit.
                  </p>
                )}
              </div>

              {/* Class Probability Distribution */}
              {analysis.probabilities && (
                <div style={{ marginBottom: 'var(--space-lg)' }}>
                  <h3 style={{ fontSize: '1.15rem', marginBottom: '8px' }}>Model Sentiment Distribution</h3>
                  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(180px, 1fr))', gap: 'var(--space-md)' }}>
                    {Object.entries(analysis.probabilities).map(([cls, prob]) => {
                      const pct = (prob * 100).toFixed(1);
                      return (
                        <div key={cls} style={{ padding: '12px 16px', backgroundColor: 'var(--color-sand-50)', borderRadius: 'var(--radius-md)', border: '1px solid var(--color-sand-200)' }}>
                          <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.88rem', marginBottom: '6px' }}>
                            <span style={{ textTransform: 'capitalize', fontWeight: 600, color: 'var(--color-slate-800)' }}>{cls}</span>
                            <span style={{ fontWeight: 700, color: 'var(--color-slate-900)' }}>{pct}%</span>
                          </div>
                          <div style={{ height: '7px', backgroundColor: 'var(--color-sand-200)', borderRadius: '4px', overflow: 'hidden' }}>
                            <div style={{ width: `${pct}%`, height: '100%', backgroundColor: cls === 'positive' ? 'var(--color-olive)' : cls === 'negative' ? 'var(--color-crimson)' : 'var(--color-amber)' }} />
                          </div>
                        </div>
                      );
                    })}
                  </div>
                </div>
              )}
            </div>
          </section>
        )}
      </div>
    </main>
  );
}
