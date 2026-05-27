from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time
app=FastAPI()
def stream():
    for i in range(1,6):
        yield f"data {i}\n"
        time.sleep(2)

@app.get("/")
async def data():
    return StreamingResponse(stream())
