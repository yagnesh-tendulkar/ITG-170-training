// ─────────────────────────────────────────────
// components/ProtectedRoute.jsx
//
// LEARNING NOTE:
// A "protected route" only renders its children if the user is logged in.
// If not logged in, it redirects to /login.
//
// This pattern is essential for auth: instead of checking auth in every
// page component, we wrap them with ProtectedRoute in App.jsx.
// ─────────────────────────────────────────────

import { Navigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import LoadingSpinner from './LoadingSpinner';

function ProtectedRoute({ children }) {
  const { user, loading } = useAuth();

  // While checking localStorage / token validation, show a spinner
  if (loading) {
    return <LoadingSpinner fullPage message="Checking session..." />;
  }

  // Not logged in → redirect to login page
  if (!user) {
    return <Navigate to="/login" replace />;
  }

  // Logged in → render the page
  return children;
}

export default ProtectedRoute;
