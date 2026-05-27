from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
import uvicorn

# ---------------- DATABASE SETUP ----------------
DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/fastapi_db"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ---------------- MODEL ----------------
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
app = FastAPI(title="Employee CRUD API", version="1.0")

# ---------------- DB DEPENDENCY ----------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------- CREATE ----------------
@app.post(
    "/employees",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED
)
def create_employee(emp: EmployeeCreate, db: Session = Depends(get_db)):
    db_emp = Employee(**emp.dict())
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp


# ---------------- READ ALL ----------------
@app.get(
    "/employees",
    response_model=List[EmployeeResponse],
    status_code=status.HTTP_200_OK
)
def get_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()


# ---------------- READ BY ID ----------------
@app.get(
    "/employees/{emp_id}",
    response_model=EmployeeResponse,
    status_code=status.HTTP_200_OK
)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()

    if not emp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )

    return emp


# ---------------- UPDATE ----------------
@app.put(
    "/employees/{emp_id}",
    response_model=EmployeeResponse,
    status_code=status.HTTP_200_OK
)
def update_employee(emp_id: int, emp_update: EmployeeUpdate, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()

    if not emp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )

    for key, value in emp_update.dict(exclude_unset=True).items():
        setattr(emp, key, value)

    db.commit()
    db.refresh(emp)
    return emp


# ---------------- DELETE ----------------
@app.delete(
    "/employees/{emp_id}",
    status_code=status.HTTP_200_OK
)
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()

    if not emp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )

    db.delete(emp)
    db.commit()

    return {
        "status": "success",
        "message": "Employee deleted successfully"
    }


# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )