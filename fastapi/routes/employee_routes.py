# from fastapi import APIRouter

# from schemas.employee_schema import EmployeeCreate

# from services.employee_service import *

# from auth.jwt_handler import verify_token
# from routes.auth_routes import LoginRequest
# router = APIRouter()


# @router.post('/employees')
# def add_employee(employee: EmployeeCreate):
#     return create_employee(employee)


# @router.get('/employees')
# def all_employees():
#     return get_employees()


# @router.get('/employees/{employee_id}')
# def single_employee(employee_id: int):
#     return get_employee(employee_id)


# @router.delete('/employees/{employee_id}')
# def remove_employee(employee_id: int):
#     return delete_employee(employee_id)
from fastapi import APIRouter, Depends, Query

from schemas.employee_schema import EmployeeCreate, EmployeeUpdate
from services.employee_service import *

from auth.auth_dependencies import verify_auth

router = APIRouter()


# Create Employee
@router.post("/employees")
def add_employee(
    employee: EmployeeCreate,
    user: dict = Depends(verify_auth)
):
    return create_employee(employee, (user.get("user") or user.get("username")))


# Get All Employees with Pagination & Filtering
@router.get("/employees")
def all_employees(
    department: str | None = Query(None),
    page: int = Query(1, ge=1),
    limit: int = Query(5, ge=1),
    user: dict = Depends(verify_auth)
):
    employees = get_employees()

    # Filtering
    if department:
        employees = [
            emp for emp in employees
            if emp.get("department") == department
        ]

    # Pagination
    start = (page - 1) * limit
    end = start + limit

    return {
        "page": page,
        "limit": limit,
        "total": len(employees),
        "data": employees[start:end]
    }


# Get Single Employee
@router.get("/employees/{employee_id}")
def single_employee(
    employee_id: int,
    user: dict = Depends(verify_auth)
):
    return get_employee(employee_id)


# Update Employee (full replacement)
@router.put("/employees/{employee_id}")
def update_employee_route(
    employee_id: int,
    employee: EmployeeCreate,
    user: dict = Depends(verify_auth)
):
    return update_employee(employee_id, employee, (user.get("user") or user.get("username")))


# Patch Employee (partial update)
@router.patch("/employees/{employee_id}")
def patch_employee_route(
    employee_id: int,
    employee: EmployeeUpdate,
    user: dict = Depends(verify_auth)
):
    return patch_employee(employee_id, employee, (user.get("user") or user.get("username")))


# Delete Employee
@router.delete("/employees/{employee_id}")
def remove_employee(
    employee_id: int,
    user: dict = Depends(verify_auth)
):
    return delete_employee(employee_id, (user.get("user") or user.get("username")))