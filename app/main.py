from fastapi import FastAPI, HTTPException
from typing import List

from app.database import engine, SessionLocal
from app.models import Base, EmployeeDB, RoleDB, StatusDB
from app.schemas import Employee, Role, Status

# =========================
# CREATE TABLES
# =========================
Base.metadata.create_all(bind=engine)

# =========================
# FASTAPI APP
# =========================
app = FastAPI()


# =========================
# HOME ROUTE
# =========================
@app.get("/")
def home():

    return {
        "message": "HR Dashboard API Running"
    }


# =========================
# CREATE ROLE
# =========================
@app.post("/roles")
def create_role(role: Role):

    db = SessionLocal()

    db_role = RoleDB(
        role_name=role.role_name
    )

    db.add(db_role)

    db.commit()

    db.refresh(db_role)

    db.close()

    return {
        "message": "Role Created Successfully"
    }


# =========================
# CREATE STATUS
# =========================
@app.post("/status")
def create_status(status: Status):

    db = SessionLocal()

    db_status = StatusDB(
        status_code=status.status_code,
        status_name=status.status_name
    )

    db.add(db_status)

    db.commit()

    db.refresh(db_status)

    db.close()

    return {
        "message": "Status Created Successfully"
    }


# =========================
# CREATE EMPLOYEE
# =========================
@app.post("/employees")
def create_employee(employee: Employee):

    db = SessionLocal()

    db_employee = EmployeeDB(

        first_name=employee.first_name,

        last_name=employee.last_name,

        corporate_mail=employee.corporate_mail,

        personal_email=employee.personal_email,

        phone_number=employee.phone_number,

        department=employee.department,

        joining_date=employee.joining_date,

        salary=employee.salary,

        address=employee.address,

        role_id=employee.role_id,

        status_id=employee.status_id
    )

    db.add(db_employee)

    db.commit()

    db.refresh(db_employee)

    db.close()

    return {
        "message": "Employee Created Successfully"
    }


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
# UPDATE EMPLOYEE
# =========================
@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, updated_employee: Employee):

    db = SessionLocal()

    employee = db.query(EmployeeDB).filter(
        EmployeeDB.id == employee_id
    ).first()

    if not employee:

        db.close()

        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    employee.first_name = updated_employee.first_name
    employee.last_name = updated_employee.last_name
    employee.corporate_mail = updated_employee.corporate_mail
    employee.personal_email = updated_employee.personal_email
    employee.phone_number = updated_employee.phone_number
    employee.department = updated_employee.department
    employee.joining_date = updated_employee.joining_date
    employee.salary = updated_employee.salary
    employee.address = updated_employee.address
    employee.role_id = updated_employee.role_id
    employee.status_id = updated_employee.status_id

    db.commit()

    db.close()

    return {
        "message": "Employee Updated Successfully"
    }


# =========================
# DELETE EMPLOYEE
# =========================
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):

    db = SessionLocal()

    employee = db.query(EmployeeDB).filter(
        EmployeeDB.id == employee_id
    ).first()

    if not employee:

        db.close()

        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )

    db.delete(employee)

    db.commit()

    db.close()

    return {
        "message": "Employee Deleted Successfully"
    }