from fastapi import FastAPI, HTTPException, status, Response
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def logger(request, call_next):
    start = time.time()
    response = await call_next(request)
    processing_time=time.time()-start
    print(processing_time)
    return response

employees = []

class Employee(BaseModel):
    id: int
    name: str
    dept: str


@app.post("/employees", status_code=status.HTTP_201_CREATED)
def create_employee(emp: Employee):
    for e in employees:
        if e["id"] == emp.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Employee already exists"
            )

    employees.append(emp.model_dump())

    return {
        "message": "Employee created",
        "data": emp
    }
@app.get("/employees", status_code=status.HTTP_200_OK)
def get_employees():
    if not employees:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return {
        "count": len(employees),
        "data": employees
    }
@app.put("/employees/{emp_id}")
def update_employee(emp_id: int, emp: Employee):

    for i, e in enumerate(employees):
        if e["id"] == emp_id:
            employees[i] = emp.model_dump()

            return {
                "message": "Employee updated",
                "data": emp
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Employee not found"
    )
@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int):

    for e in employees:
        if e["id"] == emp_id:
            employees.remove(e)
            return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Employee not found"
    )