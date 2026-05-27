from datetime import time


from fastapi import FastAPI,Request
import time
app = FastAPI()
@app.middleware("http")
async def middleware(request: Request,call_next):
    start_time = time.time()
    response = await call_next(request)
    ptime=time.time()-start_time
    print(f"process_time:{ptime}")
    return response
@app.get("/middlewares")
def home():
    return {"hello":"middle working"}

