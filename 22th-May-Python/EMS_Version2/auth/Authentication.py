from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from model import Employee
from ..dbConfig import get_db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()
router= FastAPI(title="Employee Authentication System")
db= get_db()

class LoginCredentials(BaseModel):
    email: str
    password: str
@router.post('/login')
def login(login_data:LoginCredentials, db: Session = Depends(get_db)):
    email = login_data.email
    password = login_data.password
    user = db.query(Employee).filter(
        Employee.email == email,
        Employee.password == password
    ).first()
    return user
    if user is None:
        raise HTTPException(status_code=404, detail="Incorrect email or password")
