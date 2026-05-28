# from fastapi import FastAPI,HTTPException,status
# app = FastAPI()
# @app.get("/student",status_code=status.HTTP_404_NOT_FOUND)
# def student():
#     return {"message":"Log not found"}
# @app.post("/created",status_code=status.HTTP_201_CREATED)
# def create(id: int):
#     return {"message":"Successfully registered"}
# @app.get("/student/{id}", status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
# def get_student_by_id(id: int):
#     return {
#         "message": "Server Unavailable",
#         "student_id": id
#     }
from fastapi import FastAPI
from pydantic import BaseModel, field_validator

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

    @field_validator("age")
    @classmethod
    def validate_age(User, value):

        if value < 18:
            raise ValueError("Age must be at least 18")

        return value

@app.post("/user")
def create_user(user: User):
    return {
        "message": "User created",
        "data": user
    }