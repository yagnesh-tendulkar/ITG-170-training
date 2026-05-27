#implement a custom field validator from pydantic
from fastapi import FastAPI
from pydantic import BaseModel, Field

fld=FastAPI()
class Employee(BaseModel):
    name:str=Field(...,min_length=9,max_length=20,description="Name must be between 9 and 20 characters")

# @validator('name')
# def validate_name(cls, value):
#     return value.strip()  # Remove leading/trailing whitespace

class ResponseEmployee(BaseModel):
    name:str

@fld.get("/employee")
def get_employee():
    return {"employee": {"name": "John Doe"}}

@fld.post("/employee")
def create_employee(employee: Employee,request: ResponseEmployee,status_code=201,summary="Create Employee"):
    new_emp={"name": employee.name.capitalize()}
    return {"employee": new_emp}