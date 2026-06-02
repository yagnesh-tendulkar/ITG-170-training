# Custom Field Validator from Pydantic

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Employee(BaseModel):

    name: str = Field(
        min_length=2,
        max_length=10,
        description="Only strings are allowed"
    )

    phone_number: str = Field(
        min_length=10,
        max_length=10,
        description="Enter valid 10 digit phone number"
    )

@app.post("/emp/{id}")
def post_method(id: int, employee: Employee):

    return {
        "id": id,
        "emp_name": employee.name,
        "pno": employee.phone_number
    }