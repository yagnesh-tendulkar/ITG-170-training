from fastapi import FastAPI
from app.routers import user
from app.core.cors import add_cors

app = FastAPI()

add_cors(app)

app.include_router(user.router)


@app.get("/")
def root():
    return {"message": "FastAPI Production Structure Running"}