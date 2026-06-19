import {
  BarChart,
  Bar,
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

const interviewTrend = [
  { name: "Week 1", communication: 65, technical: 70 },
  { name: "Week 2", communication: 72, technical: 74 },
  { name: "Week 3", communication: 78, technical: 80 },
  { name: "Week 4", communication: 82, technical: 84 },
];

const scoreBreakdown = [
  { name: "Technical", value: 84 },
  { name: "Communication", value: 78 },
  { name: "Improvement", value: 70 },
];

function Analytics() {
  return (
    <div style={{ padding: 24, fontFamily: "Inter, sans-serif" }}>
      <h1>Interview Analytics</h1>
      <section style={{ display: "grid", gap: 24, marginTop: 24 }}>
        <div style={{ display: "grid", gap: 8 }}>
          <div style={{ fontSize: 14, color: "#6b7280" }}>Total Interviews</div>
          <div style={{ fontSize: 32, fontWeight: 700 }}>24</div>
        </div>

        <div style={{ display: "grid", gap: 8 }}>
          <div style={{ fontSize: 14, color: "#6b7280" }}>Average Score</div>
          <div style={{ fontSize: 32, fontWeight: 700 }}>81</div>
        </div>
      </section>

      <section style={{ display: "grid", gap: 36, marginTop: 40 }}>
        <div style={{ width: "100%", height: 280, background: "#ffffff", borderRadius: 20, padding: 20, boxShadow: "0 4px 16px rgba(15, 23, 42, 0.08)" }}>
          <h2>Communication Trend</h2>
          <ResponsiveContainer width="100%" height={200}>
            <LineChart data={interviewTrend} margin={{ top: 8, right: 16, left: 0, bottom: 0 }}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Line type="monotone" dataKey="communication" stroke="#2563eb" strokeWidth={3} />
            </LineChart>
          </ResponsiveContainer>
        </div>

        <div style={{ width: "100%", height: 280, background: "#ffffff", borderRadius: 20, padding: 20, boxShadow: "0 4px 16px rgba(15, 23, 42, 0.08)" }}>
          <h2>Technical Trend</h2>
          <ResponsiveContainer width="100%" height={200}>
            <BarChart data={interviewTrend} margin={{ top: 8, right: 16, left: 0, bottom: 0 }}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="technical" fill="#10b981" radius={[6, 6, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>

        <div style={{ width: "100%", height: 320, background: "#ffffff", borderRadius: 20, padding: 20, boxShadow: "0 4px 16px rgba(15, 23, 42, 0.08)" }}>
          <h2>Score Breakdown</h2>
          <ResponsiveContainer width="100%" height={250}>
            <PieChart>
              <Pie data={scoreBreakdown} dataKey="value" nameKey="name" cx="50%" cy="50%" outerRadius={90} fill="#2563eb" label />
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>
      </section>
    </div>
  );
}

export default Analytics;
