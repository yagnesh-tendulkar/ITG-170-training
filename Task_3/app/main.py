from fastapi import FastAPI
from app.core.cors import add_cors
from app.routers import user

app = FastAPI(
    title="Production User API",
    version="1.0.0"
)

add_cors(app)

app.include_router(user.router)


@app.get("/")
def root():
    return {"message": "FastAPI Production Ready Running"}