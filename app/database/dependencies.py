from typing import Any, Generator

from fastapi import Depends, HTTPException, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from .connection import get_db

security_scheme = HTTPBearer()
"""HTTP bearer auth scheme used for JWT token extraction."""


def get_db_dependency() -> Generator[Session, None, None]:
    """Provide a reusable SQLAlchemy database session dependency."""
    yield from get_db()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Security(security_scheme),
    db: Session = Depends(get_db_dependency),
) -> dict[str, Any]:
    """Placeholder dependency for extracting and validating a JWT-authenticated user.

    In production, replace this with token validation, user lookup, and permissions checks.
    """
    token = credentials.credentials
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication credentials were not provided.",
        )

    # TODO: Validate JWT token, fetch user from database, and verify active status.
    return {"sub": "placeholder-user", "token": token}
