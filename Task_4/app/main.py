from fastapi import FastAPI
from app.core.cors import add_cors
from app.routers import user_router 

app = FastAPI()

app.include_router(user_router.router)

add_cors(app)
@app.get("/")
def root():
    return {"message": "Production FastAPI Running"}