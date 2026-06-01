import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

from app.logging.logger import logger


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        start_time = time.time()

        response = await call_next(request)

        process_time = time.time() - start_time

        log_msg = (
            f"{request.method} {request.url.path} "
            f"| status={response.status_code} "
            f"| time={round(process_time * 1000, 2)}ms"
        )

        logger.info(log_msg)

        return response