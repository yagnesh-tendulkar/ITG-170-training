// ─────────────────────────────────────────────
// src/__tests__/AuthContext.test.jsx
//
// LEARNING NOTE:
// Testing a React Context involves:
//   1. Wrapping the component under test with the Provider
//   2. Using a helper "consumer" component to read context values
//   3. Mocking external dependencies (API calls, localStorage)
//
// KEY TESTING LIBRARY CONCEPTS:
//   - render():    renders a component into the virtual DOM
//   - screen:      queries the rendered DOM (getByText, queryByText, etc.)
//   - waitFor():   waits for async state updates to settle
//   - vi.fn():     creates a mock function (Vitest's version of jest.fn())
//   - vi.mock():   replaces a module with a mock version
// ─────────────────────────────────────────────

import { render, screen, waitFor } from '@testing-library/react';
import { AuthProvider, useAuth } from '../context/AuthContext';
import { vi } from 'vitest';

// Mock the API client module — we don't want real HTTP calls in tests
vi.mock('../api/client', () => ({
  authAPI: {
    getMe: vi.fn(),
    login: vi.fn(),
    register: vi.fn(),
  },
}));

// Import the mock so we can configure its return values
import { authAPI } from '../api/client';

// Helper: a tiny component that reads AuthContext and renders the values
// This lets us inspect context state without testing a specific page
function AuthConsumer() {
  const { user, loading } = useAuth();
  if (loading) return <div>Loading...</div>;
  if (user) return <div>Logged in as: {user.username}</div>;
  return <div>Not logged in</div>;
}

describe('AuthContext', () => {
  // Reset mocks and localStorage before each test
  beforeEach(() => {
    vi.clearAllMocks();
    localStorage.clear();
  });

  it('shows "Not logged in" when no token in localStorage', async () => {
    // No token → getMe should NOT be called
    render(
      <AuthProvider>
        <AuthConsumer />
      </AuthProvider>
    );

    // Wait for loading to finish
    await waitFor(() => {
      expect(screen.getByText('Not logged in')).toBeInTheDocument();
    });

    expect(authAPI.getMe).not.toHaveBeenCalled();
  });

  it('restores session when valid token exists in localStorage', async () => {
    // Simulate having a stored token from a previous login
    localStorage.setItem('access_token', 'fake-valid-token');

    // Mock getMe to return a user (simulates successful token validation)
    authAPI.getMe.mockResolvedValueOnce({
      data: { id: 1, username: 'storeduser', email: 'stored@test.com' },
    });

    render(
      <AuthProvider>
        <AuthConsumer />
      </AuthProvider>
    );

    // Wait for the async getMe call to complete
    await waitFor(() => {
      expect(screen.getByText('Logged in as: storeduser')).toBeInTheDocument();
    });

    expect(authAPI.getMe).toHaveBeenCalledOnce();
  });

  it('clears session when stored token is invalid', async () => {
    localStorage.setItem('access_token', 'expired-token');

    // Mock getMe to fail (token expired)
    authAPI.getMe.mockRejectedValueOnce(new Error('401 Unauthorized'));

    render(
      <AuthProvider>
        <AuthConsumer />
      </AuthProvider>
    );

    await waitFor(() => {
      expect(screen.getByText('Not logged in')).toBeInTheDocument();
    });

    // Token should be removed from localStorage
    expect(localStorage.getItem('access_token')).toBeNull();
  });
});
