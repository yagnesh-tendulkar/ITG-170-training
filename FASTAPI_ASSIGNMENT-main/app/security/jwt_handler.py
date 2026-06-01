import os
from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError, ExpiredSignatureError

from app.exceptions import AuthenticationException

AUTH_DISABLED = os.getenv("AUTH_DISABLED", "0").lower() in ("1", "true", "yes")
DEFAULT_USER_ID = int(os.getenv("DEFAULT_USER_ID", "1"))
DEFAULT_USER_EMAIL = os.getenv("DEFAULT_USER_EMAIL", "dev@localhost")

security = HTTPBearer(auto_error=False)


SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY and not AUTH_DISABLED:
    raise RuntimeError("SECRET_KEY environment variable is not set")

ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    now = datetime.utcnow()
    if expires_delta is None:
        expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = now + expires_delta
    to_encode.update({"exp": expire, "iat": now})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if AUTH_DISABLED:
        return {"user_id": DEFAULT_USER_ID, "email": DEFAULT_USER_EMAIL}

    if credentials is None:
        raise AuthenticationException("Not authenticated")

    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except ExpiredSignatureError:
        raise AuthenticationException("Token has expired")
    except JWTError:
        raise AuthenticationException("Invalid token")