from datetime import date, time, datetime
from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, Field


class AttendanceCreate(BaseModel):
    """Schema used to create a new attendance entry."""

    employee_id: int = Field(
        ...,
        gt=0,
        description="Identifier of the employee associated with this attendance record.",
        example=1,
    )
    attendance_date: date = Field(
        ...,
        description="Date of the attendance entry.",
        example="2026-06-01",
    )
    check_in_time: Optional[time] = Field(
        None,
        description="Optional check-in time for the employee.",
        example="09:00:00",
    )
    check_out_time: Optional[time] = Field(
        None,
        description="Optional check-out time for the employee.",
        example="17:30:00",
    )
    status: Literal["Present", "Absent", "Half Day", "Leave"] = Field(
        ..., 
        description="Attendance status for the day.",
        example="Present",
    )
    work_hours: float = Field(
        ...,
        ge=0,
        description="Number of hours worked for this attendance entry.",
        example=8.0,
    )
    remarks: Optional[str] = Field(
        None,
        description="Optional remarks about the attendance record.",
        example="Arrived on time and completed client review.",
    )

    model_config = ConfigDict(from_attributes=True)


class AttendanceUpdate(BaseModel):
    """Schema used to update an existing attendance entry."""

    employee_id: Optional[int] = Field(
        None,
        gt=0,
        description="Identifier of the employee associated with this attendance record.",
        example=1,
    )
    attendance_date: Optional[date] = Field(
        None,
        description="Date of the attendance entry.",
        example="2026-06-01",
    )
    check_in_time: Optional[time] = Field(
        None,
        description="Updated check-in time for the employee.",
        example="09:00:00",
    )
    check_out_time: Optional[time] = Field(
        None,
        description="Updated check-out time for the employee.",
        example="17:30:00",
    )
    status: Optional[Literal["Present", "Absent", "Half Day", "Leave"]]
    remarks: Optional[str] = Field(
        None,
        description="Updated remarks about the attendance record.",
        example="Left early for a medical appointment.",
    )
    work_hours: Optional[float] = Field(
        None,
        ge=0,
        description="Updated number of hours worked for this attendance entry.",
        example=7.5,
    )

    model_config = ConfigDict(from_attributes=True)


class AttendanceResponse(BaseModel):
    """Schema returned by the API for attendance read operations."""

    id: int = Field(
        ..., 
        description="Unique attendance record identifier.",
        example=1,
    )
    employee_id: int = Field(
        ..., 
        gt=0,
        description="Identifier of the employee associated with this attendance record.",
        example=1,
    )
    attendance_date: date = Field(
        ..., 
        description="Date of the attendance entry.",
        example="2026-06-01",
    )
    check_in_time: Optional[time] = Field(
        None,
        description="Check-in time for the employee.",
        example="09:00:00",
    )
    check_out_time: Optional[time] = Field(
        None,
        description="Check-out time for the employee.",
        example="17:30:00",
    )
    status: Literal["Present", "Absent", "Half Day", "Leave"] = Field(
        ..., 
        description="Attendance status for the day.",
        example="Present",
    )
    work_hours: float = Field(
        ..., 
        ge=0,
        description="Number of hours worked for this attendance entry.",
        example=8.0,
    )
    remarks: Optional[str] = Field(
        None,
        description="Optional remarks about the attendance record.",
        example="Completed all scheduled tasks.",
    )
    created_at: datetime = Field(
        ..., 
        description="Timestamp when the attendance record was created.",
        example="2026-06-01T09:00:00Z",
    )
    updated_at: datetime = Field(
        ..., 
        description="Timestamp when the attendance record was last updated.",
        example="2026-06-01T17:30:00Z",
    )

    model_config = ConfigDict(from_attributes=True)
