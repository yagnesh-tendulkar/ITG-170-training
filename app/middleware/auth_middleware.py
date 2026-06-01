from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse

class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        public_routes = [
            "/auth/login",
            "/auth/register",
            "/docs",
            "/openapi.json"
        ]

        if request.url.path in public_routes:
            return await call_next(request)

        token = request.headers.get("Authorization")

        if not token:
            return JSONResponse(
                status_code=401,
                content={
                    "message": "Token Required"
                }
            )

        return await call_next(request)