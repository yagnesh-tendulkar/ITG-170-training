from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Process-Time"]
)
fake_db = {}

@app.get("/", status_code=status.HTTP_200_OK)
def greet():
    return {
        "status": "success",
        "message": "FastAPI code "
    }

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    if user.id in fake_db:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists"
        )

    fake_db[user.id] = user.model_dump()

    return {
        "status": "success",
        "message": "User created successfully",
        "data": fake_db[user.id]
    }

@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
def get_user(user_id: int):
    if user_id not in fake_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return {
        "status": "success",
        "data": fake_db[user_id]
    }

@app.put("/users/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: int, updated_user: User):
    if user_id not in fake_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    fake_db[user_id] = updated_user.model_dump()

    return {
        "status": "success",
        "message": "User updated successfully",
        "data": fake_db[user_id]
    }
@app.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: int):

    if user_id not in fake_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    deleted_user = fake_db.pop(user_id)

    return {
        "status": "success",
        "message": "User deleted successfully",
        "data": deleted_user
    }
