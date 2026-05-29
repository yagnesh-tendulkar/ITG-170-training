#what is middle ware,implement a custom middleware to lock request timestamp
from fastapi import FastAPI,Request
import time
mdl=FastAPI()
@mdl.middleware("http")
async def add_timestamp(request:Request,call_next):
    request.state.timestamp=time.time()
    response=await call_next(request)
    return response
@mdl.get("/timestamp")
def get_timestamp(request:Request):
    return {"timestamp": request.state.timestamp}
