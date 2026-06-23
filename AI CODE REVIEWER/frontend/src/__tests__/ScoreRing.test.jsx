// ─────────────────────────────────────────────
// src/__tests__/ScoreRing.test.jsx
//
// LEARNING NOTE:
// Testing an SVG component — we check that:
//   1. The score number is rendered correctly
//   2. The correct color class is applied based on score thresholds
//   3. Edge cases (0, 50, 100) work without errors
// ─────────────────────────────────────────────

import { render, screen } from '@testing-library/react';
import ScoreRing from '../components/ScoreRing';

describe('ScoreRing', () => {
  it('renders the score number', () => {
    render(<ScoreRing score={85} />);
    expect(screen.getByText('85')).toBeInTheDocument();
  });

  it('renders "/ 100" label', () => {
    render(<ScoreRing score={85} />);
    expect(screen.getByText('/ 100')).toBeInTheDocument();
  });

  it('renders a score of 0 without error', () => {
    render(<ScoreRing score={0} />);
    expect(screen.getByText('0')).toBeInTheDocument();
  });

  it('renders a perfect score of 100 without error', () => {
    render(<ScoreRing score={100} />);
    expect(screen.getByText('100')).toBeInTheDocument();
  });

  it('renders an SVG element for the ring', () => {
    const { container } = render(<ScoreRing score={75} />);
    // SVG should be present in the rendered output
    expect(container.querySelector('svg')).toBeInTheDocument();
    // Two circles: background track + progress arc
    expect(container.querySelectorAll('circle')).toHaveLength(2);
  });

  it('uses green color for high scores (>=75)', () => {
    render(<ScoreRing score={80} />);
    const scoreEl = screen.getByText('80');
    // Color is set via inline style — should be success green
    expect(scoreEl).toHaveStyle({ color: 'var(--color-success)' });
  });

  it('uses amber color for medium scores (50-74)', () => {
    render(<ScoreRing score={60} />);
    const scoreEl = screen.getByText('60');
    expect(scoreEl).toHaveStyle({ color: 'var(--color-warning)' });
  });

  it('uses red color for low scores (<50)', () => {
    render(<ScoreRing score={30} />);
    const scoreEl = screen.getByText('30');
    expect(scoreEl).toHaveStyle({ color: 'var(--color-error)' });
  });
});
