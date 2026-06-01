# from passlib.context import CryptContext
# from jose import jwt
# from datetime import datetime, timedelta
#
# from app.core.config import settings
#
#
# pwd_context = CryptContext(
#     schemes=["bcrypt"],
#     deprecated="auto"
# )
#
#
# # PASSWORD HASHING
# def hash_password(password: str):
#     return pwd_context.hash(password)
#
#
# def verify_password(plain, hashed):
#     return pwd_context.verify(plain, hashed)
#
#
# # JWT TOKEN
# def create_access_token(data: dict):
#     to_encode = data.copy()
#
#     expire = datetime.utcnow() + timedelta(
#         minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
#     )
#
#     to_encode.update({"exp": expire})
#
#     return jwt.encode(
#         to_encode,
#         settings.SECRET_KEY,
#         algorithm=settings.ALGORITHM
#     )
#
#
# def decode_token(token: str):
#     return jwt.decode(
#         token,
#         settings.SECRET_KEY,
#         algorithms=[settings.ALGORITHM]
#     )
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
import hashlib

from app.core.config import settings


# =========================
# PASSWORD CONTEXT
# =========================
pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)


# =========================
# PASSWORD NORMALIZATION
# (Fixes bcrypt 72-byte limit issue)
# =========================
def normalize_password(password: str) -> str:
    """
    bcrypt has a 72-byte password limit.
    If password exceeds limit, we hash it using SHA256 first.
    """
    if len(password.encode("utf-8")) > 72:
        return hashlib.sha256(password.encode()).hexdigest()
    return password


# =========================
# PASSWORD HASHING
# =========================
def hash_password(password: str) -> str:
    password = normalize_password(password)
    return pwd_context.hash(password)


# =========================
# PASSWORD VERIFY
# =========================
def verify_password(plain: str, hashed: str) -> bool:
    plain = normalize_password(plain)
    return pwd_context.verify(plain, hashed)


# =========================
# CREATE JWT TOKEN
# =========================
def create_access_token(data: dict) -> str:
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )


# =========================
# DECODE JWT TOKEN
# =========================
def decode_token(token: str) -> dict:
    return jwt.decode(
        token,
        settings.SECRET_KEY,
        algorithms=[settings.ALGORITHM]
    )