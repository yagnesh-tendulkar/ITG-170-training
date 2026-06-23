// ─────────────────────────────────────────────
// pages/HistoryPage.jsx
//
// LEARNING NOTE:
// This page shows all past reviews with:
//   - Pagination (skip/limit query params)
//   - Click to expand and view full details
//   - Delete with confirmation
// ─────────────────────────────────────────────

import { useState, useEffect } from 'react';
import { reviewsAPI } from '../api/client';
import { useToast } from '../context/ToastContext';
import ReviewCard from '../components/ReviewCard';
import ScoreRing from '../components/ScoreRing';
import LoadingSpinner from '../components/LoadingSpinner';

const PAGE_SIZE = 10;

function HistoryPage() {
  const [reviews, setReviews] = useState([]);
  const [selectedReview, setSelectedReview] = useState(null);
  const [loading, setLoading] = useState(true);
  const [detailLoading, setDetailLoading] = useState(false);
  const [page, setPage] = useState(0);
  const [hasMore, setHasMore] = useState(true);

  const { showToast } = useToast();

  // Fetch reviews when page changes
  useEffect(() => {
    setLoading(true);
    reviewsAPI.getHistory(page * PAGE_SIZE, PAGE_SIZE)
      .then((res) => {
        setReviews(res.data);
        setHasMore(res.data.length === PAGE_SIZE);
      })
      .catch(() => showToast('Failed to load history', 'error'))
      .finally(() => setLoading(false));
  }, [page]);

  const openReview = async (id) => {
    // If already open, close it
    if (selectedReview?.id === id) {
      setSelectedReview(null);
      return;
    }
    setDetailLoading(true);
    try {
      const res = await reviewsAPI.getById(id);
      setSelectedReview(res.data);
    } catch {
      showToast('Failed to load review details', 'error');
    } finally {
      setDetailLoading(false);
    }
  };

  const deleteReview = async (id, e) => {
    e.stopPropagation(); // Don't trigger openReview
    if (!window.confirm('Delete this review? This cannot be undone.')) return;

    try {
      await reviewsAPI.deleteById(id);
      setReviews((prev) => prev.filter((r) => r.id !== id));
      if (selectedReview?.id === id) setSelectedReview(null);
      showToast('Review deleted', 'info');
    } catch {
      showToast('Failed to delete review', 'error');
    }
  };

  if (loading) return <LoadingSpinner fullPage message="Loading review history..." />;

  return (
    <div className="page-container">
      <div className="page-header">
        <h1>📋 Review History</h1>
        <p>All your past code reviews. Click a row to view full details.</p>
      </div>

      {reviews.length === 0 ? (
        <div className="card">
          <div className="empty-state">
            <div className="empty-state-icon">📂</div>
            <h3>No reviews yet</h3>
            <p>Your code review history will appear here.</p>
          </div>
        </div>
      ) : (
        <>
          <div className="history-grid" style={{ marginBottom: '1rem' }}>
            {reviews.map((r) => (
              <div key={r.id}>
                {/* History Row */}
                <div
                  className="history-item"
                  onClick={() => openReview(r.id)}
                  role="button"
                  tabIndex={0}
                  style={{
                    borderColor: selectedReview?.id === r.id
                      ? 'var(--color-primary)'
                      : undefined,
                  }}
                >
                  <div>
                    <div className="history-item-title">{r.title}</div>
                    <div className="history-item-meta">
                      {new Date(r.created_at).toLocaleString()} ·{' '}
                      {r.bug_count} bug{r.bug_count !== 1 ? 's' : ''}
                    </div>
                  </div>
                  <span className="badge badge-info">{r.language}</span>
                  <ScoreRing score={Math.round(r.overall_score)} size={52} />
                  <button
                    className="btn btn-danger btn-sm"
                    onClick={(e) => deleteReview(r.id, e)}
                  >
                    🗑️
                  </button>
                </div>

                {/* Expanded Detail */}
                {selectedReview?.id === r.id && (
                  <div style={{ marginTop: '0.5rem' }}>
                    {detailLoading
                      ? <LoadingSpinner message="Loading review..." />
                      : <ReviewCard review={selectedReview} />
                    }
                  </div>
                )}
              </div>
            ))}
          </div>

          {/* Pagination */}
          <div style={{ display: 'flex', gap: '0.75rem', justifyContent: 'center' }}>
            <button
              className="btn btn-secondary"
              onClick={() => setPage((p) => Math.max(0, p - 1))}
              disabled={page === 0}
            >
              ← Previous
            </button>
            <span style={{
              display: 'flex',
              alignItems: 'center',
              color: 'var(--color-text-2)',
              fontSize: '0.875rem',
            }}>
              Page {page + 1}
            </span>
            <button
              className="btn btn-secondary"
              onClick={() => setPage((p) => p + 1)}
              disabled={!hasMore}
            >
              Next →
            </button>
          </div>
        </>
      )}
    </div>
  );
}

export default HistoryPage;
