from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String

from app.database.connection import Base


class Employee(Base):
    """SQLAlchemy ORM model representing an employee record."""

    __tablename__ = "employees"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        nullable=False,
    )
    """Primary key for the employee record."""

    first_name = Column(
        String(100),
        nullable=False,
    )
    """Employee first name; required field."""

    last_name = Column(
        String(100),
        nullable=False,
    )
    """Employee last name; required field."""

    email = Column(
        String(255),
        nullable=False,
        unique=True,
        index=True,
    )
    """Unique email address used to identify an employee."""

    phone = Column(
        String(32),
        nullable=True,
    )
    """Optional contact phone number for the employee."""

    designation = Column(
        String(128),
        nullable=True,
    )
    """Job title or position held by the employee."""

    salary = Column(
        Float,
        nullable=True,
    )
    """Optional salary amount for the employee."""

    department = Column(
        String(128),
        nullable=True,
    )
    """Department or team associated with the employee."""

    is_active = Column(
        Boolean,
        nullable=False,
        default=True,
    )
    """Indicator whether the employee is currently active."""

    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
    )
    """Creation timestamp for the employee record."""

    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )
    """Last update timestamp for the employee record."""

    def __repr__(self) -> str:
        return (
            f"<Employee(id={self.id!r}, email={self.email!r}, "
            f"first_name={self.first_name!r}, last_name={self.last_name!r})>"
        )
