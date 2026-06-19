export type HistoryRecord = {
  id: number;
  session_id?: string;
  role: string;
  question_type: string;
  question: string;
  response: string;
  feedback: string;
  score: number;
  technical_score: number;
  communication_score: number;
  confidence_score?: number;
  clarity_score?: number;
  duration_seconds?: number;
  created_at: string;
};

export type TrendPoint = {
  date: string;
  score: number;
  technical_score: number;
  communication_score: number;
};

export type DashboardData = {
  total_sessions: number;
  total_answers: number;
  average_score: number;
  average_technical_score: number;
  average_communication_score: number;
  best_role: string | null;
  recent_trend: TrendPoint[];
  role_breakdown: Record<string, number>;
  type_breakdown: Record<string, number>;
};

export type SessionFeedback = {
  session_id: string;
  overall_score: number;
  technical_score: number;
  communication_score: number;
  confidence_score: number;
  clarity_score: number;
  strengths: string[];
  weaknesses: string[];
  suggestions: string[];
  summary: string;
  questions_answered: number;
  total_duration_seconds: number;
};

export type AnswerResult = {
  score: number;
  technical_score: number;
  communication_score: number;
  confidence_score: number;
  clarity_score: number;
  feedback: string;
  strengths: string[];
  weaknesses: string[];
  suggestions: string[];
};
