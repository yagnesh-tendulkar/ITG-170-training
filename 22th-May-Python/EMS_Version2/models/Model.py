from datetime import datetime
from pydantic import BaseModel
from enum import Enum

from dbConfig.DBConnection import Base


class Department(BaseModel):
    department_id: str
    department_name: str

class Role(BaseModel):
    role_id: str
    role :str

class Status(Enum):
    a = "active"
    i = "inactive"
    p = "assigned"
    b = "bench"

class Employee(Base):
    empid: int
    fname: str
    lname: str
    phone: str
    pmail: str
    cmail:str
    password:str
    dept: Department.department_id
    role: Role.role_id
    salary: float
    status: Status.a
    join_date: datetime