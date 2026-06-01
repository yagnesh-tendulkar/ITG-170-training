from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Optional


class EmployeeCreate(BaseModel):

    name: str = Field(min_length=3, max_length=50)
    email: str
    position: str
    salary: float
    hired_at: datetime

    @field_validator("salary")
    def validate_salary(cls, value):
        if value <= 0:
            raise ValueError("Salary must be positive")
        return value


class EmployeeUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[str] = None
    position: Optional[str] = None
    salary: Optional[float] = None
    hired_at: Optional[datetime] = None

    @field_validator("salary")
    def validate_salary(cls, value):
        if value is not None and value <= 0:
            raise ValueError("Salary must be positive")
        return value
