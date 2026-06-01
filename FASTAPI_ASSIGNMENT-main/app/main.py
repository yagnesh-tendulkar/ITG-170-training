import os
import logging

from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from app.database.db import create_database, migrate_schema
from app.exceptions import AppException
from app.middleware.CORSMiddleware import set_cors
from app.middleware.CustomMiddleware import log_requests
from app.services.user_service import create_demo_user
from app.routes.auth import router as auth_router
from app.routes.users import route as user_router
from app.routes.tasks import router as task_router

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if os.getenv("RUN_DB_CREATE", "1") == "1":
    try:
        create_database()
        try:
            migrate_schema()
        except Exception:
            logger.warning("Schema migration failed on startup; continuing.")
    except Exception as e:
        logger.warning(
            "Database creation/connection failed on startup: %s. "
            "Set DB_* env vars correctly or set RUN_DB_CREATE=0 to skip automatic creation.",
            e,
        )

if os.getenv("AUTH_DISABLED", "0").lower() in ("1", "true", "yes"):
    try:
        create_demo_user()
    except Exception as e:
        logger.warning("Demo user creation failed on startup: %s", e)

app = FastAPI()


@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    logger.error("AppException: %s", exc.detail)
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": "error",
            "code": exc.code,
            "detail": exc.detail,
        },
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.warning("HTTPException: %s", exc.detail)
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": "error",
            "code": "http_error",
            "detail": exc.detail,
        },
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.warning("Validation error: %s", exc)
    return JSONResponse(
        status_code=422,
        content=jsonable_encoder({
            "status": "error",
            "code": "validation_error",
            "detail": exc.errors(),
        }),
    )


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    logger.exception("Unhandled exception: %s", exc)
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "code": "internal_server_error",
            "detail": "An unexpected error occurred.",
        },
    )


set_cors(app)

app.middleware("http")(log_requests)

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(task_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        reload=True
    )