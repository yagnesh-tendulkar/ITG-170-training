import time

from starlette.middleware.base import BaseHTTPMiddleware


class LoggingMiddleware(
    BaseHTTPMiddleware
):

    async def dispatch(
        self,
        request,
        call_next
    ):
        start = time.time()

        response = await call_next(
            request
        )

        process_time = (
            time.time() - start
        )

        print(
            f"{request.method} "
            f"{request.url.path} "
            f"{process_time:.4f}s"
        )

        return response