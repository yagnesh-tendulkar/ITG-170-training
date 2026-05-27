
from fastapi import FastAPI
from app.database import Base, engine
from app.routers import user

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Production CRUD API",
    version="1.0.0"
)

app.include_router(user.router)