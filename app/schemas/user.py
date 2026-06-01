from pydantic import BaseModel, EmailStr, field_validator, computed_field
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    age: int

    @field_validator("age")
    @classmethod
    def validate_age(cls, value: int) -> int:
        if value < 18:
            raise ValueError("Age must be 18 or above")
        return value

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        if len(value.strip()) < 2:
            raise ValueError("Name must be at least 2 characters")
        return value.strip()


class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None

    @field_validator("age")
    @classmethod
    def validate_age(cls, value: Optional[int]) -> Optional[int]:
        if value is not None and value < 18:
            raise ValueError("Age must be 18 or above")
        return value


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    age: int
    is_active: bool
    created_at: datetime

    @computed_field
    @property
    def display_name(self) -> str:
        return f"{self.name} (#{self.id})"

    model_config = {"from_attributes": True}


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
