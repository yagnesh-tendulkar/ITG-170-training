from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
import crud

from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE
@app.post("/students/", response_model=schemas.StudentResponse)
def create_student(
    student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):
    return crud.create_student(db, student)


# READ ALL
@app.get("/students/")
def read_students(db: Session = Depends(get_db)):
    return crud.get_students(db)


# READ ONE
@app.get("/students/{student_id}")
def read_student(student_id: int, db: Session = Depends(get_db)):

    student = crud.get_student(db, student_id)

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# UPDATE
@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    student: schemas.StudentCreate,
    db: Session = Depends(get_db)
):

    updated_student = crud.update_student(
        db,
        student_id,
        student
    )

    if not updated_student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return updated_student


# DELETE
@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    deleted_student = crud.delete_student(db, student_id)

    if not deleted_student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "message": "Student deleted successfully"
    }