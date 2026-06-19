import { useState } from "react";
import { Eye, EyeOff, LogIn, UserPlus } from "lucide-react";

type Props = {
  onLogin: (email: string, password: string) => void;
  onRegister: (name: string, email: string, password: string) => void;
  error: string | null;
  disabled: boolean;
};

export default function AuthPanel({ onLogin, onRegister, error, disabled }: Props) {
  const [mode, setMode] = useState<"login" | "register">("login");
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (mode === "login") {
      onLogin(email, password);
    } else {
      onRegister(name, email, password);
    }
  };

  return (
    <div className="auth-panel">
      <div className="auth-tabs">
        <button
          type="button"
          className={`auth-tab ${mode === "login" ? "active" : ""}`}
          onClick={() => setMode("login")}
        >
          <LogIn size={15} />
          Login
        </button>
        <button
          type="button"
          className={`auth-tab ${mode === "register" ? "active" : ""}`}
          onClick={() => setMode("register")}
        >
          <UserPlus size={15} />
          Register
        </button>
      </div>

      <form className="auth-form" onSubmit={handleSubmit}>
        {mode === "register" && (
          <div className="field-group">
            <label className="field-label">Full name</label>
            <input
              className="input-field"
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="Jane Doe"
              required
              autoComplete="name"
            />
          </div>
        )}

        <div className="field-group">
          <label className="field-label">Email</label>
          <input
            className="input-field"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="you@example.com"
            required
            autoComplete="email"
          />
        </div>

        <div className="field-group">
          <label className="field-label">Password</label>
          <div className="password-wrap">
            <input
              className="input-field"
              type={showPassword ? "text" : "password"}
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="••••••••"
              required
              autoComplete={mode === "login" ? "current-password" : "new-password"}
            />
            <button
              type="button"
              className="password-toggle"
              onClick={() => setShowPassword((v) => !v)}
              tabIndex={-1}
            >
              {showPassword ? <EyeOff size={16} /> : <Eye size={16} />}
            </button>
          </div>
        </div>

        {error && <div className="error-banner">{error}</div>}

        <button type="submit" className="button primary full-width" disabled={disabled}>
          {disabled
            ? "Processing..."
            : mode === "login"
            ? "Sign in"
            : "Create account"}
        </button>
      </form>

      <p className="auth-hint">
        {mode === "login"
          ? "No account yet? Switch to Register above."
          : "Already have an account? Switch to Login above."}
      </p>
    </div>
  );
}
