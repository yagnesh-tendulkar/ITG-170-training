// ─────────────────────────────────────────────
// context/AuthContext.jsx
//
// LEARNING NOTE:
// React Context is a way to share state across many components
// without "prop drilling" (passing props down many levels).
//
// Here we store the logged-in user globally so ANY component can:
//   const { user, login, logout } = useAuth();
//
// Key concepts:
//   - createContext():  creates the context object
//   - useContext():     reads the context value
//   - Context.Provider: wraps components that need access to the context
// ─────────────────────────────────────────────

import { createContext, useContext, useState, useEffect } from 'react';
import { authAPI } from '../api/client';

// 1. Create the context (starts as null)
const AuthContext = createContext(null);

// 2. Create a Provider component that holds the state
export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true); // true while we check localStorage

  // On app start: check if a token exists in localStorage
  // If it does, verify it's still valid by calling /auth/me
  useEffect(() => {
    const token = localStorage.getItem('access_token');
    if (token) {
      authAPI.getMe()
        .then((res) => setUser(res.data))
        .catch(() => {
          // Token invalid/expired — clean up
          localStorage.removeItem('access_token');
          localStorage.removeItem('user');
        })
        .finally(() => setLoading(false));
    } else {
      setLoading(false);
    }
  }, []);

  // Called after a successful login API call
  const login = (tokenData) => {
    localStorage.setItem('access_token', tokenData.access_token);
    setUser(tokenData.user);
  };

  // Called when user clicks "Log out"
  const logout = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('user');
    setUser(null);
  };

  // 3. Provide the state and functions to all child components
  return (
    <AuthContext.Provider value={{ user, login, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
}

// 3. Custom hook — shortcut to read the context
// Instead of: const { user } = useContext(AuthContext)
// We write:   const { user } = useAuth()
export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used inside an <AuthProvider>');
  }
  return context;
}
