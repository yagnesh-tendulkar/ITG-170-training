from fastapi import FastAPI

from app.routes.user import user_router
from app.routes.task import task_router
from app.routes.auth import auth_router

from app.middleware.auth_middleware import AuthMiddleware

app = FastAPI()

#app.add_middleware(AuthMiddleware)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(task_router)

@app.get("/")
def home():
    return {"message": "API is running"}