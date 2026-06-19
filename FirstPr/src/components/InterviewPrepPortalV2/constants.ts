export const API_BASE = "http://localhost:8000/api";

export const roles = [
  "Frontend Developer",
  "Backend Developer",
  "Full Stack Developer",
  "Data Scientist",
  "DevOps Engineer",
  "Product Manager",
  "Mobile Developer",
  "Machine Learning Engineer",
] as const;

export const questionTypes = [
  "Technical",
  "Behavioral",
  "Architecture",
  "System Design",
] as const;

export const difficulties = ["Easy", "Medium", "Hard"] as const;

export const experienceLevels = ["Junior", "Mid", "Senior", "Lead"] as const;

export const questionCountOptions = [3, 5, 7, 10] as const;

export const durationOptions = [10, 15, 20, 30, 45, 60] as const;
