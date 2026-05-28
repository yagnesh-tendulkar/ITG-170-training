from fastapi import FastAPI,Query,Path,HTTPException,status,Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel,Field,EmailStr
from typing import Optional, Dict
import mysql.connector
app = FastAPI()
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="M1racle@123",
    database="student_db"
)
cursor = connection.cursor(dictionary=True)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
class APIResponse(BaseModel):
    status: str
    message: str
    data: Optional[dict] = None
class Student(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=50
    )
    age: int = Field(
        ...,
        gt=0,
        lt=100
    )
    email: EmailStr
    course: str = Field(
        ...,
        min_length=2,
        max_length=50
    )
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[EmailStr] = None
    course: Optional[str] = None
@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception
):
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": "Internal Server Error"
        }
    )
@app.get("/")
def home():
    return {
        "message": "Student API Running Successfully"
    }
@app.post(
    "/students/{student_id}",
    response_model=APIResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student(
    student: Student,
    student_id: int = Path(
        ...,
        gt=0
    ),
    save: bool = Query(True)
):
    if not save:
        return APIResponse(
            status="failed",
            message="Student not saved"
        )
    # CHECK EXISTING STUDENT
    query = "SELECT * FROM students WHERE student_id = %s"
    cursor.execute(query, (student_id,))
    existing_student = cursor.fetchone()
    if existing_student:
        raise HTTPException(
            status_code=409,
            detail="Student already exists"
        )
    # INSERT QUERY
    insert_query = """
    INSERT INTO students
    (student_id, name, age, email, course)
    VALUES (%s, %s, %s, %s, %s)
    """
    values = (
        student_id,
        student.name,
        student.age,
        student.email,
        student.course
    )
    cursor.execute(insert_query, values)
    connection.commit()
    return APIResponse(
        status="success",
        message="Student created successfully",
        data={
            "student_id": student_id,
            "name": student.name,
            "age": student.age,
            "email": student.email,
            "course": student.course
        }
    )
@app.get(
    "/students/{student_id}",
    response_model=APIResponse
)
def get_student(
    student_id: int = Path(
        ...,
        gt=0
    ),
    course: Optional[str] = Query(None),
    age: Optional[int] = Query(None)
):
    query = "SELECT * FROM students WHERE student_id = %s"
    cursor.execute(query, (student_id,))
    student = cursor.fetchone()
    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    if course and student["course"] != course:
        return APIResponse(
            status="failed",
            message="Course does not match"
        )
    if age and student["age"] != age:
        return APIResponse(
            status="failed",
            message="Age does not match"
        )
    return APIResponse(
        status="success",
        message="Student fetched successfully",
        data=student
    )
@app.get("/students")
def get_all_students(
    limit: int = Query(10, gt=0),
    skip: int = Query(0, ge=0)
):
    query = "SELECT * FROM students LIMIT %s OFFSET %s"
    cursor.execute(query, (limit, skip))
    students = cursor.fetchall()
    return {
        "status": "success",
        "count": len(students),
        "data": students
    }
@app.put(
    "/students/{student_id}",
    response_model=APIResponse
)
def update_student(
    student: Student,
    student_id: int = Path(..., gt=0),
    confirm: bool = Query(...)
):
    if not confirm:
        return APIResponse(
            status="failed",
            message="Update cancelled"
        )
    check_query = "SELECT * FROM students WHERE student_id = %s"
    cursor.execute(check_query, (student_id,))
    existing_student = cursor.fetchone()
    if not existing_student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    update_query = """
    UPDATE students
    SET name=%s, age=%s, email=%s, course=%s
    WHERE student_id=%s
    """
    values = (
        student.name,
        student.age,
        student.email,
        student.course,
        student_id
    )
    cursor.execute(update_query, values)
    connection.commit()
    return APIResponse(
        status="success",
        message="Student updated successfully",
        data=student.model_dump()
    )
@app.delete(
    "/students/{student_id}",
    response_model=APIResponse
)
def delete_student(
    student_id: int = Path(..., gt=0),
    permanent: bool = Query(False)
):
    check_query = "SELECT * FROM students WHERE student_id = %s"
    cursor.execute(check_query, (student_id,))
    student = cursor.fetchone()
    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    delete_query = "DELETE FROM students WHERE student_id = %s"
    cursor.execute(delete_query, (student_id,))
    connection.commit()
    return APIResponse(
        status="success",
        message="Student deleted successfully",
        data=student
    )