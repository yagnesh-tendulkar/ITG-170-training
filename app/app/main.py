from fastapi import FastAPI

from app.database.database import engine, Base

from app.routes.user import router as user_router
from app.routes.complaint import router as complaint_router
from app.routes.auth import router as auth_router
from app.routes.stream import router as stream_router

from app.middleware.logging_middleware import LoggingMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart Complaint Management Backend"
)

app.add_middleware(LoggingMiddleware)

app.include_router(user_router)
app.include_router(complaint_router)
app.include_router(auth_router)
app.include_router(stream_router)


@app.get("/")
def home():
    return {
        "message": "Complaint Management"}