from fastapi import APIRouter

from app.exceptions import NotFoundException
from app.schemas.user_schema import (
    CreateUser,
    UpdateUser
)

from app.services.user_service import (
    create_user,
    get_users,
    get_user,
    update_user,
    delete_user
)

route = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@route.post("/")
def add_user(user: CreateUser):

    return create_user(user)


@route.get("/")
def all_users():

    return get_users()


@route.get("/{user_id}")
def get_one_user(user_id: int):

    user = get_user(user_id)

    if not user:
        raise NotFoundException("User not found")

    return user


@route.put("/{user_id}")
def edit_user(
    user_id: int,
    user: UpdateUser
):

    existing_user = get_user(user_id)

    if not existing_user:
        raise NotFoundException("User not found")

    return update_user(
        user_id,
        user
    )


@route.delete("/{user_id}")
def remove_user(user_id: int):

    existing_user = get_user(user_id)

    if not existing_user:
        raise NotFoundException("User not found")

    return delete_user(user_id)