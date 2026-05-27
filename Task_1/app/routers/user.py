from fastapi import APIRouter, HTTPException, status
from app.schemas.user import User
from app.db.fake_db import fake_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: User):

    if user.id in fake_db:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists"
        )

    fake_db[user.id] = user.model_dump()
    return fake_db[user.id]


@router.get("/{user_id}")
def get_user(user_id: int):

    if user_id not in fake_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return fake_db[user_id]


@router.put("/{user_id}")
def update_user(user_id: int, user: User):

    if user_id not in fake_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    fake_db[user_id] = user.model_dump()
    return fake_db[user_id]


@router.delete("/{user_id}")
def delete_user(user_id: int):

    if user_id not in fake_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return fake_db.pop(user_id)