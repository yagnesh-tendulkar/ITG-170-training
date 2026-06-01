import jwt
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

from auth.jwt_handler import verify_token

PUBLIC_PATHS = {
    "/login",
    "/openapi.json",
    "/docs",
    "/redoc",
    "/docs/oauth2-redirect",
    "/logs/stream",
}


def _get_bearer_token(request: Request) -> str | None:
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return None
    parts = auth_header.split()
    if len(parts) == 2 and parts[0].lower() == "bearer":
        return parts[1]
    return None


async def auth_middleware(request: Request, call_next):
    if request.url.path in PUBLIC_PATHS:
        return await call_next(request)

    token = _get_bearer_token(request)
    if token:
        try:
            payload = verify_token(token)
        except HTTPException as exc:
            return JSONResponse({"detail": exc.detail}, status_code=exc.status_code)

        request.state.user = payload
        return await call_next(request)

    return JSONResponse({"detail": "Authentication required"}, status_code=401)


def get_current_user(request: Request):
    user = getattr(request.state, "user", None)
    if not user:
        raise HTTPException(status_code=401, detail="Authentication required")
    return user
