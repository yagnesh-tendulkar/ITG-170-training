#EmpMngAPI
from datetime import datetime
from enum import Enum
from typing import Dict
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, Field, validator
from passlib.context import CryptContext 
# This dictionary will act as our temporary database table.
# Key: employee_id (int), Value: dict of employee details
employee_db: Dict[int, dict] = {}
id_counter = 1  # Simulates an Auto-Incrementing Primary Key

# Password hashing helper
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ---------------------------------------------------------
# 2. ENUMS ->enforce specific allowed values for Role and Status fields
# ---------------------------------------------------------
class RoleEnum(str, Enum):
    HR = "HR"
    DEV = "Dev"
    TL = "TL"
    MANAGER = "Manager"

class StatusEnum(str, Enum):
    ACTIVE = "A"
    INACTIVE = "I"
    ASSIGNED = "P"  # P represents 'Assigned/Project'
    BENCH = "B"

# ---------------------------------------------------------
# 3. PYDANTIC SCHEMAS (Validation & Automation)
# ---------------------------------------------------------
class EmployeeCreate(BaseModel):
    first_name: str = Field(..., example="John")
    last_name: str = Field(..., example="Doe")
    phone_no: str = Field(..., example="1234567890")
    gmail: EmailStr = Field(..., example="johndoe@gmail.com")
    department: str = Field(..., example="Engineering")
    password: str = Field(..., min_length=6, example="password123")
    role: RoleEnum = Field(..., example="Dev")
    salary: float = Field(..., example=65000.0)
    status: StatusEnum = Field(default=StatusEnum.ACTIVE, example="A")

    # Sanitize inputs by trimming spaces and converting to lowercase
    @validator("first_name", "last_name")
    def clean_names(cls, v):
        return v.strip().lower()

class EmployeeResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    phone_no: str
    gmail: str
    corporate_email: str
    department: str
    role: str
    date_of_joining: datetime
    salary: float
    status: str

# ---------------------------------------------------------
# 4. FASTAPI APP SETUP
# ---------------------------------------------------------
app = FastAPI(title="In-Memory Employee Management API")

# ---------------------------------------------------------
# 5. API ENDPOINTS
# ---------------------------------------------------------

@app.post(
    "/employees/", 
    response_model=EmployeeResponse, 
    status_code=status.HTTP_201_CREATED,
    summary="Insert Employee Data "
)
def create_employee(
    employee: EmployeeCreate, 
    requesting_user_role: RoleEnum  # Simulates role checking
):
    global id_counter

    # Rule from Notes: Only "HR" role can insert data
    if requesting_user_role != RoleEnum.HR:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access Denied: Only HR accounts are authorized to insert data."
        )

    # Check for duplicate personal email in our local dictionary
    for emp in employee_db.values():
        if emp["gmail"] == employee.gmail:
            raise HTTPException(status_code=400, detail="Gmail address already registered.")

    # Automation Rule: Automatically structure corporate email (fn.ln@company.com)
    generated_corp_email = f"{employee.first_name}.{employee.last_name}@company.com"

    # Encrypt password string
    hashed_pwd = pwd_context.hash(employee.password)

    # Process and format data records
    new_employee_record = {
        "id": id_counter,
        "first_name": employee.first_name.capitalize(),
        "last_name": employee.last_name.capitalize(),
        "phone_no": employee.phone_no,
        "gmail": employee.gmail,
        "corporate_email": generated_corp_email,
        "department": employee.department,
        "hashed_password": hashed_pwd,
        "role": employee.role.value,
        "salary": employee.salary,
        "status": employee.status.value,
        "date_of_joining": datetime.now()  # Automatically captures actual current date & time
    }

    # Store in our in-memory dictionary and increment ID
    employee_db[id_counter] = new_employee_record
    id_counter += 1

    return new_employee_record


@app.get(
    "/employees/", 
    response_model=list[EmployeeResponse], 
    summary="Get All Employees"
)
def get_all_employees():
    # Helper route to quickly view everything saved in memory
    return list(employee_db.values())