from fastapi import FastAPI, Query
from pydantic import BaseModel
import mysql.connector

app = FastAPI()
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="college"
)

cursor = conn.cursor(dictionary=True)
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
)
""")

conn.commit()


# Request Body Model
class Student(BaseModel):
    name: str
    age: int
# READ
@app.get("/students/{student_id}")
def get_student(
    student_id: int,
    course: str = Query(None),
    status: str = Query("active")
):

    cursor.execute(
        "SELECT * FROM students WHERE id=%s",
        (student_id,)
    )

    data = cursor.fetchone()

    return {
        "method": "GET",
        "student_id": student_id,
        "course": course,
        "status": status,
        "data": data
    }



# Create
@app.post("/students/{student_id}")
def create_student(
    student_id: int,
    course: str = Query("general"),
    student: Student = None
):

    query = """
    INSERT INTO students(id, name, age)
    VALUES(%s, %s, %s)
    """

    values = (
        student_id,
        student.name,
        student.age
    )

    cursor.execute(query, values)
    conn.commit()

    return {
        "method": "POST",
        "student_id": student_id,
        "course": course,
        "data": student,
        "message": "Student Created"
    }
# UPDATE

@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    course: str = Query(None),
    notify: bool = Query(False),
    student: Student = None
):

    query = """
    UPDATE students
    SET name=%s, age=%s
    WHERE id=%s
    """

    cursor.execute(
        query,
        (student.name, student.age, student_id)
    )

    conn.commit()

    return {
        "method": "PUT",
        "student_id": student_id,
        "course": course,
        "notify": notify,
        "updated_data": student,
        "message": "Student Updated"
    }
# DELETE
@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    reason: str = Query(None),
    hard_delete: bool = Query(True)
):

    cursor.execute(
        "DELETE FROM students WHERE id=%s",
        (student_id,)
    )

    conn.commit()

    return {
        "method": "DELETE",
        "student_id": student_id,
        "reason": reason,
        "hard_delete": hard_delete,
        "message": "Student Deleted"
    }