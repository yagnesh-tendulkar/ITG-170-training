from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from model import employee, Base
from schemas import employeecreate, employeeout
Base.metadata.create_all(bind=engine)
app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/employee", response_model=employeeout)
def create_employee(
    emp: employeecreate,
    db: Session = Depends(get_db)
):
    new_employee = employee(
        emp_id=emp.emp_id,
        name=emp.name,
        email=emp.email,
        phone=emp.phone
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee
@app.get("/employees", response_model=list[employeeout])
def get_employees(
    db: Session = Depends(get_db)
):
    return db.query(employee).all()
@app.get("/search")
def search_employee(
    emp_id: int = None,
    name: str = None,
    email: str = None,
    phone: str = None,
    db: Session = Depends(get_db)
):

    query = db.query(employee)

    if emp_id:
        result = query.filter(employee.emp_id == emp_id).first()

    elif name:
        result = query.filter(employee.name == name).first()

    elif email:
        result = query.filter(employee.email == email).first()

    elif phone:
        result = query.filter(employee.phone == phone).first()

    else:
        return {"message": "Provide emp_id, name, email or phone"}

    if not result:
        return {"message": "Employee Not Found"}

    return result