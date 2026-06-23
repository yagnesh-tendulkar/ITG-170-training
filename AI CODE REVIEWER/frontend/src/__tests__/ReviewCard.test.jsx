// ─────────────────────────────────────────────
// src/__tests__/ReviewCard.test.jsx
//
// LEARNING NOTE:
// Testing a pure presentational component (one that just displays data)
// is the simplest form of testing — no API calls, no navigation.
//
// We just:
//   1. Create a "mock review" object with known data
//   2. Render the component with that data as props
//   3. Assert that the right things appear on screen
//   4. Test user interactions (clicking tabs)
// ─────────────────────────────────────────────

import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { vi } from 'vitest';
import ReviewCard from '../components/ReviewCard';

// A realistic mock review matching the ReviewResponse schema
const mockReview = {
  id: 1,
  title: 'My Test Review',
  language: 'Python',
  code_snippet: 'def foo():\n    pass',
  bugs: [
    { description: 'Null pointer bug', line_hint: 'Line 3', severity: 'high' },
    { description: 'Memory leak', line_hint: 'Line 7', severity: 'medium' },
  ],
  optimizations: [
    { description: 'Use list comprehension instead', impact: 'low' },
  ],
  best_practices: [
    { description: 'Add type hints', category: 'Type Safety' },
    { description: 'Write unit tests', category: 'Testing' },
  ],
  summary: 'The code has some issues but overall structure is good.',
  overall_score: 72,
  created_at: '2024-01-15T10:30:00',
};

describe('ReviewCard', () => {
  it('renders the review title and language', () => {
    render(<ReviewCard review={mockReview} />);

    expect(screen.getByText('My Test Review')).toBeInTheDocument();
    expect(screen.getByText('Python')).toBeInTheDocument();
  });

  it('shows the overall score', () => {
    render(<ReviewCard review={mockReview} />);
    // The score ring shows "72"
    expect(screen.getByText('72')).toBeInTheDocument();
  });

  it('shows bugs tab by default with correct count badge', () => {
    render(<ReviewCard review={mockReview} />);

    // Bugs tab should be active initially — show the count
    expect(screen.getByText('2', { selector: '.tab-count' })).toBeInTheDocument();

    // Bug descriptions should be visible
    expect(screen.getByText('Null pointer bug')).toBeInTheDocument();
    expect(screen.getByText('Memory leak')).toBeInTheDocument();
  });

  it('shows severity badges on bugs', () => {
    render(<ReviewCard review={mockReview} />);
    expect(screen.getByText('high')).toBeInTheDocument();
    expect(screen.getByText('medium')).toBeInTheDocument();
  });

  it('shows line hints on bugs', () => {
    render(<ReviewCard review={mockReview} />);
    expect(screen.getByText('📍 Line 3')).toBeInTheDocument();
  });

  it('switches to optimizations tab on click', async () => {
    const user = userEvent.setup();
    render(<ReviewCard review={mockReview} />);

    // Click the optimizations tab
    await user.click(screen.getByRole('button', { name: /optimizations/i }));

    // Optimization content should now be visible
    expect(screen.getByText('Use list comprehension instead')).toBeInTheDocument();
    // Bugs content should no longer be visible
    expect(screen.queryByText('Null pointer bug')).not.toBeInTheDocument();
  });

  it('switches to best practices tab on click', async () => {
    const user = userEvent.setup();
    render(<ReviewCard review={mockReview} />);

    await user.click(screen.getByRole('button', { name: /best practices/i }));

    expect(screen.getByText('Add type hints')).toBeInTheDocument();
    expect(screen.getByText('Write unit tests')).toBeInTheDocument();
    expect(screen.getByText('Type Safety')).toBeInTheDocument();
  });

  it('switches to summary tab and shows summary text', async () => {
    const user = userEvent.setup();
    render(<ReviewCard review={mockReview} />);

    await user.click(screen.getByRole('button', { name: /summary/i }));

    expect(screen.getByText(/code has some issues/i)).toBeInTheDocument();
  });

  it('shows empty state when no bugs exist', () => {
    const cleanReview = { ...mockReview, bugs: [] };
    render(<ReviewCard review={cleanReview} />);

    expect(screen.getByText('No Bugs found!')).toBeInTheDocument();
    // Celebration emoji for no bugs!
    expect(screen.getByText('🎉')).toBeInTheDocument();
  });

  it('renders correctly with all empty arrays', () => {
    const emptyReview = {
      ...mockReview,
      bugs: [],
      optimizations: [],
      best_practices: [],
      overall_score: 100,
    };
    // Should not throw
    render(<ReviewCard review={emptyReview} />);
    expect(screen.getByText('100')).toBeInTheDocument();
  });
});
