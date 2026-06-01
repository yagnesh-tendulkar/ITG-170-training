from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from models import Employee, UpdateEmployee
from middleware import log_middleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.middleware("http")(log_middleware)

employees = [
    {
        "id": 1,
        "name": "Varshitha",
        "age": 22,
        "department": "Developer",
        "email": "varshitha@gmail.com"
    }
]

@app.get("/employees", status_code=status.HTTP_200_OK)
def get_employees():

    return {
        "success": True,
        "message": "Employees fetched successfully",
        "data": employees
    }


@app.post("/employees", status_code=status.HTTP_201_CREATED)
def create_employee(emp: Employee):

    for employee in employees:
        if employee["id"] == emp.id:
            raise HTTPException(
                status_code=400,
                detail="Employee ID already exists"
            )

    employees.append(emp.dict())

    return {
        "success": True,
        "message": "Employee created successfully",
        "employee": emp
    }


@app.put("/employees/{emp_id}", status_code=status.HTTP_200_OK)
def update_employee(emp_id: int, updated_data: UpdateEmployee):

    for employee in employees:

        if employee["id"] == emp_id:

            update_data = updated_data.dict(exclude_unset=True)

            employee.update(update_data)

            return {
                "success": True,
                "message": "Employee updated successfully",
                "employee": employee
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )


@app.delete("/employees/{emp_id}", status_code=status.HTTP_200_OK)
def delete_employee(emp_id: int):

    for employee in employees:

        if employee["id"] == emp_id:

            employees.remove(employee)

            return {
                "success": True,
                "message": "Employee deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )