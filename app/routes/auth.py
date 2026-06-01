from fastapi import APIRouter
from pydantic import BaseModel

auth_router = APIRouter(prefix="/auth", tags=["Authentication"])

class LoginRequest(BaseModel):
    email: str
    password: str


@auth_router.post("/login")
def login(user: LoginRequest):
    return {
        "message": "SUCCESS",
        "received_email": user.email,
        "received_password": user.password
    }