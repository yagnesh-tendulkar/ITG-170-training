from fastapi import APIRouter
from schemas.user_schema import UserLogin

from security.jwt_handler import create_access_token
from services.auth_service import verify_password
from services.user_service import get_user_by_email
from exceptions import AuthenticationException

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/login")
def login(
    user: UserLogin
):
    db_user = get_user_by_email(user.email)
    if not db_user:
        raise AuthenticationException("Invalid email or password")

    if not verify_password(user.password, db_user.get("password")):
        raise AuthenticationException("Invalid email or password")

    token = create_access_token(
        {
            "user_id": db_user.get("id"),
            "email": db_user.get("email"),
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }