// ─────────────────────────────────────────────
// src/__tests__/ProtectedRoute.test.jsx
//
// LEARNING NOTE:
// Testing routing behavior requires wrapping components in MemoryRouter.
// MemoryRouter is like BrowserRouter but works in test environments
// (no real browser URL bar needed).
//
// We test two scenarios:
//   1. Logged-in user → children are rendered
//   2. Logged-out user → redirected to /login
// ─────────────────────────────────────────────

import { render, screen } from '@testing-library/react';
import { MemoryRouter, Routes, Route } from 'react-router-dom';
import { vi } from 'vitest';
import ProtectedRoute from '../components/ProtectedRoute';

// Mock AuthContext so we can control whether a user is logged in
vi.mock('../context/AuthContext', () => ({
  useAuth: vi.fn(),
}));

import { useAuth } from '../context/AuthContext';

// Helper function to render ProtectedRoute in a complete router setup
function renderWithRouter(isLoggedIn, loading = false) {
  // Configure the mock auth state
  useAuth.mockReturnValue({
    user: isLoggedIn ? { id: 1, username: 'testuser' } : null,
    loading,
  });

  return render(
    <MemoryRouter initialEntries={['/protected']}>
      <Routes>
        {/* The protected route contains "secret content" */}
        <Route
          path="/protected"
          element={
            <ProtectedRoute>
              <div>Secret Protected Content</div>
            </ProtectedRoute>
          }
        />
        {/* The login route — where redirects go */}
        <Route path="/login" element={<div>Login Page</div>} />
      </Routes>
    </MemoryRouter>
  );
}

describe('ProtectedRoute', () => {
  it('renders children when user is logged in', () => {
    renderWithRouter(true);
    expect(screen.getByText('Secret Protected Content')).toBeInTheDocument();
  });

  it('redirects to /login when user is not logged in', () => {
    renderWithRouter(false);
    // Should be on the login page, not the protected page
    expect(screen.getByText('Login Page')).toBeInTheDocument();
    expect(screen.queryByText('Secret Protected Content')).not.toBeInTheDocument();
  });

  it('shows loading spinner while auth state is loading', () => {
    renderWithRouter(false, true); // loading = true
    expect(screen.getByText(/checking session/i)).toBeInTheDocument();
    // Neither the content nor the login page should show
    expect(screen.queryByText('Secret Protected Content')).not.toBeInTheDocument();
    expect(screen.queryByText('Login Page')).not.toBeInTheDocument();
  });
});
