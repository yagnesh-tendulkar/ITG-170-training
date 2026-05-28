from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Query
from fastapi import Path
from fastapi import status

from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from pydantic import Field

from typing import Optional


app = FastAPI(
    title="CRUD API with Query, Path Params and Request Body"
)


# CORS MIDDLEWARE
app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)


# TEMP DATABASE
employees = []


# Pydantic Schema
class Employee(BaseModel):

    name: str = Field(
        min_length=2,
        max_length=100
    )

    department: str = Field(
        min_length=2,
        max_length=100
    )

    salary: int = Field(
        gt=0
    )


# HOME API
@app.get("/")
def home():

    return {
        "message": "FastAPI CRUD Running"
    }


# CREATE EMPLOYEE
@app.post(
    "/employees",
    status_code=status.HTTP_201_CREATED
)
def create_employee(

    # QUERY PARAM
    bonus: int = Query(
        default=0,
        ge=0,
        description="Bonus added to salary"
    ),

    # REQUEST BODY
    employee: Employee = ...
):

    employee_dict = employee.dict()

    employee_dict["salary"] += bonus

    employee_id = len(employees) + 1

    employee_dict["id"] = employee_id

    employees.append(employee_dict)

    return {
        "message": "Employee created successfully",
        "data": employee_dict
    }


# READ EMPLOYEES
@app.get(
    "/employees",
    status_code=status.HTTP_200_OK
)
def get_employees(

    # QUERY PARAM
    department: Optional[str] = Query(
        default=None
    )
):

    if department:

        filtered_employees = [
            employee for employee in employees
            if employee["department"].lower() == department.lower()
        ]

        return filtered_employees

    return employees


# UPDATE EMPLOYEE
@app.put(
    "/employees/{employee_id}",
    status_code=status.HTTP_200_OK
)
def update_employee(

    # PATH PARAM
    employee_id: int = Path(
        ...,
        gt=0
    ),

    # QUERY PARAM
    increment_salary: int = Query(
        default=0,
        ge=0
    ),

    # REQUEST BODY
    employee: Employee = ...
):

    for one_employee in employees:

        if one_employee["id"] == employee_id:

            updated_data = employee.dict()

            updated_data["salary"] += increment_salary

            updated_data["id"] = employee_id

            one_employee.update(updated_data)

            return {
                "message": "Employee updated successfully",
                "data": one_employee
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Employee not found"
    )


# DELETE EMPLOYEE
@app.delete(
    "/employees/{employee_id}",
    status_code=status.HTTP_200_OK
)
def delete_employee(

    # PATH PARAM
    employee_id: int = Path(
        ...,
        gt=0
    ),

    # QUERY PARAM
    confirm: bool = Query(
        default=False
    )
):

    if not confirm:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Please confirm deletion"
        )

    for index, one_employee in enumerate(employees):

        if one_employee["id"] == employee_id:

            deleted_employee = employees.pop(index)

            return {
                "message": "Employee deleted successfully",
                "data": deleted_employee
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Employee not found"
    )