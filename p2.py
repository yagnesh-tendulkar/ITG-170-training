from pydantic import BaseModel, field_validator


class User(BaseModel):

    name: str
    age: int

    
    @field_validator("age")
    @classmethod
    def validate_age(cls, value):

        if value < 18:
            raise ValueError("Age must be above 18")

        return value