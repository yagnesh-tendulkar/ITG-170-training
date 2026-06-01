
import hashlib

from fastapi import APIRouter, HTTPException
from auth.jwt_handler import create_token
from database.db import mycursor
from utils.audit import log_action

router = APIRouter()


def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def get_hr_user(username: str):
    query = "SELECT username, password_hash, role FROM hr_users WHERE username=%s"
    mycursor.execute(query, (username,))
    return mycursor.fetchone()


@router.post("/login")
def login(username: str, password: str):

    user = get_hr_user(username)
    if not user or user["password_hash"] != _hash_password(password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"user": user["username"], "role": user["role"]})

    try:
        log_action(username, "LOGIN")
    except Exception:
        pass

    return {"access_token": token}