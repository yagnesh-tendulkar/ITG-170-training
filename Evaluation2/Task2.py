from fastapi import FastAPI, Request
import time

app = FastAPI()
@app.middleware("http")
async def log_time(request: Request, call_next):
    start_time = time.time()
    print(f"Request Method: {request.method}")
    print(f"Request URL: {request.url}")
    response = await call_next(request)
    process_time = time.time() - start_time
    print("response sent")
    print(f"Response Time: {process_time}")
    return response