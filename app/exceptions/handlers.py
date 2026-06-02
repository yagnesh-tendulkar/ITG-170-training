from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.custom_exceptions import (
    TaskNotFoundException,
    UserNotFoundException
)


async def task_not_found_handler(
    request: Request,
    exc: TaskNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "message": "Task not found"
        }
    )


async def user_not_found_handler(
    request: Request,
    exc: UserNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "message": "User not found"
        }
    )