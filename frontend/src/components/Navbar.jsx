import React, { useState, useEffect } from 'react';
import { Link, NavLink, useNavigate, useLocation } from 'react-router-dom';
import { Menu, X, User, LogOut } from 'lucide-react';
import { tokenStorage, getMe, logoutUser } from '../services/api';

export default function Navbar() {
  const [currentUser, setCurrentUser] = useState(null);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    let ignore = false;
    const token = tokenStorage.get();
    if (token) {
      getMe()
        .then((user) => {
          if (!ignore) setCurrentUser(user);
        })
        .catch(() => {
          if (!ignore) {
            tokenStorage.clear();
            setCurrentUser(null);
          }
        });
    } else {
      queueMicrotask(() => {
        if (!ignore) setCurrentUser((prev) => (prev ? null : prev));
      });
    }
    queueMicrotask(() => {
      if (!ignore) setMobileMenuOpen((prev) => (prev ? false : prev));
    });

    return () => {
      ignore = true;
    };
  }, [location.pathname]);

  const handleLogout = () => {
    logoutUser();
    setCurrentUser(null);
    navigate('/');
  };

  return (
    <header className="header-nav" role="banner">
      <div className="app-container header-inner">
        {/* Brand Logo */}
        <Link to="/" className="brand-logo" aria-label="TRAVELENS Home">
          <svg className="brand-logo-icon" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="16" cy="16" r="14" stroke="currentColor" strokeWidth="2" strokeDasharray="3 2" opacity="0.6"/>
            <circle cx="16" cy="16" r="9" stroke="currentColor" strokeWidth="2.2"/>
            <polygon points="16,4 19,16 16,13 13,16" fill="currentColor"/>
            <polygon points="16,28 13,16 16,19 19,16" fill="#192024" opacity="0.7"/>
          </svg>
          <span>TRAVELENS</span>
        </Link>

        {/* Primary Desktop Navigation (5 Consumer Items) */}
        <nav className="nav-links" aria-label="Main Navigation">
          <NavLink to="/" end className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}>
            Discover
          </NavLink>
          <NavLink to="/explore" className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}>
            Explore
          </NavLink>
          <NavLink to="/plan" className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}>
            Plan a Trip
          </NavLink>
          <NavLink to="/saved" className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}>
            Saved Places
          </NavLink>
        </nav>

        {/* Account / User Controls */}
        <div className="nav-actions">
          {currentUser ? (
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <Link 
                to="/profile" 
                className="btn btn-ghost" 
                style={{ padding: '6px 14px', fontSize: '0.9rem', display: 'flex', alignItems: 'center', gap: '8px' }}
                title="View My Account & Shortlist"
              >
                <div 
                  style={{
                    width: '24px',
                    height: '24px',
                    borderRadius: '50%',
                    backgroundColor: 'var(--color-terracotta)',
                    color: '#FFFFFF',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    fontSize: '0.75rem',
                    fontWeight: 700
                  }}
                >
                  {currentUser.name ? currentUser.name[0].toUpperCase() : 'U'}
                </div>
                <span style={{ fontWeight: 600 }}>{currentUser.name.split(' ')[0]}</span>
              </Link>
              <button 
                onClick={handleLogout} 
                className="btn btn-ghost" 
                title="Sign Out"
                style={{ padding: '6px 10px', fontSize: '0.85rem' }}
                aria-label="Sign Out"
              >
                <LogOut size={16} />
              </button>
            </div>
          ) : (
            <Link to="/login" className="btn btn-primary" style={{ padding: '8px 20px', fontSize: '0.9rem' }}>
              Sign In
            </Link>
          )}

          {/* Mobile Menu Button */}
          <button 
            type="button" 
            className="mobile-menu-btn" 
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            aria-label={mobileMenuOpen ? 'Close Menu' : 'Open Menu'}
            aria-expanded={mobileMenuOpen}
          >
            {mobileMenuOpen ? <X size={22} /> : <Menu size={22} />}
          </button>
        </div>
      </div>

      {/* Mobile Drawer Menu */}
      {mobileMenuOpen && (
        <div 
          className="mobile-drawer"
          style={{
            backgroundColor: 'var(--color-sand-50)',
            borderTop: '1px solid var(--color-sand-200)',
            padding: 'var(--space-lg) var(--space-md)',
            display: 'flex',
            flexDirection: 'column',
            gap: '8px'
          }}
        >
          <NavLink 
            to="/" 
            end 
            className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}
            style={{ padding: '10px 14px', fontSize: '1rem', borderRadius: 'var(--radius-sm)' }}
          >
            Discover
          </NavLink>
          <NavLink 
            to="/explore" 
            className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}
            style={{ padding: '10px 14px', fontSize: '1rem', borderRadius: 'var(--radius-sm)' }}
          >
            Explore
          </NavLink>
          <NavLink 
            to="/plan" 
            className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}
            style={{ padding: '10px 14px', fontSize: '1rem', borderRadius: 'var(--radius-sm)' }}
          >
            Plan a Trip
          </NavLink>
          <NavLink 
            to="/saved" 
            className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}
            style={{ padding: '10px 14px', fontSize: '1rem', borderRadius: 'var(--radius-sm)' }}
          >
            Saved Places
          </NavLink>

          <div style={{ borderTop: '1px solid var(--color-sand-200)', marginTop: '8px', paddingTop: '12px' }}>
            {currentUser ? (
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <Link to="/profile" style={{ display: 'flex', alignItems: 'center', gap: '8px', textDecoration: 'none', color: 'var(--color-slate-900)', fontWeight: 600 }}>
                  <User size={18} color="var(--color-terracotta)" />
                  <span>{currentUser.name}</span>
                </Link>
                <button onClick={handleLogout} className="btn btn-ghost" style={{ fontSize: '0.85rem' }}>
                  Sign Out
                </button>
              </div>
            ) : (
              <Link to="/login" className="btn btn-primary" style={{ width: '100%', textAlign: 'center', justifyContent: 'center' }}>
                Sign In
              </Link>
            )}
          </div>
        </div>
      )}
    </header>
  );
}
