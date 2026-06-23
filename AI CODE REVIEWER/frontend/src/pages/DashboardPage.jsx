// ─────────────────────────────────────────────
// pages/DashboardPage.jsx
//
// LEARNING NOTE:
// This page uses the useEffect hook to fetch data when the component mounts.
// Pattern:
//   1. useState holds the fetched data (starts as null/empty)
//   2. useEffect runs once on mount (empty dependency array [])
//   3. Inside useEffect, we call the API and set state
//   4. The component re-renders with the fetched data
// ─────────────────────────────────────────────

import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { reviewsAPI } from '../api/client';
import { useAuth } from '../context/AuthContext';
import ScoreRing from '../components/ScoreRing';
import LoadingSpinner from '../components/LoadingSpinner';

function StatCard({ icon, value, label }) {
  return (
    <div className="stat-card animate-fade-in-up">
      <div className="stat-icon">{icon}</div>
      <div className="stat-value">{value}</div>
      <div className="stat-label">{label}</div>
    </div>
  );
}

function DashboardPage() {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);

  const { user } = useAuth();
  const navigate = useNavigate();

  // Fetch dashboard data once on mount
  useEffect(() => {
    reviewsAPI.getDashboard()
      .then((res) => setStats(res.data))
      .catch((err) => console.error('Dashboard fetch error:', err))
      .finally(() => setLoading(false));
  }, []); // Empty array = run once on mount

  if (loading) return <LoadingSpinner fullPage message="Loading dashboard..." />;

  return (
    <div className="page-container">
      <div className="page-header">
        <h1>👋 Welcome back, {user?.username}!</h1>
        <p>Here's an overview of your code review activity.</p>
      </div>

      {/* Stats Grid */}
      <div className="stats-grid">
        <StatCard
          icon="📊"
          value={stats?.total_reviews ?? 0}
          label="Total Reviews"
        />
        <StatCard
          icon="⭐"
          value={`${stats?.average_score?.toFixed(1) ?? '0.0'}`}
          label="Avg Quality Score"
        />
        <StatCard
          icon="🐛"
          value={stats?.total_bugs_found ?? 0}
          label="Bugs Found"
        />
        <StatCard
          icon="💻"
          value={stats?.most_used_language ?? '—'}
          label="Top Language"
        />
      </div>

      {/* Quick Action */}
      <div style={{ marginBottom: '2rem' }}>
        <button
          className="btn btn-primary btn-lg"
          onClick={() => navigate('/review')}
        >
          🚀 Start New Review
        </button>
      </div>

      {/* Recent Reviews */}
      <div className="card">
        <div className="card-header">
          <span style={{ fontSize: '1.1rem' }}>🕐</span>
          <h3>Recent Reviews</h3>
        </div>

        {stats?.recent_reviews?.length > 0 ? (
          <div className="history-grid">
            {stats.recent_reviews.map((r) => (
              <div
                key={r.id}
                className="history-item animate-fade-in-up"
                onClick={() => navigate(`/history?open=${r.id}`)}
                role="button"
                tabIndex={0}
              >
                <div>
                  <div className="history-item-title">{r.title}</div>
                  <div className="history-item-meta">
                    {r.language} · {r.bug_count} bug{r.bug_count !== 1 ? 's' : ''} ·{' '}
                    {new Date(r.created_at).toLocaleDateString()}
                  </div>
                </div>
                <span className="badge badge-info">{r.language}</span>
                <ScoreRing score={Math.round(r.overall_score)} size={52} />
                <span style={{ color: 'var(--color-text-3)', fontSize: '1rem' }}>→</span>
              </div>
            ))}
          </div>
        ) : (
          <div className="empty-state">
            <div className="empty-state-icon">🔍</div>
            <h3>No reviews yet</h3>
            <p>Submit your first code review to see results here.</p>
            <button
              className="btn btn-primary"
              onClick={() => navigate('/review')}
            >
              Start your first review
            </button>
          </div>
        )}
      </div>
    </div>
  );
}

export default DashboardPage;
