// components/LoadingSpinner.jsx

function LoadingSpinner({ fullPage = false, message = 'Loading...' }) {
  if (fullPage) {
    return (
      <div style={{
        minHeight: '100vh',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        flexDirection: 'column',
        gap: '1rem',
      }}>
        <div className="spinner" />
        <p style={{ color: 'var(--color-text-2)', fontSize: '0.9rem' }}>{message}</p>
      </div>
    );
  }

  return (
    <div className="loading-overlay">
      <div className="spinner" />
      <p>{message}</p>
    </div>
  );
}

export default LoadingSpinner;
