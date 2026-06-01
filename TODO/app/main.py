from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.database.connection import engine, Base
from app.routes import tasks
from app.exceptions.handlers import (
    AppException,
    app_exception_handler,
    generic_exception_handler,
    http_exception_handler,
    validation_exception_handler,
)
from app.middleware.logging_middleware import LoggingAndTracingMiddleware

# Automatically initialize database structures
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Production-Ready Task Engine Showcase",
    description="Scalable clean enterprise setup structure",
    version="1.0.0"
)

# Register global exception handlers
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

# Global custom middleware injection order (First In, Last Out)
app.add_middleware(LoggingAndTracingMiddleware)

# Core Verification Route
@app.get("/health", tags=["System Performance Monitoring"])
def system_health_status():
    return {"status": "operational", "engine": "FastAPI 0.111.0"}

# Register Router Layers
app.include_router(tasks.router)