import time
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from app.logging_conf import logger

__all__ = ["LoggingMiddleware", "add_security"]

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start = time.time()

        response = await call_next(request)

        duration = round((time.time() - start) * 1000)

        logger.info(f"{request.method} {request.url.path} {response.status_code} {duration}ms")

        return response


def add_security(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )