# app/main.py

from fastapi import FastAPI

from app.database.database import Base, engine

from app.routers.user_router import router as user_router

from app.exceptions.custom_exceptions import (
    UserNotFoundException,
    UserAlreadyExistsException
)

from app.exceptions.exception_handlers import (
    user_not_found_exception_handler,
    user_already_exists_exception_handler
)
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="User Management API",
    version="1.0.0"
)
app.add_exception_handler(
    UserNotFoundException,
    user_not_found_exception_handler
)

app.add_exception_handler(
    UserAlreadyExistsException,
    user_already_exists_exception_handler
)


app.include_router(user_router)