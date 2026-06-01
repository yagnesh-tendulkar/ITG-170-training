from fastapi import Request
from fastapi.responses import JSONResponse

from exceptions.custom_exceptions import (
    TaskNotFoundException,
    UserNotFoundException,
    FileValidationException,
    AuthenticationException,
    AuthorizationException
)


async def task_not_found_handler(
    request: Request,
    exc: TaskNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "success": False,
            "message": exc.message
        }
    )


async def user_not_found_handler(
    request: Request,
    exc: UserNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "success": False,
            "message": exc.message
        }
    )


async def file_validation_handler(
    request: Request,
    exc: FileValidationException
):
    return JSONResponse(
        status_code=400,
        content={
            "success": False,
            "message": exc.message
        }
    )


async def authentication_handler(
    request: Request,
    exc: AuthenticationException
):
    return JSONResponse(
        status_code=401,
        content={
            "success": False,
            "message": exc.message
        }
    )


async def authorization_handler(
    request: Request,
    exc: AuthorizationException
):
    return JSONResponse(
        status_code=403,
        content={
            "success": False,
            "message": exc.message
        }
    )


async def generic_exception_handler(
    request: Request,
    exc: Exception
):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal Server Error"
        }
    )