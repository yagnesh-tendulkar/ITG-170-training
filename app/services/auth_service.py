from app.database.db import user
from app.utils.security import (
    hash_password,
    verify_password
)
from app.utils.jwt import create_token


def register_user(user_data):

    for existing in user:
        if existing["email"] == user_data.email:
            raise ValueError("Email already exists")

    new_user = {
        "id": len(user) + 1,
        "username": user_data.username,
        "email": user_data.email,
        "password": hash_password(user_data.password)
    }

    user.append(new_user)

    return new_user


def login_user(data):

    for existing_user in user:

        if existing_user["email"] == data.email:

            if verify_password(
                data.password,
                existing_user["password"]
            ):

                token = create_token(existing_user["email"])

                return {
                    "access_token": token,
                    "token_type": "bearer"
                }

    raise ValueError("Invalid credentials")