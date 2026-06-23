// ─────────────────────────────────────────────
// components/Navbar.jsx
//
// LEARNING NOTE:
// This uses the NavLink component from react-router-dom.
// NavLink automatically adds an "active" class when its href
// matches the current URL — great for highlighting the current page.
// ─────────────────────────────────────────────

import { NavLink, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { useToast } from '../context/ToastContext';

const navLinks = [
  { to: '/dashboard', label: '📊 Dashboard' },
  { to: '/review',   label: '🔍 New Review' },
  { to: '/history',  label: '📋 History' },
  { to: '/docs-gen', label: '📝 Docs Generator' },
];

function Navbar() {
  const { user, logout } = useAuth();
  const { showToast } = useToast();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    showToast('Logged out successfully', 'info');
    navigate('/login');
  };

  const initials = user?.username?.slice(0, 2).toUpperCase() || '?';

  return (
    <nav className="navbar">
      <div className="navbar-inner">
        {/* Brand / Logo */}
        <NavLink to="/dashboard" className="navbar-brand">
          <span className="navbar-brand-icon">🤖</span>
          <span>CodeReview AI</span>
        </NavLink>

        {/* Navigation links */}
        <div className="navbar-nav">
          {navLinks.map((link) => (
            <NavLink
              key={link.to}
              to={link.to}
              className={({ isActive }) => `nav-link${isActive ? ' active' : ''}`}
            >
              {link.label}
            </NavLink>
          ))}
        </div>

        {/* User section */}
        <div className="navbar-user">
          <div className="navbar-avatar">{initials}</div>
          <span className="navbar-username">{user?.username}</span>
          <button className="btn btn-ghost btn-sm" onClick={handleLogout}>
            Logout
          </button>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
