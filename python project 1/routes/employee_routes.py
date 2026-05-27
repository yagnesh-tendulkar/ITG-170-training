from fastapi import APIRouter, HTTPException
from app.schemas.employee_schema import EmployeeCreate, EmployeeResponse

router = APIRouter(
    prefix="/employee",
    tags=["Employee"]
)
employee_db = []
def generate_corporate_email(fname: str, lname: str) -> str:
    return f"{fname[0].lower()}{lname.lower()}@miraclesoft.com"
def generate_password(fname: str, lname: str, joining_date) -> str:
    return (
        fname[-2:].lower()
        + lname[:2].lower()
        + joining_date.strftime("%H%M%d")
    )


@router.post("/add", response_model=EmployeeResponse)
def add_employee(emp: EmployeeCreate):

    corporate_mail = generate_corporate_email(emp.fname, emp.lname)

    password = generate_password(emp.fname, emp.lname, emp.joining_date)

    new_emp = {
        "employee_id": len(employee_db) + 1,
        "fname": emp.fname,
        "lname": emp.lname,
        "personal_mail": emp.personal_mail,
        "corporate_mail": corporate_mail,
        "department": emp.department,
        "role_id": emp.role_id,
        "joining_date": emp.joining_date,
        "salary": emp.salary,
        "status_id": emp.status_id,
        "password": password
    }

    employee_db.append(new_emp)

    return new_emp


@router.get("/all")
def get_all_employees():
    return employee_db


@router.get("/{emp_id}")
def get_employee(emp_id: int):

    for emp in employee_db:
        if emp["employee_id"] == emp_id:
            return emp

    raise HTTPException(status_code=404, detail="Employee not found")