from fastapi import FastAPI

from app.core.database import Base
from app.core.database import engine


app = FastAPI()

Base.metadata.create_all(bind=engine)

from app.routes.auth import router as auth_router

from app.middleware.logging_middleware import (
    RequestLoggerMiddleware
)

from app.exceptions.custom_exception import (
    UserAlreadyExistsException,
    InvalidCredentialsException,
    ResourceNotFoundException,
    UnauthorizedAccessException
)

from app.exceptions.handlers import (
    user_exists_handler,
    invalid_credentials_handler,
    resource_not_found_handler,
    unauthorized_handler
)

from app.routes.tasks import (
    router as task_router
)


from app.routes.file import (
    router as file_router
)

app.include_router(file_router)

app.include_router(task_router)


app.add_middleware(
    RequestLoggerMiddleware
)


app.add_exception_handler(
    UserAlreadyExistsException,
    user_exists_handler
)

app.add_exception_handler(
    InvalidCredentialsException,
    invalid_credentials_handler
)

app.add_exception_handler(
    ResourceNotFoundException,
    resource_not_found_handler
)

app.add_exception_handler(
    UnauthorizedAccessException,
    unauthorized_handler
)

app.include_router(auth_router)