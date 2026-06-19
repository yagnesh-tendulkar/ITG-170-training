# FirstPr Interview Preparation Portal

A React + TypeScript frontend with a FastAPI backend for AI-powered interview practice.

## What is included

- Real AI-backed question generation and evaluation.
- Timed mock interview sessions with auto-submit.
- Personalized AI feedback reports after each session.
- Progress analytics and history tracking.
- Docker compose for local dev and Render/Vercel deployment support.

## Project structure

- `backend/` — FastAPI backend with AI orchestration, auth, and persistence.
- `src/` — React + TypeScript frontend built with Vite.
- `src/components/InterviewPrepPortalV2.tsx` — upgraded interview portal component.
- `docker-compose.yml` — local PostgreSQL, frontend, and backend services.
- `render.yaml` — Render deployment configuration.
- `vercel.json` — frontend deployment configuration.

## Local development

### Backend

1. Create a virtual environment.
2. Install requirements:

```bash
python -m pip install -r backend/requirements.txt
```

3. Copy `.env.example` to `.env` and configure secrets:

```bash
cp .env.example .env
```

4. Start the backend server:

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend

1. Install dependencies:

```bash
npm install
```

2. Start the React app:

```bash
npm run dev
```

### Docker compose

Run the full local stack:

```bash
docker compose up --build
```

## Environment variables

Use `.env.example` as a template:

```bash
DATABASE_URL=postgresql://user:password@localhost:5432/interview
SECRET_KEY=replace-with-a-secure-secret
ACCESS_TOKEN_EXPIRE_MINUTES=30
CORS_ORIGINS=http://localhost:5173
GEMINI_API_KEY=
OPENAI_API_KEY=
```

## Deployment

### Vercel

- The frontend is deployed as a static site using `vercel.json`.
- Point `VITE_API_BASE` to your backend API URL in Vercel environment variables.

### Render

- `render.yaml` defines a Python web service for the backend and a static service for the frontend.
- Set the backend env vars: `DATABASE_URL`, `SECRET_KEY`, `GEMINI_API_KEY`, `OPENAI_API_KEY`, and `CORS_ORIGINS`.

## API endpoints

- `POST /api/auth/register`
- `POST /api/auth/login`
- `GET /api/auth/me`
- `GET /api/questions`
- `POST /api/interview/session`
- `POST /api/interview/session/{session_id}/answer`
- `POST /api/interview/session/{session_id}/complete`
- `GET /api/analytics/dashboard`
- `GET /api/analytics/progress`

## Notes

- If `OPENAI_API_KEY` is set, the backend will use OpenAI for richer, real AI feedback.
- Without an API key, the backend still provides a fallback scoring flow so the portal remains usable.
- The upgraded portal in `src/components/InterviewPrepPortalV2.tsx` is now the default app experience.
