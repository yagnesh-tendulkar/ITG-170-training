from datetime import date

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.attendance import Attendance
from app.schemas.attendance_schema import (
    AttendanceCreate,
    AttendanceResponse,
    AttendanceUpdate,
)

router = APIRouter(prefix="/attendance", tags=["attendance"])


@router.post(
    "/",
    response_model=AttendanceResponse,
    status_code=status.HTTP_201_CREATED,
)
def mark_attendance(
    attendance: AttendanceCreate,
    db: Session = Depends(get_db),
) -> AttendanceResponse:
    """
    Mark attendance for an employee on a specific date.

    Args:
        attendance: Attendance creation schema with employee and date details.
        db: SQLAlchemy session dependency for database operations.

    Returns:
        AttendanceResponse: The created attendance record with id and timestamps.

    Raises:
        HTTPException: If attendance already exists for the employee on that date.
    """
    existing_attendance = db.query(Attendance).filter(
        Attendance.employee_id == attendance.employee_id,
        Attendance.attendance_date == attendance.attendance_date,
    ).first()
    if existing_attendance:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Attendance already marked for this employee on this date.",
        )

    new_attendance = Attendance(**attendance.model_dump())
    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)
    return new_attendance


@router.get(
    "/",
    response_model=list[AttendanceResponse],
    status_code=status.HTTP_200_OK,
)
def get_all_attendance(
    skip: int = 0,
    limit: int = 100,
    status_filter: str = None,
    employee_id: int = None,
    sort_by: str = "attendance_date",
    db: Session = Depends(get_db),
) -> list[AttendanceResponse]:
    """
    Retrieve all attendance records with optional pagination and filtering.

    Args:
        skip: Number of records to skip for pagination (default 0).
        limit: Maximum number of records to return (default 100).
        status_filter: Optional filter by attendance status.
        employee_id: Optional filter by employee ID.
        sort_by: Field to sort by (default "attendance_date").
        db: SQLAlchemy session dependency for database operations.

    Returns:
        list[AttendanceResponse]: List of attendance records matching filters.
    """
    query = db.query(Attendance)

    if employee_id:
        query = query.filter(Attendance.employee_id == employee_id)

    if status_filter:
        query = query.filter(Attendance.status == status_filter)

    if sort_by == "attendance_date":
        query = query.order_by(Attendance.attendance_date.desc())
    elif sort_by == "employee_id":
        query = query.order_by(Attendance.employee_id)

    attendance_records = query.offset(skip).limit(limit).all()
    return attendance_records


@router.get(
    "/{attendance_id}",
    response_model=AttendanceResponse,
    status_code=status.HTTP_200_OK,
)
def get_attendance_by_id(
    attendance_id: int,
    db: Session = Depends(get_db),
) -> AttendanceResponse:
    """
    Retrieve a single attendance record by ID.

    Args:
        attendance_id: The ID of the attendance record to retrieve.
        db: SQLAlchemy session dependency for database operations.

    Returns:
        AttendanceResponse: The attendance record if found.

    Raises:
        HTTPException: 404 if the attendance record does not exist.
    """
    attendance = db.query(Attendance).filter(
        Attendance.id == attendance_id
    ).first()
    if not attendance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Attendance record with ID {attendance_id} not found.",
        )
    return attendance


@router.get(
    "/employee/{employee_id}",
    response_model=list[AttendanceResponse],
    status_code=status.HTTP_200_OK,
)
def get_attendance_by_employee(
    employee_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> list[AttendanceResponse]:
    """
    Retrieve all attendance records for a specific employee.

    Args:
        employee_id: The ID of the employee to retrieve attendance for.
        skip: Number of records to skip for pagination (default 0).
        limit: Maximum number of records to return (default 100).
        db: SQLAlchemy session dependency for database operations.

    Returns:
        list[AttendanceResponse]: List of attendance records for the employee.
    """
    attendance_records = db.query(Attendance).filter(
        Attendance.employee_id == employee_id
    ).order_by(Attendance.attendance_date.desc()).offset(skip).limit(limit).all()
    return attendance_records


@router.get(
    "/date/{attendance_date}",
    response_model=list[AttendanceResponse],
    status_code=status.HTTP_200_OK,
)
def get_attendance_by_date(
    attendance_date: date,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> list[AttendanceResponse]:
    """
    Retrieve all attendance records for a specific date.

    Args:
        attendance_date: The date to retrieve attendance records for.
        skip: Number of records to skip for pagination (default 0).
        limit: Maximum number of records to return (default 100).
        db: SQLAlchemy session dependency for database operations.

    Returns:
        list[AttendanceResponse]: List of attendance records for the date.
    """
    attendance_records = db.query(Attendance).filter(
        Attendance.attendance_date == attendance_date
    ).offset(skip).limit(limit).all()
    return attendance_records


@router.put(
    "/{attendance_id}",
    response_model=AttendanceResponse,
    status_code=status.HTTP_200_OK,
)
def update_attendance(
    attendance_id: int,
    attendance_update: AttendanceUpdate,
    db: Session = Depends(get_db),
) -> AttendanceResponse:
    """
    Update an existing attendance record.

    Args:
        attendance_id: The ID of the attendance record to update.
        attendance_update: Attendance update schema with fields to modify.
        db: SQLAlchemy session dependency for database operations.

    Returns:
        AttendanceResponse: The updated attendance record.

    Raises:
        HTTPException: 404 if the attendance record does not exist.
    """
    attendance = db.query(Attendance).filter(
        Attendance.id == attendance_id
    ).first()
    if not attendance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Attendance record with ID {attendance_id} not found.",
        )

    update_data = attendance_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(attendance, key, value)

    db.commit()
    db.refresh(attendance)
    return attendance


@router.delete(
    "/{attendance_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_attendance(
    attendance_id: int,
    db: Session = Depends(get_db),
) -> None:
    """
    Delete an attendance record by ID.

    Args:
        attendance_id: The ID of the attendance record to delete.
        db: SQLAlchemy session dependency for database operations.

    Raises:
        HTTPException: 404 if the attendance record does not exist.
    """
    attendance = db.query(Attendance).filter(
        Attendance.id == attendance_id
    ).first()
    if not attendance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Attendance record with ID {attendance_id} not found.",
        )

    db.delete(attendance)
    db.commit()
