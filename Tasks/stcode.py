from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
import uvicorn

# ---------------- STATUS CODE CLASS ----------------
class StatusCodes:
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    CONFLICT = 409
    VALIDATION_ERROR = 422
    INTERNAL_ERROR = 500
    DATABASE_ERROR = 503

# ---------------- DATABASE SETUP ----------------
DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/fastapi_db"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ---------------- SINGLE TABLE ----------------
class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    department = Column(String(100), nullable=False)
    salary = Column(Integer, nullable=False)

Base.metadata.create_all(bind=engine)

# ---------------- SCHEMAS ----------------
class EmployeeCreate(BaseModel):
    name: str
    department: str
    salary: int

class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    department: Optional[str] = None
    salary: Optional[int] = None

class EmployeeResponse(BaseModel):
    id: int
    name: str
    department: str
    salary: int

    class Config:
        from_attributes = True

# ---------------- APP ----------------
app = FastAPI(title="Single Table CRUD with Status Class")

# ---------------- DB DEPENDENCY ----------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        raise HTTPException(
            status_code=StatusCodes.DATABASE_ERROR,
            detail="Database error occurred"
        )
    finally:
        db.close()

# ---------------- CREATE ----------------
@app.post("/employees", response_model=EmployeeResponse)
def create_employee(emp: EmployeeCreate, db: Session = Depends(get_db)):
    if not emp.name or not emp.department:
        raise HTTPException(
            status_code=StatusCodes.BAD_REQUEST,
            detail="Name and Department are required"
        )

    db_emp = Employee(**emp.dict())
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)

    return db_emp


# ---------------- READ ALL ----------------
@app.get("/employees", response_model=List[EmployeeResponse])
def get_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()


# ---------------- READ BY ID ----------------
@app.get("/employees/{emp_id}", response_model=EmployeeResponse)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()

    if not emp:
        raise HTTPException(
            status_code=StatusCodes.NOT_FOUND,
            detail="Employee not found"
        )

    return emp


# ---------------- UPDATE ----------------
@app.put("/employees/{emp_id}", response_model=EmployeeResponse)
def update_employee(emp_id: int, emp_update: EmployeeUpdate, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()

    if not emp:
        raise HTTPException(
            status_code=StatusCodes.NOT_FOUND,
            detail="Employee not found"
        )

    # validation example
    if emp_update.salary is not None and emp_update.salary < 0:
        raise HTTPException(
            status_code=StatusCodes.BAD_REQUEST,
            detail="Salary cannot be negative"
        )

    for key, value in emp_update.dict(exclude_unset=True).items():
        setattr(emp, key, value)

    db.commit()
    db.refresh(emp)

    return emp


# ---------------- DELETE ----------------
@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()

    if not emp:
        raise HTTPException(
            status_code=StatusCodes.NOT_FOUND,
            detail="Employee not found"
        )

    db.delete(emp)
    db.commit()

    return {
        "status_code": StatusCodes.OK,
        "message": "Employee deleted successfully"
    }


# ---------------- RUN ----------------
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )