from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI()


# -----------------------------
# Pydantic Model
# -----------------------------
class User(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    first_name: str
    last_name: str
    age: int


# -----------------------------
# Home Route
# -----------------------------
@app.get("/")
def home():
    return {"message": "Welcome to Balaji Services"}


# -----------------------------
# GET ALL USERS
# -----------------------------
@app.get("/users")
def get_users():
    return {
        "users": [
            {
                "username": "balaji",
                "first_name": "Pasam",
                "last_name": "Kumar",
                "age": 22
            },
            {
                "username": "rahul",
                "first_name": "Ravi",
                "last_name": "Teja",
                "age": 23
            }
        ]
    }


# -----------------------------
# GET SINGLE USER
# -----------------------------
@app.get("/users/{username}")
def get_user(username: str):
    return {
        "message": f"User {username} found successfully"
    }


# -----------------------------
# CREATE USER
# -----------------------------
@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    # user=append.users
    return {
        "message": "User created successfully",
        "data": user
    }


# -----------------------------
# UPDATE USER
# -----------------------------
@app.put("/users/{username}")
def update_user(username: str, user: User):
    return {
        "message": f"{username} updated successfully",
        "updated_data": user
    }


# -----------------------------
# DELETE USER
# -----------------------------
@app.delete("/users/{username}")
def delete_user(username: str):
    return {
        "message": f"{username} deleted successfully"
    }


# -----------------------------
# SEARCH USER USING QUERY PARAMETER
# Example:
# /search?age=22
# -----------------------------
@app.get("/search")
def search_user(age: int):
    return {
        "message": f"Users with age {age} fetched successfully"
    }


# -----------------------------
# EXCEPTION HANDLING
# -----------------------------
@app.get("/error/{username}")
def get_error(username: str):

    if username != "balaji":
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": f"Welcome {username}"
    }