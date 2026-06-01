from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String

from app.database.connection import Base


class User(Base):
    """SQLAlchemy ORM model representing an application user."""

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
    )
    """Primary key for the user record."""

    username = Column(
        String(128),
        nullable=False,
        unique=True,
        index=True,
    )
    """Unique username for logging in and identifying the user."""

    email = Column(
        String(255),
        nullable=False,
        unique=True,
        index=True,
    )
    """Unique email address used for account communication."""

    hashed_password = Column(
        String(255),
        nullable=False,
    )
    """Hashed password for secure authentication."""

    role = Column(
        String(32),
        nullable=False,
        default="Employee",
    )
    """Role assigned to the user (Admin, HR, Manager, Employee)."""

    is_active = Column(
        Boolean,
        nullable=False,
        default=True,
    )
    """Flag indicating if the user account is currently active."""

    is_verified = Column(
        Boolean,
        nullable=False,
        default=False,
    )
    """Flag indicating whether the user's email or account is verified."""

    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
    )
    """Timestamp when the user record was created."""

    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )
    """Timestamp updated automatically when the user record changes."""

    def __repr__(self) -> str:
        return (
            f"<User(id={self.id!r}, username={self.username!r}, "
            f"email={self.email!r}, role={self.role!r})>"
        )
