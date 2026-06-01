from fastapi import Request
from fastapi.responses import JSONResponse

from app.logging.logger import logger


async def global_exception_handler(request: Request, exc: Exception):

    logger.error(f"ERROR at {request.url.path} | {str(exc)}")

    return JSONResponse(
        status_code=500,
        content={
            "message": "Internal Server Error",
            "detail": str(exc)
        }
    )