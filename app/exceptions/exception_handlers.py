"""
Centralized exception handlers for the FastAPI application.

Provides a single `register_exception_handlers` function that wires handlers
for application-specific `AppException` types as well as framework and
infrastructure errors (HTTPException, ValidationError, SQLAlchemyError,
and a global catch-all).

Handlers return a consistent JSON structure and log errors via the app's
configured logger when available.
"""
from __future__ import annotations

import logging
from typing import Any, Dict

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError
from starlette.exceptions import HTTPException as StarletteHTTPException

from .custom_exceptions import (
    AppException,
    BadRequestException,
    ConflictException,
    ForbiddenException,
    NotFoundException,
    UnauthorizedException,
)


def _get_app_logger(app: FastAPI) -> logging.Logger:
    """
    Retrieve a logger from the FastAPI `app` object if available.

    Tries the following in order:
    - `app.logging.logger` (recommended if an app-level logging wrapper exists)
    - `app.logger` attribute
    - fallback to the module logger
    """
    logger = None
    app_logging = getattr(app, "logging", None)
    if app_logging is not None:
        logger = getattr(app_logging, "logger", None)
    if logger is None:
        logger = getattr(app, "logger", None)
    if logger is None:
        logger = logging.getLogger("app.exception_handlers")
    return logger


def _error_payload(error_type: str, message: str, details: Any | None = None) -> Dict[str, Any]:
    """Build the standardized error payload."""
    payload: Dict[str, Any] = {
        "success": False,
        "error": {"type": error_type, "message": message, "details": details or {}},
    }
    return payload


def register_exception_handlers(app: FastAPI) -> None:
    """
    Register centralized exception handlers on the provided FastAPI app.

    This function attaches handlers for:
    - `AppException` and its concrete subclasses
    - Starlette `HTTPException`
    - Pydantic `ValidationError`
    - SQLAlchemy `SQLAlchemyError`
    - global `Exception` (catch-all)

    Args:
        app: FastAPI application instance to register handlers on.
    """
    logger = _get_app_logger(app)

    async def _handle_app_exception(request: Request, exc: AppException) -> JSONResponse:
        logger.exception("AppException caught: %s", exc)
        payload = _error_payload(type(exc).__name__, exc.message, exc.details)
        return JSONResponse(status_code=exc.status_code, content=payload)

    async def _handle_starlette_http_exception(request: Request, exc: StarletteHTTPException) -> JSONResponse:
        # Starlette HTTP exceptions already carry a status code and detail
        logger.exception("HTTPException caught: %s", exc)
        message = getattr(exc, "detail", str(exc))
        payload = _error_payload("HTTPException", message, {})
        return JSONResponse(status_code=getattr(exc, "status_code", 500), content=payload)

    async def _handle_validation_error(request: Request, exc: ValidationError) -> JSONResponse:
        logger.exception("ValidationError caught: %s", exc)
        # Pydantic ValidationError has .errors() which is useful for clients
        details = exc.errors() if hasattr(exc, "errors") else None
        payload = _error_payload("ValidationError", "Request validation failed", details)
        return JSONResponse(status_code=422, content=payload)

    async def _handle_sqlalchemy_error(request: Request, exc: SQLAlchemyError) -> JSONResponse:
        logger.exception("SQLAlchemyError caught: %s", exc)
        # Hide DB internals from clients; surface a generic message and optionally details in logs
        payload = _error_payload("DatabaseError", "Internal database error", {})
        return JSONResponse(status_code=500, content=payload)

    async def _handle_generic_exception(request: Request, exc: Exception) -> JSONResponse:
        logger.exception("Unhandled exception caught: %s", exc)
        payload = _error_payload("InternalServerError", "An unexpected error occurred", {})
        return JSONResponse(status_code=500, content=payload)

    # Register handlers for custom AppException and its common subtypes
    app.add_exception_handler(AppException, _handle_app_exception)
    app.add_exception_handler(NotFoundException, _handle_app_exception)
    app.add_exception_handler(BadRequestException, _handle_app_exception)
    app.add_exception_handler(UnauthorizedException, _handle_app_exception)
    app.add_exception_handler(ForbiddenException, _handle_app_exception)
    app.add_exception_handler(ConflictException, _handle_app_exception)

    # Register framework and infrastructure handlers
    app.add_exception_handler(StarletteHTTPException, _handle_starlette_http_exception)
    app.add_exception_handler(ValidationError, _handle_validation_error)
    app.add_exception_handler(SQLAlchemyError, _handle_sqlalchemy_error)

    # Global catch-all should be last fallback
    app.add_exception_handler(Exception, _handle_generic_exception)
