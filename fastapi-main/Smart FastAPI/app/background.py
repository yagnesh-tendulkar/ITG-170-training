import time
from fastapi import BackgroundTasks
from app.logging_conf import logger


def write_notification(email: str, message: str = ""):
    logger.info(f"Notification sent to {email}: {message}")


def send_email_background(email: str, task_id: int):
    time.sleep(3)
    logger.info(f"Email sent to {email} for task {task_id}")


async def send_background_email(background_tasks: BackgroundTasks, email: str):
    background_tasks.add_task(write_notification, email, message="Some notification")
