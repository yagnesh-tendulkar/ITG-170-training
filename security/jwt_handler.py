import os
from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError, ExpiredSignatureError

from exceptions import AuthenticationException

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
    now = datetime.utcnow()
    expire = now + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    payload = {**data, "exp": expire, "iat": now}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if AUTH_DISABLED:
        return {"user_id": DEFAULT_USER_ID, "email": DEFAULT_USER_EMAIL}
    if credentials is None:
        raise AuthenticationException("Not authenticated")
    try:
        return jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
    except ExpiredSignatureError:
        raise AuthenticationException("Token has expired")
    except JWTError:
        raise AuthenticationException("Invalid token")
