from datetime import date
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, Session, relationship
from sqlalchemy.ext.hybrid import hybrid_property

DATABASE_URL = "mysql+pymysql://root:M1racle%40123@localhost:3306/practice_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Role(Base):
    __tablename__ = "roles"

    id = Column(String(1), primary_key=True)
    role_name = Column(String(50), nullable=False)

    employees = relationship(
        "Employee",
        back_populates="role"
    )

class Status(Base):
    __tablename__ = "statuses"

    id = Column(String(1), primary_key=True)
    status_name = Column(String(50), nullable=False)

    employees = relationship(
        "Employee",
        back_populates="status"
    )

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)

    personal_email = Column(
        String(100),
        unique=True,
        nullable=False
    )

    phone_number = Column(
        String(20),
        nullable=False
    )

    join_date = Column(
        Date,
        default=date.today
    )

    salary = Column(
        Integer,
        nullable=False
    )

    department = Column(
        String(50),
        nullable=False
    )

    role_id = Column(
        String(1),
        ForeignKey("roles.id")
    )

    status_id = Column(
        String(1),
        ForeignKey("statuses.id")
    )

    role = relationship(
        "Role",
        back_populates="employees"
    )

    status = relationship(
        "Status",
        back_populates="employees"
    )

    @hybrid_property
    def corporate_email(self):
        return (
            f"{self.first_name[0].lower()}"
            f"{self.last_name.lower()}@corporate.com"
        )

    @hybrid_property
    def generated_password(self):
        return (
            f"{self.first_name[-2:].lower()}"
            f"{self.last_name[-2:].lower()}"
        )

class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    personal_email: EmailStr
    phone_number: str
    salary: int
    department: str
    role_id: str
    status_id: str

class EmployeeResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    corporate_email: str
    generated_password: str
    personal_email: str
    phone_number: str
    join_date: date
    salary: int
    department: str
    role_code: str
    role_name: str
    status_code: str
    status_name: str

    class Config:
        from_attributes = True

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.post("/employees")
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):

    role = db.query(Role).filter(
        Role.id == employee.role_id
    ).first()

    if not role:
        raise HTTPException(
            status_code=404,
            detail="Role not found"
        )

    status = db.query(Status).filter(
        Status.id == employee.status_id
    ).first()

    if not status:
        raise HTTPException(
            status_code=404,
            detail="Status not found"
        )

    new_employee = Employee(
        first_name=employee.first_name,
        last_name=employee.last_name,
        personal_email=employee.personal_email,
        phone_number=employee.phone_number,
        salary=employee.salary,
        department=employee.department,
        role_id=employee.role_id,
        status_id=employee.status_id
    )

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return {
        "message": "Employee created successfully",
        "employee_id": new_employee.id,
        "corporate_email": new_employee.corporate_email,
        "generated_password": new_employee.generated_password
    }

@app.get(
    "/employees/{employee_id}",
    response_model=EmployeeResponse
)

def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    employee = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "id": employee.id,
        "first_name": employee.first_name,
        "last_name": employee.last_name,
        "corporate_email": employee.corporate_email,
        "generated_password": employee.generated_password,
        "personal_email": employee.personal_email,
        "phone_number": employee.phone_number,
        "join_date": employee.join_date,
        "salary": employee.salary,
        "department": employee.department,
        "role_code": employee.role_id,
        "role_name": employee.role.role_name,
        "status_code": employee.status_id,
        "status_name": employee.status.status_name
    }