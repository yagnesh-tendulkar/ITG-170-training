# CURD Operations

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

students = {}

class Student(BaseModel):
    id: int
    name: str
    course: str

@app.post("/students", status_code=status.HTTP_201_CREATED)
def create_student(student: Student):

    students[student.id] = student

    return {
        "message": "Student created",
        "data": student
    }

@app.get("/students/{student_id}")
def get_student(student_id: int):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return students[student_id]

@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    students[student_id] = updated_student

    return {
        "message": "Student updated successfully"
    }

@app.delete("/students/{student_id}",
            status_code=status.HTTP_200_OK)
def delete_student(student_id: int):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    del students[student_id]

    return {
        "message": "Student deleted successfully"
    }