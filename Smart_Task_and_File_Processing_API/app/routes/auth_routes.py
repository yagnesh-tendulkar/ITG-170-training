from fastapi import APIRouter
from fastapi import HTTPException

from schemas.auth_schema import (
    UserRegister,
    UserLogin
)

from services.auth_service import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# Temporary In-Memory Storage
users = []


@router.post("/register")
def register_user(
    user: UserRegister
):
    """
    Register new user.
    """

    for existing_user in users:

        if (
            existing_user["email"]
            == user.email
        ):
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

    hashed_password = hash_password(
        user.password
    )

    user_data = {
        "id": len(users) + 1,
        "name": user.name,
        "email": user.email,
        "password": hashed_password
    }

    users.append(user_data)

    return {
        "message": "User registered successfully",
        "user": {
            "id": user_data["id"],
            "name": user_data["name"],
            "email": user_data["email"]
        }
    }


@router.post("/login")
def login_user(
    user: UserLogin
):
    """
    User Login.
    """

    for existing_user in users:

        if (
            existing_user["email"]
            == user.email
        ):

            is_valid = verify_password(
                user.password,
                existing_user["password"]
            )

            if not is_valid:

                raise HTTPException(
                    status_code=401,
                    detail="Invalid password"
                )

            token = create_access_token(
                {
                    "sub": existing_user["email"]
                }
            )

            return {
                "access_token": token,
                "token_type": "bearer"
            }

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


@router.get("/users")
def get_all_users():
    """
    View all users.
    """

    return [
        {
            "id": user["id"],
            "name": user["name"],
            "email": user["email"]
        }
        for user in users
    ]