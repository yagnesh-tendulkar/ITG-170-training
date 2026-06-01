from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.auth_schema import (
    RegisterRequest,
    LoginRequest,
    TokenResponse
)

from app.services.auth_service import (
    register_user,
    login_user
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
        user: RegisterRequest,
        db: Session = Depends(get_db)
):

    try:

        created_user = register_user(
            db,
            user.username,
            user.email,
            user.password
        )

        return {
            "message": "User Registered Successfully",
            "user_id": created_user.id
        }

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
        credentials: LoginRequest,
        db: Session = Depends(get_db)
):

    token = login_user(
        db,
        credentials.email,
        credentials.password
    )

    if not token:

        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )

    return {
        "access_token": token,
        "token_type": "bearer"
    }