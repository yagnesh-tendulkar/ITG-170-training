from fastapi import FastAPI
from app.models import create_tables
from app.middleware import LoggingMiddleware, add_security
from app.exceptions import app_exception_handler, AppException
from app.routes import auth_routes, user_routes, task_routes, metrics_routes, upload_routes

app = FastAPI(title="Smart Task API")

# security / middleware
add_security(app)
app.add_middleware(LoggingMiddleware)

# exception handler
app.add_exception_handler(AppException, app_exception_handler)

# create tables (best-effort, ignore failures across different DB backends)
try:
    create_tables()
except Exception:
    pass

# routes
app.include_router(auth_routes, prefix="/api/v1", tags=["auth"])
app.include_router(user_routes, prefix="/api/v1", tags=["users"])
app.include_router(task_routes, prefix="/api/v1", tags=["tasks"])
app.include_router(metrics_routes, prefix="/api/v1", tags=["metrics"])
app.include_router(upload_routes, prefix="/api/v1", tags=["upload"])