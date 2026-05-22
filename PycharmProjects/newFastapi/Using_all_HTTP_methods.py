from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
# Temporary Database
students = {}
# Request Body Model
class Student(BaseModel):
    name: str
    age: int
    branch: str
# 1. GET ALL STUDENTS
@app.get("/students")
def get_students():
    return students
# 2. GET PARTICULAR STUDENT
@app.get("/students/{id}")
def get_student(id: int):
    if id in students:
        return students[id]
    return {"message": "Student Not Found"}
# 3. ADD NEW STUDENT
@app.post("/students/add/{id}")
def add_student(id: int, student: Student):
    students[id] = {
        "name": student.name,
        "age": student.age,
        "branch": student.branch
    }
    return {
        "message": "Student Added Successfully",
        "student_id": id,
        "student": students[id]
    }
# 4. FULL UPDATE STUDENT
@app.put("/students/update/{id}")
def update_student(id: int, student: Student):
    if id not in students:
        return {"message": "Student Not Found"}
    students[id] = {
        "name": student.name,
        "age": student.age,
        "branch": student.branch
    }
    return {
        "message": "Student Fully Updated",
        "student_id": id,
        "updated_data": students[id]
    }
# 5. PARTIAL UPDATE STUDENT
@app.patch("/students/patch/{id}")
def patch_student(id: int, updated_data:Student):
    if id not in students:
        return {"message": "Student Not Found"}
    students[id]["name"] = student.name
    students[id]["age"] = student.age
    students[id]["branch"] = student.branch
    return {
        "message": "Student Updated Successfully",
        "student": students[id]
    }
# 6. DELETE STUDENT
@app.delete("/students/delete/{id}")
def delete_student(id: int):
    if id not in students:
        return {"message": "Student Not Found"}
    deleted_student = students.pop(id)
    return {
        "message": "Student Deleted Successfully",
        "student_id": id,
        "deleted_data": deleted_student
    }