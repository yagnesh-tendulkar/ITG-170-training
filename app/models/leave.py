from datetime import datetime

from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Leave(Base):
    """SQLAlchemy ORM model representing an employee leave request."""

    __tablename__ = "leaves"

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
    )
    """Primary key for the leave record."""

    employee_id = Column(
        Integer,
        ForeignKey("employees.id"),
        nullable=False,
        index=True,
    )
    """Foreign key linking this leave request to an employee."""

    leave_type = Column(
        String(64),
        nullable=False,
        default="Sick Leave",
    )
    """Type of leave such as Sick, Casual, Earned, Maternity, or Unpaid."""

    start_date = Column(
        Date,
        nullable=False,
    )
    """First day of the leave period."""

    end_date = Column(
        Date,
        nullable=False,
    )
    """Last day of the leave period."""

    total_days = Column(
        Float,
        nullable=False,
        default=0.0,
    )
    """Total number of leave days requested."""

    reason = Column(
        String(512),
        nullable=True,
    )
    """Optional reason or notes for the leave request."""

    status = Column(
        String(32),
        nullable=False,
        default="Pending",
    )
    """Current approval status of the leave request."""

    approved_by = Column(
        String(128),
        nullable=True,
    )
    """Name of the manager or approver for the leave request."""

    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
    )
    """Timestamp when the leave record was created."""

    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )
    """Timestamp updated automatically when the leave record changes."""

    employee = relationship(
        "Employee",
        backref="leave_records",
    )
    """SQLAlchemy relationship linking a leave request to its employee."""

    def __repr__(self) -> str:
        return (
            f"<Leave(id={self.id!r}, employee_id={self.employee_id!r}, "
            f"leave_type={self.leave_type!r}, status={self.status!r})>"
        )
