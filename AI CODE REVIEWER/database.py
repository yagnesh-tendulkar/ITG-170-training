# ─────────────────────────────────────────────
# database.py
#
# LEARNING NOTE:
# This file sets up SQLAlchemy — the ORM (Object Relational Mapper) we use
# to talk to our SQLite database. Instead of writing raw SQL, we use Python
# classes and SQLAlchemy handles the SQL for us.
#
# Key concepts:
#   - engine: the connection to the database file
#   - SessionLocal: a factory that creates database sessions (think: a transaction)
#   - Base: all our models (tables) inherit from this
#   - get_db(): a FastAPI "dependency" — auto-injects a DB session into routes
# ─────────────────────────────────────────────

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./codereview.db")

# connect_args is needed only for SQLite — allows multiple threads to use it
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# SessionLocal is a class. Each time we call SessionLocal() we get a new session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# All our model classes will inherit from Base
Base = declarative_base()


def get_db():
    """
    FastAPI Dependency: yields a database session.

    Usage in a route:
        @app.get("/something")
        def my_route(db: Session = Depends(get_db)):
            ...

    The 'finally' block ensures the session is always closed,
    even if an error occurs — preventing resource leaks.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
