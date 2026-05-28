################# Assignment ##################

from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
import time
import asyncio

app = FastAPI()
Students = []

class StatusCode:
    OK = status.HTTP_200_OK
    CREATED = status.HTTP_201_CREATED
    NOT_FOUND = status.HTTP_404_NOT_FOUND
    BAD_REQUEST = status.HTTP_400_BAD_REQUEST

class Message:
    STUDENT_ADDED = "Student added Successfully"
    STUDENT_UPDATED = "Student updated Successfully"
    STUDENT_DELETED = "Student deleted Successfully"
    STUDENT_NOT_FOUND = "Student Not Found"



class Student(BaseModel):
    id: int
    age: int = Field(gt=18, lt=22)
    name: str

@app.get("/student", status_code=StatusCode.OK)
def get_all():
    return Students


@app.get("/student/{id}", status_code=StatusCode.OK)
def get_by_id(id: int):
    for obj in Students:
        if obj.id == id:
            return obj
    raise HTTPException(
        status_code=StatusCode.NOT_FOUND,
        detail=Message.STUDENT_NOT_FOUND
    )

@app.post("/student", status_code=StatusCode.CREATED)
def post_student(new_student: Student):
    Students.append(new_student)
    return {
        "message": Message.STUDENT_ADDED
    }

@app.delete("/student/{id}", status_code=StatusCode.OK)
def delete_student(id: int):
    for index in range(len(Students)):
        if Students[index].id == id:
            Students.pop(index)
            return {
                "message": Message.STUDENT_DELETED
            }
    raise HTTPException(
        status_code=StatusCode.NOT_FOUND,
        detail=Message.STUDENT_NOT_FOUND
    )

@app.put("/student/{id}", status_code=StatusCode.OK)
def update_student(id: int, updated_Details: Student):
    for index in range(len(Students)):
        if Students[index].id == id:
            Students[index] = updated_Details
            return {
                "message": Message.STUDENT_UPDATED
            }
    raise HTTPException(
        status_code=StatusCode.NOT_FOUND,
        detail=Message.STUDENT_NOT_FOUND
    )

@app.middleware("http")
async def log_time(req: Request, call_next):
    print("Request Time:", time.time())
    res = await call_next(req)
    return res

async def stream_students():
    for student in Students:
        yield f"ID: {student.id}, Name: {student.name}, Age: {student.age}\n"
        await asyncio.sleep(1)

@app.get("/stream-students")
async def stream_student_data():
    return StreamingResponse(
        stream_students(),
        media_type="text/plain"
    )