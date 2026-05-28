from fastapi import FastAPI, HTTPException

app = FastAPI()

employees = {}

@app.post("/employees/{id}", status_code=201)
def create_employee(id: int, name: str):

    if id in employees:
        raise HTTPException(
            status_code=400,
            detail="Employee already exists"
        )

    employees[id] = name

    return {
        "message": "Employee created",
        "data": employees
    }


@app.get("/employees/{id}")
def get_employee(id: int):

    if id not in employees:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "id": id,
        "name": employees[id]
    }


@app.put("/employees/{id}")
def update_employee(id: int, name: str):

    if id not in employees:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    employees[id] = name

    return {
        "message": "Employee updated"
    }


@app.delete("/employees/{id}", status_code=204)
def delete_employee(id: int):

    if id not in employees:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    del employees[id]