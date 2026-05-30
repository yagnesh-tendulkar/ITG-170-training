"""Custom global exception handlers (placeholder)."""
from fastapi import Request
from fastapi.responses import JSONResponse

async def http_exception_handler(request: Request, exc):
    return JSONResponse({"detail": str(exc)}, status_code=500)
