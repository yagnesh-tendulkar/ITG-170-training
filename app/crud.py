from sqlalchemy.orm import Session
from models import Employee, StatusEnum
from utils import generate_email, generate_password

def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Employee).offset(skip).limit(limit).all()

def get_employee(db: Session, emp_id: int):
    return db.query(Employee).filter(Employee.emp_id == emp_id).first()

def create_employee(db: Session, first_name: str, last_name: str, department: str):
    email = generate_email(first_name, last_name)
    emp = Employee(
        first_name=first_name,
        last_name=last_name,
        department=department,
        email=email,
        status=StatusEnum.p
    )
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return emp

def update_employee(db: Session, emp_id: int, first_name=None, last_name=None,
                   department=None, status=None):
    emp = get_employee(db, emp_id)
    if not emp:
        return None
    if first_name:
        emp.first_name = first_name
    if last_name:
        emp.last_name = last_name
    if department:
        emp.department = department
    if status:
        emp.status = StatusEnum(status)
    db.commit()
    db.refresh(emp)
    return emp

def delete_employee(db: Session, emp_id: int):
    emp = get_employee(db, emp_id)
    if emp:
        db.delete(emp)
        db.commit()
        return True
    return False

