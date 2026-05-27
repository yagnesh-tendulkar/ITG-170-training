from fastapi import FastAPI , Request
import time
app = FastAPI()
@app.middleware("http")
async def middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    return response
@app.get("/")
async def home():
        return{"message" : "This is my custom middleware"}