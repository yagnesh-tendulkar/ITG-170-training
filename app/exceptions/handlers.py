from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.custom_exception import (
    UserAlreadyExistsException,
    InvalidCredentialsException,
    ResourceNotFoundException,
    UnauthorizedAccessException
)


async def user_exists_handler(
        request: Request,
        exc: UserAlreadyExistsException
):
    return JSONResponse(
        status_code=400,
        content={
            "success": False,
            "message": str(exc)
        }
    )


async def invalid_credentials_handler(
        request: Request,
        exc: InvalidCredentialsException
):
    return JSONResponse(
        status_code=401,
        content={
            "success": False,
            "message": str(exc)
        }
    )


async def resource_not_found_handler(
        request: Request,
        exc: ResourceNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "success": False,
            "message": str(exc)
        }
    )


async def unauthorized_handler(
        request: Request,
        exc: UnauthorizedAccessException
):
    return JSONResponse(
        status_code=403,
        content={
            "success": False,
            "message": str(exc)
        }
    )