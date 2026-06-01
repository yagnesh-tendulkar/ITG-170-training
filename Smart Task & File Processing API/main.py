from fastapi import FastAPI

from routers.auth_router import (
    router as auth_router
)

from routers.task_router import (
    router as task_router
)

from database.connection import engine
from database.base import Base
from fastapi import HTTPException

from models.user_model import User
from models.task_model import Task
from exceptions.exception_handlers import (
    http_exception_handler,
    generic_exception_handler
)
from middleware.logging_middleware import logging_middleware
from routers.file_router import (
    router as file_router
)
from routers.health_router import (
    router as health_router
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ITG-170 Smart Task API",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(task_router)
app.include_router(file_router)

app.include_router(
    health_router
)
app.middleware("http")(
    logging_middleware
)


app.add_exception_handler(
    HTTPException,
    http_exception_handler
)

app.add_exception_handler(
    Exception,
    generic_exception_handler
)

@app.get("/")
def home():
    return {
        "message":
            "ITG-170 Smart Task API Running"
    }