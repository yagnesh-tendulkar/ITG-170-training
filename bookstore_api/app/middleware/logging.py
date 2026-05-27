# app/middleware/logging.py
import time
from fastapi import Request

async def add_process_time_header(request: Request, call_next):
    """
    Middleware that measures endpoint processing speed.
    Appends execution time metrics to response headers.
    """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = f"{process_time:.4f} seconds"
    return response