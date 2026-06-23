// ─────────────────────────────────────────────
// vite.config.js
//
// LEARNING NOTE:
// This file configures both the Vite dev server AND Vitest test runner.
// Vitest re-uses Vite's transform pipeline, which means your tests
// understand JSX, imports, and all the same module syntax as your app.
//
// Key test config:
//   - environment: 'jsdom'  → simulates a browser DOM in Node.js
//   - setupFiles: runs global test setup (like importing jest-dom matchers)
//   - globals: true         → enables describe/it/expect without importing
// ─────────────────────────────────────────────

import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],

  test: {
    // Use jsdom to simulate a browser environment
    // This lets us render React components and interact with the DOM
    environment: 'jsdom',

    // Run this file before every test file
    // We use it to import @testing-library/jest-dom matchers
    setupFiles: './src/__tests__/setup.js',

    // Allow describe(), it(), expect() etc. without importing
    globals: true,

    // Show a nice test coverage report
    coverage: {
      provider: 'v8',
      reporter: ['text', 'lcov'],
      include: ['src/**/*.{js,jsx}'],
      exclude: ['src/__tests__/**', 'src/main.jsx'],
    },
  },
});
