from fastapi import APIRouter

from exceptions import AuthenticationException
from schemas.user_schema import UserLogin
from security.jwt_handler import create_access_token
from services.auth_service import verify_password
from services.user_service import get_user_by_email

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login")
def login(user: UserLogin):
    db_user = get_user_by_email(user.email)
    if not db_user or not verify_password(user.password, db_user.get("password")):
        raise AuthenticationException("Invalid email or password")

    return {
        "access_token": create_access_token({
            "user_id": db_user.get("id"),
            "email": db_user.get("email"),
        }),
        "token_type": "bearer",
    }
