from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

students = {}

class Student(BaseModel):
    name: str
    age: int
    course: str


@app.post("/students/{student_id}", status_code=201)
def create_student(student_id: int, student: Student):

    if student_id in students:
        raise HTTPException(
            status_code=400,
            detail="Student already exists"
        )

    students[student_id] = student

    return {
        "message": "Student added",
        "data": student
    }


@app.get("/students/{student_id}")
def get_student(student_id: int = Path(..., gt=0)):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return students[student_id]


@app.get("/search")
def search_student(course: Optional[str] = Query(None), age: Optional[int] = Query(None)):

    data = []

    for id, student in students.items():

        if course and student.course != course:
            continue

        if age and student.age != age:
            continue

        data.append({
            "id": id,
            "student": student
        })

    return data


@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    students[student_id] = student

    return {
        "message": "Student updated"
    }


@app.delete("/students/{student_id}", status_code=204)
def delete_student(student_id: int):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    del students[student_id]