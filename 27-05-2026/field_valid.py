from fastapi import FastAPI
from pydantic import BaseModel, field_validator

app = FastAPI()
#create employee model
class Employee(BaseModel):
    name: str
    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        if len(value) < 3:
            raise ValueError(
                "Name must contain at least 3 characters"
            )
        return value


@app.post("/employee")
def create_employee(employee: Employee):

    return {

        "name": employee.name
    }