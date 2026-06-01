import time

def task_stream_generator(task_id: int):
    yield f"Task {task_id} processing started...\n"
    time.sleep(1)

    yield "Step 1: Fetching task data...\n"
    time.sleep(1)

    yield "Step 2: Validating task...\n"
    time.sleep(1)

    yield "Step 3: Running background analysis...\n"
    time.sleep(1)

    yield "Step 4: Finalizing task...\n"
    time.sleep(1)

    yield "Task completed successfully.\n"