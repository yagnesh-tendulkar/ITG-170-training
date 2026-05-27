from fastapi import FastAPI, HTTPException

app = FastAPI()
students = {}
@app.post("/students/{id}")
async def create_student(id: int, name: str):

    students[id] = name

    return {
        "status": 201,
        "message": "Student Created"
    }
@app.get("/students/{id}")
async def get_student(id: int):

    if id not in students:
        raise HTTPException(status_code=404, detail="Student Not Found")

    return {
        "status": 200,
        "student": students[id]
    }
@app.put("/students/{id}")
async def update_student(id: int, name: str):

    if id not in students:
        raise HTTPException(status_code=404, detail="Student Not Found")

    students[id] = name

    return {
        "status": 200,
        "message": "Student Updated"
    }

@app.delete("/students/{id}")
async def delete_student(id: int):

    if id not in students:
        raise HTTPException(status_code=404, detail="Student Not Found")

    del students[id]

    return {
        "status": 200,
        "message": "Student Deleted"
    }
