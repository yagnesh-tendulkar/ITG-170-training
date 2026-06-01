from fastapi import Request
import time

async def log_requests(request: Request, call_next):
    start_time = time.time()
    print(f"{request.method} {request.url}")
    response = await call_next(request)
    end = time.time()
    print(f"Time Taken: {end - start_time}")
    return response