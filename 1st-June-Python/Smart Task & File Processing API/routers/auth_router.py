from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from schemas.auth_schema import RegisterRequest
from database.session import get_db
from models.user_model import User

from utils.password_handler import hash_password
from schemas.auth_schema import LoginRequest

from utils.password_handler import verify_password

from utils.jwt_handler import create_access_token
router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register_user(
        request: RegisterRequest,
        db: Session = Depends(get_db)
):
    print("PASSWORD =", request.password)
    print("LENGTH =", len(request.password))

    hashed = hash_password(request.password)
    print(hashed)

    existing_user = (
        db.query(User)
        .filter(User.username == request.username)
        .first()
    )

    if existing_user:

        raise HTTPException(
            status_code=409,
            detail="Username already exists"
        )

    user = User(
        username=request.username,
        email=request.email,
        password=hash_password(
            request.password
        )
    )

    db.add(user)

    db.commit()

    return {
        "message":
        "User registered successfully"
    }


@router.post("/login")
def login(
        request: LoginRequest,
        db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(
            User.username == request.username
        )
        .first()
    )

    if not user:

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    if not verify_password(
            request.password,
            user.password
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    token = create_access_token(
        {
            "user_id": user.id,
            "username": user.username
        }
    )

    return {
        "message": "Login successful",
        "token": token,
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    }


@router.post("/logout")
def logout():
    return {
        "message": "Logout successful. Please remove token from client."
    }