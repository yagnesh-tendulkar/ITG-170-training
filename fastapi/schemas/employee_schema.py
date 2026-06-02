from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, field_validator


def _to_utc(value: datetime) -> datetime:
    if value.tzinfo is None or value.tzinfo.utcoffset(value) is None:
        return value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc)


class EmployeeCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    position: str = Field(..., min_length=2, max_length=50)
    salary: float = Field(..., gt=0)
    hired_at: datetime

    @field_validator("position")
    def validate_position(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Position must not be empty")
        return value.strip()

    @field_validator("hired_at")
    def validate_hired_at(cls, value: datetime) -> datetime:
        if _to_utc(value) > datetime.now(timezone.utc):
            raise ValueError("Hired date cannot be in the future")
        return value


class EmployeeUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    position: Optional[str] = Field(None, min_length=2, max_length=50)
    salary: Optional[float] = Field(None, gt=0)
    hired_at: Optional[datetime] = None

    @field_validator("position")
    def validate_position(cls, value: Optional[str]) -> Optional[str]:
        if value is not None and not value.strip():
            raise ValueError("Position must not be empty")
        return value.strip() if value is not None else value

    @field_validator("hired_at")
    def validate_hired_at(cls, value: Optional[datetime]) -> Optional[datetime]:
        if value is not None and _to_utc(value) > datetime.now(timezone.utc):
            raise ValueError("Hired date cannot be in the future")
        return value
