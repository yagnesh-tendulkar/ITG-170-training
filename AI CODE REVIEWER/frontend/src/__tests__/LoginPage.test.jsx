// ─────────────────────────────────────────────
// src/__tests__/LoginPage.test.jsx
//
// LEARNING NOTE:
// Testing a form page involves:
//   1. Rendering the page wrapped in its required providers
//   2. Finding form elements by their label/role
//   3. Typing into inputs with userEvent (simulates real typing)
//   4. Clicking submit and checking what happens
//
// IMPORTANT QUERIES (prefer accessible queries — they match what users see):
//   getByLabelText()   → find input by its <label> text
//   getByRole()        → find by ARIA role (button, textbox, etc.)
//   getByText()        → find by visible text
//   queryByText()      → like getByText but returns null if missing (no error)
//   findByText()       → async version that waits for the element
// ─────────────────────────────────────────────

import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { MemoryRouter } from 'react-router-dom';
import { vi } from 'vitest';
import LoginPage from '../pages/LoginPage';
import { AuthProvider } from '../context/AuthContext';
import { ToastProvider } from '../context/ToastContext';

// Mock the modules this page depends on
vi.mock('../api/client', () => ({
  authAPI: {
    getMe: vi.fn().mockRejectedValue(new Error('no token')),
    login: vi.fn(),
  },
}));

vi.mock('react-router-dom', async (importOriginal) => {
  const actual = await importOriginal();
  return {
    ...actual,
    useNavigate: () => vi.fn(),   // mock navigation so we don't need a real router
  };
});

import { authAPI } from '../api/client';

// Helper: wrap LoginPage in all its required providers
function renderLoginPage() {
  return render(
    <MemoryRouter>
      <AuthProvider>
        <ToastProvider>
          <LoginPage />
        </ToastProvider>
      </AuthProvider>
    </MemoryRouter>
  );
}

describe('LoginPage', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    localStorage.clear();
  });

  it('renders email and password fields', () => {
    renderLoginPage();

    expect(screen.getByLabelText(/email address/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/password/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /sign in/i })).toBeInTheDocument();
  });

  it('shows a link to the register page', () => {
    renderLoginPage();
    expect(screen.getByText(/create one for free/i)).toBeInTheDocument();
  });

  it('calls login API with correct credentials on submit', async () => {
    const user = userEvent.setup();

    authAPI.login.mockResolvedValueOnce({
      data: {
        access_token: 'fake-jwt-token',
        token_type: 'bearer',
        user: { id: 1, username: 'testuser', email: 'test@test.com', is_active: true },
      },
    });

    renderLoginPage();

    // Type into fields (userEvent simulates real user typing)
    await user.type(screen.getByLabelText(/email address/i), 'test@test.com');
    await user.type(screen.getByLabelText(/password/i), 'password123');

    // Click submit
    await user.click(screen.getByRole('button', { name: /sign in/i }));

    // Verify API was called with the right data
    await waitFor(() => {
      expect(authAPI.login).toHaveBeenCalledWith({
        email: 'test@test.com',
        password: 'password123',
      });
    });
  });

  it('shows error message when login fails', async () => {
    const user = userEvent.setup();

    authAPI.login.mockRejectedValueOnce({
      response: { data: { detail: 'Invalid email or password.' } },
    });

    renderLoginPage();

    await user.type(screen.getByLabelText(/email address/i), 'bad@test.com');
    await user.type(screen.getByLabelText(/password/i), 'wrongpassword');
    await user.click(screen.getByRole('button', { name: /sign in/i }));

    // Wait for the error message to appear
    await waitFor(() => {
      expect(screen.getByText(/invalid email or password/i)).toBeInTheDocument();
    });
  });

  it('disables submit button while loading', async () => {
    const user = userEvent.setup();

    // Make login take a long time (never resolve during test)
    authAPI.login.mockImplementation(() => new Promise(() => {}));

    renderLoginPage();

    await user.type(screen.getByLabelText(/email address/i), 'test@test.com');
    await user.type(screen.getByLabelText(/password/i), 'password123');
    await user.click(screen.getByRole('button', { name: /sign in/i }));

    // Button should be disabled while the request is in flight
    expect(screen.getByRole('button', { name: /signing in/i })).toBeDisabled();
  });
});
