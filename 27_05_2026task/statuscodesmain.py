from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
from statuscodesclass import AppStatus
from statuscodesclass import (
    StudentNotFoundException,
    StudentAlreadyExistsException
)
app = FastAPI()
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="M1racle@123",
    database="studentdb"
)
cursor = connection.cursor(dictionary=True)
class Student(BaseModel):
    name: str
    course: str
@app.post("/students/{student_id}")
def create_student(student_id: int, student: Student):
    # CHECK STUDENT EXISTS
    select_query = "SELECT * FROM students WHERE id = %s"
    cursor.execute(select_query, (student_id,))
    existing_student = cursor.fetchone()
    if existing_student:
        raise StudentAlreadyExistsException()
    # INSERT STUDENT
    insert_query = """
        INSERT INTO students(id, name, course)
        VALUES(%s, %s, %s)
    """
    values = (
        student_id,
        student.name,
        student.course
    )
    cursor.execute(insert_query, values)
    connection.commit()
    return {
        "success": True,
        "status": AppStatus.HTTP_201_CREATED,
        "message": AppStatus.STUDENT_CREATED,
        "data": {
            "id": student_id,
            "name": student.name,
            "course": student.course
        }
    }
@app.get("/students/{student_id}")
def get_student(student_id: int):
    query = "SELECT * FROM students WHERE id = %s"
    cursor.execute(query, (student_id,))
    student = cursor.fetchone()
    if not student:
        raise StudentNotFoundException()
    return {
        "success": True,
        "status": AppStatus.HTTP_200_OK,
        "message": AppStatus.STUDENT_FETCHED,
        "data": student
    }