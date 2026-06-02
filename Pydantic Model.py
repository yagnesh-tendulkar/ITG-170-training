# Pydantic model

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    course: str

@app.post("/student")
def create_student(student: Student):
    return {
        "message": "Student created successfully",
        "data": student
    }