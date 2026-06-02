import datetime
import os
from pathlib import Path

import jwt
from dotenv import load_dotenv
from fastapi import HTTPException

load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env")

SECRET = os.getenv("JWT_SECRET")
if not SECRET:
    raise ValueError("JWT_SECRET is required. Set it in .env or the environment.")


def create_token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)

    return jwt.encode(payload, SECRET, algorithm="HS256")


def verify_token(token: str):
    try:
        return jwt.decode(token, SECRET, algorithms=["HS256"])
    except:
        raise HTTPException(status_code=401, detail="Invalid token")