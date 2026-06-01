# schemas/employee_schema.py

from pydantic import BaseModel

class Employee(BaseModel):
    name:str
    email:str
    password:str