from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserRegister(BaseModel):
    """Schema used to register a new user."""

    username: str = Field(
        ..., 
        min_length=3,
        description="Username for the new account.",
        example="jane_doe",
    )
    email: EmailStr = Field(
        ..., 
        description="Email address used for authentication and notifications.",
        example="jane.doe@example.com",
    )
    password: str = Field(
        ..., 
        min_length=8,
        description="User password; must be at least 8 characters.",
        example="StrongP@ssw0rd",
    )
    role: Literal["Admin", "HR", "Manager", "Employee"] = Field(
        ..., 
        description="Role assigned to the user.",
        example="Employee",
    )

    model_config = ConfigDict(from_attributes=True)


class UserLogin(BaseModel):
    """Schema used for user login requests."""

    email: EmailStr = Field(
        ..., 
        description="Registered email address for login.",
        example="jane.doe@example.com",
    )
    password: str = Field(
        ..., 
        min_length=8,
        description="Password for the user account.",
        example="StrongP@ssw0rd",
    )

    model_config = ConfigDict(from_attributes=True)


class TokenResponse(BaseModel):
    """Schema returned after a successful authentication request."""

    access_token: str = Field(
        ..., 
        description="JWT access token used for authenticated requests.",
        example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    )
    token_type: str = Field(
        default="bearer",
        description="Type of token returned by the authentication endpoint.",
        example="bearer",
    )

    model_config = ConfigDict(from_attributes=True)


class UserResponse(BaseModel):
    """Schema returned by the API for user profile responses."""

    id: int = Field(
        ..., 
        description="Unique identifier for the user.",
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
        example="Employee",
    )
    is_active: bool = Field(
        ..., 
        description="Indicates whether the user account is active.",
        example=True,
    )
    is_verified: bool = Field(
        ..., 
        description="Indicates whether the user's email has been verified.",
        example=False,
    )
    created_at: datetime = Field(
        ..., 
        description="Timestamp when the user account was created.",
        example="2026-06-01T12:34:56Z",
    )

    model_config = ConfigDict(from_attributes=True)
