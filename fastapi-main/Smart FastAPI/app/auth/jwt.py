from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
from app.config import settings


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=getattr(settings, 'access_token_expire_minutes', getattr(settings, 'ACCESS_TOKEN_EXPIRE_MINUTES', 30)))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, getattr(settings, 'secret_key', getattr(settings, 'JWT_SECRET', 'secret')), algorithm=getattr(settings, 'algorithm', getattr(settings, 'JWT_ALGORITHM', 'HS256')))
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(token, getattr(settings, 'secret_key', getattr(settings, 'JWT_SECRET', 'secret')), algorithms=[getattr(settings, 'algorithm', getattr(settings, 'JWT_ALGORITHM', 'HS256'))])
        return payload
    except JWTError:
        return None


# Backwards-compatible aliases
def create_token(data: dict, expires_delta: Optional[timedelta] = None):
    return create_access_token(data, expires_delta)


def decode_token(token: str):
    return verify_token(token)