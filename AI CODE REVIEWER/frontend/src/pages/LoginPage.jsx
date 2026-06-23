// ─────────────────────────────────────────────
// pages/LoginPage.jsx
//
// LEARNING NOTE:
// This demonstrates the core form pattern in React:
//   1. Controlled inputs: input value bound to state with useState
//   2. onChange handler: updates state as the user types
//   3. onSubmit: prevents default form submission, calls API
//   4. Error states: show validation/server errors
//   5. Loading state: disable button while request is in flight
// ─────────────────────────────────────────────

import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { authAPI } from '../api/client';
import { useAuth } from '../context/AuthContext';
import { useToast } from '../context/ToastContext';

function LoginPage() {
  // Form state (controlled inputs)
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  // UI state
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const { login } = useAuth();
  const { showToast } = useToast();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault(); // Prevent browser from reloading the page
    setError('');
    setLoading(true);

    try {
      const res = await authAPI.login({ email, password });
      login(res.data);          // Save token + user to context
      showToast('Welcome back! 👋', 'success');
      navigate('/dashboard');   // Redirect to dashboard
    } catch (err) {
      // Extract error message from API response, or use a fallback
      const msg = err.response?.data?.detail || 'Login failed. Please try again.';
      setError(msg);
    } finally {
      setLoading(false); // Always re-enable the button
    }
  };

  return (
    <div className="auth-page">
      <div className="auth-card card animate-fade-in-up">
        {/* Logo */}
        <div className="auth-logo">
          <div className="auth-logo-icon">🤖</div>
          <h1>CodeReview AI</h1>
          <p>Sign in to your account</p>
        </div>

        {/* Error message */}
        {error && (
          <div style={{
            background: 'rgba(239,68,68,0.1)',
            border: '1px solid rgba(239,68,68,0.3)',
            borderRadius: 'var(--radius-sm)',
            padding: '0.75rem 1rem',
            marginBottom: '1rem',
            color: 'var(--color-error)',
            fontSize: '0.875rem',
          }}>
            ❌ {error}
          </div>
        )}

        {/* Login Form */}
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label className="form-label" htmlFor="email">Email Address</label>
            <input
              id="email"
              type="email"
              className="form-input"
              placeholder="you@example.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              autoFocus
            />
          </div>

          <div className="form-group">
            <label className="form-label" htmlFor="password">Password</label>
            <input
              id="password"
              type="password"
              className="form-input"
              placeholder="••••••••"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>

          <button
            type="submit"
            className="btn btn-primary btn-lg"
            disabled={loading}
            style={{ width: '100%', marginTop: '0.5rem' }}
          >
            {loading ? 'Signing in...' : 'Sign In →'}
          </button>
        </form>

        <div className="auth-footer">
          Don't have an account?{' '}
          <Link to="/register">Create one for free</Link>
        </div>
      </div>
    </div>
  );
}

export default LoginPage;
