from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class DepartmentCreate(BaseModel):
    """Schema used to create a new department."""

    name: str = Field(
        ...,
        min_length=2,
        description="Name of the department.",
        example="Human Resources",
    )
    description: Optional[str] = Field(
        None,
        description="Optional description of the department's responsibilities.",
        example="Handles all employee onboarding and benefits.",
    )
    location: Optional[str] = Field(
        None,
        description="Location of the department or team.",
        example="Headquarters, Building A",
    )
    manager_name: Optional[str] = Field(
        None,
        description="Name of the department manager.",
        example="Alex Johnson",
    )
    budget: float = Field(
        ..., 
        ge=0,
        description="Budget allocated to the department.",
        example=125000.0,
    )
    is_active: bool = Field(
        default=True,
        description="Whether the department is currently active.",
        example=True,
    )

    model_config = ConfigDict(from_attributes=True)


class DepartmentUpdate(BaseModel):
    """Schema used for partial updates to a department."""

    name: Optional[str] = Field(
        None,
        min_length=2,
        description="Updated department name.",
        example="Human Resources",
    )
    description: Optional[str] = Field(
        None,
        description="Updated department description.",
        example="Handles employee training and retention.",
    )
    location: Optional[str] = Field(
        None,
        description="Updated department location.",
        example="Satellite Office, Floor 3",
    )
    manager_name: Optional[str] = Field(
        None,
        description="Updated name of the department manager.",
        example="Alex Johnson",
    )
    budget: Optional[float] = Field(
        None,
        ge=0,
        description="Updated budget for the department.",
        example=130000.0,
    )
    is_active: Optional[bool] = Field(
        None,
        description="Whether the department is active.",
        example=True,
    )

    model_config = ConfigDict(from_attributes=True)


class DepartmentResponse(BaseModel):
    """Schema returned by the API for department read operations."""

    id: int = Field(
        ..., 
        description="Unique department identifier.",
        example=1,
    )
    name: str = Field(
        ..., 
        description="Name of the department.",
        example="Human Resources",
    )
    description: Optional[str] = Field(
        None,
        description="Description of the department's responsibilities.",
        example="Handles employee onboarding and benefits.",
    )
    location: Optional[str] = Field(
        None,
        description="Location of the department.",
        example="Headquarters, Building A",
    )
    manager_name: Optional[str] = Field(
        None,
        description="Name of the department manager.",
        example="Alex Johnson",
    )
    budget: float = Field(
        ..., 
        ge=0,
        description="Budget allocated to the department.",
        example=125000.0,
    )
    is_active: bool = Field(
        ..., 
        description="Whether the department is currently active.",
        example=True,
    )
    created_at: datetime = Field(
        ..., 
        description="Timestamp when the department record was created.",
        example="2026-06-01T12:34:56Z",
    )
    updated_at: datetime = Field(
        ..., 
        description="Timestamp when the department record was last updated.",
        example="2026-06-02T12:34:56Z",
    )

    model_config = ConfigDict(from_attributes=True)
