from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.base import Base
from app.database.session import engine
# ROUTES
from app.api.v1.auth import router as auth_router
from app.api.v1.files import router as files_router
from app.api.v1.background import router as bg_router
from app.api.v1.health import router as health_router
from app.api.v1.tasks import router as tasks_router
import app.models

# MIDDLEWARE
from app.logging.middleware import LoggingMiddleware

# EXCEPTION HANDLERS
from fastapi.exceptions import RequestValidationError
from app.exceptions.base import AppException
from app.exceptions.handlers import (
    app_exception_handler,
    validation_exception_handler,
    global_exception_handler
)

app = FastAPI(
    title="Smart Task & File Processing API",
    version="1.0.0"
)

# -----------------------------
# MIDDLEWARE REGISTRATION
# -----------------------------
app.add_middleware(LoggingMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# ROUTER REGISTRATION
# -----------------------------
app.include_router(auth_router)
app.include_router(tasks_router)
app.include_router(files_router)
app.include_router(bg_router)
app.include_router(health_router)


# -----------------------------
# EXCEPTION HANDLERS
# -----------------------------
app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)

Base.metadata.create_all(bind=engine)
# -----------------------------
# ROOT ENDPOINT
# -----------------------------
@app.get("/")
def root():
    return {
        "message": "Smart Task & File API is running 🚀"
    }