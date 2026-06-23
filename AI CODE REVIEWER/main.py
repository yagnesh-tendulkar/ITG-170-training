# ─────────────────────────────────────────────
# main.py
#
# LEARNING NOTE:
# This is the entry point of the FastAPI application.
#
# Key concepts here:
#   - FastAPI() creates the app instance
#   - CORSMiddleware: allows our React frontend (running on port 5173)
#     to make requests to this backend (port 8000). Browsers block
#     cross-origin requests by default — CORS configures exceptions.
#   - app.include_router(): mounts our routers onto the main app
#   - @app.on_event("startup"): runs code when the server starts
# ─────────────────────────────────────────────

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine, Base
from routers import auth_router, review_router, docs_router

# Create all database tables from our models
# (equivalent to running CREATE TABLE IF NOT EXISTS in SQL)
Base.metadata.create_all(bind=engine)

# ── App Instance ────────────────────────────────────────────────

app = FastAPI(
    title="AI Code Review Assistant",
    description="An AI-powered code review API. Submit code and get bug reports, optimizations, and best practices.",
    version="1.0.0",
    # These appear in the auto-generated /docs page
)

# ── CORS Middleware ────────────────────────────────────────────────
# CORS = Cross-Origin Resource Sharing
# This tells the browser it's OK for our React app to call this API

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite dev server
        "http://localhost:3000",  # Alternative port
    ],
    allow_credentials=True,
    allow_methods=["*"],    # Allow GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],    # Allow Authorization header etc.
)

# ── Mount Routers ────────────────────────────────────────────────
# Each router handles a group of related endpoints

app.include_router(auth_router.router)
app.include_router(review_router.router)
app.include_router(docs_router.router)


# ── Root Endpoint ────────────────────────────────────────────────

@app.get("/", tags=["Health"])
def root():
    """
    Health check endpoint.
    Visit http://localhost:8000 to confirm the server is running.
    Visit http://localhost:8000/docs for the interactive API explorer!
    """
    return {
        "message": "AI Code Review Assistant API",
        "status": "running",
        "docs": "http://localhost:8000/docs",
    }


# ── Run directly with: python main.py ────────────────────────────
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
