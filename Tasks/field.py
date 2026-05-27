from fastapi import FastAPI
from pydantic import BaseModel, field_validator

app = FastAPI()


class User(BaseModel):
    username: str

    @field_validator("username")
    @classmethod
    def validate_username(cls, value):
        if len(value) < 3:
            raise ValueError("username must be at least 3 characters")
        return value


@app.post("/user")
def create_user(user: User):
    return user