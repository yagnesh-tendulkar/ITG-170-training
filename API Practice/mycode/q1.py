#pydantic models

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Initialized properly with 'id' fields to match your logic
student = [
    {"id": "1", "name": "Alice", "grade": 90},
    {"id": "2", "name": "Bob", "grade": 85}
]

# --- Pydantic Models (Schemas) ---
# Used for validating incoming data when creating a student
class StudentCreate(BaseModel):
    name: str
    grade: int

# Used for structuring outgoing data (Response)
class StudentResponse(BaseModel):
    id: str
    name: str
    grade: int


# --- API Endpoints ---

# 1. Get all students
@app.get("/students")
def get_students():
    return {"students": student}


# 2. Get a single student by ID
@app.get("/students/{st_id}")
def get_student_by_id(st_id: str):
    # Loop through list to find matching student ID
    for student in student:
        if student["id"] == st_id:
            return student
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Student not found"
    )


# 3. Create a new student (ID passed in URL, body details passed via Pydantic)
@app.post("/students/{st_id}", status_code=status.HTTP_201_CREATED)
def create_student(st_id: str, student_data: StudentCreate):
    
    if any(s["id"] == st_id for s in student):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Student with this ID already exists"
        )
    
    new_student = {
        "id": st_id,
        "name": student_data.name,
        "grade": student_data.grade
    }
    
    student.append(new_student)
    return {"message": "Student created successfully", "student": new_student}