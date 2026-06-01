from fastapi import FastAPI
from sqlmodel import SQLModel

from .database.db import engine
from .routes.user_routes import router as user_router

app = FastAPI()

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

# Register routes
app.include_router(user_router)

@app.get("/")
def home():
    return {"message": "Smart Task API Running"}