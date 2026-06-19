import { render, screen } from "@testing-library/react";
import { describe, it, expect } from "vitest";
import Dashboard from "../pages/Dashboard";

describe("Dashboard page", () => {
  it("shows interview dashboard text", () => {
    render(<Dashboard />);
    expect(screen.getByText("Interview Dashboard")).toBeInTheDocument();
    expect(screen.getByText(/Track your interview performance/i)).toBeInTheDocument();
  });
});
