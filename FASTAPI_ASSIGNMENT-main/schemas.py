from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, field_validator


class CreateUser(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    age: int = Field(..., ge=18)
    password: str = Field(..., min_length=8)


class UpdateUser(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = Field(None, ge=18)


class CreateTask(BaseModel):
    title: str
    description: str
    priority: str
    due_date: datetime
    user_id: Optional[int] = None

    @field_validator("priority")
    def validate_priority(cls, value):
        value = value.lower()
        if value not in {"low", "medium", "high"}:
            raise ValueError("Priority must be low, medium, or high")
        return value


class UpdateTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    status: Optional[str] = None
    due_date: Optional[datetime] = None

    @field_validator("priority")
    def validate_priority(cls, value):
        if value is None:
            return value
        value = value.lower()
        if value not in {"low", "medium", "high"}:
            raise ValueError("Priority must be low, medium, or high")
        return value
