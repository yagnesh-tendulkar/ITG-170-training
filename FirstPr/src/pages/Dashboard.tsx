function Dashboard() {
  return (
    <div style={{ padding: 24, fontFamily: "Inter, sans-serif" }}>
      <h1>Interview Dashboard</h1>
      <p>Track your interview performance, saved sessions, and recommended next steps.</p>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(240px, 1fr))", gap: 20, marginTop: 24 }}>
        <div style={{ borderRadius: 18, padding: 20, background: "#ffffff", boxShadow: "0 8px 24px rgba(0, 0, 0, 0.05)" }}>
          <h2>Recent Sessions</h2>
          <p>View your latest questions and AI feedback to refine your answers.</p>
        </div>
        <div style={{ borderRadius: 18, padding: 20, background: "#ffffff", boxShadow: "0 8px 24px rgba(0, 0, 0, 0.05)" }}>
          <h2>Top Metrics</h2>
          <p>Analyze communication and technical scores across interviews.</p>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
