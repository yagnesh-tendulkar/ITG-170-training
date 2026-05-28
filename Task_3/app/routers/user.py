from fastapi import APIRouter, HTTPException, Query
from app.models.user import User
from app.db.fake_db import fake_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/{user_id}")
def create_user(user_id: int, role: str = Query(None), user: User = None):

    if user_id in fake_db:
        raise HTTPException(status_code=409, detail="User already exists")

    data = user.model_dump()
    data["role"] = role

    fake_db[user_id] = data

    return {"message": "User created", "data": fake_db[user_id]}


@router.put("/{user_id}")
def update_user(user_id: int, notify: bool = Query(False), user: User = None):

    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")

    fake_db[user_id] = user.model_dump()

    return {
        "message": f"User updated (notify={notify})",
        "data": fake_db[user_id]
    }


@router.get("/{user_id}")
def get_user(user_id: int):

    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")

    user = fake_db[user_id]

    return {"id": user["id"], "name": user["first_name"]}

@router.delete("/{user_id}")
def delete_user(user_id: int):

    if user_id not in fake_db:
        raise HTTPException(status_code=404, detail="User not found")

    deleted_user = fake_db.pop(user_id)

    return {
        "message": "User deleted successfully",
        "deleted_user": deleted_user
    }