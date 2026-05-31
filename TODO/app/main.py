from fastapi import FastAPI
from app.database.connection import engine, Base
from app.routes import tasks
from app.middleware.logging_middleware import LoggingAndTracingMiddleware

# Automatically initialize database structures
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Production-Ready Task Engine Showcase",
    description="Scalable clean enterprise setup structure",
    version="1.0.0"
)

# Global custom middleware injection order (First In, Last Out)
app.add_middleware(LoggingAndTracingMiddleware)

# Core Verification Route
@app.get("/health", tags=["System Performance Monitoring"])
def system_health_status():
    return {"status": "operational", "engine": "FastAPI 0.111.0"}

# Register Router Layers
app.include_router(tasks.router)