"""Custom global exception handlers for the TODO app."""
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR


class AppException(Exception):
    def __init__(self, status_code: int = 400, detail: str = "Application error"):
        self.status_code = status_code
        self.detail = detail


async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        {"detail": exc.detail},
        status_code=exc.status_code,
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        {
            "detail": exc.errors(),
            "body": exc.body,
        },
        status_code=422,
    )


async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        {"detail": exc.detail},
        status_code=exc.status_code,
    )


async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        {"detail": "Internal Server Error"},
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
    )
