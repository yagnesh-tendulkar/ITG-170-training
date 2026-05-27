from fastapi import FastAPI, HTTPException, Request, status
from database import students, student_id_counter
from schemas import Student, UpdateStudent
from middleware import log_requests

app = FastAPI()


@app.middleware("http")
async def add_headers(request: Request, call_next):

    response = await call_next(request)

    response.headers["X-App"] = "Student-System"

    return response

app.middleware("http")(log_requests)

@app.post("/students", status_code=status.HTTP_201_CREATED)
def create_student(student: Student):

    global student_id_counter

    students[student_id_counter] = student.dict()

    students[student_id_counter]["id"] = student_id_counter

    student_id_counter += 1

    return {
        "message": "Student created successfully",
        "data": students[student_id_counter - 1]
    }

@app.get("/students", status_code=status.HTTP_200_OK)
def get_students():

    return {
        "message": "All students fetched",
        "data": list(students.values())
    }

@app.get("/students/{student_id}", status_code=status.HTTP_200_OK)
def get_student(student_id: int):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return students[student_id]

@app.put("/students/{student_id}", status_code=status.HTTP_200_OK)
def update_student(student_id: int, student: Student):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    students[student_id] = student.dict()

    students[student_id]["id"] = student_id

    return {
        "message": "Student fully updated",
        "data": students[student_id]
    }

@app.patch("/students/{student_id}", status_code=status.HTTP_200_OK)
def patch_student(student_id: int, student: UpdateStudent):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    stored_student = students[student_id]

    if student.name is not None:
        stored_student["name"] = student.name

    if student.age is not None:
        stored_student["age"] = student.age

    if student.email is not None:
        stored_student["email"] = student.email

    if student.course is not None:
        stored_student["course"] = student.course

    return {
        "message": "Student partially updated",
        "data": stored_student
    }
@app.delete(
    "/students/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_student(student_id: int):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    del students[student_id]

    return None