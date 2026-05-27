from sqlalchemy import Column, Integer, String, Float
from app.database import Base


# =========================
# EMPLOYEES TABLE
# =========================
class EmployeeDB(Base):

    __tablename__ = "employees"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True)

    # Employee First Name
    first_name = Column(String(100))

    # Employee Last Name
    last_name = Column(String(100))

    # Corporate Mail
    corporate_mail = Column(String(150))

    # Personal Email
    personal_email = Column(String(150))

    # Phone Number
    phone_number = Column(String(20))

    # Department
    department = Column(String(100))

    # Joining Date
    joining_date = Column(String(50))

    # Salary
    salary = Column(Float)

    # Address
    address = Column(String(200))

    # Role ID
    role_id = Column(Integer)

    # Status ID
    status_id = Column(Integer)


# =========================
# ROLES TABLE
# =========================
class RoleDB(Base):

    __tablename__ = "roles"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True)

    # Role Name
    role_name = Column(String(100))


# =========================
# STATUS TABLE
# =========================
class StatusDB(Base):

    __tablename__ = "status"

    # Primary Key
    id = Column(Integer, primary_key=True, index=True)

    # Status Code
    status_code = Column(String(10))

    # Status Name
    status_name = Column(String(100))