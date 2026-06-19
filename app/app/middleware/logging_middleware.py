from starlette.middleware.base import BaseHTTPMiddleware

class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        print(f"Request Path: {request.url.path}")

        response = await call_next(request)

        print(f"Response Status: {response.status_code}")

        return response