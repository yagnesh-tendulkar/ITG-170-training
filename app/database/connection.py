from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./smartapi.db"
"""Database URL for the SQLite engine."""

# SQLite needs check_same_thread=False when using SQLAlchemy with FastAPI
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    future=True,
)
"""SQLAlchemy engine bound to the SQLite database."""

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=Session,
)
"""Factory for SQLAlchemy session objects used by request-scoped dependencies."""

Base = declarative_base()
"""Base class for SQLAlchemy declarative models."""


def get_db() -> Generator[Session, None, None]:
    """Yield a database session for a single request and ensure it is closed."""
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
