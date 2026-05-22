from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

app = FastAPI()

# =========================
# DATABASE CONNECTION
# =========================
DATABASE_URL = "mysql+pymysql://root:M1racle%40123@localhost:3306/fastapi_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# =========================
# DATABASE MODEL
# =========================
class EmployeeDB(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    department = Column(String(100))
    salary = Column(Float)

Base.metadata.create_all(bind=engine)

# =========================
# PYDANTIC SCHEMA
# =========================
class Employee(BaseModel):
    id: int
    name: str
    department: str
    salary: float

# =========================
# HOME ROUTE
# =========================
@app.get("/")
def home():
    return {"message": "FastAPI with MySQL is running"}

# =========================
# GET ALL EMPLOYEES
# =========================
@app.get("/employees", response_model=List[Employee])
def get_employees():
    db = SessionLocal()
    employees = db.query(EmployeeDB).all()
    db.close()
    return employees

# =========================
# POST EMPLOYEE
# =========================
@app.post("/employees")
def add_employee(employee: Employee):
    db = SessionLocal()
    db_employee = EmployeeDB(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    db.close()

    return {"message": "Employee added", "employee": employee}

# =========================
# PUT EMPLOYEE
# =========================
@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, updated_employee: Employee):
    db = SessionLocal()

    emp = db.query(EmployeeDB).filter(EmployeeDB.id == employee_id).first()

    if not emp:
        db.close()
        raise HTTPException(status_code=404, detail="Employee not found")

    emp.name = updated_employee.name
    emp.department = updated_employee.department
    emp.salary = updated_employee.salary

    db.commit()
    db.close()

    return {"message": "Employee updated"}

# =========================
# DELETE EMPLOYEE
# =========================
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    db = SessionLocal()

    emp = db.query(EmployeeDB).filter(EmployeeDB.id == employee_id).first()

    if not emp:
        db.close()
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(emp)
    db.commit()
    db.close()

    return {"message": "Employee deleted"}