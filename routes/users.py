from fastapi import APIRouter

from schemas.user_schema import CreateUser, UpdateUser
from services.user_service import create_user, delete_user, get_user, get_users, update_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def add_user(user: CreateUser):
    return create_user(user)


@router.get("/")
def all_users():
    return get_users()


@router.get("/{user_id}")
def get_one_user(user_id: int):
    return get_user(user_id)


@router.put("/{user_id}")
def edit_user(user_id: int, user: UpdateUser):
    return update_user(user_id, user)


@router.delete("/{user_id}")
def remove_user(user_id: int):
    return delete_user(user_id)
