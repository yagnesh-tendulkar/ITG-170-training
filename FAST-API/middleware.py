from fastapi import FastAPI, Request
import time
app = FastAPI()

@app.middleware("http")
async def log_request_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    end_time = time.time()
    process_time = end_time - start_time

    print(f"Time Taken: {process_time}")
    return response

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}