from fastapi import Request
import time

async def log_middleware(request: Request, call_next):

    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    print(f"""
    METHOD : {request.method}
    URL    : {request.url}
    TIME   : {process_time}
    """)

    return response