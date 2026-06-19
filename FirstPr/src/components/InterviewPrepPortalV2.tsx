import { useEffect, useRef, useState } from "react";
import AuthPanel from "./InterviewPrepPortalV2/AuthPanel";
import AnalyticsSection from "./InterviewPrepPortalV2/AnalyticsSection";
import HistorySection from "./InterviewPrepPortalV2/HistorySection";
import PracticePanel from "./InterviewPrepPortalV2/PracticePanel";
import { API_BASE, difficulties, experienceLevels, questionCountOptions, questionTypes, roles } from "./InterviewPrepPortalV2/constants";
import type { DashboardData, HistoryRecord, SessionFeedback, AnswerResult } from "./InterviewPrepPortalV2/types";

function InterviewPrepPortalV2() {
  const [role, setRole] = useState<typeof roles[number]>("Frontend Developer");
  const [questionType, setQuestionType] = useState<typeof questionTypes[number]>("Technical");
  const [difficulty, setDifficulty] = useState<typeof difficulties[number]>("Medium");
  const [experienceLevel, setExperienceLevel] = useState<typeof experienceLevels[number]>("Mid");
  const [numQuestions, setNumQuestions] = useState<typeof questionCountOptions[number]>(5);
  const [questions, setQuestions] = useState<string[]>([]);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [response, setResponse] = useState("");
  const [feedback, setFeedback] = useState<string | null>(null);
  const [sessionFeedback, setSessionFeedback] = useState<SessionFeedback | null>(null);
  const [sessionId, setSessionId] = useState<string | null>(null);
  const [sessionStatus, setSessionStatus] = useState<"idle" | "in_progress" | "completed">("idle");
  const [selectedDuration, setSelectedDuration] = useState<number>(15);
  const [timerSeconds, setTimerSeconds] = useState<number>(0);
  const [sessionResponses, setSessionResponses] = useState<string[]>([]);
  const [history, setHistory] = useState<HistoryRecord[]>([]);
  const [dashboard, setDashboard] = useState<DashboardData | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [token, setToken] = useState<string | null>(null);
  const [currentUser, setCurrentUser] = useState<{ name?: string; email: string } | null>(null);
  const [viewMode, setViewMode] = useState<"practice" | "analytics" | "history">("practice");
  const [questionStart, setQuestionStart] = useState<number>(Date.now());
  const intervalRef = useRef<number | null>(null);

  const currentQuestion = questions[currentQuestionIndex] || "Loading question...";
  const isAuthenticated = Boolean(currentUser && token);
  const welcomeName = currentUser?.name || currentUser?.email?.split("@")[0] || "Candidate";

  useEffect(() => {
    const storedToken = typeof window !== "undefined" ? window.localStorage.getItem("firstpr_token") : null;
    const storedUser = typeof window !== "undefined" ? window.localStorage.getItem("firstpr_user") : null;
    if (storedToken) setToken(storedToken);
    if (storedUser) {
      try {
        setCurrentUser(JSON.parse(storedUser));
      } catch {
        localStorage.removeItem("firstpr_user");
      }
    }
  }, []);

  useEffect(() => {
    fetchQuestions();
  }, [role, questionType, difficulty, experienceLevel, numQuestions]);

  useEffect(() => {
    if (!token) return;
    fetchDashboard();
    fetchHistory();
  }, [token]);

  useEffect(() => {
    if (sessionStatus !== "in_progress") {
      if (intervalRef.current) {
        window.clearInterval(intervalRef.current);
      }
      return;
    }

    intervalRef.current = window.setInterval(() => {
      setTimerSeconds((seconds) => {
        if (seconds <= 1) {
          if (intervalRef.current) window.clearInterval(intervalRef.current);
          handleCompleteInterview();
          return 0;
        }
        return seconds - 1;
      });
    }, 1000);

    return () => {
      if (intervalRef.current) {
        window.clearInterval(intervalRef.current);
      }
    };
  }, [sessionStatus]);

  const callWithAuth = (init: RequestInit = {}) => {
    const headers = {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...((init.headers as Record<string, string>) || {}),
    };
    return { ...init, headers };
  };

  const fetchQuestions = async () => {
    try {
      const response = await fetch(
        `${API_BASE}/questions?role=${encodeURIComponent(role)}&question_type=${encodeURIComponent(
          questionType
        )}&difficulty=${encodeURIComponent(difficulty)}&experience_level=${encodeURIComponent(experienceLevel)}&num_questions=${numQuestions}`
      );
      if (!response.ok) {
        throw new Error("Unable to fetch questions from backend.");
      }
      const payload = await response.json();
      setQuestions(payload.questions || []);
      setCurrentQuestionIndex(0);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Question fetch failed");
      setQuestions(["Describe your most recent project experience."]);
    }
  };

  const fetchHistory = async () => {
    if (!token) return;
    try {
      const res = await fetch(`${API_BASE}/history`, callWithAuth());
      if (!res.ok) throw new Error("Unable to load history.");
      setHistory(await res.json());
    } catch {
      setHistory([]);
    }
  };

  const fetchDashboard = async () => {
    if (!token) return;
    try {
      const res = await fetch(`${API_BASE}/analytics/dashboard`, callWithAuth());
      if (!res.ok) throw new Error("Unable to load dashboard.");
      setDashboard(await res.json());
    } catch {
      setDashboard(null);
    }
  };

  const loadUser = async (sessionToken: string) => {
    try {
      const res = await fetch(`${API_BASE}/auth/me`, callWithAuth({ headers: { Authorization: `Bearer ${sessionToken}` } }));
      if (!res.ok) throw new Error("Unable to resolve profile.");
      const user = await res.json();
      setCurrentUser(user);
      localStorage.setItem("firstpr_user", JSON.stringify(user));
    } catch {
      setCurrentUser({ email: "guest" });
    }
  };

  const handleLogin = async (email: string, password: string) => {
    setError(null);
    setIsLoading(true);
    try {
      const res = await fetch(`${API_BASE}/auth/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });
      if (!res.ok) {
        const body = await res.json().catch(() => null);
        throw new Error(body?.detail || "Login failed");
      }
      const data = await res.json();
      setToken(data.access_token);
      localStorage.setItem("firstpr_token", data.access_token);
      await loadUser(data.access_token);
      fetchHistory();
      fetchDashboard();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Login failed");
    } finally {
      setIsLoading(false);
    }
  };

  const handleRegister = async (name: string, email: string, password: string) => {
    setError(null);
    setIsLoading(true);
    try {
      const res = await fetch(`${API_BASE}/auth/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, password }),
      });
      if (!res.ok) {
        const body = await res.json().catch(() => null);
        throw new Error(body?.detail || "Registration failed");
      }
      await handleLogin(email, password);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Registration failed");
    } finally {
      setIsLoading(false);
    }
  };

  const clearAuth = () => {
    setToken(null);
    setCurrentUser(null);
    localStorage.removeItem("firstpr_token");
    localStorage.removeItem("firstpr_user");
  };

  const startInterview = async () => {
    setError(null);
    setIsLoading(true);
    try {
      const res = await fetch(`${API_BASE}/interview/session`, callWithAuth({
        method: "POST",
        body: JSON.stringify({
          role,
          question_type: questionType,
          difficulty,
          experience_level: experienceLevel,
          duration_minutes: selectedDuration,
        }),
      }));
      if (!res.ok) throw new Error("Could not start interview session.");
      const data = await res.json();
      setSessionId(data.session_id);
      setSessionStatus("in_progress");
      setTimerSeconds(selectedDuration * 60);
      setResponse("");
      setFeedback(null);
      setSessionFeedback(null);
      setSessionResponses([]);
      setQuestionStart(Date.now());
    } catch (err) {
      setError(err instanceof Error ? err.message : "Session start failed");
    } finally {
      setIsLoading(false);
    }
  };

  const submitAnswer = async () => {
    if (!response.trim() || !sessionId) {
      setError("Enter a response and start an interview session first.");
      return;
    }

    setError(null);
    setIsLoading(true);
    try {
      const durationSeconds = Math.floor((Date.now() - questionStart) / 1000);
      const res = await fetch(`${API_BASE}/interview/session/${sessionId}/answer`, callWithAuth({
        method: "POST",
        body: JSON.stringify({
          question: currentQuestion,
          response,
          question_type: questionType,
          duration_seconds: durationSeconds,
        }),
      }));
      if (!res.ok) {
        const body = await res.json().catch(() => null);
        throw new Error(body?.detail || "Evaluation failed");
      }
      const data: AnswerResult = await res.json();
      setFeedback(
        `Score: ${data.score}/100\nTechnical: ${data.technical_score}\nCommunication: ${data.communication_score}\nConfidence: ${data.confidence_score}\nClarity: ${data.clarity_score}\n\n${data.feedback}`
      );
      setSessionResponses((prev) => [...prev, currentQuestion]);
      setResponse("");
      setQuestionStart(Date.now());
      if (currentQuestionIndex < questions.length - 1) {
        setCurrentQuestionIndex((index) => index + 1);
      }
      if (token) {
        fetchHistory();
        fetchDashboard();
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : "Answer submission failed");
    } finally {
      setIsLoading(false);
    }
  };

  const handleCompleteInterview = async () => {
    if (!sessionId || sessionStatus !== "in_progress") return;
    setSessionStatus("completed");
    setIsLoading(true);
    try {
      const res = await fetch(`${API_BASE}/interview/session/${sessionId}/complete`, callWithAuth({
        method: "POST",
      }));
      if (!res.ok) {
        const body = await res.json().catch(() => null);
        throw new Error(body?.detail || "Could not complete interview.");
      }
      const data: SessionFeedback = await res.json();
      setSessionFeedback(data);
      setFeedback("Interview ended. Review your personalized feedback below.");
      if (token) {
        fetchHistory();
        fetchDashboard();
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : "Completion failed");
    } finally {
      setIsLoading(false);
    }
  };

  const handleSkipQuestion = () => {
    setCurrentQuestionIndex((index) => (index + 1) % questions.length);
    setResponse("");
    setFeedback(null);
    setQuestionStart(Date.now());
  };

  const handlePrevQuestion = () => {
    setCurrentQuestionIndex((index) => (index - 1 + questions.length) % questions.length);
    setResponse("");
    setFeedback(null);
    setQuestionStart(Date.now());
  };

  const formatTimer = (seconds: number) => {
    const m = Math.floor(seconds / 60);
    const s = seconds % 60;
    return `${m}:${s.toString().padStart(2, "0")}`;
  };

  return (
    <div className="portal-shell">
      <header className="portal-header">
        <div className="hero-copy">
          <span className="eyebrow">AI Interview Practice</span>
          <h1>FirstPr Interview Prep Portal</h1>
          <p>
            Practice mock interviews with real AI-powered question generation, timed sessions, structured feedback,
            and analytics that track progress across multiple runs.
          </p>
        </div>

        <div className="user-panel">
          {currentUser ? (
            <>
              <div className="status-pill">Signed in as {currentUser.email}</div>
              <button className="button secondary" onClick={clearAuth} type="button">
                Logout
              </button>
            </>
          ) : (
            <div className="status-pill">Login or register to save progress</div>
          )}
        </div>
      </header>

      <section className="section-grid two-column">
        {!isAuthenticated ? (
          <aside className="auth-card">
            <h2 className="card-title">Login / Register</h2>
            <AuthPanel onLogin={handleLogin} onRegister={handleRegister} error={error} disabled={isLoading} />
          </aside>
        ) : (
          <aside className="welcome-card">
            <div className="welcome-head">
              <div>
                <p className="eyebrow">Ready to practice</p>
                <h2>Welcome back, {welcomeName}!</h2>
                <p>Run a timed mock interview, review AI feedback, and compare your results on the analytics dashboard.</p>
              </div>
            </div>

            <div className="overview-row">
              <div className="overview-item">
                <strong>Sessions completed</strong>
                <span>{dashboard?.total_sessions ?? 0}</span>
              </div>
              <div className="overview-item">
                <strong>Avg score</strong>
                <span>{dashboard?.average_score ?? 0}</span>
              </div>
            </div>
          </aside>
        )}

        <main className="coach-card">
          <div className="tab-row">
            <button
              className={`toggle-button ${viewMode === "practice" ? "active" : ""}`}
              onClick={() => setViewMode("practice")}
              type="button"
            >
              Practice
            </button>
            <button
              className={`toggle-button ${viewMode === "analytics" ? "active" : ""}`}
              onClick={() => setViewMode("analytics")}
              type="button"
              disabled={!isAuthenticated}
            >
              Analytics
            </button>
            <button
              className={`toggle-button ${viewMode === "history" ? "active" : ""}`}
              onClick={() => setViewMode("history")}
              type="button"
              disabled={!isAuthenticated}
            >
              History
            </button>
          </div>

          {viewMode === "analytics" ? (
            <AnalyticsSection dashboard={dashboard} />
          ) : viewMode === "history" ? (
            <HistorySection history={history} />
          ) : (
            <PracticePanel
              role={role}
              questionType={questionType}
              difficulty={difficulty}
              experienceLevel={experienceLevel}
              numQuestions={numQuestions}
              selectedDuration={selectedDuration}
              sessionStatus={sessionStatus}
              timerSeconds={timerSeconds}
              questions={questions}
              currentQuestion={currentQuestion}
              sessionResponses={sessionResponses}
              response={response}
              feedback={feedback}
              sessionFeedback={sessionFeedback}
              error={error}
              isLoading={isLoading}
              setRole={setRole}
              setQuestionType={setQuestionType}
              setDifficulty={setDifficulty}
              setExperienceLevel={setExperienceLevel}
              setNumQuestions={setNumQuestions}
              setSelectedDuration={setSelectedDuration}
              setResponse={setResponse}
              startInterview={startInterview}
              submitAnswer={submitAnswer}
              handleSkipQuestion={handleSkipQuestion}
              handlePrevQuestion={handlePrevQuestion}
              handleCompleteInterview={handleCompleteInterview}
              formatTimer={formatTimer}
            />
          )}
        </main>
      </section>

      <section className="info-card" style={{ marginTop: 24 }}>
        <h2 className="card-title">What this portal now includes</h2>
        <ul>
          <li>AI-powered question generation based on role, difficulty, interview type, and experience level.</li>
          <li>Timed mock interviews with auto-complete and per-question durations.</li>
          <li>Professional analytics showing weekly and monthly progress.</li>
          <li>Personalized AI feedback reports for every completed interview session.</li>
        </ul>
      </section>
    </div>
  );
}

export default InterviewPrepPortalV2;
