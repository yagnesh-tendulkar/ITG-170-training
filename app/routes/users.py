from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/")
def create_user():
    return {
        "message": "User created"
    }


@router.get("/")
def get_users():
    return {
        "message": "Get all users"
    }


@router.get("/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id
    }


@router.put("/{user_id}")
def update_user(user_id: int):
    return {
        "message": "User updated",
        "user_id": user_id
    }


@router.delete("/{user_id}")
def delete_user(user_id: int):
    return {
        "message": "User deleted",
        "user_id": user_id
    }