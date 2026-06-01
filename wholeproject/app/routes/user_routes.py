from fastapi import APIRouter, HTTPException, status, Query, Depends 
from app.database.database import dbUser
from app.schemas.schemes import User
from app.auth.dependencies import get_current_user

from app.auth.security import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter(
    tags=["user"]
)


# CREATE USER
@router.post("/user", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):

    if user.id in dbUser:
        raise HTTPException(
            status_code=409,
            detail="User already exists"
        )

    dbUser[user.id] = user
    return user



# GET USERS 

@router.get("/user")
async def get_user(
    skip: int = 0,
    limit: int = 3,
    search: str | None = None,
    sort_by: str = "id",
    order: str = "asc"
):

    result = list(dbUser.values())

    # SEARCH FIXED
    if search:
        result = [
            user for user in result
            if search.lower() in user.name.lower()
        ]

    # SORTING
    reverse = order.lower() == "desc"

    try:
        result.sort(
            key=lambda x: getattr(x, sort_by),
            reverse=reverse
        )
    except AttributeError:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sort field: {sort_by}"
        )

    # PAGINATION
    result = result[skip:skip + limit]

    return {
        "total": len(result),
        "skip": skip,
        "limit": limit,
        "data": result
    }


# GET USER BY ID

@router.get("/user/{user_id}")
async def get_user_id(user_id: int):

    result = dbUser.get(user_id)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return result


# UPDATE USER

@router.put("/user/{user_id}")
async def update_user(user_id: int, updated_user: User):

    if user_id not in dbUser:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    updated_user.id = user_id
    dbUser[user_id] = updated_user

    return updated_user



# DELETE USER

@router.delete("/user/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(user_id: int):

    if user_id not in dbUser:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    del dbUser[user_id]
    return None



# AUTH PART (JWT)




# REGISTER

@router.post("/register")
async def register_user(user: User):

    if user.id in dbUser:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    # hash password
    user.password = hash_password(user.password)

    dbUser[user.id] = user

    return {"message": "User registered successfully"}



# LOGIN 

@router.post("/login")
async def login(user: User):

    db_user = None

    for u in dbUser.values():
        if u.email == user.email:
            db_user = u
            break

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

 
    if not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {"sub": db_user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }



# PROTECTED TEST ROUTE

@router.get("/protected")
def protected_route(current_user: str = Depends(get_current_user)):

    return {
        "message": "You are authenticated",
        "user": current_user
    }