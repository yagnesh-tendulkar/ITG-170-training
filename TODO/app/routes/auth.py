"""Authentication endpoints (placeholder)."""
from fastapi import APIRouter

router = APIRouter(prefix="/auth")

@router.post("/login")
def login():
    return {"msg": "login placeholder"}

@router.post("/register")
def register():
    return {"msg": "register placeholder"}
