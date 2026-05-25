from sqlalchemy import Column, Integer, String 
from database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String(100), unique=True)

    email = Column(String(100), unique=True)

    password = Column(String(255))


class Employee(Base):    

    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100))

    department = Column(String(100))

    salary = Column(Integer)


