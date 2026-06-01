from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from starlette.middleware.base import BaseHTTPMiddleware



from app.database.connection import engine, Base
from app.routes.user_routes import router as user_router
from app.routes.task_routes import router as task_router
from app.exceptions.handlers import validation_exception_handler, not_found_handler
from app.middleware.logging_middleware import log_requests

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart Task API",@app.get("/")
def root():
    return {"message": "Welcome to Smart Task API 🚀"}
    description="A production-ready Task Management API",
    version="1.0.0"
)

# Middleware
app.add_middleware(BaseHTTPMiddleware, dispatch=log_requests)
app.add_middleware(CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)
app.add_middleware(GZipMiddleware, minimum_size=1000)

# Exception handlers
app.add_exception_handler(RequestValidationError, validation_exception_handler)

# Routes
app.include_router(user_router)
app.include_router(task_router)

@app.get("/")
def root():
    return {"message": "Welcome to Smart Task API "}


