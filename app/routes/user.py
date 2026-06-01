from fastapi import APIRouter, Depends, Query
from typing import Optional

from app.database import db
from app.models import model
from app.exceptions.exception import AppException
from app.utils.security import oauth2_scheme

user_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# ✅ TOKEN TEST (for Swagger auth check)
@user_router.post("/user-protected")
def protected_route(token: str = Depends(oauth2_scheme)):
    return {"message": "Token received", "token": token}


# ✅ CREATE USER
@user_router.post("/user")
def create_user(user: model.users):
    db.user.append(user.model_dump())
    return user


# GET ALL USERS
@user_router.get("/")
def get_users():
    return db.user


# GET USER BY ID
@user_router.get("/user/{user_id}")
def get_user(user_id: int):
    for user in db.user:
        if user["id"] == user_id:
            return user
    raise AppException.not_found("User is not available")


# UPDATE USER
@user_router.put("/user/{user_id}")
def update_user(user_id: int, update_user: model.users):
    for user in db.user:
        if user["id"] == user_id:
            user.update(update_user.model_dump())
            return user
    raise AppException.not_found("No user found")


# DELETE USER
@user_router.delete("/user/{user_id}")
def delete_user(user_id: int):
    for user in db.user:
        if user["id"] == user_id:
            db.user.remove(user)
            return user
    raise AppException.not_found("User is not available")


# QUERY PARAMS
@user_router.get("/search")
def get_users_query(
    name: Optional[str] = Query(None),
    role: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    sort_by: str = Query("id"),
    order: str = Query("asc"),
    page: int = Query(1),
    limit: int = Query(10)
):

    results = db.user

    if name:
        results = [u for u in results if u["name"] == name]

    if role:
        results = [u for u in results if u["role"] == role]

    if search:
        results = [
            u for u in results
            if search.lower() in u["name"].lower()
            or search.lower() in u["role"].lower()
        ]

    reverse = order == "desc"

    results = sorted(results, key=lambda x: x.get(sort_by), reverse=reverse)

    start = (page - 1) * limit
    end = start + limit

    return {
        "page": page,
        "limit": limit,
        "total": len(results),
        "data": results[start:end]
    }