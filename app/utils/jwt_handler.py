"""
JWT token handling utility module for secure token management.

Provides functions for creating, validating, and decoding JWT access tokens.
"""

from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Optional

from jose import JWTError, jwt

# JWT Configuration constants
SECRET_KEY = "your-secret-key-change-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(
    data: Dict[str, Any],
    expires_delta: Optional[timedelta] = None,
) -> str:
    """
    Create a JWT access token with optional expiration.

    Args:
        data: Dictionary containing token claims (e.g., {"sub": user_id}).
        expires_delta: Optional token expiration time delta. If not provided,
                      uses ACCESS_TOKEN_EXPIRE_MINUTES default.

    Returns:
        str: Encoded JWT access token.

    Example:
        >>> token = create_access_token({"sub": 1})
        >>> # Token can be sent to client
    """
    to_encode = data.copy()

    # Set expiration time
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )

    # Add expiration claim to token
    to_encode.update({"exp": expire})

    # Encode and sign the token
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_token(token: str) -> Optional[Dict[str, Any]]:
    """
    Decode and validate a JWT access token.

    Args:
        token: JWT token string to decode.

    Returns:
        Optional[Dict]: Token payload as dictionary if valid, None if invalid.

    Example:
        >>> payload = decode_token(token)
        >>> if payload:
        ...     user_id = payload.get("sub")
    """
    try:
        payload: Dict[str, Any] = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )
        return payload
    except JWTError:
        return None


def verify_token(token: str) -> bool:
    """
    Verify if a JWT token is valid without decoding the full payload.

    Checks for expiration and valid signature.

    Args:
        token: JWT token string to verify.

    Returns:
        bool: True if token is valid and not expired, False otherwise.

    Example:
        >>> if verify_token(token):
        ...     # Token is valid, proceed with authorization
        ...     pass
    """
    return decode_token(token) is not None


def get_token_expiration(token: str) -> Optional[datetime]:
    """
    Extract the expiration timestamp from a JWT token.

    Args:
        token: JWT token string.

    Returns:
        Optional[datetime]: Token expiration datetime if valid, None if invalid.

    Example:
        >>> exp_time = get_token_expiration(token)
        >>> if exp_time:
        ...     print(f"Token expires at: {exp_time}")
    """
    payload = decode_token(token)
    if not payload:
        return None

    exp: Optional[int] = payload.get("exp")
    if not exp:
        return None

    return datetime.fromtimestamp(exp, tz=timezone.utc)


def is_token_expired(token: str) -> bool:
    """
    Check if a JWT token has expired.

    Args:
        token: JWT token string.

    Returns:
        bool: True if token is expired, False if still valid or invalid.

    Example:
        >>> if is_token_expired(token):
        ...     # Request a new token
        ...     pass
    """
    expiration = get_token_expiration(token)
    if not expiration:
        return True

    return datetime.now(timezone.utc) > expiration


def get_user_id_from_token(token: str) -> Optional[int]:
    """
    Extract the user ID (subject) from a JWT token.

    Args:
        token: JWT token string.

    Returns:
        Optional[int]: User ID if valid token, None otherwise.

    Example:
        >>> user_id = get_user_id_from_token(token)
        >>> if user_id:
        ...     # Load user from database
        ...     user = get_user(user_id)
    """
    payload = decode_token(token)
    if not payload:
        return None

    user_id: Optional[int] = payload.get("sub")
    return user_id
