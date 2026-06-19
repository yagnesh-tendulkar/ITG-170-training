import { render, screen } from "@testing-library/react";
import { describe, it, expect } from "vitest";
import InterviewPrepPortal from "../components/InterviewPrepPortal";

describe("Login form", () => {
  it("renders login and register controls", () => {
    render(<InterviewPrepPortal />);
    expect(screen.getByPlaceholderText("Email")).toBeInTheDocument();
    expect(screen.getByPlaceholderText("Password")).toBeInTheDocument();
    expect(screen.getAllByText("Login").length).toBeGreaterThanOrEqual(1);
  });
});
