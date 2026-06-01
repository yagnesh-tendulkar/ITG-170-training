from fastapi import APIRouter
from app.database import get_db

router = APIRouter()

@router.get("/metrics")
def get_metrics():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")
    users = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tasks")
    tasks = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tasks WHERE status='completed'")
    completed = cursor.fetchone()[0]

    conn.close()

    return {
        "total_users": users,
        "total_tasks": tasks,
        "completed_tasks": completed
    }