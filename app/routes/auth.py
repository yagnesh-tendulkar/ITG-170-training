from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.dependencies.database import get_db

from app.schemas.auth import (
    RegisterRequest,
    LoginRequest
)
from app.services.auth_service import (
    AuthService
)

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register")
def register(
    data: RegisterRequest, 
    db: Session = Depends(get_db)
):
    return AuthService.register(
        data,
        db
    )


@router.post("/login")
def login(
    data: LoginRequest,
    db: Session = Depends(get_db)
):
    return AuthService.login(
        data,
        db
    )