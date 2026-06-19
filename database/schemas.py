from pydantic import BaseModel
class employeecreate(BaseModel):
    emp_id : int
    name: str
    email : str
    phone: str
class employeeout(BaseModel):
    emp_id : int
    name: str
    email : str
    phone: str