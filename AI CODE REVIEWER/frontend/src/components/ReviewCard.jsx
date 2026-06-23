// ─────────────────────────────────────────────
// components/ReviewCard.jsx
//
// LEARNING NOTE:
// This component displays the AI review results in a tabbed UI.
// Key patterns demonstrated:
//   - useState for tracking the active tab
//   - Conditional rendering based on active tab
//   - Rendering arrays with .map()
//   - Props destructuring
// ─────────────────────────────────────────────

import { useState } from 'react';
import ScoreRing from './ScoreRing';

// Severity badge renders different colors depending on level
function SeverityBadge({ level }) {
  const normalized = level?.toLowerCase() || 'medium';
  return <span className={`badge badge-${normalized}`}>{normalized}</span>;
}

// Single bug item in the list
function BugItem({ bug, index }) {
  return (
    <div className="review-item animate-fade-in-up">
      <span className="review-item-icon">🐛</span>
      <div className="review-item-body">
        <p className="review-item-desc">{bug.description}</p>
        <div className="review-item-meta">
          <SeverityBadge level={bug.severity} />
          {bug.line_hint && (
            <span style={{ fontSize: '0.75rem', color: 'var(--color-text-3)' }}>
              📍 {bug.line_hint}
            </span>
          )}
        </div>
      </div>
    </div>
  );
}

// Single optimization suggestion
function OptimizationItem({ opt }) {
  return (
    <div className="review-item animate-fade-in-up">
      <span className="review-item-icon">⚡</span>
      <div className="review-item-body">
        <p className="review-item-desc">{opt.description}</p>
        <div className="review-item-meta">
          <span className={`badge badge-${opt.impact?.toLowerCase() || 'medium'}`}>
            {opt.impact || 'medium'} impact
          </span>
        </div>
      </div>
    </div>
  );
}

// Single best practice suggestion
function BestPracticeItem({ practice }) {
  return (
    <div className="review-item animate-fade-in-up">
      <span className="review-item-icon">✨</span>
      <div className="review-item-body">
        <p className="review-item-desc">{practice.description}</p>
        <div className="review-item-meta">
          <span className="badge badge-info">{practice.category}</span>
        </div>
      </div>
    </div>
  );
}

// Empty state when a tab has no items
function EmptyTab({ label }) {
  return (
    <div className="empty-state" style={{ padding: '2rem' }}>
      <div className="empty-state-icon">🎉</div>
      <h3>No {label} found!</h3>
      <p>The AI didn't detect any {label.toLowerCase()} in your code.</p>
    </div>
  );
}

// ── Main ReviewCard Component ──────────────────

function ReviewCard({ review }) {
  const [activeTab, setActiveTab] = useState('bugs');

  const tabs = [
    { id: 'bugs',          label: '🐛 Bugs',           count: review.bugs?.length || 0 },
    { id: 'optimizations', label: '⚡ Optimizations',  count: review.optimizations?.length || 0 },
    { id: 'best_practices',label: '✨ Best Practices',  count: review.best_practices?.length || 0 },
    { id: 'summary',       label: '📝 Summary',         count: null },
  ];

  return (
    <div className="card" style={{ marginTop: '1.5rem' }}>
      {/* Header: title + score ring */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '1.25rem' }}>
        <div>
          <h2 style={{ marginBottom: '0.25rem' }}>{review.title}</h2>
          <div style={{ display: 'flex', gap: '0.5rem', alignItems: 'center' }}>
            <span className="badge badge-info">{review.language}</span>
            <span style={{ fontSize: '0.78rem', color: 'var(--color-text-3)' }}>
              {new Date(review.created_at).toLocaleString()}
            </span>
          </div>
        </div>
        <ScoreRing score={Math.round(review.overall_score)} />
      </div>

      {/* Tabs */}
      <div className="tabs">
        {tabs.map((tab) => (
          <button
            key={tab.id}
            className={`tab-btn${activeTab === tab.id ? ' active' : ''}`}
            onClick={() => setActiveTab(tab.id)}
          >
            {tab.label}
            {tab.count !== null && (
              <span className="tab-count">{tab.count}</span>
            )}
          </button>
        ))}
      </div>

      {/* Tab Content */}
      <div>
        {activeTab === 'bugs' && (
          review.bugs?.length > 0
            ? review.bugs.map((bug, i) => <BugItem key={i} bug={bug} index={i} />)
            : <EmptyTab label="Bugs" />
        )}

        {activeTab === 'optimizations' && (
          review.optimizations?.length > 0
            ? review.optimizations.map((opt, i) => <OptimizationItem key={i} opt={opt} />)
            : <EmptyTab label="Optimizations" />
        )}

        {activeTab === 'best_practices' && (
          review.best_practices?.length > 0
            ? review.best_practices.map((p, i) => <BestPracticeItem key={i} practice={p} />)
            : <EmptyTab label="Best Practice suggestions" />
        )}

        {activeTab === 'summary' && (
          <div style={{
            background: 'var(--color-surface-2)',
            border: '1px solid var(--color-border)',
            borderRadius: 'var(--radius-md)',
            padding: '1.25rem',
            lineHeight: '1.7',
          }}>
            <p style={{ color: 'var(--color-text)', fontSize: '0.9rem' }}>
              {review.summary || 'No summary available.'}
            </p>
          </div>
        )}
      </div>
    </div>
  );
}

export default ReviewCard;
