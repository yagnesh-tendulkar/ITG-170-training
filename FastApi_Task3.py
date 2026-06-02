from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

employees = []

class Employee(BaseModel):
    id: int
    first_name: str
    last_name: str
    department: str
    salary: float

@app.post("/employee")
def create_employee(emp: Employee):

    for e in employees:

        if e["id"] == emp.id:
            raise HTTPException(
                status_code=400,
                detail="Employee already exists"
            )

    employees.append(emp.dict())

    return {
        "message": "Employee created successfully",
        "data": emp
    }

@app.get("/employee/{emp_id}")
def get_employee(emp_id: int):

    for emp in employees:

        if emp["id"] == emp_id:
            return emp

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )

@app.put("/employee/{emp_id}")
def update_employee(emp_id: int, updated: Employee):

    for i, emp in enumerate(employees):

        if emp["id"] == emp_id:

            employees[i] = updated.dict()

            return {
                "message": "Employee updated successfully",
                "data": updated
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )

@app.delete("/employee/{emp_id}")
def delete_employee(emp_id: int):

    for i, emp in enumerate(employees):

        if emp["id"] == emp_id:

            employees.pop(i)

            return {
                "message": "Employee deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )