# ─────────────────────────────────────────────
# routers/auth_router.py
#
# LEARNING NOTE:
# A FastAPI "router" groups related endpoints together.
# Think of it like a chapter in a book — all auth-related
# routes go here, all review routes go elsewhere.
#
# Endpoints:
#   POST /auth/register  — create a new account
#   POST /auth/login     — get a JWT token
#   GET  /auth/me        — get current user's profile (protected)
# ─────────────────────────────────────────────

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
import models
import schemas
from auth import hash_password, verify_password, create_access_token, get_current_user

# APIRouter is like a mini FastAPI app — we mount it in main.py
router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=schemas.UserResponse, status_code=201)
def register(user_data: schemas.UserRegister, db: Session = Depends(get_db)):
    """
    Register a new user account.

    FastAPI automatically:
      - Parses the JSON body into UserRegister schema
      - Validates email format, password length, etc.
      - Returns 422 if validation fails
    """
    # Check if email already taken
    if db.query(models.User).filter(models.User.email == user_data.email).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="An account with this email already exists."
        )

    # Check if username already taken
    if db.query(models.User).filter(models.User.username == user_data.username).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This username is already taken."
        )

    # Create user with hashed password
    new_user = models.User(
        email=user_data.email,
        username=user_data.username,
        hashed_password=hash_password(user_data.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/login", response_model=schemas.TokenResponse)
def login(credentials: schemas.UserLogin, db: Session = Depends(get_db)):
    """
    Log in and receive a JWT access token.

    The token should be stored by the client and sent in the
    Authorization header for all protected requests:
        Authorization: Bearer <token>
    """
    # Find user by email
    user = db.query(models.User).filter(models.User.email == credentials.email).first()

    # IMPORTANT: We check both "user exists" and "password correct" with the same
    # error message. This prevents "email enumeration" attacks where someone could
    # figure out which emails are registered by trying different error messages.
    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password."
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is deactivated."
        )

    # Create and return JWT token
    token = create_access_token(data={"sub": user.email})

    return schemas.TokenResponse(
        access_token=token,
        token_type="bearer",
        user=schemas.UserResponse.model_validate(user),
    )


@router.get("/me", response_model=schemas.UserResponse)
def get_me(current_user: models.User = Depends(get_current_user)):
    """
    Get the currently logged-in user's profile.
    This is a protected route — requires a valid JWT token.
    """
    return current_user
