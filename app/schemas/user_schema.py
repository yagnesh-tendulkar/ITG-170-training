from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
    """Schema used to create a new user."""

    username: str = Field(
        ..., 
        min_length=3,
        description="Unique username for the user account.",
        example="jane_doe",
    )
    email: EmailStr = Field(
        ..., 
        description="User email address for authentication and notifications.",
        example="jane.doe@example.com",
    )
    role: Literal["Admin", "HR", "Manager", "Employee"] = Field(
        ..., 
        description="Role assigned to the user.",
        example="Employee",
    )
    is_active: bool = Field(
        default=True,
        description="Whether the user account is currently active.",
        example=True,
    )
    is_verified: bool = Field(
        default=False,
        description="Whether the user's email has been verified.",
        example=False,
    )

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    """Schema used to update an existing user."""

    username: Optional[str] = Field(
        None,
        min_length=3,
        description="Updated username for the user account.",
        example="jane_doe",
    )
    email: Optional[EmailStr] = Field(
        None,
        description="Updated user email address.",
        example="jane.doe@example.com",
    )
    role: Optional[Literal["Admin", "HR", "Manager", "Employee"]]
    is_active: Optional[bool] = Field(
        None,
        description="Whether the user account is currently active.",
        example=True,
    )
    is_verified: Optional[bool] = Field(
        None,
        description="Whether the user's email has been verified.",
        example=True,
    )

    model_config = ConfigDict(from_attributes=True)


class UserResponse(BaseModel):
    """Schema returned by the API for user read operations."""

    id: int = Field(
        ..., 
        description="Unique user identifier.",
        example=1,
    )
    username: str = Field(
        ..., 
        description="Username of the user.",
        example="jane_doe",
    )
    email: EmailStr = Field(
        ..., 
        description="User's email address.",
        example="jane.doe@example.com",
    )
    role: Literal["Admin", "HR", "Manager", "Employee"] = Field(
        ..., 
        description="Role assigned to the user.",
        example="Manager",
    )
    is_active: bool = Field(
        ..., 
        description="Whether the user account is active.",
        example=True,
    )
    is_verified: bool = Field(
        ..., 
        description="Whether the user's email has been verified.",
        example=False,
    )
    created_at: datetime = Field(
        ..., 
        description="Timestamp when the user was created.",
        example="2026-06-01T12:34:56Z",
    )
    updated_at: datetime = Field(
        ..., 
        description="Timestamp when the user was last updated.",
        example="2026-06-02T12:34:56Z",
    )

    model_config = ConfigDict(from_attributes=True)
