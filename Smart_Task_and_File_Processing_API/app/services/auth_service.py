from datetime import datetime, timedelta, timezone

from jose import jwt
from passlib.context import CryptContext


# Secret Key
SECRET_KEY = "your_secret_key"

# JWT Algorithm
ALGORITHM = "HS256"

# Token Expiration Time
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# Password Hashing Context
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(
    password: str
) -> str:
    """
    Hash plain password.
    """

    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    """
    Verify password against hash.
    """

    return pwd_context.verify(
        plain_password,
        hashed_password
    )


def create_access_token(
    data: dict
) -> str:
    """
    Generate JWT token.
    """

    to_encode = data.copy()

    expire = datetime.now(
        timezone.utc
    ) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update(
        {"exp": expire}
    )

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


def verify_token(
    token: str
):
    """
    Decode and verify JWT token.
    """

    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )

    return payload