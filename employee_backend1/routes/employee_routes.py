from fastapi import APIRouter

from schemas.employee_schema import EmployeeCreate

from services.employee_service import (
    create_employee,
    get_all_employees,
    get_single_employee,
    update_employee,
    delete_employee
)

router = APIRouter()


# CREATE
@router.post("/employee")
async def add_employee(data: EmployeeCreate):

    return create_employee(data)


# GET ALL
@router.get("/employees")
async def fetch_all_employees():

    return get_all_employees()


# GET SINGLE
@router.get("/employee/{emp_id}")
async def fetch_single_employee(emp_id: int):

    return get_single_employee(emp_id)


# UPDATE
@router.put("/employee/{emp_id}")
async def edit_employee(emp_id: int, data: EmployeeCreate):

    return update_employee(emp_id, data)


# DELETE
@router.delete("/employee/{emp_id}")
async def remove_employee(emp_id: int):

    return delete_employee(emp_id)