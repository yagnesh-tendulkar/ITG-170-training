import {
  AlertCircle,
  ChevronLeft,
  ChevronRight,
  Clock,
  Loader2,
  Play,
  Send,
  Square,
} from "lucide-react";
import type { SessionFeedback } from "./types";
import {
  difficulties,
  durationOptions,
  experienceLevels,
  questionCountOptions,
  questionTypes,
  roles,
} from "./constants";

type Props = {
  role: (typeof roles)[number];
  questionType: (typeof questionTypes)[number];
  difficulty: (typeof difficulties)[number];
  experienceLevel: (typeof experienceLevels)[number];
  numQuestions: (typeof questionCountOptions)[number];
  selectedDuration: number;
  sessionStatus: "idle" | "in_progress" | "completed";
  timerSeconds: number;
  questions: string[];
  currentQuestion: string;
  sessionResponses: string[];
  response: string;
  feedback: string | null;
  sessionFeedback: SessionFeedback | null;
  error: string | null;
  isLoading: boolean;
  setRole: (v: (typeof roles)[number]) => void;
  setQuestionType: (v: (typeof questionTypes)[number]) => void;
  setDifficulty: (v: (typeof difficulties)[number]) => void;
  setExperienceLevel: (v: (typeof experienceLevels)[number]) => void;
  setNumQuestions: (v: (typeof questionCountOptions)[number]) => void;
  setSelectedDuration: (v: number) => void;
  setResponse: (v: string) => void;
  startInterview: () => void;
  submitAnswer: () => void;
  handleSkipQuestion: () => void;
  handlePrevQuestion: () => void;
  handleCompleteInterview: () => void;
  formatTimer: (s: number) => string;
};

export default function PracticePanel({
  role,
  questionType,
  difficulty,
  experienceLevel,
  numQuestions,
  selectedDuration,
  sessionStatus,
  timerSeconds,
  questions,
  currentQuestion,
  sessionResponses,
  response,
  feedback,
  sessionFeedback,
  error,
  isLoading,
  setRole,
  setQuestionType,
  setDifficulty,
  setExperienceLevel,
  setNumQuestions,
  setSelectedDuration,
  setResponse,
  startInterview,
  submitAnswer,
  handleSkipQuestion,
  handlePrevQuestion,
  handleCompleteInterview,
  formatTimer,
}: Props) {
  const currentIndex = sessionResponses.length;
  const timerUrgent = timerSeconds > 0 && timerSeconds <= 60;

  return (
    <div className="practice-wrap">
      <div className="config-grid">
        <div className="field-group">
          <label className="field-label">Role</label>
          <select
            className="select-field"
            value={role}
            onChange={(e) => setRole(e.target.value as (typeof roles)[number])}
            disabled={sessionStatus === "in_progress"}
          >
            {roles.map((r) => (
              <option key={r} value={r}>{r}</option>
            ))}
          </select>
        </div>

        <div className="field-group">
          <label className="field-label">Question Type</label>
          <select
            className="select-field"
            value={questionType}
            onChange={(e) => setQuestionType(e.target.value as (typeof questionTypes)[number])}
            disabled={sessionStatus === "in_progress"}
          >
            {questionTypes.map((t) => (
              <option key={t} value={t}>{t}</option>
            ))}
          </select>
        </div>

        <div className="field-group">
          <label className="field-label">Difficulty</label>
          <select
            className="select-field"
            value={difficulty}
            onChange={(e) => setDifficulty(e.target.value as (typeof difficulties)[number])}
            disabled={sessionStatus === "in_progress"}
          >
            {difficulties.map((d) => (
              <option key={d} value={d}>{d}</option>
            ))}
          </select>
        </div>

        <div className="field-group">
          <label className="field-label">Experience Level</label>
          <select
            className="select-field"
            value={experienceLevel}
            onChange={(e) => setExperienceLevel(e.target.value as (typeof experienceLevels)[number])}
            disabled={sessionStatus === "in_progress"}
          >
            {experienceLevels.map((l) => (
              <option key={l} value={l}>{l}</option>
            ))}
          </select>
        </div>

        <div className="field-group">
          <label className="field-label">Questions</label>
          <select
            className="select-field"
            value={numQuestions}
            onChange={(e) => setNumQuestions(Number(e.target.value) as (typeof questionCountOptions)[number])}
            disabled={sessionStatus === "in_progress"}
          >
            {questionCountOptions.map((n) => (
              <option key={n} value={n}>{n} questions</option>
            ))}
          </select>
        </div>

        <div className="field-group">
          <label className="field-label">Session Duration</label>
          <select
            className="select-field"
            value={selectedDuration}
            onChange={(e) => setSelectedDuration(Number(e.target.value))}
            disabled={sessionStatus === "in_progress"}
          >
            {durationOptions.map((m) => (
              <option key={m} value={m}>{m} minutes</option>
            ))}
          </select>
        </div>
      </div>

      {sessionStatus === "idle" && (
        <button
          className="button primary start-btn"
          type="button"
          onClick={startInterview}
          disabled={isLoading}
        >
          {isLoading ? (
            <><Loader2 size={16} className="spin" /> Starting...</>
          ) : (
            <><Play size={16} /> Start Interview Session</>
          )}
        </button>
      )}

      {sessionStatus === "in_progress" && (
        <>
          <div className={`timer-bar ${timerUrgent ? "urgent" : ""}`}>
            <Clock size={15} />
            <span>{formatTimer(timerSeconds)} remaining</span>
            <div className="timer-progress">
              <div
                className="timer-fill"
                style={{ width: `${(timerSeconds / (selectedDuration * 60)) * 100}%` }}
              />
            </div>
            <span className="q-counter">Q {currentIndex + 1}/{questions.length}</span>
          </div>

          <div className="question-card">
            <span className="question-tag">Question {currentIndex + 1}</span>
            <p className="question-text">{currentQuestion}</p>
          </div>

          <div className="field-group">
            <label className="field-label">Your Answer</label>
            <textarea
              className="textarea-input"
              value={response}
              onChange={(e) => setResponse(e.target.value)}
              placeholder="Type your answer here…"
              rows={6}
            />
          </div>

          <div className="action-row">
            <button type="button" className="button ghost icon-btn" onClick={handlePrevQuestion}>
              <ChevronLeft size={16} /> Prev
            </button>
            <button type="button" className="button ghost icon-btn" onClick={handleSkipQuestion}>
              Skip <ChevronRight size={16} />
            </button>
            <button
              type="button"
              className="button primary icon-btn"
              onClick={submitAnswer}
              disabled={isLoading || !response.trim()}
            >
              {isLoading ? <Loader2 size={15} className="spin" /> : <Send size={15} />}
              Submit Answer
            </button>
            <button
              type="button"
              className="button danger icon-btn"
              onClick={handleCompleteInterview}
              disabled={isLoading}
            >
              <Square size={15} /> End Session
            </button>
          </div>
        </>
      )}

      {sessionStatus === "completed" && !sessionFeedback && (
        <div className="notice-banner">
          <Loader2 size={16} className="spin" /> Generating your session report…
        </div>
      )}

      {error && (
        <div className="error-banner">
          <AlertCircle size={15} /> {error}
        </div>
      )}

      {feedback && sessionStatus !== "completed" && (
        <div className="feedback-card">
          <strong>Answer Feedback</strong>
          <p style={{ whiteSpace: "pre-wrap", marginTop: 10 }}>{feedback}</p>
        </div>
      )}

      {sessionFeedback && (
        <div className="session-report">
          <h3 className="report-title">Session Report</h3>
          <div className="report-scores">
            <div className="report-score">
              <span>Overall</span>
              <strong>{sessionFeedback.overall_score}</strong>
            </div>
            <div className="report-score">
              <span>Technical</span>
              <strong>{sessionFeedback.technical_score}</strong>
            </div>
            <div className="report-score">
              <span>Communication</span>
              <strong>{sessionFeedback.communication_score}</strong>
            </div>
            <div className="report-score">
              <span>Confidence</span>
              <strong>{sessionFeedback.confidence_score}</strong>
            </div>
            <div className="report-score">
              <span>Clarity</span>
              <strong>{sessionFeedback.clarity_score}</strong>
            </div>
          </div>

          {sessionFeedback.summary && (
            <p className="report-summary">{sessionFeedback.summary}</p>
          )}

          {sessionFeedback.strengths?.length > 0 && (
            <div className="report-section">
              <h4>Strengths</h4>
              <ul>
                {sessionFeedback.strengths.map((s, i) => <li key={i}>{s}</li>)}
              </ul>
            </div>
          )}

          {sessionFeedback.weaknesses?.length > 0 && (
            <div className="report-section">
              <h4>Areas to improve</h4>
              <ul>
                {sessionFeedback.weaknesses.map((w, i) => <li key={i}>{w}</li>)}
              </ul>
            </div>
          )}

          {sessionFeedback.suggestions?.length > 0 && (
            <div className="report-section">
              <h4>Suggestions</h4>
              <ul>
                {sessionFeedback.suggestions.map((s, i) => <li key={i}>{s}</li>)}
              </ul>
            </div>
          )}

          <div className="report-meta">
            <span>{sessionFeedback.questions_answered} questions answered</span>
            {sessionFeedback.total_duration_seconds > 0 && (
              <span>{Math.round(sessionFeedback.total_duration_seconds / 60)} min session</span>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
