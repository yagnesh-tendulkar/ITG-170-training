from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# -----------------------------
# Fake Database
# -----------------------------

students = [
    {"id": 1, "name": "Balaji", "age": 21},
    {"id": 2, "name": "Ravi", "age": 22}
]

# -----------------------------
# Request Body Model
# -----------------------------

class Student(BaseModel):
    name: str
    age: int

# -----------------------------
# GET METHOD
# -----------------------------

@app.get("/students")
def get_students():
    return students

# -----------------------------
# GET SINGLE STUDENT
# -----------------------------

@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:
        if student["id"] == student_id:
            return student

    return {"message": "Student not found"}

# -----------------------------
# POST METHOD
# -----------------------------

@app.post("/students")
def create_student(student: Student):

    new_student = {
        "id": len(students) + 1,
        "name": student.name,
        "age": student.age
    }

    students.append(new_student)

    return {
        "message": "Student created",
        "student": new_student
    }

# -----------------------------
# PUT METHOD
# -----------------------------

@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):

    for student in students:

        if student["id"] == student_id:

            student["name"] = updated_student.name
            student["age"] = updated_student.age

            return {
                "message": "Student updated",
                "student": student
            }

    return {"message": "Student not found"}

# -----------------------------
# PATCH METHOD
# -----------------------------

@app.patch("/students/{student_id}")
def patch_student(student_id: int, name: str):

    for student in students:

        if student["id"] == student_id:

            student["name"] = name

            return {
                "message": "Student name updated ",
                "student": student
            }

    return {"message": "Student not found"}

# -----------------------------
# DELETE METHOD
# -----------------------------̨
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            return {
                "message": "Student deleted"
            }

    return {"message": "Student not found"}