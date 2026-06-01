import time
from logging_config import get_logger

logger = get_logger("background_tasks")


def send_task_created_email(user_email: str, task_title: str) -> None:
    """Simulate sending a task-created notification email."""
    logger.info(f"Sending email to {user_email} about task: '{task_title}'")
    time.sleep(1)  # Simulate I/O delay
    logger.info(f"Email sent successfully to {user_email}")


def send_task_completed_email(user_email: str, task_title: str) -> None:
    """Simulate sending a task-completed notification email."""
    logger.info(f"Sending completion email to {user_email} for task: '{task_title}'")
    time.sleep(1)
    logger.info(f"Completion email sent to {user_email}")
