from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Base class for models
Base = declarative_base()
DB_USER = "root"
DB_PASSWORD = "M1racle@123"  # your password
DB_HOST = "localhost"
DB_NAME = "ITG_170"

password = quote_plus(DB_PASSWORD)
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{password}@{DB_HOST}/{DB_NAME}"


# Assuming you already have DATABASE_URL defined
engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()