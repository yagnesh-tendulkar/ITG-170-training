from datetime import datetime
from pathlib import Path

from fastapi import FastAPI, HTTPException, Query

from db import get_conn, init_db
from schemas import CreateTask, CreateUser, UpdateTask, UpdateUser

app = FastAPI(title="Simple Task API")


@app.on_event("startup")
def startup():
    init_db()


def row_to_dict(row):
    if row is None:
        return None
    return {k: row[k] for k in row.keys()}


@app.get("/")
def read_root():
    return {"message": "Simple Task API"}


@app.post("/users/")
def create_user(user: CreateUser):
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE email = ?", (user.email,))
        if cursor.fetchone():
            raise HTTPException(status_code=400, detail="Email already exists")

        cursor.execute(
            "INSERT INTO users (first_name, last_name, email, age, password) VALUES (?, ?, ?, ?, ?)",
            (user.first_name, user.last_name, user.email, user.age, user.password),
        )
        conn.commit()
        user_id = cursor.lastrowid
        return {"id": user_id, "message": "User created"}


@app.get("/users/")
def list_users():
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, first_name, last_name, email, age FROM users")
        rows = cursor.fetchall()
        return [row_to_dict(row) for row in rows]


@app.get("/users/{user_id}")
def get_user(user_id: int):
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, first_name, last_name, email, age FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="User not found")
        return row_to_dict(row)


@app.put("/users/{user_id}")
def update_user(user_id: int, user: UpdateUser):
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE id = ?", (user_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="User not found")

        fields = []
        values = []
        for name in ["first_name", "last_name", "email", "age"]:
            value = getattr(user, name)
            if value is not None:
                fields.append(f"{name} = ?")
                values.append(value)

        if not fields:
            raise HTTPException(status_code=400, detail="At least one field is required")

        values.append(user_id)
        cursor.execute(f"UPDATE users SET {', '.join(fields)} WHERE id = ?", tuple(values))
        conn.commit()
        return {"message": "User updated"}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found")
        conn.commit()
        return {"message": "User deleted"}


@app.post("/tasks/")
def create_task(task: CreateTask):
    with get_conn() as conn:
        cursor = conn.cursor()
        if task.user_id is not None:
            cursor.execute("SELECT id FROM users WHERE id = ?", (task.user_id,))
            if not cursor.fetchone():
                raise HTTPException(status_code=404, detail="User not found")

        cursor.execute(
            "INSERT INTO tasks (title, description, priority, due_date, user_id) VALUES (?, ?, ?, ?, ?)",
            (task.title, task.description, task.priority, task.due_date.isoformat(), task.user_id),
        )
        conn.commit()
        return {"id": cursor.lastrowid, "message": "Task created"}


@app.get("/tasks/")
def list_tasks(user_id: int | None = Query(None, description="Filter by user id")):
    with get_conn() as conn:
        cursor = conn.cursor()
        if user_id is not None:
            cursor.execute(
                "SELECT id, title, description, priority, status, due_date, user_id FROM tasks WHERE user_id = ?",
                (user_id,),
            )
        else:
            cursor.execute("SELECT id, title, description, priority, status, due_date, user_id FROM tasks")
        rows = cursor.fetchall()
        return [row_to_dict(row) for row in rows]


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, title, description, priority, status, due_date, user_id FROM tasks WHERE id = ?",
            (task_id,),
        )
        row = cursor.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Task not found")
        return row_to_dict(row)


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: UpdateTask):
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM tasks WHERE id = ?", (task_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Task not found")

        fields = []
        values = []
        for name in ["title", "description", "priority", "status", "due_date"]:
            value = getattr(task, name)
            if value is not None:
                if name == "due_date":
                    value = value.isoformat()
                fields.append(f"{name} = ?")
                values.append(value)

        if not fields:
            raise HTTPException(status_code=400, detail="At least one field is required")

        values.append(task_id)
        cursor.execute(f"UPDATE tasks SET {', '.join(fields)} WHERE id = ?", tuple(values))
        conn.commit()
        return {"message": "Task updated"}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    with get_conn() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Task not found")
        conn.commit()
        return {"message": "Task deleted"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
