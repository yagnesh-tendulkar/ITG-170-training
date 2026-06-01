import time


def process_file(file_id: int):

    print(f"[BG] Starting processing for file {file_id}")

    time.sleep(3)  # simulate heavy work

    print(f"[BG] File {file_id} processed successfully")


def process_task(task_id: int):

    print(f"[BG] Processing task {task_id}")

    time.sleep(5)

    print(f"[BG] Task {task_id} completed")


def send_email(email: str):

    print(f"[BG] Sending email to {email}")

    time.sleep(2)

    print(f"[BG] Email sent successfully")