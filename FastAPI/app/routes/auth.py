from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/login")
def login():
    return {
        "access_token": "demo_token",
        "token_type": "bearer"
    }