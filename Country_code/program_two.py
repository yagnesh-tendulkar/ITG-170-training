# what is middle ware and impleemtn a custom midle ware to og the request time stamp
import time
from fastapi import FastAPI,Request
from pydantic import BaseModel
app = FastAPI()
@app.middleware("http")
def request_timestamp(req:Request,call_next):
    st = time.time()
    print("the middleware started")
    response = call_next(req)
    end_time = time.time() - st
    response.headers['X-Process-Time'] = str(end_time)
    return response
@app.get("/")
def original_api_function():
    time.sleep(1)
    return {"msg" :"the original api endpoint is allowed by middleware"}



