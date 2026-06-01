from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from fastapi.responses import StreamingResponse
from app.database import get_db
from app.dependencies import get_current_user
from app.services.stream_service import task_stream_generator
from app.background import send_email_background

router = APIRouter()

# ---------------- CREATE TASK ----------------
@router.post("/tasks")
def create_task(task: dict, user=Depends(get_current_user)):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO tasks (title, description, priority, user_id)
        VALUES (%s,%s,%s,%s)
        """,
        (task["title"], task["description"], task["priority"], user["user_id"])
    )

    conn.commit()
    conn.close()

    return {"message": "Task created"}


# ---------------- GET ALL TASKS (FILTER + PAGINATION START) ----------------
@router.get("/tasks")
def get_tasks(status: str = None, priority: str = None, page: int = 1, limit: int = 10):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM tasks WHERE 1=1"
    params = []

    if status:
        query += " AND status=%s"
        params.append(status)

    if priority:
        query += " AND priority=%s"
        params.append(priority)

    offset = (page - 1) * limit
    query += " LIMIT %s OFFSET %s"
    params.extend([limit, offset])

    cursor.execute(query, params)
    tasks = cursor.fetchall()

    conn.close()
    return tasks


# ---------------- GET TASK BY ID ----------------
@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tasks WHERE id=%s", (task_id,))
    task = cursor.fetchone()

    conn.close()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


# ---------------- UPDATE TASK ----------------
@router.put("/tasks/{task_id}")
def update_task(task_id: int, task: dict):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE tasks 
        SET title=%s, description=%s, status=%s, priority=%s
        WHERE id=%s
        """,
        (task["title"], task["description"], task["status"], task["priority"], task_id)
    )

    conn.commit()
    conn.close()

    return {"message": "Task updated"}


# ---------------- DELETE TASK ----------------
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
    conn.commit()
    conn.close()

    return {"message": "Task deleted"}


@router.get("/tasks/{task_id}/stream")
def stream_task(task_id: int):
    return StreamingResponse(
        task_stream_generator(task_id),
        media_type="text/plain"
    )


@router.post("/tasks/{task_id}/notify")
def notify_task(task_id: int, background_tasks: BackgroundTasks, user_email: str):
    background_tasks.add_task(send_email_background, user_email, task_id)

    return {"message": "Notification queued"}