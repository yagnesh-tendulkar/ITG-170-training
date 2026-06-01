from sqlalchemy import create_engine
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker
)

from core.config import settings


# Database URL
DATABASE_URL = settings.DATABASE_URL


# Database Engine
engine = create_engine(
    DATABASE_URL,
    echo=True
)


# Session Factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base Class For Models
Base = declarative_base()


# Dependency Injection
def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()