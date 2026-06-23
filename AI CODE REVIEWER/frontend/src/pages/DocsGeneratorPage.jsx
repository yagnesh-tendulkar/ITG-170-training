// ─────────────────────────────────────────────
// pages/DocsGeneratorPage.jsx
//
// Documentation generator — paste a function/class,
// choose a doc style, and get AI-generated docstrings.
// ─────────────────────────────────────────────

import { useState } from 'react';
import { docsAPI } from '../api/client';
import { useToast } from '../context/ToastContext';
import LoadingSpinner from '../components/LoadingSpinner';

const DOC_STYLES = [
  { value: 'google', label: 'Google Style (Python)' },
  { value: 'numpy',  label: 'NumPy Style (Python)' },
  { value: 'jsdoc',  label: 'JSDoc (JavaScript)' },
];

const EXAMPLE_CODE = `def calculate_compound_interest(principal, rate, time, n=12):
    amount = principal * (1 + rate / (n * 100)) ** (n * time)
    return round(amount - principal, 2)`;

function DocsGeneratorPage() {
  const [form, setForm] = useState({
    code: EXAMPLE_CODE,
    language: 'Python',
    doc_style: 'google',
  });
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [copied, setCopied] = useState(false);

  const { showToast } = useToast();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResult(null);

    try {
      const res = await docsAPI.generate(form);
      setResult(res.data);
      showToast('Documentation generated! 📝', 'success');
    } catch (err) {
      const msg = err.response?.data?.detail || 'Generation failed.';
      showToast(msg, 'error');
    } finally {
      setLoading(false);
    }
  };

  const copyToClipboard = async () => {
    try {
      await navigator.clipboard.writeText(result.documented_code);
      setCopied(true);
      showToast('Copied to clipboard!', 'success');
      setTimeout(() => setCopied(false), 2000);
    } catch {
      showToast('Copy failed', 'error');
    }
  };

  return (
    <div className="page-container">
      <div className="page-header">
        <h1>📝 Documentation Generator</h1>
        <p>Paste a function or class and get AI-generated docstrings instantly.</p>
      </div>

      <div style={{ display: 'grid', gap: '1.5rem', gridTemplateColumns: result ? '1fr 1fr' : '1fr' }}>
        {/* Input Card */}
        <div className="card">
          <form onSubmit={handleSubmit}>
            {/* Doc Style */}
            <div className="form-group">
              <label className="form-label">Documentation Style</label>
              <select
                className="form-select"
                value={form.doc_style}
                onChange={(e) => setForm((p) => ({ ...p, doc_style: e.target.value }))}
              >
                {DOC_STYLES.map((s) => (
                  <option key={s.value} value={s.value}>{s.label}</option>
                ))}
              </select>
            </div>

            {/* Language */}
            <div className="form-group">
              <label className="form-label">Language</label>
              <input
                type="text"
                className="form-input"
                value={form.language}
                onChange={(e) => setForm((p) => ({ ...p, language: e.target.value }))}
                placeholder="Python"
              />
            </div>

            {/* Code */}
            <div className="form-group">
              <label className="form-label" htmlFor="docs-code">Code</label>
              <textarea
                id="docs-code"
                className="form-textarea code-textarea"
                value={form.code}
                onChange={(e) => setForm((p) => ({ ...p, code: e.target.value }))}
                rows={10}
                spellCheck={false}
              />
            </div>

            <button type="submit" className="btn btn-primary btn-lg" disabled={loading}>
              {loading ? '⏳ Generating...' : '✨ Generate Docs'}
            </button>
          </form>
        </div>

        {/* Output Card */}
        {(loading || result) && (
          <div className="card">
            <div className="card-header">
              <span>📄</span>
              <h3>Generated Documentation</h3>
              {result && (
                <button
                  className="btn btn-secondary btn-sm copy-btn"
                  style={{ position: 'static', marginLeft: 'auto' }}
                  onClick={copyToClipboard}
                >
                  {copied ? '✅ Copied!' : '📋 Copy'}
                </button>
              )}
            </div>

            {loading ? (
              <LoadingSpinner message="AI is generating documentation..." />
            ) : result ? (
              <>
                {result.explanation && (
                  <div style={{
                    background: 'rgba(99,102,241,0.08)',
                    border: '1px solid rgba(99,102,241,0.2)',
                    borderRadius: 'var(--radius-sm)',
                    padding: '0.75rem 1rem',
                    marginBottom: '1rem',
                    fontSize: '0.875rem',
                    color: 'var(--color-text)',
                  }}>
                    💡 {result.explanation}
                  </div>
                )}
                <div className="code-block">
                  <pre>{result.documented_code}</pre>
                </div>
              </>
            ) : null}
          </div>
        )}
      </div>
    </div>
  );
}

export default DocsGeneratorPage;
