from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String

from app.database.connection import Base


class Department(Base):
    """SQLAlchemy ORM model representing a department within the HR system."""

    __tablename__ = "departments"

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
    )
    """Primary key for the department record."""

    name = Column(
        String(128),
        nullable=False,
        unique=True,
        index=True,
    )
    """Unique name of the department; required for each department."""

    description = Column(
        String(512),
        nullable=True,
    )
    """Optional description of department responsibilities."""

    location = Column(
        String(256),
        nullable=True,
    )
    """Optional office or geographic location for the department."""

    manager_name = Column(
        String(128),
        nullable=True,
    )
    """Optional name of the department manager."""

    budget = Column(
        Float,
        nullable=False,
        default=0.0,
    )
    """Department budget with a default value for financial tracking."""

    is_active = Column(
        Boolean,
        nullable=False,
        default=True,
    )
    """Flag indicating whether the department is active."""

    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
    )
    """Timestamp when the department record was created."""

    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )
    """Timestamp updated automatically when the record changes."""

    def __repr__(self) -> str:
        return (
            f"<Department(id={self.id!r}, name={self.name!r}, "
            f"is_active={self.is_active!r})>"
        )
