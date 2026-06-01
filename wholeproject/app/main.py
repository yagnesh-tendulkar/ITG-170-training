from fastapi import FastAPI
from app.routes.user_routes import router as userRouter
from app.routes.test_router import router as testRouter
from app.middleware.cors import get_middleware

app = FastAPI()

get_middleware(app)

app.include_router(userRouter)
app.include_router(testRouter)