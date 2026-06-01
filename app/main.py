from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from database import Base, engine
from models import User, Task  # noqa: F401 — needed for table creation
from routes import users_router, tasks_router, health_router
from middleware import RequestIDMiddleware, RequestLoggingMiddleware
from exceptions import register_exception_handlers
from logging_config import get_logger

logger = get_logger("main")

# ── Create all DB tables ──────────────────────────────────────────
Base.metadata.create_all(bind=engine)

# ── App instance ──────────────────────────────────────────────────
app = FastAPI(
    title="Smart Task & File Processing API",
    description="Production-ready FastAPI backend covering CRUD, Auth, Streaming, File Upload and more.",
    version="1.0.0",
)

# ── Built-in Middleware ───────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])

# ── Custom Middleware ─────────────────────────────────────────────
app.add_middleware(RequestLoggingMiddleware)
app.add_middleware(RequestIDMiddleware)

# ── Exception Handlers ────────────────────────────────────────────
register_exception_handlers(app)

# ── Routers ───────────────────────────────────────────────────────
app.include_router(health_router)
app.include_router(users_router)
app.include_router(tasks_router)


@app.get("/", tags=["Root"])
def root():
    return {"message": "Welcome to Smart Task API 🚀", "docs": "/docs"}


logger.info("Smart Task API started successfully")
