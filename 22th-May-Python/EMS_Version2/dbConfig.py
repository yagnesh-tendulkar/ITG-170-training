from sqlalchemy import create_engine
from fastapi import FastAPI
import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

load_dotenv()

engine = create_engine(f'mysql+pymysql://root:{os.getenv("DB_PASSWORD")}@localhost:3306/ITG_170', echo=True, future=True)
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.rollback()
    finally:
        db.close()