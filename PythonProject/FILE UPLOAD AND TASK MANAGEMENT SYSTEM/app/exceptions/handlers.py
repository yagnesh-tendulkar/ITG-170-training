from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from app.exceptions.base import AppException
from app.logging.logger import logger
async def app_exception_handler(request: Request, exc: AppException):

    logger.error(f"{exc.status_code} | {exc.message} | {request.url.path}")

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": exc.message
        }
    )
async def validation_exception_handler(request: Request, exc: RequestValidationError):

    logger.error(f"Validation error | {request.url.path} | {exc.errors()}")

    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "error": "Validation Error",
            "details": exc.errors()
        }
    )
async def global_exception_handler(request: Request, exc: Exception):

    logger.error(f"Unhandled error | {request.url.path} | {str(exc)}")

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": "Internal Server Error"
        }
    )