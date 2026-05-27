from pydantic import BaseModel   

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class LoginSchema(BaseModel):
    username: str
    password: str

class EmployeeCreate(BaseModel):
    name: str
    department: str
    salary: int