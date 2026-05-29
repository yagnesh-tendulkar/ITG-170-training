from fastapi import FastAPI, HTTPException, Depends, Request
from pydantic import BaseModel
from datetime import datetime, timedelta, date
import mysql.connector
from jose import jwt, JWTError
from passlib.context import CryptContext
from typing import Optional
app = FastAPI()
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="M1racle@123",
    database="employee_management"
)
cursor = conn.cursor(dictionary=True)
print("Database Connected Successfully")
SECRET_KEY = "MYSECRETKEY"
ALGORITHM = "HS256"
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)
class EmployeePatch(BaseModel):
    department: Optional[str] = None
    salary: Optional[float] = None
    employee_status: Optional[str] = None
class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    mobile_number: str
    email: str
    department: str
    role_id: int
    joining_date: date
    salary: float
    employee_status: str
class LoginSchema(BaseModel):
    username: str
    password: str
def hash_password(password):
    return pwd_context.hash(password)
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )
def create_token(data):
    payload = data.copy()
    expire = datetime.utcnow() + timedelta(hours=5)
    payload.update({"exp": expire})
    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return token
async def verify_hr(request: Request):
    token = request.headers.get("token")
    if not token:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized Access. Only HR users can add, update, or delete employee records."
        )
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        role = payload.get("role")
        if role != "HR":
            raise HTTPException(
                status_code=403,
                detail="Only HR Allowed"
            )
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )
@app.get("/")
def home():
    return {
        "message": "Employee Management System Running"
    }
@app.post("/add-employee")
async def add_employee(
    employee: EmployeeCreate,
    request: Request
):
    # Check whether any employee exists
    cursor.execute(
        "SELECT COUNT(*) AS total FROM employees"
    )
    result = cursor.fetchone()
    # First Employee => Automatically HR
    if result["total"] == 0:
        role_id = 1
    else:
        # Existing System => Only HR can add employees
        await verify_hr(request)
        role_id = employee.role_id
    # Username Generation
    username = (
        employee.first_name[0].lower()
        + employee.last_name.lower()
    )
    # Duplicate Username Check
    cursor.execute(
        "SELECT * FROM employees WHERE username=%s",
        (username,)
    )
    existing_user = cursor.fetchone()
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username Already Exists"
        )
    # Password Generation
    current_datetime = datetime.now().strftime(
        "%d%m%Y%H%M"
    )
    raw_password = (
        employee.first_name[-2:].lower()
        + employee.last_name[:2].lower()
        + current_datetime
    )
    hashed_password = hash_password(
        raw_password
    )
    # Corporate Email Generation
    corporate_email = (
        employee.first_name.lower()
        + "."
        + employee.last_name.lower()
        + "@miracle.com"
    )
    password_created_at = datetime.now()
    query = """
    INSERT INTO employees
    (
        first_name,
        last_name,
        mobile_number,
        email,
        corporate_email,
        department,
        role_id,
        joining_date,
        salary,
        employee_status,
        username,
        password,
        password_created_at
    )
    VALUES
    (
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
    )
    """
    values = (
        employee.first_name,
        employee.last_name,
        employee.mobile_number,
        employee.email,
        corporate_email,
        employee.department,
        role_id,
        employee.joining_date,
        employee.salary,
        employee.employee_status,
        username,
        hashed_password,
        password_created_at
    )
    cursor.execute(query, values)
    conn.commit()
    if result["total"] == 0:
        return {
            "message": "First HR Created Successfully",
            "username": username,
            "password": raw_password,
            "corporate_email": corporate_email
        }
    return {
        "message": "Employee Added Successfully",
        "username": username,
        "password": raw_password,
        "corporate_email": corporate_email
    }
@app.get("/employees")
def get_employees():
    query = """
    SELECT
        e.employee_id,
        e.first_name,
        e.last_name,
        e.department,
        e.salary,
        e.employee_status,
        r.role_name
    FROM employees e
    JOIN roles r
    ON e.role_id = r.role_id
    """
    cursor.execute(query)
    employees = cursor.fetchall()
    return employees
@app.get("/employee/{employee_id}")
def get_single_employee(employee_id: int):
    query = """
    SELECT
        e.employee_id,
        e.first_name,
        e.last_name,
        e.mobile_number,
        e.email,
        e.corporate_email,
        e.department,
        e.salary,
        e.employee_status,
        r.role_name
    FROM employees e
    JOIN roles r
    ON e.role_id = r.role_id
    WHERE employee_id=%s
    """
    cursor.execute(query, (employee_id,))
    employee = cursor.fetchone()
    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee Not Found"
        )
    return employee
@app.put("/update-employee/{employee_id}")
def update_employee(
    employee_id: int,
    department: str,
    salary: float,
    auth=Depends(verify_hr)
):
    query = """
    UPDATE employees
    SET
        department=%s,
        salary=%s
    WHERE employee_id=%s
    """
    values = (
        department,
        salary,
        employee_id
    )
    cursor.execute(query, values)
    conn.commit()
    return {
        "message": "Employee Updated Successfully"
    }
@app.delete("/delete-employee/{employee_id}")
def delete_employee(
    employee_id: int,
    auth=Depends(verify_hr)
):
    query = """
    DELETE FROM employees
    WHERE employee_id=%s
    """
    cursor.execute(query, (employee_id,))
    conn.commit()
    return {
        "message": "Employee Deleted Successfully"
    }
@app.patch("/employee/{employee_id}")
async def patch_employee(
    employee_id: int,
    employee: EmployeePatch,
    request: Request
):

    await verify_hr(request)

    updates = []
    values = []

    if employee.department is not None:
        updates.append("department=%s")
        values.append(employee.department)

    if employee.salary is not None:
        updates.append("salary=%s")
        values.append(employee.salary)

    if employee.employee_status is not None:
        updates.append("employee_status=%s")
        values.append(employee.employee_status)

    if not updates:
        raise HTTPException(
            status_code=400,
            detail="No fields provided for update"
        )

    query = f"""
    UPDATE employees
    SET {', '.join(updates)}
    WHERE employee_id=%s
    """

    values.append(employee_id)

    cursor.execute(query, tuple(values))
    conn.commit()

    return {
        "message": "Employee Updated Successfully"
    }
@app.post("/login")
def login(user: LoginSchema):
    query = """
    SELECT
        e.*,
        r.role_name
    FROM employees e
    JOIN roles r
    ON e.role_id = r.role_id
    WHERE username=%s
    """
    cursor.execute(query, (user.username,))
    db_user = cursor.fetchone()
    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="User Not Found"
        )
    if not verify_password(
            user.password,
            db_user["password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid Password"
        )
    token = create_token({
        "username": db_user["username"],
        "role": db_user["role_name"]
    })
    return {
        "message": "Login Successful",
        "token": token
    }
@app.get("/create-tables")
def create_tables():
    roles_table = """
    CREATE TABLE IF NOT EXISTS roles(
        role_id INT PRIMARY KEY AUTO_INCREMENT,
        role_name VARCHAR(50) UNIQUE
    )
    """
    cursor.execute(roles_table)
    employee_status_table = """
    CREATE TABLE IF NOT EXISTS employee_status(
        status_code CHAR(1) PRIMARY KEY,
        status_name VARCHAR(50)
    )
    """
    cursor.execute(employee_status_table)
    employees_table = """
    CREATE TABLE IF NOT EXISTS employees(
        employee_id INT PRIMARY KEY AUTO_INCREMENT,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        mobile_number VARCHAR(15),
        email VARCHAR(100),
        corporate_email VARCHAR(100),
        department VARCHAR(50),
        role_id INT,
        joining_date DATE,
        salary DECIMAL(10,2),
        employee_status CHAR(1),
        username VARCHAR(100) UNIQUE,
        password VARCHAR(255),
        password_created_at DATETIME,
        FOREIGN KEY(role_id)
        REFERENCES roles(role_id),
        FOREIGN KEY(employee_status)
        REFERENCES employee_status(status_code)
    )
    """
    cursor.execute(employees_table)
    conn.commit()
    return {
        "message": "Tables Created Successfully"
    }