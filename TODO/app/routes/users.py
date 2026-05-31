"""User management endpoints (placeholder)."""
from fastapi import APIRouter

router = APIRouter(prefix="/users")

@router.get("/me")
def read_me():
    return {"msg": "user profile placeholder"}
