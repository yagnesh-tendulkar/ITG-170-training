from fastapi import FastAPI, HTTPException
from statuscodes import StatusCode

app = FastAPI()

employees = {
    1: {"name": "Dora", "role": "Developer"},
    2: {"name": "Bujji", "role": "Tester"}
}

@app.get("/employees/{emp_id}")
def get_employee(emp_id: int):

    if emp_id not in employees:
        raise HTTPException(
            status_code=StatusCode.NOT_FOUND,
            detail="Employee not found"
        )

    return {
        "status": StatusCode.OK,
        "data": employees[emp_id]
    }


@app.post("/employees/{emp_id}")
def create_employee(emp_id: int, name: str, role: str):

    if emp_id in employees:
        raise HTTPException(
            status_code=StatusCode.BAD_REQUEST,
            detail="Employee already exists"
        )

    employees[emp_id] = {
        "name": name,
        "role": role
    }

    return {
        "status": StatusCode.CREATED,
        "message": "Employee created successfully"
    }


@app.put("/employees/{emp_id}")
def update_employee(emp_id: int, name: str, role: str):

    if emp_id not in employees:
        raise HTTPException(
            status_code=StatusCode.NOT_FOUND,
            detail="Employee not found for update"
        )

    employees[emp_id] = {
        "name": name,
        "role": role
    }

    return {
        "status": StatusCode.OK,
        "message": "Employee updated successfully"
    }

@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int):

    if emp_id not in employees:
        raise HTTPException(
            status_code=StatusCode.NOT_FOUND,
            detail="Employee not found for delete"
        )

    del employees[emp_id]

    return {
        "status": StatusCode.OK,
        "message": "Employee deleted successfully"
    }