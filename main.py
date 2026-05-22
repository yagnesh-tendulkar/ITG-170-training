from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
import schemas

from database import engine, SessionLocal

app = FastAPI()

# Create tables
models.Base.metadata.create_all(bind=engine)


# Database connection
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# CREATE
@app.post("/todos")
def create_todo(todo: schemas.TodoCreate,
                db: Session = Depends(get_db)):

    new_todo = models.Todo(
        title=todo.title,
        completed=todo.completed
    )

    db.add(new_todo)

    db.commit()

    db.refresh(new_todo)

    return new_todo


# READ ALL
@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):

    return db.query(models.Todo).all()


# READ ONE
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int,
             db: Session = Depends(get_db)):

    todo = db.query(models.Todo).filter(
        models.Todo.id == todo_id
    ).first()

    if not todo:
        return {"error": "Todo not found"}

    return todo


# UPDATE
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int,
                updated_todo: schemas.TodoCreate,
                db: Session = Depends(get_db)):

    todo = db.query(models.Todo).filter(
        models.Todo.id == todo_id
    ).first()

    if not todo:
        return {"error": "Todo not found"}

    todo.title = updated_todo.title
    todo.completed = updated_todo.completed

    db.commit()

    db.refresh(todo)

    return {
        "message": "Updated successfully",
        "data": todo
    }



# DELETE
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int,
                db: Session = Depends(get_db)):

    todo = db.query(models.Todo).filter(
        models.Todo.id == todo_id
    ).first()

    if not todo:
        return {"error": "Todo not found"}

    db.delete(todo)

    db.commit()

    return {"message": "Deleted successfully"}