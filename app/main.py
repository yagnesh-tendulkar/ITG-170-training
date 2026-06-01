from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from sqlalchemy.exc import SQLAlchemyError

from app.database.connection import Base, engine
from app.exceptions.exception_handlers import register_exception_handlers
from app.logging.logger import get_logger
from app.middleware.request_id_middleware import RequestIDMiddleware
from app.middleware.request_logging import RequestLoggingMiddleware
from app.routes.auth_routes import router as auth_router
from app.routes.attendance_routes import router as attendance_router
from app.routes.department_routes import router as department_router
from app.routes.employee_routes import router as employee_router
from app.routes.health_routes import router as health_router
from app.routes.leave_routes import router as leave_router


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="SmartAPI Backend",
        description="A production-style FastAPI backend using SQLite, SQLAlchemy, and Pydantic v2.",
        version="1.0.0",
    )

    app.logger = get_logger("app")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(GZipMiddleware, minimum_size=1000)
    app.add_middleware(RequestIDMiddleware)
    app.add_middleware(RequestLoggingMiddleware)

    register_exception_handlers(app)

    app.include_router(auth_router)
    app.include_router(employee_router)
    app.include_router(department_router)
    app.include_router(attendance_router)
    app.include_router(leave_router)
    app.include_router(health_router)

    @app.get("/", summary="Application info")
    async def root() -> dict[str, str]:
        return {
            "app": app.title,
            "description": app.description,
            "version": app.version,
            "status": "running",
        }

    @app.on_event("startup")
    async def startup_event() -> None:
        try:
            Base.metadata.create_all(bind=engine)
        except SQLAlchemyError as error:
            app.logger.error("Database initialization failed: %s", error)
            raise

    @app.on_event("shutdown")
    async def shutdown_event() -> None:
        engine.dispose()

    return app


app = create_app()


__all__ = ["app"]
