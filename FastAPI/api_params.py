from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

students = []

class Student(BaseModel):
    id: int
    name: str
    age: int

@app.post("/students", status_code=status.HTTP_201_CREATED)
def create_student(student: Student):
    for s in students:
        if s["id"] == student.id:
            raise HTTPException(
                status_code=400,
                detail="Student with this ID already exists"
            )

    students.append(student.model_dump())

    return {
        "message": "Student created successfully",
        "data": student
    }

@app.get("/students")
def get_students(name: str = None, age: int = None):

    if not students:
        raise HTTPException(
            status_code=404,
            detail="No students found"
        )

    result = []

    for s in students:
        if (name is None or s["name"] == name) and \
           (age is None or s["age"] == age):
            result.append(s)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="No matching students found"
        )

    return {"data": result}