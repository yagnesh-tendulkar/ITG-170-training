"""
Request logging middleware for the SmartAPI backend.

Logs incoming requests and outgoing responses at INFO level while preserving
request timing and request ID tracing.
"""
from __future__ import annotations

import logging
import time
from typing import Callable

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """Middleware that logs request and response metadata."""

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        logger = getattr(request.app, "logger", logging.getLogger("app.request_logging"))
        request_id = getattr(request.state, "request_id", None)
        start_time = time.perf_counter()

        logger.info(
            "Request started: %s %s %s",
            request.method,
            request.url.path,
            f"request_id={request_id}" if request_id else "",
        )

        response = await call_next(request)
        elapsed_ms = (time.perf_counter() - start_time) * 1000

        logger.info(
            "Request completed: %s %s %s status=%s duration=%.2fms",
            request.method,
            request.url.path,
            f"request_id={request_id}" if request_id else "",
            response.status_code,
            elapsed_ms,
        )

        return response
