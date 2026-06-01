from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.employee import Employee
from app.schemas.employee_schema import (
    EmployeeCreate,
    EmployeeResponse,
    EmployeeUpdate,
)

router = APIRouter(prefix="/employees", tags=["employees"])


@router.post(
    "/",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db),
) -> EmployeeResponse:
    """
    Create a new employee record.

    Args:
        employee: Employee creation schema with required fields.
        db: SQLAlchemy session dependency for database operations.

    Returns:
        EmployeeResponse: The created employee record with id and timestamps.

    Raises:
        HTTPException: If the email already exists in the database.
    """
    existing_employee = db.query(Employee).filter(
        Employee.email == employee.email
    ).first()
    if existing_employee:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered.",
        )

    new_employee = Employee(**employee.model_dump())
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee


@router.get(
    "/",
    response_model=list[EmployeeResponse],
    status_code=status.HTTP_200_OK,
)
def get_all_employees(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> list[EmployeeResponse]:
    """
    Retrieve all employees with optional pagination.

    Args:
        skip: Number of records to skip (default 0).
        limit: Maximum number of records to return (default 100).
        db: SQLAlchemy session dependency for database operations.

    Returns:
        list[EmployeeResponse]: List of employee records.
    """
    employees = db.query(Employee).offset(skip).limit(limit).all()
    return employees


@router.get(
    "/{employee_id}",
    response_model=EmployeeResponse,
    status_code=status.HTTP_200_OK,
)
def get_employee_by_id(
    employee_id: int,
    db: Session = Depends(get_db),
) -> EmployeeResponse:
    """
    Retrieve a single employee by ID.

    Args:
        employee_id: The ID of the employee to retrieve.
        db: SQLAlchemy session dependency for database operations.

    Returns:
        EmployeeResponse: The employee record if found.

    Raises:
        HTTPException: 404 if the employee does not exist.
    """
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID {employee_id} not found.",
        )
    return employee


@router.put(
    "/{employee_id}",
    response_model=EmployeeResponse,
    status_code=status.HTTP_200_OK,
)
def update_employee(
    employee_id: int,
    employee_update: EmployeeUpdate,
    db: Session = Depends(get_db),
) -> EmployeeResponse:
    """
    Update an existing employee record.

    Args:
        employee_id: The ID of the employee to update.
        employee_update: Employee update schema with fields to modify.
        db: SQLAlchemy session dependency for database operations.

    Returns:
        EmployeeResponse: The updated employee record.

    Raises:
        HTTPException: 404 if the employee does not exist.
        HTTPException: 400 if the email is already in use by another employee.
    """
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID {employee_id} not found.",
        )

    if employee_update.email:
        existing_email = db.query(Employee).filter(
            Employee.email == employee_update.email,
            Employee.id != employee_id,
        ).first()
        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered by another employee.",
            )

    update_data = employee_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(employee, key, value)

    db.commit()
    db.refresh(employee)
    return employee


@router.delete(
    "/{employee_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db),
) -> None:
    """
    Delete an employee record by ID.

    Args:
        employee_id: The ID of the employee to delete.
        db: SQLAlchemy session dependency for database operations.

    Raises:
        HTTPException: 404 if the employee does not exist.
    """
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID {employee_id} not found.",
        )

    db.delete(employee)
    db.commit()
