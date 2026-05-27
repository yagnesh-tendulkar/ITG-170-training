from pydantic import BaseModel, field_validator

class User(BaseModel):
    username: str
    password: str

    @field_validator("username")
    @classmethod
    def validate_username(cls, value: str):
        if len(value) < 4:
            raise ValueError("Username must be at least 4 characters long")
