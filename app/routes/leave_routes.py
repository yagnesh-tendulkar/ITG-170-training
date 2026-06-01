from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.leave import Leave
from app.schemas.leave_schema import (
    LeaveCreate,
    LeaveResponse,
    LeaveUpdate,
)

router = APIRouter(prefix="/leaves", tags=["leaves"])


@router.post(
    "/",
    response_model=LeaveResponse,
    status_code=status.HTTP_201_CREATED,
)
def apply_leave(
    leave: LeaveCreate,
    db: Session = Depends(get_db),
) -> LeaveResponse:
    """
    Apply for leave by creating a new leave request.

    Args:
        leave: Leave creation schema with employee and date details.
        db: SQLAlchemy session dependency for database operations.

    Returns:
        LeaveResponse: The created leave request with id and timestamps.

    Raises:
        HTTPException: If the leave dates are invalid.
    """
    new_leave = Leave(**leave.model_dump())
    db.add(new_leave)
    db.commit()
    db.refresh(new_leave)
    return new_leave


@router.get(
    "/",
    response_model=list[LeaveResponse],
    status_code=status.HTTP_200_OK,
)
def get_all_leaves(
    skip: int = 0,
    limit: int = 100,
    status_filter: str = None,
    leave_type: str = None,
    employee_id: int = None,
    sort_by: str = "start_date",
    db: Session = Depends(get_db),
) -> list[LeaveResponse]:
    """
    Retrieve all leave requests with optional pagination and filtering.

    Args:
        skip: Number of records to skip for pagination (default 0).
        limit: Maximum number of records to return (default 100).
        status_filter: Optional filter by leave status.
        leave_type: Optional filter by leave type.
        employee_id: Optional filter by employee ID.
        sort_by: Field to sort by (default "start_date").
        db: SQLAlchemy session dependency for database operations.

    Returns:
        list[LeaveResponse]: List of leave requests matching filters.
    """
    query = db.query(Leave)

    if status_filter:
        query = query.filter(Leave.status == status_filter)

    if leave_type:
        query = query.filter(Leave.leave_type == leave_type)

    if employee_id:
        query = query.filter(Leave.employee_id == employee_id)

    if sort_by == "start_date":
        query = query.order_by(Leave.start_date.desc())
    elif sort_by == "employee_id":
        query = query.order_by(Leave.employee_id)

    leaves = query.offset(skip).limit(limit).all()
    return leaves


@router.get(
    "/{leave_id}",
    response_model=LeaveResponse,
    status_code=status.HTTP_200_OK,
)
def get_leave_by_id(
    leave_id: int,
    db: Session = Depends(get_db),
) -> LeaveResponse:
    """
    Retrieve a single leave request by ID.

    Args:
        leave_id: The ID of the leave request to retrieve.
        db: SQLAlchemy session dependency for database operations.

    Returns:
        LeaveResponse: The leave request if found.

    Raises:
        HTTPException: 404 if the leave request does not exist.
    """
    leave = db.query(Leave).filter(Leave.id == leave_id).first()
    if not leave:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Leave request with ID {leave_id} not found.",
        )
    return leave


@router.get(
    "/employee/{employee_id}",
    response_model=list[LeaveResponse],
    status_code=status.HTTP_200_OK,
)
def get_leaves_by_employee(
    employee_id: int,
    skip: int = 0,
    limit: int = 100,
    status_filter: str = None,
    db: Session = Depends(get_db),
) -> list[LeaveResponse]:
    """
    Retrieve all leave requests for a specific employee.

    Args:
        employee_id: The ID of the employee to retrieve leave requests for.
        skip: Number of records to skip for pagination (default 0).
        limit: Maximum number of records to return (default 100).
        status_filter: Optional filter by leave status.
        db: SQLAlchemy session dependency for database operations.

    Returns:
        list[LeaveResponse]: List of leave requests for the employee.
    """
    query = db.query(Leave).filter(Leave.employee_id == employee_id)

    if status_filter:
        query = query.filter(Leave.status == status_filter)

    leaves = query.order_by(Leave.start_date.desc()).offset(skip).limit(limit).all()
    return leaves


@router.put(
    "/{leave_id}",
    response_model=LeaveResponse,
    status_code=status.HTTP_200_OK,
)
def update_leave(
    leave_id: int,
    leave_update: LeaveUpdate,
    db: Session = Depends(get_db),
) -> LeaveResponse:
    """
    Update an existing leave request.

    Args:
        leave_id: The ID of the leave request to update.
        leave_update: Leave update schema with fields to modify.
        db: SQLAlchemy session dependency for database operations.

    Returns:
        LeaveResponse: The updated leave request.

    Raises:
        HTTPException: 404 if the leave request does not exist.
    """
    leave = db.query(Leave).filter(Leave.id == leave_id).first()
    if not leave:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Leave request with ID {leave_id} not found.",
        )

    update_data = leave_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(leave, key, value)

    db.commit()
    db.refresh(leave)
    return leave


@router.patch(
    "/{leave_id}/approve",
    response_model=LeaveResponse,
    status_code=status.HTTP_200_OK,
)
def approve_leave(
    leave_id: int,
    approved_by: str,
    db: Session = Depends(get_db),
) -> LeaveResponse:
    """
    Approve a leave request by updating its status to Approved.

    Args:
        leave_id: The ID of the leave request to approve.
        approved_by: Name of the manager approving the leave.
        db: SQLAlchemy session dependency for database operations.

    Returns:
        LeaveResponse: The updated leave request with Approved status.

    Raises:
        HTTPException: 404 if the leave request does not exist.
    """
    leave = db.query(Leave).filter(Leave.id == leave_id).first()
    if not leave:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Leave request with ID {leave_id} not found.",
        )

    leave.status = "Approved"
    leave.approved_by = approved_by
    db.commit()
    db.refresh(leave)
    return leave


@router.patch(
    "/{leave_id}/reject",
    response_model=LeaveResponse,
    status_code=status.HTTP_200_OK,
)
def reject_leave(
    leave_id: int,
    db: Session = Depends(get_db),
) -> LeaveResponse:
    """
    Reject a leave request by updating its status to Rejected.

    Args:
        leave_id: The ID of the leave request to reject.
        db: SQLAlchemy session dependency for database operations.

    Returns:
        LeaveResponse: The updated leave request with Rejected status.

    Raises:
        HTTPException: 404 if the leave request does not exist.
    """
    leave = db.query(Leave).filter(Leave.id == leave_id).first()
    if not leave:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Leave request with ID {leave_id} not found.",
        )

    leave.status = "Rejected"
    db.commit()
    db.refresh(leave)
    return leave


@router.delete(
    "/{leave_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_leave(
    leave_id: int,
    db: Session = Depends(get_db),
) -> None:
    """
    Delete a leave request by ID.

    Args:
        leave_id: The ID of the leave request to delete.
        db: SQLAlchemy session dependency for database operations.

    Raises:
        HTTPException: 404 if the leave request does not exist.
    """
    leave = db.query(Leave).filter(Leave.id == leave_id).first()
    if not leave:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Leave request with ID {leave_id} not found.",
        )

    db.delete(leave)
    db.commit()
