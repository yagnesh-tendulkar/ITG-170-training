from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class EmployeeCreate(BaseModel):
    """Schema for creating a new employee record."""

    first_name: str = Field(
        ...,
        min_length=2,
        description="Employee first name.",
        example="Jane",
    )
    last_name: str = Field(
        ...,
        min_length=2,
        description="Employee last name.",
        example="Doe",
    )
    email: EmailStr = Field(
        ...,
        description="Employee email address.",
        example="jane.doe@example.com",
    )
    phone: str = Field(
        ...,
        min_length=10,
        description="Employee contact phone number.",
        example="+1234567890",
    )
    designation: Optional[str] = Field(
        None,
        description="Job title or role for the employee.",
        example="Product Manager",
    )
    salary: float = Field(
        ...,
        gt=0,
        description="Employee salary amount, must be greater than zero.",
        example=85000.0,
    )
    department: Optional[str] = Field(
        None,
        description="Department or team name for the employee.",
        example="Human Resources",
    )
    is_active: bool = Field(
        default=True,
        description="Whether the employee is currently active.",
        example=True,
    )

    model_config = ConfigDict(from_attributes=True)


class EmployeeUpdate(BaseModel):
    """Schema for updating an existing employee record."""

    first_name: Optional[str] = Field(
        None,
        min_length=2,
        description="Employee first name.",
        example="Jane",
    )
    last_name: Optional[str] = Field(
        None,
        min_length=2,
        description="Employee last name.",
        example="Doe",
    )
    email: Optional[EmailStr] = Field(
        None,
        description="Employee email address.",
        example="jane.doe@example.com",
    )
    phone: Optional[str] = Field(
        None,
        min_length=10,
        description="Employee contact phone number.",
        example="+1234567890",
    )
    designation: Optional[str] = Field(
        None,
        description="Job title or role for the employee.",
        example="Product Manager",
    )
    salary: Optional[float] = Field(
        None,
        gt=0,
        description="Employee salary amount; must be greater than zero.",
        example=85000.0,
    )
    department: Optional[str] = Field(
        None,
        description="Department or team name for the employee.",
        example="Human Resources",
    )
    is_active: Optional[bool] = Field(
        None,
        description="Whether the employee is currently active.",
        example=True,
    )

    model_config = ConfigDict(from_attributes=True)


class EmployeeResponse(BaseModel):
    """Schema returned by the API for employee read operations."""

    id: int = Field(
        ..., 
        description="Unique employee identifier.",
        example=1,
    )
    first_name: str = Field(
        ..., 
        description="Employee first name.",
        example="Jane",
    )
    last_name: str = Field(
        ..., 
        description="Employee last name.",
        example="Doe",
    )
    email: EmailStr = Field(
        ..., 
        description="Employee email address.",
        example="jane.doe@example.com",
    )
    phone: str = Field(
        ..., 
        description="Employee contact phone number.",
        example="+1234567890",
    )
    designation: Optional[str] = Field(
        None,
        description="Job title or role for the employee.",
        example="Product Manager",
    )
    salary: float = Field(
        ..., 
        gt=0,
        description="Employee salary amount.",
        example=85000.0,
    )
    department: Optional[str] = Field(
        None,
        description="Department or team name for the employee.",
        example="Human Resources",
    )
    is_active: bool = Field(
        ..., 
        description="Whether the employee is currently active.",
        example=True,
    )
    created_at: datetime = Field(
        ..., 
        description="Timestamp when the employee record was created.",
        example="2026-06-01T12:34:56Z",
    )
    updated_at: datetime = Field(
        ..., 
        description="Timestamp when the employee record was last updated.",
        example="2026-06-02T12:34:56Z",
    )

    model_config = ConfigDict(from_attributes=True)
