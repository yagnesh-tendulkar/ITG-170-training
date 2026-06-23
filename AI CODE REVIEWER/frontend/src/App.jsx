// ─────────────────────────────────────────────
// App.jsx
//
// LEARNING NOTE:
// This is the root component. It sets up:
//   1. Context Providers — wrap the whole app so all children can use them
//   2. React Router — maps URLs to page components
//   3. Protected Routes — wrap pages that require login
//
// Route structure:
//   /login        → LoginPage      (public)
//   /register     → RegisterPage   (public)
//   /dashboard    → DashboardPage  (protected)
//   /review       → ReviewPage     (protected)
//   /history      → HistoryPage    (protected)
//   /docs-gen     → DocsGeneratorPage (protected)
//   /             → redirect to /dashboard
// ─────────────────────────────────────────────

import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import { ToastProvider } from './context/ToastContext';
import ProtectedRoute from './components/ProtectedRoute';
import Navbar from './components/Navbar';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import DashboardPage from './pages/DashboardPage';
import ReviewPage from './pages/ReviewPage';
import HistoryPage from './pages/HistoryPage';
import DocsGeneratorPage from './pages/DocsGeneratorPage';

// Layout component for authenticated pages (includes Navbar)
function AppLayout({ children }) {
  return (
    <div className="app-layout">
      <Navbar />
      <main style={{ flex: 1 }}>
        {children}
      </main>
    </div>
  );
}

function App() {
  return (
    // BrowserRouter enables URL-based navigation
    <BrowserRouter>
      {/* AuthProvider wraps everything so all pages know if user is logged in */}
      <AuthProvider>
        {/* ToastProvider wraps everything so any page can show notifications */}
        <ToastProvider>
          <Routes>
            {/* Public Routes (no login required) */}
            <Route path="/login"    element={<LoginPage />} />
            <Route path="/register" element={<RegisterPage />} />

            {/* Protected Routes (login required) */}
            <Route path="/dashboard" element={
              <ProtectedRoute>
                <AppLayout><DashboardPage /></AppLayout>
              </ProtectedRoute>
            } />
            <Route path="/review" element={
              <ProtectedRoute>
                <AppLayout><ReviewPage /></AppLayout>
              </ProtectedRoute>
            } />
            <Route path="/history" element={
              <ProtectedRoute>
                <AppLayout><HistoryPage /></AppLayout>
              </ProtectedRoute>
            } />
            <Route path="/docs-gen" element={
              <ProtectedRoute>
                <AppLayout><DocsGeneratorPage /></AppLayout>
              </ProtectedRoute>
            } />

            {/* Default redirect */}
            <Route path="/" element={<Navigate to="/dashboard" replace />} />
            <Route path="*" element={<Navigate to="/dashboard" replace />} />
          </Routes>
        </ToastProvider>
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;
