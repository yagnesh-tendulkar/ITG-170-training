from fastapi import FastAPI
from app import user

app = FastAPI()

app.include_router(user.router)