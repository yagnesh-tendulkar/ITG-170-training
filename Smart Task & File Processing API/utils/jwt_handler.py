from datetime import datetime
from datetime import timedelta

from jose import jwt

SECRET_KEY = "itg170-secret-key-973238753287resdfgvbvdserfcxzsertye34567ygqgwhsdfrewsc"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(data: dict):

    payload = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload["exp"] = expire

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token