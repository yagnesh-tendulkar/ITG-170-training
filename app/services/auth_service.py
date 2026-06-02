from app.models.user import User

from app.utils.security import (
    hash_password,
    verify_password,
    create_access_token
)


class AuthService:

    @staticmethod
    def register(data, db):

        user = User(
            username=data.username,
            email=data.email,
            password=hash_password(
                data.password
            )
        )

        db.add(user)

        db.commit()

        db.refresh(user)

        return {
            "message": "User registered"
        }

    @staticmethod
    def login(data, db):

        user = db.query(User).filter(
            User.email == data.email
        ).first()

        if not user:

            return {
                "message": "Invalid credentials"
            }

        if not verify_password(
            data.password,
            user.password
        ):

            return {
                "message": "Invalid credentials"
            }

        token = create_access_token(
            {
                "sub": user.email
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }