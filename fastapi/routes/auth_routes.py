# from pydantic import BaseModel
# from fastapi import APIRouter, HTTPException
# from auth.jwt_handler import create_token

# router = APIRouter()

# HR_USER = "hr"
# HR_PASS = "1234"


# class LoginRequest(BaseModel):
#     username: str
#     password: str


# @router.post("/login")
# def login(data: LoginRequest):

#     if data.username != HR_USER or data.password != HR_PASS:
#         raise HTTPException(status_code=401, detail="Invalid username or password")

#     token = create_token({"user": data.username, "role": "hr"})
#     return {"token": token}

from fastapi import APIRouter, HTTPException
from auth.jwt_handler import create_token
from utils.audit import log_action

router = APIRouter()

HR_USER = "hr"
HR_PASS = "1234"


@router.post("/login")
def login(username: str, password: str):

    if username != HR_USER or password != HR_PASS:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"user": username})

    try:
        log_action(username, "LOGIN")
    except Exception:
        pass

    return {"access_token": token}