from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

students = {}

class Student(BaseModel):
    name: str
    age: int
#to create
@app.post("/student/{student_id}")
def create_student(
    student_id: int,
    student: Student,
    course: str = Query(...)):
        students[student_id] = {
        "name": student.name,
        "age": student.age,
        "course": course
    }
    return {
        "message": "Created",
        "data": students[student_id]
    }

@app.put("/student/{student_id}")
def update_student(
    student_id: int,
    student: Student,
    city: str = Query(...)):

    students[student_id] = {
        "name": student.name,
        "age": student.age,
        "city": city
    }

    return {
        "message": "Updated",
        "data": students[student_id]
    }
#to dele the data

@app.delete("/student/{student_id}")
def delete_student(
    student_id: int,
    confirm: bool = Query(...)):

    if not confirm:
        return {"message": "Deletion cancelled"}

    students.pop(student_id, None)

    return {
        "message": "Deleted"
    }