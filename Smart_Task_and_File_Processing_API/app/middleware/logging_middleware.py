import time

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from utils.logger import logger


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(
        self,
        request: Request,
        call_next
    ):

        start_time = time.time()

        logger.info(
            f"Request Started | "
            f"Method={request.method} "
            f"Path={request.url.path}"
        )

        response = await call_next(request)

        process_time = round(
            (time.time() - start_time) * 1000,
            2
        )

        logger.info(
            f"Request Completed | "
            f"Method={request.method} "
            f"Path={request.url.path} "
            f"Status={response.status_code} "
            f"Time={process_time}ms"
        )

        return response