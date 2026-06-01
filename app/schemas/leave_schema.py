from datetime import date, datetime
from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


class LeaveCreate(BaseModel):
    """Schema used to create a new leave request."""

    employee_id: int = Field(
        ...,
        gt=0,
        description="Identifier of the employee requesting leave.",
        example=1,
    )
    leave_type: Literal[
        "Sick Leave",
        "Casual Leave",
        "Earned Leave",
        "Maternity Leave",
        "Unpaid Leave",
    ] = Field(
        ..., 
        description="Type of leave requested.",
        example="Sick Leave",
    )
    start_date: date = Field(
        ...,
        description="First day of the leave period.",
        example="2026-06-10",
    )
    end_date: date = Field(
        ...,
        description="Last day of the leave period.",
        example="2026-06-12",
    )
    total_days: float = Field(
        ...,
        gt=0,
        description="Total number of leave days.",
        example=3.0,
    )
    reason: Optional[str] = Field(
        None,
        description="Optional reason for the leave request.",
        example="Medical appointment.",
    )
    status: Literal[
        "Pending",
        "Approved",
        "Rejected",
        "Cancelled",
    ] = Field(
        default="Pending",
        description="Current approval status of the leave request.",
        example="Pending",
    )
    approved_by: Optional[str] = Field(
        None,
        description="Name of the approver for the leave request.",
        example="Alex Johnson",
    )

    @field_validator("approved_by")
    def normalize_approved_by(cls, value: Optional[str]) -> Optional[str]:
        if value is None:
            return None
        stripped = value.strip()
        if stripped == "":
            raise ValueError("approved_by cannot be blank if provided")
        return stripped

    @model_validator(mode="after")
    def validate_date_range(self) -> "LeaveCreate":
        if self.start_date > self.end_date:
            raise ValueError("start_date must not be after end_date")
        return self

    model_config = ConfigDict(from_attributes=True)


class LeaveUpdate(BaseModel):
    """Schema used to update an existing leave request."""

    employee_id: Optional[int] = Field(
        None,
        gt=0,
        description="Identifier of the employee requesting leave.",
        example=1,
    )
    leave_type: Optional[Literal[
        "Sick Leave",
        "Casual Leave",
        "Earned Leave",
        "Maternity Leave",
        "Unpaid Leave",
    ]] = Field(
        None,
        description="Updated type of leave requested.",
        example="Earned Leave",
    )
    start_date: Optional[date] = Field(
        None,
        description="Updated first day of the leave period.",
        example="2026-06-10",
    )
    end_date: Optional[date] = Field(
        None,
        description="Updated last day of the leave period.",
        example="2026-06-12",
    )
    total_days: Optional[float] = Field(
        None,
        gt=0,
        description="Updated total number of leave days.",
        example=2.5,
    )
    reason: Optional[str] = Field(
        None,
        description="Updated reason for the leave request.",
        example="Extended family care.",
    )
    status: Optional[Literal[
        "Pending",
        "Approved",
        "Rejected",
        "Cancelled",
    ]] = Field(
        None,
        description="Updated approval status of the leave request.",
        example="Approved",
    )
    approved_by: Optional[str] = Field(
        None,
        description="Updated approver name for the leave request.",
        example="Alex Johnson",
    )

    @field_validator("approved_by")
    def normalize_approved_by(cls, value: Optional[str]) -> Optional[str]:
        if value is None:
            return None
        stripped = value.strip()
        if stripped == "":
            raise ValueError("approved_by cannot be blank if provided")
        return stripped

    @model_validator(mode="after")
    def validate_date_range(self) -> "LeaveUpdate":
        if self.start_date is not None and self.end_date is not None:
            if self.start_date > self.end_date:
                raise ValueError("start_date must not be after end_date")
        return self

    model_config = ConfigDict(from_attributes=True)


class LeaveResponse(BaseModel):
    """Schema returned by the API for leave request responses."""

    id: int = Field(
        ..., 
        description="Unique leave request identifier.",
        example=1,
    )
    employee_id: int = Field(
        ..., 
        gt=0,
        description="Identifier of the employee requesting leave.",
        example=1,
    )
    leave_type: Literal[
        "Sick Leave",
        "Casual Leave",
        "Earned Leave",
        "Maternity Leave",
        "Unpaid Leave",
    ] = Field(
        ..., 
        description="Type of leave requested.",
        example="Sick Leave",
    )
    start_date: date = Field(
        ..., 
        description="First day of the leave period.",
        example="2026-06-10",
    )
    end_date: date = Field(
        ..., 
        description="Last day of the leave period.",
        example="2026-06-12",
    )
    total_days: float = Field(
        ..., 
        gt=0,
        description="Total number of leave days.",
        example=3.0,
    )
    reason: Optional[str] = Field(
        None,
        description="Reason for the leave request.",
        example="Medical appointment.",
    )
    status: Literal[
        "Pending",
        "Approved",
        "Rejected",
        "Cancelled",
    ] = Field(
        ..., 
        description="Current approval status of the leave request.",
        example="Pending",
    )
    approved_by: Optional[str] = Field(
        None,
        description="Approver name for the leave request.",
        example="Alex Johnson",
    )
    created_at: datetime = Field(
        ..., 
        description="Timestamp when the leave request was created.",
        example="2026-06-01T12:34:56Z",
    )
    updated_at: datetime = Field(
        ..., 
        description="Timestamp when the leave request was last updated.",
        example="2026-06-02T12:34:56Z",
    )

    model_config = ConfigDict(from_attributes=True)
