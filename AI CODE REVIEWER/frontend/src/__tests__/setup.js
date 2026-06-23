// ─────────────────────────────────────────────
// src/__tests__/setup.js
//
// LEARNING NOTE:
// This file runs before every test file.
// It extends Vitest's built-in 'expect' with extra DOM matchers from
// @testing-library/jest-dom, enabling assertions like:
//   expect(element).toBeInTheDocument()
//   expect(button).toBeDisabled()
//   expect(input).toHaveValue('hello')
// ─────────────────────────────────────────────

import '@testing-library/jest-dom';
