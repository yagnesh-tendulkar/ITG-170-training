from fastapi import FastAPI
from pydantic import BaseModel, field_validator

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: str
    password: str

    @field_validator("age")
    def validate_age(cls, value):
        if value < 18:
            raise ValueError("Age must be at least 18")
        if value > 100:
            raise ValueError("Age must be less than 100")
        return value

    @field_validator("password")
    def validate_password(cls, value):
        if len(value) < 10:
            raise ValueError("Password must be at least 10 characters")
        if "@" not in value:
            raise ValueError("Password must contain '@'")
        return value

@app.post("/user")
def create_user(u: User):
    return {"data": u}