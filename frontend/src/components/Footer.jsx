import React from 'react';
import { Link } from 'react-router-dom';

const CURRENT_YEAR = new Date().getFullYear();

export default function Footer() {
  return (
    <footer 
      style={{
        backgroundColor: 'var(--color-sand-100)',
        borderTop: '1px solid var(--color-sand-200)',
        padding: 'var(--space-3xl) 0 var(--space-xl)',
        marginTop: 'var(--space-3xl)',
        fontSize: '0.95rem'
      }}
    >
      <div className="app-container">
        <div 
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))',
            gap: 'var(--space-2xl)',
            marginBottom: 'var(--space-2xl)'
          }}
        >
          {/* Brand Col */}
          <div style={{ maxWidth: '320px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '12px' }}>
              <span style={{ fontFamily: 'var(--font-serif)', fontSize: '1.4rem', fontWeight: 700, color: 'var(--color-slate-900)' }}>
                TRAVELENS
              </span>
            </div>
            <p style={{ fontStyle: 'italic', fontSize: '1rem', color: 'var(--color-terracotta)', fontWeight: 600, marginBottom: '8px' }}>
              Find places worth travelling for.
            </p>
            <p style={{ fontSize: '0.92rem', color: 'var(--color-slate-600)', lineHeight: 1.6, margin: 0 }}>
              Discover destinations, understand what visiting them is really like from genuine traveller reviews, and plan realistic trips in Indian Rupees.
            </p>
          </div>

          {/* Quick Navigation Links */}
          <div>
            <h4 style={{ fontSize: '1rem', marginBottom: '14px', fontFamily: 'var(--font-sans)', color: 'var(--color-slate-900)', fontWeight: 600 }}>
              Travel Discovery
            </h4>
            <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '10px', padding: 0, margin: 0 }}>
              <li><Link to="/" style={{ color: 'var(--color-slate-600)', textDecoration: 'none' }}>Discover Home</Link></li>
              <li><Link to="/explore" style={{ color: 'var(--color-slate-600)', textDecoration: 'none' }}>Explore Destinations</Link></li>
              <li><Link to="/plan" style={{ color: 'var(--color-slate-600)', textDecoration: 'none' }}>Plan a Trip & Itinerary</Link></li>
              <li><Link to="/compare" style={{ color: 'var(--color-slate-600)', textDecoration: 'none' }}>Compare Destinations</Link></li>
              <li><Link to="/saved" style={{ color: 'var(--color-slate-600)', textDecoration: 'none' }}>Saved Places & Shortlist</Link></li>
              <li><Link to="/about" style={{ color: 'var(--color-slate-600)', textDecoration: 'none' }}>About TRAVELENS</Link></li>
            </ul>
          </div>

          {/* The 9 Tourism Aspects */}
          <div>
            <h4 style={{ fontSize: '1rem', marginBottom: '14px', fontFamily: 'var(--font-sans)', color: 'var(--color-slate-900)', fontWeight: 600 }}>
              What We Check in Every Review
            </h4>
            <p style={{ fontSize: '0.88rem', color: 'var(--color-slate-500)', marginBottom: '12px' }}>
              We evaluate 9 core travel dimensions to reveal honest strengths and caveats:
            </p>
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px' }}>
              {['Attractions', 'Food', 'Cleanliness', 'Price', 'Crowd', 'Safety', 'Transport', 'Accommodation', 'Hospitality'].map(asp => (
                <span 
                  key={asp} 
                  className="badge badge-category" 
                  style={{ fontSize: '0.78rem', padding: '4px 10px', backgroundColor: 'var(--color-white)', border: '1px solid var(--color-sand-200)' }}
                >
                  {asp}
                </span>
              ))}
            </div>
          </div>
        </div>

        {/* Footer Bottom */}
        <div 
          style={{
            borderTop: '1px solid var(--color-sand-200)',
            paddingTop: 'var(--space-md)',
            display: 'flex',
            flexWrap: 'wrap',
            justifyContent: 'space-between',
            alignItems: 'center',
            gap: '12px',
            color: 'var(--color-slate-500)',
            fontSize: '0.85rem'
          }}
        >
          <span>© {CURRENT_YEAR} TRAVELENS. Find places worth travelling for.</span>
          <span>Honest travel discovery based on authentic visitor reviews.</span>
        </div>
      </div>
    </footer>
  );
}
