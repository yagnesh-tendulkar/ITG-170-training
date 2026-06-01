from pydantic import BaseModel, EmailStr
from typing import Optional

class Employee(BaseModel):
    id: int
    name: str
    age: int
    department: str
    email: EmailStr

class UpdateEmployee(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    department: Optional[str] = None
    email: Optional[EmailStr] = None