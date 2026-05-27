from pydantic import BaseModel


# =========================
# EMPLOYEE SCHEMA
# =========================
class Employee(BaseModel):

    first_name: str

    last_name: str

    corporate_mail: str

    personal_email: str

    phone_number: str

    department: str

    joining_date: str

    salary: float

    address: str

    role_id: int

    status_id: int


# =========================
# ROLE SCHEMA
# =========================
class Role(BaseModel):

    role_name: str


# =========================
# STATUS SCHEMA
# =========================
class Status(BaseModel):

    status_code: str

    status_name: str