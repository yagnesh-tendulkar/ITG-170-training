from fastapi import APIRouter
from app.services.user_service import UserService
from app.core.exceptions import AppException
from app.schemas.user_schema import User

router = APIRouter(prefix="/user", tags=["Users"])


@router.get("/{user_id}")
def get_user(user_id: int):

    user = UserService.get_user(user_id)

    if not user:
        AppException.not_found("User not found")

    return user


@router.post("/{user_id}")
def create_user(user_id: int, user: User):

    if UserService.get_user(user_id):
        AppException.conflict("User already exists")

    return UserService.create_user(user_id, user.model_dump())


@router.put("/{user_id}")
def update_user(user_id: int, user: User):

    if not UserService.get_user(user_id):
        AppException.not_found("User not found")

    return UserService.update_user(user_id, user.model_dump())


@router.delete("/{user_id}")
def delete_user(user_id: int):

    if not UserService.get_user(user_id):
        AppException.not_found("User not found")

    return UserService.delete_user(user_id)