import logging
import time
from typing import Callable

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

logger = logging.getLogger(__name__)


class LoggingMiddleware(BaseHTTPMiddleware):
    """
    Custom middleware for logging HTTP requests and responses.

    Logs detailed information about each request including method, URL, IP address,
    response status code, and processing time.
    """

    async def dispatch(
        self,
        request: Request,
        call_next: Callable,
    ) -> Response:
        """
        Process the request, log details, and return the response.

        Args:
            request: The incoming HTTP request object.
            call_next: Callable function that processes the request through the route.

        Returns:
            Response: The HTTP response from the route handler.
        """
        # Extract request details
        method: str = request.method
        url: str = str(request.url)
        client_ip: str = self._get_client_ip(request)
        path: str = request.url.path

        # Log incoming request
        logger.info(
            f"Request started: {method} {path} from {client_ip}"
        )

        # Record start time for processing time calculation
        start_time: float = time.time()

        try:
            # Call the route handler
            response: Response = await call_next(request)
        except Exception as exc:
            # Log any exceptions that occur during request processing
            processing_time: float = (time.time() - start_time) * 1000  # ms
            logger.error(
                f"Request error: {method} {path} from {client_ip} - "
                f"Exception: {str(exc)} ({processing_time:.2f}ms)"
            )
            raise

        # Calculate processing time in milliseconds
        processing_time: float = (time.time() - start_time) * 1000

        # Extract response status code
        status_code: int = response.status_code

        # Log outgoing response with all details
        logger.info(
            f"Request completed: {method} {path} {status_code} "
            f"from {client_ip} ({processing_time:.2f}ms)"
        )

        # Add custom headers for monitoring
        response.headers["X-Process-Time"] = str(processing_time / 1000)

        return response

    @staticmethod
    def _get_client_ip(request: Request) -> str:
        """
        Extract the client IP address from the request.

        Checks X-Forwarded-For header first (for proxied requests),
        then falls back to the direct client connection IP.

        Args:
            request: The HTTP request object.

        Returns:
            str: The client IP address.
        """
        if request.headers.get("x-forwarded-for"):
            return request.headers.get("x-forwarded-for").split(",")[0].strip()
        return request.client.host if request.client else "unknown"
