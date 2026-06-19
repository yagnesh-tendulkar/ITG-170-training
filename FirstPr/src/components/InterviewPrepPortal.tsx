import React, { useEffect, useRef, useState } from "react";
import {
  CartesianGrid,
  Line,
  LineChart,
  Pie,
  PieChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

type HistoryRecord = {
  id: number;
  role: string;
  question_type: string;
  question: string;
  response: string;
  feedback: string;
  score: number;
  technical_score: number;
  communication_score: number;
  duration_seconds?: number;
  created_at: string;
};

type TrendPoint = {
  date: string;
  score: number;
  technical_score: number;
  communication_score: number;
};

type AnalyticsData = {
  total_responses: number;
  avg_score: number;
  avg_technical_score: number;
  avg_communication_score: number;
  recent_trend: TrendPoint[];
  role_breakdown: Record<string, number>;
};

type QuestionSet = Record<string, string[]>;

const roleQuestions: Record<string, QuestionSet> = {
  "Frontend Developer": {
    Technical: [
      "Explain the difference between React state and props.",
      "How do you optimize rendering in a React application?",
      "Describe your approach to responsive web design.",
    ],
    Behavioral: [
      "Tell me about a time you fixed a production bug under pressure.",
      "How do you stay aligned with designers and backend engineers?",
      "Describe a project where you improved the user experience.",
    ],
    Architecture: [
      "How would you design a scalable React application for a large team?",
      "What approach do you use for reusable component libraries?",
      "How do you structure CSS and component styles for maintainability?",
    ],
  },
  "Backend Developer": {
    Technical: [
      "Explain RESTful API design and how you choose HTTP status codes.",
      "How do you manage database migrations in a production service?",
      "Describe how you secure an API endpoint and protect sensitive data.",
    ],
    Behavioral: [
      "Tell me about a time you improved service reliability.",
      "How do you balance technical debt against feature delivery?",
      "Describe your process for collaborating with frontend teams.",
    ],
    Architecture: [
      "How would you design a microservice architecture for a payment system?",
      "What caching strategies do you use for high-traffic APIs?",
      "How do you ensure data consistency across distributed services?",
    ],
  },
  "Data Scientist": {
    Technical: [
      "How do you choose between classification and regression models?",
      "Explain cross-validation and its role in model selection.",
      "What is bias-variance tradeoff, and how do you manage it?",
    ],
    Behavioral: [
      "Tell me about a data project that had business impact.",
      "How do you explain model results to non-technical stakeholders?",
      "Describe a time you handled incomplete or messy data.",
    ],
    Architecture: [
      "How would you architect a production machine learning pipeline?",
      "What is your approach to model monitoring and retraining?",
      "How do you deploy models with reliable inference latency?",
    ],
  },
};

const questionTypes = ["Technical", "Behavioral", "Architecture"] as const;

const portalFeatures = [
  "Role-specific questions",
  "Targeted interview feedback",
  "Session progress tracking",
  "Realistic role-based scenarios",
  "Modern portal experience",
];

const API_BASE = "http://localhost:8000/api";

function InterviewPrepPortal() {
  const [role, setRole] = useState("Frontend Developer");
  const [questionType, setQuestionType] = useState<typeof questionTypes[number]>("Technical");
  const [questions, setQuestions] = useState<string[]>(roleQuestions[role][questionType]);
  const [questionIndex, setQuestionIndex] = useState(0);
  const [response, setResponse] = useState("");
  const [feedback, setFeedback] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  const [authMode, setAuthMode] = useState<"login" | "register">("login");
  const [authEmail, setAuthEmail] = useState("");
  const [authPassword, setAuthPassword] = useState("");
  const [authName, setAuthName] = useState("");
  const [token, setToken] = useState<string | null>(null);
  const [currentUser, setCurrentUser] = useState<{ name?: string; email: string } | null>(null);
  const [history, setHistory] = useState<HistoryRecord[]>([]);
  const [analytics, setAnalytics] = useState<AnalyticsData | null>(null);
  const [viewMode, setViewMode] = useState<"practice" | "analytics" | "history">("practice");
  const [timedMode, setTimedMode] = useState(false);
  const [timeRemaining, setTimeRemaining] = useState(90);
  const [sessionId, setSessionId] = useState(() => {
    return typeof window !== "undefined" && typeof window.crypto !== "undefined" && "randomUUID" in window.crypto
      ? window.crypto.randomUUID()
      : `session-${Date.now()}`;
  });
  const [questionDuration, setQuestionDuration] = useState(90);
  const [recordingTime, setRecordingTime] = useState(0);
  const [isRecording, setIsRecording] = useState(false);
  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const audioChunksRef = useRef<Blob[]>([]);
  const recordingIntervalRef = useRef<ReturnType<typeof setInterval> | null>(null);

  const currentQuestion = questions[questionIndex] || roleQuestions[role][questionType][0];
  const isAuthenticated = Boolean(currentUser && token);
  const welcomeName = currentUser?.name || currentUser?.email?.split("@")[0] || "Candidate";

  useEffect(() => {
    const storage = typeof window !== "undefined" ? window.localStorage : null;
    const savedToken = storage?.getItem("interviewprep_token");
    const savedUser = storage?.getItem("interviewprep_user");

    if (savedToken) {
      setToken(savedToken);
    }

    if (savedUser) {
      try {
        setCurrentUser(JSON.parse(savedUser));
      } catch {
        storage?.removeItem("interviewprep_user");
      }
    }
  }, []);

  useEffect(() => {
    const fetchQuestions = async () => {
      try {
        setError(null);
        const res = await fetch(
          `${API_BASE}/questions?role=${encodeURIComponent(role)}&question_type=${encodeURIComponent(questionType)}`
        );
        if (!res.ok) {
          throw new Error("Backend unavailable");
        }
        const data = await res.json();
        setQuestions(data.questions || roleQuestions[role][questionType]);
        setQuestionIndex(0);
      } catch {
        setError("Unable to fetch questions from backend. Using local fallback.");
        setQuestions(roleQuestions[role][questionType]);
        setQuestionIndex(0);
      }
    };

    fetchQuestions();
  }, [role, questionType]);

  useEffect(() => {
    if (!token) {
      setHistory([]);
      setAnalytics(null);
      return;
    }

    const fetchHistory = async () => {
      try {
        setError(null);
        const res = await fetch(`${API_BASE}/history`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        if (!res.ok) {
          throw new Error("Unable to fetch history");
        }
        const data = await res.json();
        setHistory(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : "History fetch failed");
      }
    };

    const fetchAnalytics = async () => {
      try {
        const res = await fetch(`${API_BASE}/analytics`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        if (!res.ok) {
          throw new Error("Unable to fetch analytics");
        }
        const data = await res.json();
        setAnalytics(data);
      } catch (err) {
        setAnalytics(null);
      }
    };

    fetchHistory();
    fetchAnalytics();
  }, [token]);

  useEffect(() => {
    if (!timedMode) {
      return;
    }

    if (timeRemaining <= 0) {
      setTimedMode(false);
      return;
    }

    const timer = window.setInterval(() => {
      setTimeRemaining((prev) => {
        if (prev <= 1) {
          setTimedMode(false);
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => window.clearInterval(timer);
  }, [timedMode, timeRemaining]);

  const clearAuth = () => {
    setToken(null);
    setCurrentUser(null);
    const storage = typeof window !== "undefined" ? window.localStorage : null;
    storage?.removeItem("interviewprep_token");
    storage?.removeItem("interviewprep_user");
  };

  const loadUserProfile = async (sessionToken: string) => {
    try {
      const res = await fetch(`${API_BASE}/auth/me`, {
        headers: {
          Authorization: `Bearer ${sessionToken}`,
        },
      });

      if (!res.ok) {
        throw new Error("Unable to fetch profile");
      }

      const user = await res.json();
      setCurrentUser(user);
      const storage = typeof window !== "undefined" ? window.localStorage : null;
      storage?.setItem("interviewprep_user", JSON.stringify(user));
    } catch {
      setCurrentUser({ email: authEmail });
    }
  };

  const handleLogin = async () => {
    try {
      setError(null);
      setIsLoading(true);
      const res = await fetch(`${API_BASE}/auth/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email: authEmail, password: authPassword }),
      });
      if (!res.ok) {
        const errorBody = await res.json().catch(() => null);
        throw new Error(errorBody?.detail || "Login failed");
      }
      const data = await res.json();
      setToken(data.access_token);
      localStorage.setItem("interviewprep_token", data.access_token);
      await loadUserProfile(data.access_token);
      setAuthPassword("");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Login failed");
    } finally {
      setIsLoading(false);
    }
  };

  const handleRegister = async () => {
    try {
      setError(null);
      setIsLoading(true);
      const res = await fetch(`${API_BASE}/auth/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: authName, email: authEmail, password: authPassword }),
      });
      if (!res.ok) {
        const errorBody = await res.json().catch(() => null);
        throw new Error(errorBody?.detail || "Registration failed");
      }
      await handleLogin();
      setAuthName("");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Registration failed");
    } finally {
      setIsLoading(false);
    }
  };

  const startTimedInterview = () => {
    const sessionUuid =
      typeof window !== "undefined" && typeof window.crypto !== "undefined" && "randomUUID" in window.crypto
        ? window.crypto.randomUUID()
        : `session-${Date.now()}`;

    setSessionId(sessionUuid);
    setTimeRemaining(questionDuration);
    setTimedMode(true);
    setFeedback(null);
    setResponse("");
  };

  const formatTimer = (seconds: number) => {
    const minutes = Math.floor(seconds / 60);
    const remainder = seconds % 60;
    return `${minutes}:${remainder.toString().padStart(2, "0")}`;
  };

  const handleEvaluate = async () => {
    if (!response.trim()) {
      setFeedback("Please enter your answer before requesting feedback.");
      return;
    }

    try {
      setIsLoading(true);
      setError(null);
      const headers: Record<string, string> = { "Content-Type": "application/json" };
      if (token) {
        headers.Authorization = `Bearer ${token}`;
      }

      const durationSeconds = questionDuration - timeRemaining;
      const payload = {
        role,
        question: currentQuestion,
        response,
        question_type: questionType,
        session_id: sessionId,
        duration_seconds: durationSeconds > 0 ? durationSeconds : undefined,
      } as Record<string, unknown>;

      const res = await fetch(`${API_BASE}/evaluate`, {
        method: "POST",
        headers,
        body: JSON.stringify(payload),
      });

      if (!res.ok) {
        const errorBody = await res.json().catch(() => null);
        throw new Error(errorBody?.detail || "Evaluation service failed");
      }

      const result = await res.json();
      setFeedback(
        `Overall score: ${result.score}\nTechnical score: ${result.technical_score}\nCommunication score: ${result.communication_score}\n${result.feedback}\n\nStrengths:\n- ${result.strengths.join("\n- ")}\n\nWeaknesses:\n- ${result.weaknesses.join("\n- ")}\n\nSuggestions:\n- ${result.suggestions.join("\n- ")}\n\nNext question: ${result.next_question}`
      );
      if (token) {
        const historyRes = await fetch(`${API_BASE}/history`, {
          headers: { Authorization: `Bearer ${token}` },
        });
        if (historyRes.ok) {
          const historyData = await historyRes.json();
          setHistory(historyData);
        }
        const analyticsRes = await fetch(`${API_BASE}/analytics`, {
          headers: { Authorization: `Bearer ${token}` },
        });
        if (analyticsRes.ok) {
          const analyticsData = await analyticsRes.json();
          setAnalytics(analyticsData);
        }
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to evaluate response.");
    } finally {
      setIsLoading(false);
    }
  };

  const handleRoleChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setRole(event.target.value);
    setQuestionIndex(0);
    setResponse("");
    setFeedback(null);
    setError(null);
  };

  const handleQuestionTypeChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setQuestionType(event.target.value as typeof questionTypes[number]);
    setQuestionIndex(0);
    setResponse("");
    setFeedback(null);
    setError(null);
  };

  const handleNextQuestion = () => {
    const nextIndex = (questionIndex + 1) % questions.length;
    setQuestionIndex(nextIndex);
    setResponse("");
    setFeedback(null);
    setError(null);
  };

  const startRecording = async () => {
    try {
      setError(null);
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const recorder = new MediaRecorder(stream);
      audioChunksRef.current = [];

      recorder.ondataavailable = (event) => {
        audioChunksRef.current.push(event.data);
      };

      recorder.onstop = async () => {
        const audioBlob = new Blob(audioChunksRef.current, { type: "audio/wav" });
        await transcribeAudio(audioBlob);
        stream.getTracks().forEach((track) => track.stop());
      };

      mediaRecorderRef.current = recorder;
      recorder.start();
      setIsRecording(true);
      setRecordingTime(0);

      recordingIntervalRef.current = setInterval(() => {
        setRecordingTime((prev) => prev + 1);
      }, 1000);
    } catch (err) {
      setError(
        err instanceof Error
          ? err.message
          : "Microphone access denied. Please enable microphone permissions."
      );
    }
  };

  const stopRecording = () => {
    if (mediaRecorderRef.current && isRecording) {
      mediaRecorderRef.current.stop();
      setIsRecording(false);
      if (recordingIntervalRef.current) {
        clearInterval(recordingIntervalRef.current);
      }
    }
  };

  const transcribeAudio = async (audioBlob: Blob) => {
    try {
      setIsLoading(true);
      setError(null);

      const formData = new FormData();
      formData.append("file", audioBlob, "answer.wav");

      const res = await fetch(`${API_BASE}/transcribe`, {
        method: "POST",
        body: formData,
      });

      if (!res.ok) {
        const errorBody = await res.json().catch(() => null);
        throw new Error(errorBody?.detail || "Transcription failed");
      }

      const data = await res.json();
      setResponse(data.text || "");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to transcribe audio");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="portal-shell">
      <header className="portal-header">
        <div className="hero-copy">
          <span className="eyebrow">Interactive Interview Coach</span>
          <h1>AI Interview Preparation Portal</h1>
          <p>
            Role-specific questions, AI feedback, and candidate progress tracking. Log in to save your
            answers and build a reviewable response history.
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
            <div className="toggle-row">
              <button
                className={`toggle-button ${authMode === "login" ? "active" : ""}`}
                onClick={() => setAuthMode("login")}
                type="button"
              >
                Login
              </button>
              <button
                className={`toggle-button ${authMode === "register" ? "active" : ""}`}
                onClick={() => setAuthMode("register")}
                type="button"
              >
                Register
              </button>
            </div>

            <div className="input-grid">
              {authMode === "register" && (
                <input
                  className="input-field"
                  value={authName}
                  onChange={(event) => setAuthName(event.target.value)}
                  placeholder="Full name"
                  type="text"
                />
              )}
              <input
                className="input-field"
                value={authEmail}
                onChange={(event) => setAuthEmail(event.target.value)}
                placeholder="Email"
                type="email"
              />
              <input
                className="input-field"
                value={authPassword}
                onChange={(event) => setAuthPassword(event.target.value)}
                placeholder="Password"
                type="password"
              />
              <button
                className="button"
                onClick={authMode === "login" ? handleLogin : handleRegister}
                disabled={isLoading}
                type="button"
              >
                {isLoading ? "Processing..." : authMode === "login" ? "Login" : "Register"}
              </button>
            </div>

            <div className="auth-helper">
              <p>Register now to save answer history, review feedback later, and keep all interview progress in one place.</p>
            </div>
          </aside>
        ) : (
          <aside className="welcome-card">
            <div className="welcome-head">
              <div>
                <p className="eyebrow">Portal ready</p>
                <h2>Welcome back, {welcomeName}!</h2>
                <p>Use the portal to practice interview answers, get AI feedback, and keep a saved history of your sessions.</p>
              </div>
            </div>

            <div className="overview-row">
              <div className="overview-item">
                <strong>Saved responses</strong>
                <span>{history.length}</span>
              </div>
              <div className="overview-item">
                <strong>Selected role</strong>
                <span>{role}</span>
              </div>
            </div>

            <button className="button secondary" onClick={clearAuth} type="button">
              Logout
            </button>
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
            <div style={{ display: "grid", gap: 18 }}>
              <h2 className="card-title">Interview Analytics</h2>
              {!analytics ? (
                <div className="notice-banner">Sign in to unlock analytics, progress trends, and session score breakdowns.</div>
              ) : (
                <>
                  <div className="overview-row">
                    <div className="overview-item">
                      <strong>Total submissions</strong>
                      <span>{analytics.total_responses}</span>
                    </div>
                    <div className="overview-item">
                      <strong>Average score</strong>
                      <span>{analytics.avg_score}</span>
                    </div>
                    <div className="overview-item">
                      <strong>Avg technical</strong>
                      <span>{analytics.avg_technical_score}</span>
                    </div>
                    <div className="overview-item">
                      <strong>Avg communication</strong>
                      <span>{analytics.avg_communication_score}</span>
                    </div>
                  </div>

                  <div style={{ display: "grid", gap: 24 }}>
                    <div className="data-panel">
                      <h3>Performance trend</h3>
                      <ResponsiveContainer width="100%" height={200}>
                        <LineChart data={analytics.recent_trend} margin={{ top: 8, right: 14, left: 0, bottom: 0 }}>
                          <CartesianGrid strokeDasharray="3 3" />
                          <XAxis dataKey="date" />
                          <YAxis />
                          <Tooltip />
                          <Line type="monotone" dataKey="technical_score" stroke="#10b981" strokeWidth={3} />
                          <Line type="monotone" dataKey="communication_score" stroke="#2563eb" strokeWidth={3} />
                        </LineChart>
                      </ResponsiveContainer>
                    </div>

                    <div className="data-panel">
                      <h3>Role distribution</h3>
                      <ResponsiveContainer width="100%" height={220}>
                        <PieChart>
                          <Pie
                            data={Object.entries(analytics.role_breakdown).map(([name, value]) => ({ name, value }))}
                            dataKey="value"
                            nameKey="name"
                            cx="50%"
                            cy="50%"
                            outerRadius={80}
                            fill="#2563eb"
                            label
                          />
                          <Tooltip />
                        </PieChart>
                      </ResponsiveContainer>
                    </div>
                  </div>
                </>
              )}
            </div>
          ) : viewMode === "history" ? (
            <div>
              <h2 className="card-title">Saved Responses</h2>
              {history.length === 0 ? (
                <div className="notice-banner">No saved responses yet. Submit one answer to see it here.</div>
              ) : (
                <div className="history-list">
                  {history.map((item) => (
                    <article key={item.id} className="history-item">
                      <div style={{ display: "flex", justifyContent: "space-between", gap: 12, flexWrap: "wrap" }}>
                        <div style={{ fontWeight: 700 }}>{item.role}</div>
                        <time>{new Date(item.created_at).toLocaleString()}</time>
                      </div>
                      <p style={{ margin: "12px 0 6px" }}><strong>Type:</strong> {item.question_type}</p>
                      <p style={{ margin: "6px 0" }}><strong>Question:</strong> {item.question}</p>
                      <p style={{ margin: "6px 0" }}><strong>Answer:</strong> {item.response}</p>
                      <p style={{ margin: "6px 0" }}><strong>Feedback:</strong> {item.feedback}</p>
                      {item.duration_seconds != null && (
                        <p style={{ margin: "6px 0" }}><strong>Duration:</strong> {item.duration_seconds}s</p>
                      )}
                    </article>
                  ))}
                </div>
              )}
            </div>
          ) : (
            <>
              <h2 className="card-title">Practice a role-based interview</h2>
              <div style={{ display: "grid", gap: 16, marginBottom: 18 }}>
                <label style={{ display: "grid", gap: 8 }}>
                  Select Role:
                  <select className="select-field" value={role} onChange={handleRoleChange}>
                    {Object.keys(roleQuestions).map((roleName) => (
                      <option key={roleName} value={roleName}>
                        {roleName}
                      </option>
                    ))}
                  </select>
                </label>

                <label style={{ display: "grid", gap: 8 }}>
                  Question Type:
                  <select className="select-field" value={questionType} onChange={handleQuestionTypeChange}>
                    {questionTypes.map((type) => (
                      <option key={type} value={type}>
                        {type}
                      </option>
                    ))}
                  </select>
                </label>

                <label style={{ display: "grid", gap: 8 }}>
                  Timed mock interview:
                  <div style={{ display: "grid", gap: 10, gridTemplateColumns: "1fr auto" }}>
                    <select
                      className="select-field"
                      value={questionDuration}
                      onChange={(e) => setQuestionDuration(Number(e.target.value))}
                    >
                      {[60, 90, 120].map((seconds) => (
                        <option key={seconds} value={seconds}>
                          {seconds}s response window
                        </option>
                      ))}
                    </select>
                    <button className="button secondary" type="button" onClick={startTimedInterview}>
                      Start timed run
                    </button>
                  </div>
                </label>

                {timedMode && (
                  <div className="notice-banner">
                    Time remaining: <strong>{formatTimer(timeRemaining)}</strong>. Your answer will be sent with the session data when evaluated.
                  </div>
                )}
              </div>

              <div
                className="question-card"
                style={{ marginTop: 0, padding: 20, borderRadius: 20, border: "1px solid rgba(15,75,199,0.12)", background: "#fff" }}
              >
                <div style={{ fontSize: "0.95rem", color: "#5f6f8d", marginBottom: 8 }}>Question</div>
                <p style={{ margin: 0, fontSize: "1.05rem", fontWeight: 600, color: "#16203b" }}>{currentQuestion}</p>
              </div>

              <textarea
                className="textarea-input"
                value={response}
                onChange={(event) => setResponse(event.target.value)}
                placeholder="Type your answer here..."
              />

              <div className="button-row">
                {!isRecording ? (
                  <button
                    className="button record-btn"
                    onClick={startRecording}
                    type="button"
                    title="Record your answer using your microphone"
                  >
                    🎤 Record Answer
                  </button>
                ) : (
                  <button
                    className="button stop-btn"
                    onClick={stopRecording}
                    type="button"
                    title="Stop recording"
                  >
                    ⏹ Stop ({recordingTime}s)
                  </button>
                )}
                <button className="button" onClick={handleEvaluate} disabled={isLoading || isRecording} type="button">
                  {isLoading ? "Evaluating..." : "Evaluate Response"}
                </button>
                <button className="button secondary" onClick={handleNextQuestion} type="button">
                  Next Question
                </button>
              </div>

              {error && <div className="error-banner">{error}</div>}
              {feedback && (
                <div className="feedback-card">
                  <strong>Feedback</strong>
                  <p style={{ margin: "12px 0 0", whiteSpace: "pre-wrap" }}>{feedback}</p>
                </div>
              )}
            </>
          )}
        </main>
      </section>

      <section className="info-card" style={{ marginTop: 24 }}>
        <h2 className="card-title">Technology Concepts Covered</h2>
        <p style={{ marginTop: 0, color: "var(--muted)" }}>
          A full implementation connects this React UI to a FastAPI backend for AI prompt orchestration, uses a database for user progress, and enforces authentication and authorization for secure access.
        </p>
        <div className="feature-grid">
          {portalFeatures.map((feature) => (
            <span key={feature} className="feature-pill">
              {feature}
            </span>
          ))}
        </div>
      </section>

      {currentUser && viewMode === "practice" && (
        <section className="history-card" style={{ marginTop: 24 }}>
          <h2>Your Response History</h2>
          {history.length === 0 ? (
            <div className="notice-banner">No saved responses yet. Submit one answer to see it here.</div>
          ) : (
            <div className="history-list">
              {history.map((item) => (
                <article key={item.id} className="history-item">
                  <div style={{ display: "flex", justifyContent: "space-between", gap: 12, flexWrap: "wrap" }}>
                    <div style={{ fontWeight: 700 }}>{item.role}</div>
                    <time>{new Date(item.created_at).toLocaleString()}</time>
                  </div>
                  <p style={{ margin: "12px 0 6px" }}><strong>Type:</strong> {item.question_type}</p>
                  <p style={{ margin: "6px 0" }}><strong>Question:</strong> {item.question}</p>
                  <p style={{ margin: "6px 0" }}><strong>Response:</strong> {item.response}</p>
                  <p style={{ margin: "6px 0" }}><strong>Feedback:</strong> {item.feedback}</p>
                  {item.duration_seconds != null && (
                    <p style={{ margin: "6px 0" }}><strong>Duration:</strong> {item.duration_seconds}s</p>
                  )}
                </article>
              ))}
            </div>
          )}
        </section>
      )}
    </div>
  );
}

export default InterviewPrepPortal;
