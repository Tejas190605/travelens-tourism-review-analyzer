import React from 'react';
import { Link } from 'react-router-dom';
import { ShieldCheck, Sparkles, ArrowRight, Eye } from 'lucide-react';

export default function About() {
  return (
    <main style={{ padding: 'var(--space-2xl) 0 var(--space-4xl)' }}>
      <div className="app-container" style={{ maxWidth: '960px' }}>
        {/* Brand Header */}
        <header style={{ marginBottom: 'var(--space-3xl)', textAlign: 'center' }}>
          <span style={{ textTransform: 'uppercase', fontSize: '0.82rem', letterSpacing: '0.12em', color: 'var(--color-terracotta)', fontWeight: 700 }}>
            Our Mission & Philosophy
          </span>
          <h1 style={{ marginTop: '8px', marginBottom: '12px', fontSize: 'clamp(2.2rem, 4vw, 3rem)' }}>
            About TRAVELENS
          </h1>
          <p style={{ fontStyle: 'italic', fontSize: '1.25rem', color: 'var(--color-terracotta)', marginBottom: '12px', fontFamily: 'var(--font-serif)' }}>
            "Find places worth travelling for."
          </p>
          <p style={{ maxWidth: '720px', margin: '0 auto', fontSize: '1.1rem', color: 'var(--color-slate-600)', lineHeight: 1.65 }}>
            Discover destinations, understand what visiting them is really like from genuine traveller reviews, compare your options, and plan a trip that truly suits you.
          </p>
        </header>

        {/* 1. Why We Built TRAVELENS */}
        <section 
          style={{
            backgroundColor: 'var(--color-white)',
            padding: 'var(--space-2xl)',
            borderRadius: 'var(--radius-lg)',
            border: '1px solid var(--color-sand-200)',
            marginBottom: 'var(--space-2xl)',
            boxShadow: 'var(--shadow-card)',
            lineHeight: 1.7
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '16px' }}>
            <Eye size={24} color="var(--color-terracotta)" />
            <h2 style={{ fontSize: '1.5rem', margin: 0 }}>The Problem with Traditional Travel Ratings</h2>
          </div>
          <p style={{ fontSize: '1.02rem', color: 'var(--color-slate-700)', marginBottom: '14px' }}>
            Planning a trip usually forces travellers to sift through hundreds of conflicting online reviews. A single 4.2-star rating often conceals critical drawbacks: a destination might boast majestic heritage monuments, but suffer from chaotic local transport, aggressive taxi overcharging, or unmaintained public sanitation.
          </p>
          <p style={{ fontSize: '1.02rem', color: 'var(--color-slate-700)', margin: 0 }}>
            <strong>TRAVELENS</strong> was created to solve this confusion. We look beneath superficial star ratings by analysing what travellers actually say across nine specific travel dimensions. We show you both sides of every destination—the highlights visitors loved, and the caveats to watch out for—so you can make informed decisions before booking.
          </p>
        </section>

        {/* 2. The 9 Travel Dimensions We Examine */}
        <section 
          style={{
            backgroundColor: 'var(--color-white)',
            padding: 'var(--space-2xl)',
            borderRadius: 'var(--radius-lg)',
            border: '1px solid var(--color-sand-200)',
            marginBottom: 'var(--space-2xl)',
            boxShadow: 'var(--shadow-card)'
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '8px' }}>
            <Sparkles size={24} color="var(--color-terracotta)" />
            <h2 style={{ fontSize: '1.5rem', margin: 0 }}>The 9 Dimensions of Every Trip</h2>
          </div>
          <p style={{ fontSize: '0.98rem', color: 'var(--color-slate-600)', marginBottom: 'var(--space-xl)' }}>
            Every destination in our catalogue is evaluated across these fundamental aspects of travel:
          </p>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))', gap: '14px' }}>
            {[
              ['Attractions', 'Iconic sights, monuments, natural landscapes, viewpoints, and museums.'],
              ['Food & Dining', 'Authentic regional dishes, street food quality, cafes, and restaurant variety.'],
              ['Cleanliness', 'Street maintenance, beach hygiene, public facilities, and hotel cleanliness.'],
              ['Price & Value', 'Affordability, reasonable entry fees, fair dining rates, and value for money.'],
              ['Crowd & Pacing', 'Queue lengths, tourist congestion, serenity, and off-peak comfort.'],
              ['Safety', 'Night walks, street illumination, safe transit, and security for solo travellers.'],
              ['Transport & Transit', 'Walkability, metro access, reliable local cabs, and airport connectivity.'],
              ['Accommodation', 'Quality of stays, comfortable bedding, noise isolation, and hospitality.'],
              ['Hospitality & Welcome', 'Warmth of locals, helpful guides, courteous staff, and communication ease.']
            ].map(([title, desc]) => (
              <div 
                key={title} 
                style={{ 
                  padding: '16px', 
                  backgroundColor: 'var(--color-sand-50)', 
                  borderRadius: 'var(--radius-md)', 
                  border: '1px solid var(--color-sand-200)' 
                }}
              >
                <span style={{ fontWeight: 700, color: 'var(--color-slate-900)', display: 'block', marginBottom: '4px', fontSize: '1rem' }}>
                  {title}
                </span>
                <span style={{ fontSize: '0.88rem', color: 'var(--color-slate-600)', lineHeight: 1.5, display: 'block' }}>
                  {desc}
                </span>
              </div>
            ))}
          </div>
        </section>

        {/* 3. Our Consumer Principles */}
        <section 
          style={{
            backgroundColor: 'var(--color-white)',
            padding: 'var(--space-2xl)',
            borderRadius: 'var(--radius-lg)',
            border: '1px solid var(--color-sand-200)',
            marginBottom: 'var(--space-2xl)',
            boxShadow: 'var(--shadow-card)'
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '16px' }}>
            <ShieldCheck size={24} color="var(--color-olive)" />
            <h2 style={{ fontSize: '1.5rem', margin: 0 }}>Our Editorial Principles</h2>
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: 'var(--space-lg)' }}>
            <div>
              <h3 style={{ fontSize: '1.1rem', marginBottom: '6px', color: 'var(--color-slate-900)' }}>100% Independent</h3>
              <p style={{ fontSize: '0.92rem', color: 'var(--color-slate-600)', lineHeight: 1.55 }}>
                We do not sell sponsored destination ranks or take payments to conceal negative feedback. What you see reflects genuine visitor consensus.
              </p>
            </div>

            <div>
              <h3 style={{ fontSize: '1.1rem', marginBottom: '6px', color: 'var(--color-slate-900)' }}>Both Sides of the Story</h3>
              <p style={{ fontSize: '0.92rem', color: 'var(--color-slate-600)', lineHeight: 1.55 }}>
                Every destination page clearly highlights what travellers appreciated alongside recurring bottlenecks or challenges to watch out for.
              </p>
            </div>

            <div>
              <h3 style={{ fontSize: '1.1rem', marginBottom: '6px', color: 'var(--color-slate-900)' }}>Transparent INR Budgets</h3>
              <p style={{ fontSize: '0.92rem', color: 'var(--color-slate-600)', lineHeight: 1.55 }}>
                Prices are shown exclusively in Indian Rupees (₹) with clear daily rates and mathematically sound trip calculators to prevent budget surprises.
              </p>
            </div>

            <div>
              <h3 style={{ fontSize: '1.1rem', marginBottom: '6px', color: 'var(--color-slate-900)' }}>Honest Sample Limits</h3>
              <p style={{ fontSize: '0.92rem', color: 'var(--color-slate-600)', lineHeight: 1.55 }}>
                If there are not enough reviews to establish a reliable score for a dimension, we tell you openly rather than fabricating a score.
              </p>
            </div>
          </div>
        </section>

        {/* CTA Banner */}
        <section 
          style={{ 
            backgroundColor: 'var(--color-sand-100)', 
            padding: 'var(--space-2xl)', 
            borderRadius: 'var(--radius-lg)', 
            border: '1px solid var(--color-sand-200)',
            textAlign: 'center'
          }}
        >
          <h2 style={{ fontSize: '1.6rem', marginBottom: '8px' }}>Ready to discover your next trip?</h2>
          <p style={{ fontSize: '1rem', color: 'var(--color-slate-600)', maxWidth: '540px', margin: '0 auto 20px' }}>
            Explore 50+ curated destinations with verified review insights, daily INR budgets, and practical itineraries.
          </p>
          <div style={{ display: 'flex', justifyContent: 'center', gap: '14px', flexWrap: 'wrap' }}>
            <Link to="/explore" className="btn btn-primary" style={{ padding: '12px 26px', fontSize: '1rem' }}>
              <span>Explore Destinations</span>
              <ArrowRight size={18} />
            </Link>
            <Link to="/plan" className="btn btn-secondary" style={{ padding: '12px 24px', fontSize: '1rem' }}>
              <span>Plan a Trip</span>
            </Link>
          </div>
        </section>
      </div>
    </main>
  );
}
