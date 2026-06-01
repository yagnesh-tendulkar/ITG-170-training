import mysql.connector
from datetime import timezone

from database.db import get_connection
from exceptions import DatabaseException, NotFoundException, ValidationException


def _normalize_due_date(due_date):
    if due_date.tzinfo is None:
        return due_date.replace(tzinfo=timezone.utc)
    return due_date.astimezone(timezone.utc)


def create_task(task, user_id: int):
    if not task.title or not task.due_date:
        raise ValidationException("Task title and due date are required.")

    due_date = _normalize_due_date(task.due_date).replace(tzinfo=None)

    try:
        with get_connection() as conn, conn.cursor() as cursor:
            query = """
            INSERT INTO tasks
            (user_id,title,description,priority,due_date)
            VALUES (%s,%s,%s,%s,%s)
            """

            cursor.execute(
                query,
                (
                    user_id,
                    task.title,
                    task.description,
                    task.priority,
                    due_date,
                ),
            )

            conn.commit()
    except mysql.connector.Error as err:
        raise DatabaseException(f"Unable to create task: {err}")

    return {"message": "Task created successfully"}


def get_tasks(user_id: int, priority: str | None = None):
    try:
        with get_connection() as conn, conn.cursor(dictionary=True) as cursor:
            query = "SELECT id, title, description, priority, status, due_date FROM tasks WHERE user_id=%s"
            params = [user_id]

            if priority:
                normalized = priority.lower()
                if normalized not in ("low", "medium", "high"):
                    raise ValidationException("Priority must be low, medium, or high.")
                query += " AND priority=%s"
                params.append(normalized)

            cursor.execute(query, tuple(params))
            return cursor.fetchall()
    except mysql.connector.Error as err:
        raise DatabaseException(f"Unable to fetch tasks: {err}")


def get_task(task_id, user_id: int):
    try:
        with get_connection() as conn, conn.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT id, title, description, priority, status, due_date FROM tasks WHERE id=%s AND user_id=%s", (task_id, user_id))
            task = cursor.fetchone()
            if not task:
                raise NotFoundException("Task not found")
            return task
    except mysql.connector.Error as err:
        raise DatabaseException(f"Unable to fetch task: {err}")


def update_task(task_id, user_id: int, data):
    if not any((data.title, data.description, data.priority, data.status, data.due_date)):
        raise ValidationException("At least one field must be provided for update.")

    updates = []
    params = []
    if data.title is not None:
        updates.append("title=%s")
        params.append(data.title)
    if data.description is not None:
        updates.append("description=%s")
        params.append(data.description)
    if data.priority is not None:
        updates.append("priority=%s")
        params.append(data.priority)
    if data.status is not None:
        updates.append("status=%s")
        params.append(data.status)
    if data.due_date is not None:
        updates.append("due_date=%s")
        params.append(_normalize_due_date(data.due_date).replace(tzinfo=None))

    params.extend([task_id, user_id])

    try:
        with get_connection() as conn, conn.cursor() as cursor:
            query = f"UPDATE tasks SET {', '.join(updates)} WHERE id=%s AND user_id=%s"
            cursor.execute(query, tuple(params))
            if cursor.rowcount == 0:
                raise NotFoundException("Task not found")

            conn.commit()
    except mysql.connector.Error as err:
        raise DatabaseException(f"Unable to update task: {err}")

    return {"message": "Task updated successfully"}


def delete_task(task_id, user_id: int):
    try:
        with get_connection() as conn, conn.cursor() as cursor:
            cursor.execute("DELETE FROM tasks WHERE id=%s AND user_id=%s", (task_id, user_id))
            if cursor.rowcount == 0:
                raise NotFoundException("Task not found")

            conn.commit()
    except mysql.connector.Error as err:
        raise DatabaseException(f"Unable to delete task: {err}")

    return {"message": "Task deleted successfully"}