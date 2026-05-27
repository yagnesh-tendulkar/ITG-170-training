from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
app = FastAPI()
users = {}
class User(BaseModel):
    username: str
    password: str
@app.post("/user/{user_id}", status_code=status.HTTP_201_CREATED)
def create_user(user_id: str, user: User):

    if user_id in users:
        raise HTTPException(
            status_code=409,
            detail="User already exists"
        )

    return {
        "message": "User created",
        "data": users[user_id]
    }
@app.get("/user/{user_id}", status_code=status.HTTP_200_OK)
def get_user(user_id: str):

    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return users[user_id]
@app.put("/user/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: str, user: User):

    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    users[user_id] = user.model_dump()

    return {
        "message": "User updated",
        "data": users[user_id]
    }
@app.patch("/user/{user_id}", status_code=status.HTTP_200_OK)
def update_password(user_id: str, password: str):

    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    users[user_id]["password"] = password

    return {
        "message": "Password updated"
    }
@app.delete("/user/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: str):

    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    del users[user_id]

    return {
        "message": "User deleted"
    }
