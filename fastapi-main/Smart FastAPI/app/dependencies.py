from fastapi import Header, HTTPException, status
from typing import Generator, Optional
from app.database import get_db as get_db_conn
from app.auth.jwt import decode_token


def get_db() -> Generator:
    conn = get_db_conn()
    try:
        yield conn
    finally:
        try:
            conn.close()
        except Exception:
            pass


def get_current_user(authorization: Optional[str] = Header(None)):
    if not authorization:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing token")

    token = authorization.replace("Bearer ", "")

    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    return payload
