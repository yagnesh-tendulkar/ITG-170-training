// ─────────────────────────────────────────────
// pages/ReviewPage.jsx
//
// LEARNING NOTE:
// This is the main feature page. Key patterns:
//   - useState for form fields and results
//   - async/await for API calls
//   - Conditional rendering: show form OR results based on state
//   - Language selection as pill buttons (not a dropdown)
// ─────────────────────────────────────────────

import { useState } from 'react';
import { reviewsAPI } from '../api/client';
import { useToast } from '../context/ToastContext';
import ReviewCard from '../components/ReviewCard';
import LoadingSpinner from '../components/LoadingSpinner';

const LANGUAGES = [
  'Python', 'JavaScript', 'TypeScript', 'Java', 'C++', 'C#',
  'Go', 'Rust', 'PHP', 'Ruby', 'Swift', 'Kotlin',
];

const EXAMPLE_CODE = `def calculate_discount(price, discount):
    # Apply discount to price
    result = price - (price * discount / 100)
    data = []
    for i in range(100):
        data.append(i * 2)
    return result`;

function ReviewPage() {
  const [form, setForm] = useState({
    title: '',
    language: 'Python',
    code_snippet: EXAMPLE_CODE,
  });
  const [review, setReview] = useState(null);
  const [loading, setLoading] = useState(false);

  const { showToast } = useToast();

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (form.code_snippet.trim().length < 10) {
      showToast('Please enter some code to review (min 10 characters)', 'error');
      return;
    }

    setLoading(true);
    setReview(null);

    try {
      const res = await reviewsAPI.analyze(form);
      setReview(res.data);
      showToast('Review complete! 🎉', 'success');
      // Scroll to results
      setTimeout(() => {
        document.getElementById('review-results')?.scrollIntoView({ behavior: 'smooth' });
      }, 100);
    } catch (err) {
      const msg = err.response?.data?.detail || 'Review failed. Is the backend running?';
      showToast(msg, 'error');
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setReview(null);
    setForm((prev) => ({ ...prev, title: '', code_snippet: '' }));
  };

  return (
    <div className="page-container">
      <div className="page-header">
        <h1>🔍 New Code Review</h1>
        <p>Paste your code below and let AI analyze it for bugs, optimizations, and best practices.</p>
      </div>

      {/* Review Form */}
      <div className="card">
        <form onSubmit={handleSubmit}>
          {/* Title */}
          <div className="form-group">
            <label className="form-label" htmlFor="review-title">
              Review Title
            </label>
            <input
              id="review-title"
              type="text"
              className="form-input"
              placeholder="e.g. User authentication function"
              value={form.title}
              onChange={(e) => setForm((p) => ({ ...p, title: e.target.value }))}
              required
            />
          </div>

          {/* Language Selection */}
          <div className="form-group">
            <label className="form-label">Programming Language</label>
            <div className="lang-grid">
              {LANGUAGES.map((lang) => (
                <button
                  key={lang}
                  type="button"
                  className={`lang-pill${form.language === lang ? ' selected' : ''}`}
                  onClick={() => setForm((p) => ({ ...p, language: lang }))}
                >
                  {lang}
                </button>
              ))}
            </div>
          </div>

          {/* Code Input */}
          <div className="form-group">
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.4rem' }}>
              <label className="form-label" style={{ margin: 0 }} htmlFor="code-input">
                Code Snippet
              </label>
              <span style={{ fontSize: '0.75rem', color: 'var(--color-text-3)' }}>
                {form.code_snippet.length} characters
              </span>
            </div>
            <textarea
              id="code-input"
              className="form-textarea code-textarea"
              placeholder="Paste your code here..."
              value={form.code_snippet}
              onChange={(e) => setForm((p) => ({ ...p, code_snippet: e.target.value }))}
              rows={14}
              spellCheck={false}
            />
          </div>

          {/* Buttons */}
          <div style={{ display: 'flex', gap: '0.75rem' }}>
            <button
              type="submit"
              className="btn btn-primary btn-lg"
              disabled={loading}
            >
              {loading ? '🔄 Analyzing...' : '🚀 Analyze Code'}
            </button>
            {review && (
              <button type="button" className="btn btn-secondary" onClick={handleReset}>
                New Review
              </button>
            )}
          </div>
        </form>
      </div>

      {/* Loading State */}
      {loading && (
        <div className="card" style={{ marginTop: '1.5rem' }}>
          <LoadingSpinner message="AI is reviewing your code... this takes a few seconds ✨" />
        </div>
      )}

      {/* Results */}
      {review && !loading && (
        <div id="review-results">
          <ReviewCard review={review} />
        </div>
      )}
    </div>
  );
}

export default ReviewPage;
