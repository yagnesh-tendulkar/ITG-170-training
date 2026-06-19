import type { HistoryRecord } from "./types";
import { Calendar, Clock, Copy } from "lucide-react";

type Props = {
  history: HistoryRecord[];
};

export default function HistorySection({ history }: Props) {
  const handleCopy = (text: string) => {
    navigator.clipboard.writeText(text);
  };

  if (history.length === 0) {
    return (
      <div className="empty-state">
        <History size={40} strokeWidth={1.5} />
        <p>No saved responses yet. Submit an answer to see your history here.</p>
      </div>
    );
  }

  return (
    <div className="history-wrap">
      <h2 className="section-title">Response History</h2>

      <div className="history-list">
        {history.map((item, idx) => (
          <article key={item.id} className="history-item">
            <div className="item-header">
              <div className="item-meta">
                <span className="item-index">#{idx + 1}</span>
                <span className="item-role">{item.role}</span>
                <span className="item-type">{item.question_type}</span>
              </div>
              <div className="item-time">
                <Calendar size={13} />
                {new Date(item.created_at).toLocaleDateString()}
              </div>
            </div>

            <div className="item-content">
              <div className="question-block">
                <strong>Question:</strong>
                <p>{item.question}</p>
              </div>

              <div className="response-block">
                <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                  <strong>Your Response:</strong>
                  <button
                    className="icon-btn"
                    onClick={() => handleCopy(item.response)}
                    title="Copy response"
                  >
                    <Copy size={14} />
                  </button>
                </div>
                <p>{item.response}</p>
              </div>

              {item.feedback && (
                <div className="feedback-block">
                  <strong>Feedback:</strong>
                  <p>{item.feedback}</p>
                </div>
              )}
            </div>

            <div className="item-footer">
              <div className="score-badges">
                <span className="score-badge">Overall: {item.score}</span>
                <span className="score-badge">Technical: {item.technical_score}</span>
                <span className="score-badge">Communication: {item.communication_score}</span>
                {item.confidence_score !== undefined && (
                  <span className="score-badge">Confidence: {item.confidence_score}</span>
                )}
                {item.clarity_score !== undefined && (
                  <span className="score-badge">Clarity: {item.clarity_score}</span>
                )}
              </div>
              {item.duration_seconds && (
                <span className="duration-info">
                  <Clock size={13} /> {Math.round(item.duration_seconds / 60)}m {item.duration_seconds % 60}s
                </span>
              )}
            </div>
          </article>
        ))}
      </div>
    </div>
  );
}

function History({ size, strokeWidth }: { size: number; strokeWidth: number }) {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth={strokeWidth}
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <circle cx="12" cy="12" r="10" />
      <polyline points="12 6 12 12 16 14" />
    </svg>
  );
}

