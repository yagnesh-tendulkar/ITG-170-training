// ─────────────────────────────────────────────
// api/client.js
//
// LEARNING NOTE:
// Axios is a popular HTTP library for making API requests.
// We configure a single "instance" here with:
//   - baseURL: so we don't repeat "http://localhost:8000" everywhere
//   - Interceptors: middleware that runs on every request/response
//     * Request interceptor: automatically adds JWT token to headers
//     * Response interceptor: handles 401 errors globally (auto-logout)
// ─────────────────────────────────────────────

import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

// Create a configured axios instance
const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// ── Request Interceptor ──────────────────────
// Runs BEFORE every request is sent
// Reads the JWT token from localStorage and adds it to the Authorization header
apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// ── Response Interceptor ──────────────────────
// Runs AFTER every response comes back
// If we get a 401 (Unauthorized), the token expired — log out automatically
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Token expired or invalid — clear stored data
      localStorage.removeItem('access_token');
      localStorage.removeItem('user');
      // Redirect to login (only if not already there)
      if (!window.location.pathname.includes('/login')) {
        window.location.href = '/login';
      }
    }
    return Promise.reject(error);
  }
);

// ── API Functions ──────────────────────────────
// Each function corresponds to one backend endpoint

export const authAPI = {
  register: (data) => apiClient.post('/auth/register', data),
  login: (data) => apiClient.post('/auth/login', data),
  getMe: () => apiClient.get('/auth/me'),
};

export const reviewsAPI = {
  analyze: (data) => apiClient.post('/reviews/analyze', data),
  getHistory: (skip = 0, limit = 20) =>
    apiClient.get(`/reviews/history?skip=${skip}&limit=${limit}`),
  getById: (id) => apiClient.get(`/reviews/${id}`),
  deleteById: (id) => apiClient.delete(`/reviews/${id}`),
  getDashboard: () => apiClient.get('/reviews/dashboard'),
};

export const docsAPI = {
  generate: (data) => apiClient.post('/docs-gen/generate', data),
};

export default apiClient;
