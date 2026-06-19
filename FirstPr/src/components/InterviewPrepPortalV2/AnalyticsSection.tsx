import {
  CartesianGrid,
  Cell,
  Legend,
  Line,
  LineChart,
  Pie,
  PieChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import type { DashboardData } from "./types";
import { BarChart2, TrendingUp } from "lucide-react";

const PIE_COLORS = ["#2563eb", "#10b981", "#f59e0b", "#ef4444", "#8b5cf6", "#06b6d4", "#f97316", "#84cc16"];

type Props = {
  dashboard: DashboardData | null;
};

export default function AnalyticsSection({ dashboard }: Props) {
  if (!dashboard) {
    return (
      <div className="empty-state">
        <BarChart2 size={40} strokeWidth={1.5} />
        <p>Complete an interview session to unlock analytics and progress charts.</p>
      </div>
    );
  }

  const roleData = Object.entries(dashboard.role_breakdown).map(([name, value]) => ({ name, value }));
  const typeData = Object.entries(dashboard.type_breakdown ?? {}).map(([name, value]) => ({ name, value }));

  return (
    <div className="analytics-wrap">
      <h2 className="section-title">Interview Analytics</h2>

      <div className="stats-grid">
        <div className="stat-card">
          <span className="stat-label">Sessions</span>
          <span className="stat-value">{dashboard.total_sessions}</span>
        </div>
        <div className="stat-card">
          <span className="stat-label">Answers</span>
          <span className="stat-value">{dashboard.total_answers}</span>
        </div>
        <div className="stat-card">
          <span className="stat-label">Avg Score</span>
          <span className="stat-value">{dashboard.average_score ?? 0}</span>
        </div>
        <div className="stat-card">
          <span className="stat-label">Avg Technical</span>
          <span className="stat-value">{dashboard.average_technical_score ?? 0}</span>
        </div>
        <div className="stat-card">
          <span className="stat-label">Avg Communication</span>
          <span className="stat-value">{dashboard.average_communication_score ?? 0}</span>
        </div>
        {dashboard.best_role && (
          <div className="stat-card accent">
            <span className="stat-label">Best Role</span>
            <span className="stat-value small">{dashboard.best_role}</span>
          </div>
        )}
      </div>

      {dashboard.recent_trend && dashboard.recent_trend.length > 0 && (
        <div className="chart-panel">
          <h3 className="chart-title">
            <TrendingUp size={16} /> Performance Trend
          </h3>
          <ResponsiveContainer width="100%" height={220}>
            <LineChart data={dashboard.recent_trend} margin={{ top: 8, right: 16, left: -10, bottom: 0 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="rgba(0,0,0,0.06)" />
              <XAxis dataKey="date" tick={{ fontSize: 11 }} />
              <YAxis domain={[0, 100]} tick={{ fontSize: 11 }} />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="score" stroke="#2563eb" strokeWidth={2.5} dot={false} name="Overall" />
              <Line type="monotone" dataKey="technical_score" stroke="#10b981" strokeWidth={2} dot={false} name="Technical" />
              <Line type="monotone" dataKey="communication_score" stroke="#f59e0b" strokeWidth={2} dot={false} name="Communication" />
            </LineChart>
          </ResponsiveContainer>
        </div>
      )}

      <div className="charts-row">
        {roleData.length > 0 && (
          <div className="chart-panel">
            <h3 className="chart-title">Role Distribution</h3>
            <ResponsiveContainer width="100%" height={220}>
              <PieChart>
                <Pie data={roleData} dataKey="value" nameKey="name" cx="50%" cy="50%" outerRadius={75} label>
                  {roleData.map((_, i) => (
                    <Cell key={i} fill={PIE_COLORS[i % PIE_COLORS.length]} />
                  ))}
                </Pie>
                <Tooltip />
              </PieChart>
            </ResponsiveContainer>
          </div>
        )}

        {typeData.length > 0 && (
          <div className="chart-panel">
            <h3 className="chart-title">Question Type Breakdown</h3>
            <ResponsiveContainer width="100%" height={220}>
              <PieChart>
                <Pie data={typeData} dataKey="value" nameKey="name" cx="50%" cy="50%" outerRadius={75} label>
                  {typeData.map((_, i) => (
                    <Cell key={i} fill={PIE_COLORS[(i + 3) % PIE_COLORS.length]} />
                  ))}
                </Pie>
                <Tooltip />
              </PieChart>
            </ResponsiveContainer>
          </div>
        )}
      </div>
    </div>
  );
}

