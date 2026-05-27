from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.custom_exceptions import (
    UserNotFoundException,
    UserAlreadyExistsException
)


async def user_not_found_exception_handler(
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


async def user_already_exists_exception_handler(
    request: Request,
    exc: UserAlreadyExistsException
):

    return JSONResponse(
        status_code=409,
        content={
            "success": False,
            "message": exc.message
        }
    )