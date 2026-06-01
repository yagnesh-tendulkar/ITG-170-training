import os
import logging

from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from database.db import create_database, migrate_schema
from exceptions import AppException
from middleware.CORSMiddleware import set_cors
from middleware.CustomMiddleware import log_requests
from routes.auth import router as auth_router
from routes.users import router as user_router
from routes.tasks import router as task_router
from services.user_service import create_demo_user

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def _is_enabled(value: str | None) -> bool:
    return str(value or "").lower() in ("1", "true", "yes")


def _initialize_database() -> None:
    if not _is_enabled(os.getenv("RUN_DB_CREATE", "1")):
        return
    try:
        create_database()
        try:
            migrate_schema()
        except Exception:
            logger.warning("Schema migration failed on startup; continuing.")
    except Exception as exc:
        logger.warning(
            "Database creation/connection failed on startup: %s. "
            "Set DB_* env vars correctly or set RUN_DB_CREATE=0 to skip automatic creation.",
            exc,
        )


def _initialize_demo_user() -> None:
    if not _is_enabled(os.getenv("AUTH_DISABLED", "0")):
        return
    try:
        create_demo_user()
    except Exception as exc:
        logger.warning("Demo user creation failed on startup: %s", exc)


def _error_response(status_code: int, code: str, detail):
    return JSONResponse(
        status_code=status_code,
        content={
            "status": "error",
            "code": code,
            "detail": detail,
        },
    )

_initialize_database()
_initialize_demo_user()

app = FastAPI()


@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    logger.error("AppException: %s", exc.detail)
    return _error_response(exc.status_code, exc.code, exc.detail)


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.warning("HTTPException: %s", exc.detail)
    return _error_response(exc.status_code, "http_error", exc.detail)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.warning("Validation error: %s", exc)
    return _error_response(422, "validation_error", exc.errors())


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    logger.exception("Unhandled exception: %s", exc)
    return _error_response(500, "internal_server_error", "An unexpected error occurred.")

set_cors(app)
app.middleware("http")(log_requests)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(task_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
