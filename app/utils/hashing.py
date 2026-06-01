"""
Password hashing utility module for secure password management.

Uses passlib with bcrypt for industry-standard password hashing.
"""

from passlib.context import CryptContext

# Create a CryptContext instance with bcrypt as the primary algorithm
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


def get_password_hash(password: str) -> str:
    """
    Hash a plain text password using bcrypt.

    Args:
        password: Plain text password to hash.

    Returns:
        str: Hashed password that can be stored securely in the database.

    Example:
        >>> hashed = get_password_hash("user_password")
        >>> # Store hashed in database
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain text password against a stored hashed password.

    Uses bcrypt's timing-safe comparison to prevent timing attacks.

    Args:
        plain_password: Plain text password to verify (from user input).
        hashed_password: Hashed password stored in the database.

    Returns:
        bool: True if passwords match, False otherwise.

    Example:
        >>> is_valid = verify_password("user_password", stored_hash)
        >>> if is_valid:
        ...     # Password is correct, authenticate user
        ...     pass
    """
    return pwd_context.verify(plain_password, hashed_password)
