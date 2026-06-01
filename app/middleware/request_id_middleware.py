import uuid
from typing import Callable

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response


class RequestIDMiddleware(BaseHTTPMiddleware):
    """
    Custom middleware for generating and tracking unique request IDs.

    Generates a UUID for each incoming request, stores it in request state,
    and adds it to response headers for request tracing and debugging.
    """

    async def dispatch(
        self,
        request: Request,
        call_next: Callable,
    ) -> Response:
        """
        Generate a unique request ID and attach it to the request and response.

        Args:
            request: The incoming HTTP request object.
            call_next: Callable function that processes the request through the route.

        Returns:
            Response: The HTTP response with request ID in headers.
        """
        # Generate a unique UUID for this request
        request_id: str = str(uuid.uuid4())

        # Store request ID in request state for access in route handlers
        request.state.request_id = request_id

        # Process the request through the route handler
        response: Response = await call_next(request)

        # Add request ID to response headers for client tracking
        response.headers["X-Request-ID"] = request_id

        return response
