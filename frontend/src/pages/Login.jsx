import React, { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { Lock, Mail, User, AlertCircle } from 'lucide-react';
import { loginUser, registerUser } from '../services/api';

export default function Login() {
  const [isRegister, setIsRegister] = useState(false);
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const navigate = useNavigate();
  const location = useLocation();

  // If navigated from somewhere with state
  const from = location.state?.from?.pathname || '/saved';

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);

    if (isRegister && name.trim().length < 2) {
      setError('Please provide your full name.');
      return;
    }
    if (!email || !password) {
      setError('Please fill in all required fields.');
      return;
    }
    if (password.length < 6) {
      setError('Password must contain at least 6 characters.');
      return;
    }

    setLoading(true);
    try {
      if (isRegister) {
        await registerUser(name.trim(), email.trim(), password);
      } else {
        await loginUser(email.trim(), password);
      }
      setLoading(false);
      navigate(from, { replace: true });
      window.location.reload(); // Refresh session state across Navbar
    } catch (err) {
      setError(err.message || 'Authentication failed. Please verify credentials.');
      setLoading(false);
    }
  };

  const handleDemoFill = () => {
    setEmail('traveler@travelens.com');
    setPassword('userpassword123');
    setIsRegister(false);
    setError(null);
  };

  return (
    <main style={{ padding: 'var(--space-4xl) 0' }}>
      <div className="app-container" style={{ maxWidth: '440px' }}>
        <div 
          style={{
            backgroundColor: 'var(--color-white)',
            padding: 'var(--space-3xl) var(--space-2xl)',
            borderRadius: 'var(--radius-lg)',
            border: '1px solid var(--color-sand-200)',
            boxShadow: 'var(--shadow-card)'
          }}
        >
          {/* Header */}
          <div style={{ textAlign: 'center', marginBottom: 'var(--space-xl)' }}>
            <span style={{ fontFamily: 'var(--font-serif)', fontSize: '1.4rem', fontWeight: 700, color: 'var(--color-slate-900)' }}>
              TRAVELENS
            </span>
            <h1 style={{ fontSize: '1.65rem', marginTop: '6px', marginBottom: '6px' }}>
              {isRegister ? 'Create an Account' : 'Welcome Back'}
            </h1>
            <p style={{ fontSize: '0.92rem', color: 'var(--color-slate-500)', margin: 0 }}>
              {isRegister ? 'Join TRAVELENS to shortlist places and plan your trips.' : 'Sign in to access your saved places and travel plans.'}
            </p>
          </div>

          {/* Error Message */}
          {error && (
            <div 
              style={{
                backgroundColor: 'var(--color-crimson-light)',
                color: 'var(--color-crimson)',
                padding: '10px 14px',
                borderRadius: 'var(--radius-sm)',
                marginBottom: 'var(--space-lg)',
                fontSize: '0.88rem',
                display: 'flex',
                alignItems: 'center',
                gap: '8px'
              }}
            >
              <AlertCircle size={16} style={{ flexShrink: 0 }} />
              <span>{error}</span>
            </div>
          )}

          {/* Form */}
          <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: 'var(--space-md)' }}>
            {isRegister && (
              <div>
                <label htmlFor="reg-name" style={{ display: 'block', fontSize: '0.88rem', fontWeight: 600, color: 'var(--color-slate-700)', marginBottom: '6px' }}>
                  Full Name
                </label>
                <div style={{ position: 'relative' }}>
                  <User size={18} color="var(--color-slate-400)" style={{ position: 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)' }} />
                  <input
                    id="reg-name"
                    type="text"
                    required
                    placeholder="e.g. Maya Sharma"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    style={{
                      width: '100%',
                      padding: '11px 12px 11px 40px',
                      borderRadius: 'var(--radius-md)',
                      border: '1px solid var(--color-sand-200)',
                      fontSize: '0.95rem',
                      fontFamily: 'var(--font-sans)',
                      color: 'var(--color-slate-900)',
                      backgroundColor: 'var(--color-sand-50)'
                    }}
                  />
                </div>
              </div>
            )}

            <div>
              <label htmlFor="auth-email" style={{ display: 'block', fontSize: '0.88rem', fontWeight: 600, color: 'var(--color-slate-700)', marginBottom: '6px' }}>
                Email Address
              </label>
              <div style={{ position: 'relative' }}>
                <Mail size={18} color="var(--color-slate-400)" style={{ position: 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)' }} />
                <input
                  id="auth-email"
                  type="email"
                  required
                  placeholder="name@example.com"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  style={{
                    width: '100%',
                    padding: '11px 12px 11px 40px',
                    borderRadius: 'var(--radius-md)',
                    border: '1px solid var(--color-sand-200)',
                    fontSize: '0.95rem',
                    fontFamily: 'var(--font-sans)',
                    color: 'var(--color-slate-900)',
                    backgroundColor: 'var(--color-sand-50)'
                  }}
                />
              </div>
            </div>

            <div>
              <label htmlFor="auth-password" style={{ display: 'block', fontSize: '0.88rem', fontWeight: 600, color: 'var(--color-slate-700)', marginBottom: '6px' }}>
                Password
              </label>
              <div style={{ position: 'relative' }}>
                <Lock size={18} color="var(--color-slate-400)" style={{ position: 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)' }} />
                <input
                  id="auth-password"
                  type="password"
                  required
                  placeholder="••••••••"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  style={{
                    width: '100%',
                    padding: '11px 12px 11px 40px',
                    borderRadius: 'var(--radius-md)',
                    border: '1px solid var(--color-sand-200)',
                    fontSize: '0.95rem',
                    fontFamily: 'var(--font-sans)',
                    color: 'var(--color-slate-900)',
                    backgroundColor: 'var(--color-sand-50)'
                  }}
                />
              </div>
            </div>

            <button
              type="submit"
              disabled={loading}
              className="btn btn-primary"
              style={{ width: '100%', padding: '12px', marginTop: 'var(--space-sm)', fontSize: '0.95rem' }}
            >
              {loading ? 'Signing in...' : isRegister ? 'Create Account' : 'Sign In'}
            </button>
          </form>

          {/* Friendly Demo Autofill */}
          <div style={{ marginTop: 'var(--space-lg)', padding: '10px 14px', backgroundColor: 'var(--color-sand-50)', borderRadius: 'var(--radius-md)', border: '1px solid var(--color-sand-200)', textAlign: 'center' }}>
            <span style={{ fontSize: '0.8rem', color: 'var(--color-slate-500)', display: 'block', marginBottom: '6px' }}>
              Want to test saving places quickly?
            </span>
            <button 
              type="button" 
              onClick={handleDemoFill} 
              style={{ background: 'none', border: 'none', color: 'var(--color-terracotta)', fontWeight: 600, fontSize: '0.85rem', cursor: 'pointer', textDecoration: 'underline' }}
            >
              Use demo traveller credentials
            </button>
          </div>

          {/* Toggle between Login and Register */}
          <div style={{ marginTop: 'var(--space-lg)', textAlign: 'center', fontSize: '0.88rem', color: 'var(--color-slate-600)' }}>
            {isRegister ? (
              <span>
                Already have an account?{' '}
                <button 
                  onClick={() => { setIsRegister(false); setError(null); }} 
                  style={{ background: 'none', border: 'none', color: 'var(--color-terracotta)', fontWeight: 600, cursor: 'pointer' }}
                >
                  Sign In
                </button>
              </span>
            ) : (
              <span>
                Don't have an account yet?{' '}
                <button 
                  onClick={() => { setIsRegister(true); setError(null); }} 
                  style={{ background: 'none', border: 'none', color: 'var(--color-terracotta)', fontWeight: 600, cursor: 'pointer' }}
                >
                  Register
                </button>
              </span>
            )}
          </div>
        </div>
      </div>
    </main>
  );
}
