from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

from core.config import settings

from core.database import (
    Base,
    engine
)

# Import Models

# Import Routers
from routes.auth_routes import (
    router as auth_router
)

from routes.task_routes import (
    router as task_router
)

from routes.upload_routes import (
    router as upload_router
)

from routes.stream_routes import (
    router as stream_router
)

from routes.health_routes import (
    router as health_router
)

# Import Middleware
from middleware.logging_middleware import (
    LoggingMiddleware
)

from middleware.request_id_middleware import (
    RequestIDMiddleware
)

# Import Exceptions
from exceptions.custom_exceptions import (
    TaskNotFoundException,
    UserNotFoundException,
    FileValidationException,
    AuthenticationException,
    AuthorizationException
)

from exceptions.exception_handlers import (
    task_not_found_handler,
    user_not_found_handler,
    file_validation_handler,
    authentication_handler,
    authorization_handler,
    generic_exception_handler
)
# Import Models
from models.user_model import User
from models.task_model import Task
from models.file_model import File

# Create Database Tables
Base.metadata.create_all(bind=engine)

# FastAPI App
app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION
)

# =========================
# Built-in Middleware
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.add_middleware(
    GZipMiddleware,
    minimum_size=1000
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"]
)

app.add_middleware(
    RequestIDMiddleware
)

app.add_middleware(
    LoggingMiddleware
)

app.add_exception_handler(
    TaskNotFoundException,
    task_not_found_handler
)

app.add_exception_handler(
    UserNotFoundException,
    user_not_found_handler
)

app.add_exception_handler(
    FileValidationException,
    file_validation_handler
)

app.add_exception_handler(
    AuthenticationException,
    authentication_handler
)

app.add_exception_handler(
    AuthorizationException,
    authorization_handler
)

app.add_exception_handler(
    Exception,
    generic_exception_handler
)

app.include_router(auth_router)

app.include_router(task_router)

app.include_router(upload_router)

app.include_router(stream_router)

app.include_router(health_router)

@app.get("/")
def root():

    return {
        "message": "Welcome to Smart Task API",
        "version": settings.APP_VERSION,
        "status": "running"
    }