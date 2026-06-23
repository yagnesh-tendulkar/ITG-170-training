# ─────────────────────────────────────────────
# auth.py
#
# LEARNING NOTE:
# This file handles everything authentication-related:
#
# 1. PASSWORD HASHING — we use bcrypt to hash passwords before storing.
#    Hashing is a one-way operation: you can verify a password but never
#    "un-hash" it back. This protects users if the DB is ever stolen.
#
# 2. JWT TOKENS — JSON Web Tokens are a way to prove identity without
#    storing sessions on the server. The token contains: user_id + expiry.
#    The server signs it with a secret key. Any tampered token is rejected.
#
# Flow:
#    Register → hash password → store in DB
#    Login    → verify password → create JWT → send to client
#    Request  → client sends JWT in header → we verify & identify user
# ─────────────────────────────────────────────

from datetime import datetime, timedelta, timezone
from typing import Optional
import os

from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from dotenv import load_dotenv

from database import get_db
import models

load_dotenv()

# ── Config ────────────────────────────────────────────────

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
ALGORITHM = "HS256"                     # Signing algorithm for JWT
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

# ── Password Hashing ────────────────────────────────────────────────

# CryptContext manages password hashing. We use bcrypt — the industry standard.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(plain_password: str) -> str:
    """Convert a plain text password to a secure hash"""
    return pwd_context.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Check if a plain password matches the stored hash"""
    return pwd_context.verify(plain_password, hashed_password)


# ── JWT Token ────────────────────────────────────────────────

# OAuth2PasswordBearer tells FastAPI where to look for the token in requests
# (Authorization: Bearer <token> header)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Create a signed JWT token.

    The token payload (called 'claims') contains:
      - sub: the subject (user email)
      - exp: expiration timestamp
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})

    # jwt.encode signs the data with our SECRET_KEY
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str) -> Optional[str]:
    """
    Decode and validate a JWT token.
    Returns the user email (stored in 'sub' claim) or None if invalid.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        return email
    except JWTError:
        return None


# ── Current User Dependency ────────────────────────────────────────────────

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> models.User:
    """
    FastAPI Dependency: extracts and validates the current logged-in user.

    Usage in protected routes:
        @router.get("/protected")
        def protected_route(current_user: User = Depends(get_current_user)):
            ...

    Raises 401 if the token is missing, expired, or invalid.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials. Please log in again.",
        headers={"WWW-Authenticate": "Bearer"},
    )

    email = decode_token(token)
    if email is None:
        raise credentials_exception

    user = db.query(models.User).filter(models.User.email == email).first()
    if user is None or not user.is_active:
        raise credentials_exception

    return user
