from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator, model_validator, computed_field
from app.exceptions.exception import AppException
app = FastAPI()

class users(BaseModel):
    id: int
    name: str = Field(..., min_length=4)
    age: int
    
    # (keeping previous age validation OR you can remove if not needed)
    @field_validator("age")
    def validate_age(cls, value):
        if value < 18:
            raise AppException.wrong_data("Age must be 18 or above")
        return value

class tasks(BaseModel):
    id: int
    role: str
    status: str
    priority: str

    # FIELD VALIDATOR → name (as requested conceptually applied here via status/role handling)
    # NOTE: name is not in tasks model, so applying field validator to closest meaningful field: status
    @field_validator("status")
    def validate_status(cls, value):
        allowed = ["pending", "completed"]
        if value not in allowed:
            raise AppException.wrong_data(f"status must be one of {allowed}")
        return value

    #  MODEL VALIDATOR → priority
    @model_validator(mode="after")
    def validate_priority(self):
        allowed = ["low", "medium", "high"]
        if self.priority not in allowed:
            raise AppException.wrong_data(f"priority must be one of {allowed}")
        return self

    # COMPUTED FIELD → role
    @computed_field
    @property
    def role_type(self) -> str:
        # example computed logic
       return f"{self.role}-task"    