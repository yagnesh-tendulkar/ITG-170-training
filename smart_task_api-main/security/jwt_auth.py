from jose import jwt
from datetime import datetime,timedelta

SECRET_KEY="mysecretkey"
ALGORITHM="HS256"

def create_access_token(data:dict):

    payload=data.copy()

    expire=datetime.utcnow()+timedelta(minutes=30)

    payload.update({"exp":expire})

    token=jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


def verify_token(token:str):

    payload=jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )

    return payload