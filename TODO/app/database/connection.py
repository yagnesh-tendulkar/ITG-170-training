from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

# Fallback to local SQLite if environment variable is missing
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todo_production.db")

# 'check_same_thread' is only needed for SQLite to support multi-threading
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Context-aware Dependency Injection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()