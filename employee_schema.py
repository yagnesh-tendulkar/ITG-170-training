from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class EmployeeCreate(BaseModel):
    fname: str = Field(..., min_length=2, max_length=50)
    lname: str = Field(..., min_length=2, max_length=50)

    personal_mail: EmailStr

    department: str = Field(..., min_length=2, max_length=50)

    role_id: str = Field(..., min_length=1, max_length=1)   # H, D, T, M

    joining_date: datetime

    salary: float = Field(..., gt=0)

    status_id: str = Field(..., min_length=1, max_length=1)  # A, P, I, B


class EmployeeResponse(BaseModel):
    employee_id: int
    fname: str
    lname: str
    personal_mail: EmailStr
    corporate_mail: str
    department: str
    role_id: str
    joining_date: datetime
    salary: float
    status_id: str

    class Config:
        from_attributes = True