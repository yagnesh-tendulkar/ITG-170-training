from fastapi import FastAPI, HTTPException
from statuscodes import StatusCode

app = FastAPI()

staff_data = {
    1: {"emp_name": "Dora", "designation": "Developer"},
    2: {"emp_name": "Bujji", "designation": "Tester"}
}

@app.get("/staff/{staff_id}")
def fetch_staff(staff_id: int):

    if staff_id not in staff_data:
        raise HTTPException(
            status_code=StatusCode.NOT_FOUND,
            detail="Staff details not found")

    return {
        "status": StatusCode.OK,
        "result": staff_data[staff_id] }

@app.post("/staff/{staff_id}")
def add_staff(
    staff_id: int,
    emp_name: str,
    designation: str
):

    if staff_id in staff_data:
        raise HTTPException(
            status_code=StatusCode.BAD_REQUEST,
            detail="Staff exists"  )
    staff_data[staff_id] = {
        "emp_name": emp_name,
        "designation": designation
    }
    return {
        "status": StatusCode.CREATED,
        "message": "Staff added successfully"
    }

@app.put("/staff/{staff_id}")
def edit_staff(
    staff_id: int,
    emp_name: str,
    designation: str
):
    if staff_id not in staff_data:
        raise HTTPException(
            status_code=StatusCode.NOT_FOUND,
            detail="Staff not available for update")        )
    staff_data[staff_id] = {
        "emp_name": emp_name,
        "designation": designation
    }
    return {
        "status": StatusCode.OK,
        "message": "Staff updated successfully"
    }
@app.delete("/staff/{staff_id}")
def remove_staff(staff_id: int):

    if staff_id not in staff_data:
        raise HTTPException(
            status_code=StatusCode.NOT_FOUND,
            detail="Staff not available for delete"
        )

    del staff_data[staff_id]

    return {
        "status": StatusCode.OK,
        "message": "Staff removed successfully"
    }