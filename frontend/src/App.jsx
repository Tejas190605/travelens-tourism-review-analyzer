import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';

import Home from './pages/Home';
import Explore from './pages/Explore';
import DestinationDetails from './pages/DestinationDetails';
import Compare from './pages/Compare';
import Recommend from './pages/Recommend';
import Profile from './pages/Profile';
import About from './pages/About';
import Login from './pages/Login';

export default function App() {
  return (
    <BrowserRouter>
      <div style={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
        <Navbar />
        <div style={{ flex: 1 }}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/explore" element={<Explore />} />
            <Route path="/destinations" element={<Explore />} />
            <Route path="/destination/:id" element={<DestinationDetails />} />
            <Route path="/destinations/:id" element={<DestinationDetails />} />
            <Route path="/plan" element={<Recommend />} />
            <Route path="/recommend" element={<Recommend />} />
            <Route path="/compare" element={<Compare />} />
            <Route path="/saved" element={<Profile />} />
            <Route path="/profile" element={<Profile />} />
            <Route path="/account" element={<Profile />} />
            <Route path="/about" element={<About />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Login />} />
            {/* Redirect legacy /analyze route to /plan */}
            <Route path="/analyze" element={<Navigate to="/plan" replace />} />
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </div>
        <Footer />
      </div>
    </BrowserRouter>
  );
}
