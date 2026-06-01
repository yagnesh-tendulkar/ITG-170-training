from datetime import date
from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.leave import Leave
from app.schemas.leave_schema import LeaveCreate, LeaveUpdate


class LeaveService:
    """Service layer for leave business logic and database operations."""

    def __init__(self, db: Session):
        """
        Initialize the LeaveService with a database session.

        Args:
            db: SQLAlchemy session for database operations.
        """
        self.db = db

    def create_leave(self, leave_data: LeaveCreate) -> Leave:
        """
        Create a new leave request.

        Args:
            leave_data: LeaveCreate schema with leave details.

        Returns:
            Leave: The created leave object.

        Raises:
            ValueError: If dates are invalid or overlapping approved leaves exist.
        """
        if leave_data.start_date > leave_data.end_date:
            raise ValueError("start_date must not be after end_date.")

        existing_approved_leave = self.db.query(Leave).filter(
            Leave.employee_id == leave_data.employee_id,
            Leave.status == "Approved",
            Leave.start_date <= leave_data.end_date,
            Leave.end_date >= leave_data.start_date,
        ).first()
        if existing_approved_leave:
            raise ValueError(
                "Employee has overlapping approved leave during this period."
            )

        new_leave = Leave(**leave_data.model_dump())
        self.db.add(new_leave)
        self.db.commit()
        self.db.refresh(new_leave)
        return new_leave

    def get_all_leaves(
        self,
        skip: int = 0,
        limit: int = 100,
        status_filter: Optional[str] = None,
        leave_type: Optional[str] = None,
        employee_id: Optional[int] = None,
        sort_by: str = "start_date",
    ) -> List[Leave]:
        """
        Retrieve all leave requests with optional filtering and pagination.

        Args:
            skip: Number of records to skip (default 0).
            limit: Maximum number of records to return (default 100).
            status_filter: Optional filter by leave status.
            leave_type: Optional filter by leave type.
            employee_id: Optional filter by employee ID.
            sort_by: Field to sort by (default "start_date").

        Returns:
            List[Leave]: List of leave requests matching filters.
        """
        query = self.db.query(Leave)

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

    def get_leave_by_id(self, leave_id: int) -> Optional[Leave]:
        """
        Retrieve a single leave request by ID.

        Args:
            leave_id: The ID of the leave request to retrieve.

        Returns:
            Optional[Leave]: The leave object if found, None otherwise.
        """
        leave = self.db.query(Leave).filter(Leave.id == leave_id).first()
        return leave

    def get_leaves_by_employee(
        self,
        employee_id: int,
        skip: int = 0,
        limit: int = 100,
        status_filter: Optional[str] = None,
    ) -> List[Leave]:
        """
        Retrieve all leave requests for a specific employee.

        Args:
            employee_id: The ID of the employee to retrieve leave requests for.
            skip: Number of records to skip (default 0).
            limit: Maximum number of records to return (default 100).
            status_filter: Optional filter by leave status.

        Returns:
            List[Leave]: List of leave requests for the employee.
        """
        query = self.db.query(Leave).filter(Leave.employee_id == employee_id)

        if status_filter:
            query = query.filter(Leave.status == status_filter)

        leaves = query.order_by(Leave.start_date.desc()).offset(skip).limit(limit).all()
        return leaves

    def get_pending_leaves(
        self,
        skip: int = 0,
        limit: int = 100,
    ) -> List[Leave]:
        """
        Retrieve all pending leave requests awaiting approval.

        Args:
            skip: Number of records to skip (default 0).
            limit: Maximum number of records to return (default 100).

        Returns:
            List[Leave]: List of pending leave requests.
        """
        leaves = self.db.query(Leave).filter(
            Leave.status == "Pending"
        ).order_by(Leave.start_date).offset(skip).limit(limit).all()
        return leaves

    def update_leave(
        self,
        leave_id: int,
        leave_update: LeaveUpdate,
    ) -> Optional[Leave]:
        """
        Update an existing leave request.

        Args:
            leave_id: The ID of the leave request to update.
            leave_update: LeaveUpdate schema with fields to modify.

        Returns:
            Optional[Leave]: The updated leave object if found, None otherwise.

        Raises:
            ValueError: If dates are invalid.
        """
        leave = self.db.query(Leave).filter(Leave.id == leave_id).first()
        if not leave:
            return None

        if (
            leave_update.start_date
            and leave_update.end_date
            and leave_update.start_date > leave_update.end_date
        ):
            raise ValueError("start_date must not be after end_date.")

        update_data = leave_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(leave, key, value)

        self.db.commit()
        self.db.refresh(leave)
        return leave

    def approve_leave(self, leave_id: int, approved_by: str) -> Optional[Leave]:
        """
        Approve a leave request.

        Args:
            leave_id: The ID of the leave request to approve.
            approved_by: Name of the manager approving the leave.

        Returns:
            Optional[Leave]: The updated leave object with Approved status if found, None otherwise.
        """
        leave = self.db.query(Leave).filter(Leave.id == leave_id).first()
        if not leave:
            return None

        leave.status = "Approved"
        leave.approved_by = approved_by
        self.db.commit()
        self.db.refresh(leave)
        return leave

    def reject_leave(self, leave_id: int) -> Optional[Leave]:
        """
        Reject a leave request.

        Args:
            leave_id: The ID of the leave request to reject.

        Returns:
            Optional[Leave]: The updated leave object with Rejected status if found, None otherwise.
        """
        leave = self.db.query(Leave).filter(Leave.id == leave_id).first()
        if not leave:
            return None

        leave.status = "Rejected"
        self.db.commit()
        self.db.refresh(leave)
        return leave

    def cancel_leave(self, leave_id: int) -> Optional[Leave]:
        """
        Cancel an existing leave request.

        Args:
            leave_id: The ID of the leave request to cancel.

        Returns:
            Optional[Leave]: The updated leave object with Cancelled status if found, None otherwise.
        """
        leave = self.db.query(Leave).filter(Leave.id == leave_id).first()
        if not leave:
            return None

        leave.status = "Cancelled"
        self.db.commit()
        self.db.refresh(leave)
        return leave

    def delete_leave(self, leave_id: int) -> bool:
        """
        Delete a leave request by ID.

        Args:
            leave_id: The ID of the leave request to delete.

        Returns:
            bool: True if deletion was successful, False if leave not found.
        """
        leave = self.db.query(Leave).filter(Leave.id == leave_id).first()
        if not leave:
            return False

        self.db.delete(leave)
        self.db.commit()
        return True

    def get_approved_leaves_for_period(
        self,
        employee_id: int,
        start_date: date,
        end_date: date,
    ) -> List[Leave]:
        """
        Retrieve approved leave records for an employee within a date range.

        Args:
            employee_id: The ID of the employee.
            start_date: The start date of the period.
            end_date: The end date of the period.

        Returns:
            List[Leave]: List of approved leave records within the date range.
        """
        leaves = self.db.query(Leave).filter(
            Leave.employee_id == employee_id,
            Leave.status == "Approved",
            Leave.start_date >= start_date,
            Leave.end_date <= end_date,
        ).order_by(Leave.start_date).all()
        return leaves

    def get_leave_count_by_type(self, leave_type: str) -> int:
        """
        Get the count of leave requests of a specific type.

        Args:
            leave_type: The leave type to count.

        Returns:
            int: Number of leave requests of the specified type.
        """
        count = self.db.query(Leave).filter(Leave.leave_type == leave_type).count()
        return count

    def get_employee_approved_leave_days(self, employee_id: int) -> float:
        """
        Get the total number of approved leave days for an employee.

        Args:
            employee_id: The ID of the employee.

        Returns:
            float: Total approved leave days.
        """
        result = self.db.query(Leave).filter(
            Leave.employee_id == employee_id,
            Leave.status == "Approved",
        ).all()
        total_days = sum(leave.total_days for leave in result)
        return total_days

    def count_leaves_by_status(self, status: str) -> int:
        """
        Get the count of leave requests with a specific status.

        Args:
            status: The leave status to count.

        Returns:
            int: Number of leave requests with the specified status.
        """
        count = self.db.query(Leave).filter(Leave.status == status).count()
        return count

    def get_employee_leave_count(self, employee_id: int) -> int:
        """
        Get the count of leave requests for a specific employee.

        Args:
            employee_id: The ID of the employee.

        Returns:
            int: Number of leave requests for the employee.
        """
        count = self.db.query(Leave).filter(
            Leave.employee_id == employee_id
        ).count()
        return count
