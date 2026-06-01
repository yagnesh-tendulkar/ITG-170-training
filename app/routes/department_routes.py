from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.department import Department
from app.schemas.department_schema import (
    DepartmentCreate,
    DepartmentResponse,
    DepartmentUpdate,
)

router = APIRouter(prefix="/departments", tags=["departments"])


@router.post(
    "/",
    response_model=DepartmentResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_department(
    department: DepartmentCreate,
    db: Session = Depends(get_db),
) -> DepartmentResponse:
    """
    Create a new department.

    Args:
        department: Department creation schema with required fields.
        db: SQLAlchemy session dependency for database operations.

    Returns:
        DepartmentResponse: The created department record with id and timestamps.

    Raises:
        HTTPException: If the department name already exists.
    """
    existing_department = db.query(Department).filter(
        Department.name == department.name
    ).first()
    if existing_department:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Department name already exists.",
        )

    new_department = Department(**department.model_dump())
    db.add(new_department)
    db.commit()
    db.refresh(new_department)
    return new_department


@router.get(
    "/",
    response_model=list[DepartmentResponse],
    status_code=status.HTTP_200_OK,
)
def get_all_departments(
    skip: int = 0,
    limit: int = 100,
    search: str = None,
    is_active: bool = None,
    db: Session = Depends(get_db),
) -> list[DepartmentResponse]:
    """
    Retrieve all departments with optional pagination, search, and filtering.

    Args:
        skip: Number of records to skip for pagination (default 0).
        limit: Maximum number of records to return (default 100).
        search: Optional search string to filter departments by name.
        is_active: Optional filter by active status (True/False).
        db: SQLAlchemy session dependency for database operations.

    Returns:
        list[DepartmentResponse]: List of department records matching filters.
    """
    query = db.query(Department)

    if search:
        query = query.filter(Department.name.ilike(f"%{search}%"))

    if is_active is not None:
        query = query.filter(Department.is_active == is_active)

    departments = query.offset(skip).limit(limit).all()
    return departments


@router.get(
    "/{department_id}",
    response_model=DepartmentResponse,
    status_code=status.HTTP_200_OK,
)
def get_department_by_id(
    department_id: int,
    db: Session = Depends(get_db),
) -> DepartmentResponse:
    """
    Retrieve a single department by ID.

    Args:
        department_id: The ID of the department to retrieve.
        db: SQLAlchemy session dependency for database operations.

    Returns:
        DepartmentResponse: The department record if found.

    Raises:
        HTTPException: 404 if the department does not exist.
    """
    department = db.query(Department).filter(
        Department.id == department_id
    ).first()
    if not department:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Department with ID {department_id} not found.",
        )
    return department


@router.put(
    "/{department_id}",
    response_model=DepartmentResponse,
    status_code=status.HTTP_200_OK,
)
def update_department(
    department_id: int,
    department_update: DepartmentUpdate,
    db: Session = Depends(get_db),
) -> DepartmentResponse:
    """
    Update an existing department.

    Args:
        department_id: The ID of the department to update.
        department_update: Department update schema with fields to modify.
        db: SQLAlchemy session dependency for database operations.

    Returns:
        DepartmentResponse: The updated department record.

    Raises:
        HTTPException: 404 if the department does not exist.
        HTTPException: 400 if the name is already in use by another department.
    """
    department = db.query(Department).filter(
        Department.id == department_id
    ).first()
    if not department:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Department with ID {department_id} not found.",
        )

    if department_update.name:
        existing_name = db.query(Department).filter(
            Department.name == department_update.name,
            Department.id != department_id,
        ).first()
        if existing_name:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Department name already exists.",
            )

    update_data = department_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(department, key, value)

    db.commit()
    db.refresh(department)
    return department


@router.delete(
    "/{department_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_department(
    department_id: int,
    db: Session = Depends(get_db),
) -> None:
    """
    Delete a department by ID.

    Args:
        department_id: The ID of the department to delete.
        db: SQLAlchemy session dependency for database operations.

    Raises:
        HTTPException: 404 if the department does not exist.
    """
    department = db.query(Department).filter(
        Department.id == department_id
    ).first()
    if not department:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Department with ID {department_id} not found.",
        )

    db.delete(department)
    db.commit()
