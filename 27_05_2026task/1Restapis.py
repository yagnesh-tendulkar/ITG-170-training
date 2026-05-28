from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, EmailStr
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
import mysql.connector
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(
    SessionMiddleware,
    secret_key="mysecretkey")
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="M1racle@123",
    database="companydb"
)
cursor = connection.cursor(dictionary=True)
class Employee(BaseModel):
    id: int
    name: str = Field(..., min_length=3)
    age: int = Field(..., gt=20, lt=60)
    email: EmailStr
    department: str
@app.get("/")
def home():
    return {
        "message": "Employee API Running Successfully"
    }
@app.post("/employees", status_code=status.HTTP_201_CREATED)
def create_employee(employee: Employee, request: Request):
    query = """
    INSERT INTO employees(id, name, age, email, department)
    VALUES(%s, %s, %s, %s, %s)
    """
    values = (
        employee.id,
        employee.name,
        employee.age,
        employee.email,
        employee.department
    )
    cursor.execute(query, values)
    connection.commit()
    request.session["employee_name"] = employee.name
    return {
        "message": "Employee Added Successfully",
        "employee": employee
    }
@app.get("/employees")
def get_employees(request: Request):
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    session_employee = request.session.get(
        "employee_name",
        "No Session Data"
    )
    return {
        "last_added_employee": session_employee,
        "total_employees": len(employees),
        "employees": employees
    }
@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, updated_employee: Employee):
    check_query = "SELECT * FROM employees WHERE id = %s"
    cursor.execute(check_query, (employee_id,))
    existing_employee = cursor.fetchone()
    if not existing_employee:
        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )
    update_query = """
    UPDATE employees
    SET name=%s, age=%s, email=%s, department=%s
    WHERE id=%s
    """
    values = (
        updated_employee.name,
        updated_employee.age,
        updated_employee.email,
        updated_employee.department,
        employee_id
    )
    cursor.execute(update_query, values)
    connection.commit()
    return {
        "message": "Employee Updated Successfully"
    }
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    check_query = "SELECT * FROM employees WHERE id = %s"
    cursor.execute(check_query, (employee_id,))
    employee = cursor.fetchone()
    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )
    delete_query = "DELETE FROM employees WHERE id = %s"
    cursor.execute(delete_query, (employee_id,))
    connection.commit()
    return {
        "message": "Employee Deleted Successfully"
    }
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "message": "Internal Server Error",
            "error": str(exc)
        }
    )

