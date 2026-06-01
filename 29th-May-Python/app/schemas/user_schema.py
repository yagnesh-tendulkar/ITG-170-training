from pydantic import BaseModel, field_validator

class UserCreate(BaseModel):

    name: str
    email: str
    age: int

    @field_validator("age")
    def validate_age(cls, value):

        if value < 18:
            raise ValueError("Age must be above 18")

        return value