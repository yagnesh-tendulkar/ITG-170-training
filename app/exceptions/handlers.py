from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder

from logging_config import get_logger

logger = get_logger("exceptions")


class TaskNotFoundException(Exception):
    def __init__(self, task_id: int):
        self.task_id = task_id


class UserNotFoundException(Exception):
    def __init__(self, user_id: int):
        self.user_id = user_id


class DuplicateEmailException(Exception):
    def __init__(self, email: str):
        self.email = email


def register_exception_handlers(app: FastAPI) -> None:

    @app.exception_handler(TaskNotFoundException)
    async def task_not_found_handler(
        request: Request,
        exc: TaskNotFoundException
    ):
        logger.warning(f"Task {exc.task_id} not found")

        return JSONResponse(
            status_code=404,
            content={
                "success": False,
                "message": f"Task {exc.task_id} not found",
            },
        )

    @app.exception_handler(UserNotFoundException)
    async def user_not_found_handler(
        request: Request,
        exc: UserNotFoundException
    ):
        logger.warning(f"User {exc.user_id} not found")

        return JSONResponse(
            status_code=404,
            content={
                "success": False,
                "message": f"User {exc.user_id} not found",
            },
        )

    @app.exception_handler(DuplicateEmailException)
    async def duplicate_email_handler(
        request: Request,
        exc: DuplicateEmailException
    ):
        logger.warning(f"Duplicate email: {exc.email}")

        return JSONResponse(
            status_code=409,
            content={
                "success": False,
                "message": f"Email '{exc.email}' is already registered",
            },
        )

    @app.exception_handler(RequestValidationError)
    async def validation_error_handler(
        request: Request,
        exc: RequestValidationError
    ):
        logger.error(
            f"ValidationError on {request.url}: {exc.errors()}"
        )

        formatted_errors = []

        for err in exc.errors():
            formatted_errors.append(
                {
                    "field": ".".join(map(str, err.get("loc", []))),
                    "message": err.get("msg"),
                    "type": err.get("type"),
                }
            )

        return JSONResponse(
            status_code=422,
            content=jsonable_encoder(
                {
                    "success": False,
                    "message": "Invalid input",
                    "details": formatted_errors,
                }
            ),
        )

    @app.exception_handler(HTTPException)
    async def http_exception_handler(
        request: Request,
        exc: HTTPException
    ):
        logger.error(
            f"HTTPException {exc.status_code} on {request.url}: {exc.detail}"
        )

        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "message": exc.detail,
            },
        )

    @app.exception_handler(Exception)
    async def generic_exception_handler(
        request: Request,
        exc: Exception
    ):
        logger.critical(
            f"Unhandled exception on {request.url}: {str(exc)}",
            exc_info=True,
        )

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": "Internal server error",
            },
        )
