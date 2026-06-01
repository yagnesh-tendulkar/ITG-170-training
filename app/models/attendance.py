from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Time,
)
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Attendance(Base):
    """SQLAlchemy ORM model representing a single attendance entry."""

    __tablename__ = "attendance"

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
    )
    """Primary key for the attendance record."""

    employee_id = Column(
        Integer,
        ForeignKey("employees.id"),
        nullable=False,
        index=True,
    )
    """Foreign key linking this attendance entry to an Employee."""

    attendance_date = Column(
        Date,
        nullable=False,
    )
    """Date when the attendance event occurred."""

    check_in_time = Column(
        Time,
        nullable=True,
    )
    """Optional check-in time for the employee on the attendance date."""

    check_out_time = Column(
        Time,
        nullable=True,
    )
    """Optional check-out time for the employee on the attendance date."""

    status = Column(
        String(32),
        nullable=False,
        default="Present",
    )
    """Attendance status such as Present, Absent, Half Day, or Leave."""

    work_hours = Column(
        Float,
        nullable=False,
        default=0.0,
    )
    """Number of hours worked for this attendance entry."""

    remarks = Column(
        String(512),
        nullable=True,
    )
    """Optional notes or remarks about the attendance entry."""

    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
    )
    """Timestamp when the attendance record was created."""

    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )
    """Timestamp updated automatically when the record changes."""

    employee = relationship(
        "Employee",
        backref="attendance_records",
    )
    """Relationship linking this attendance entry to its employee."""

    def __repr__(self) -> str:
        return (
            f"<Attendance(id={self.id!r}, employee_id={self.employee_id!r}, "
            f"attendance_date={self.attendance_date!r}, status={self.status!r})>"
        )
