from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional, List

class User(BaseModel):
    id: int
    name: str
    email: EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

    @field_validator("password")
    def validate_password(cls, v):
        if len(v) < 6:
            raise ValueError("Password too short")
        return v


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class TaskCreate(BaseModel):
    title: str
    description: str
    priority: str
    tags: List[str] = []

    @field_validator("priority")
    def validate_priority(cls, v):
        if v not in ["low", "medium", "high"]:
            raise ValueError("Invalid priority")
        return v


class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[str]
