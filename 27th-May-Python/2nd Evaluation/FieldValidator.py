from pydantic import BaseModel, field_validator

class Employee(BaseModel):
    name: str
    age: int

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")

        if not value.isalpha():
            raise ValueError("Name must contain only alphabets")

        return value