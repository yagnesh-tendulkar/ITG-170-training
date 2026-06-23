# 🤖 AI Code Review Assistant

A full-stack learning project covering **React**, **FastAPI**, **SQLAlchemy**, **JWT Auth**, and **Google Gemini AI**.

---

## 🗂️ Project Structure

```
AIcodereviewer/
├── backend/    ← FastAPI Python server
└── frontend/   ← React (Vite) app
```

---

## 🚀 Quick Start

### 1. Start the Backend

```bash
cd backend
source venv/bin/activate   # On Windows: venv\Scripts\activate
uvicorn main:app --reload
```

Backend runs at: http://localhost:8000
Interactive API docs: http://localhost:8000/docs

### 2. Start the Frontend

```bash
cd frontend
npm run dev
```

Frontend runs at: http://localhost:5173

---

## 🔑 Add a Gemini API Key (Optional)

The app works without a key using mock AI responses. To get real AI reviews:

1. Visit https://aistudio.google.com/ and create a free API key
2. Open `backend/.env`
3. Set `GEMINI_API_KEY=your-key-here`
4. Restart the backend

---

## 📚 What You're Learning

### React Concepts
| File | Concept |
|------|---------|
| `context/AuthContext.jsx` | `createContext`, `useContext`, global state |
| `context/ToastContext.jsx` | Context pattern for notifications |
| `pages/LoginPage.jsx` | Controlled inputs, `useState`, form handling |
| `pages/DashboardPage.jsx` | `useEffect` for data fetching |
| `pages/HistoryPage.jsx` | Pagination, conditional rendering |
| `components/ReviewCard.jsx` | Props, tabs, list rendering with `.map()` |
| `components/ProtectedRoute.jsx` | Route guarding with React Router |
| `App.jsx` | `BrowserRouter`, `Routes`, `Route` |

### FastAPI Concepts
| File | Concept |
|------|---------|
| `main.py` | App setup, CORS middleware |
| `database.py` | SQLAlchemy engine, sessions, dependencies |
| `models.py` | ORM models, relationships, column types |
| `schemas.py` | Pydantic validation, request/response shapes |
| `auth.py` | JWT tokens, bcrypt hashing, OAuth2 |
| `routers/` | APIRouter, path params, query params |
| `services/` | Business logic layer separation |

### AI Concepts
| File | Concept |
|------|---------|
| `services/ai_service.py` | Prompt engineering, structured JSON output |

---

## 🧪 API Testing

Once the backend is running, visit http://localhost:8000/docs for a full interactive API explorer (Swagger UI). You can:
- Register a user
- Log in and get a token
- Test all endpoints directly in the browser

---

## 🏗️ Architecture

```
React Frontend (port 5173)
    ↕ HTTP + JWT
FastAPI Backend (port 8000)
    ↕ SQLAlchemy ORM
SQLite Database (codereview.db)
    
FastAPI Backend ↔ Google Gemini API (AI)
```
