from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time

app = FastAPI()

# Generator function
def number_stream():
    for i in range(1, 6):
        yield f"{i}\n"   # sends each number separately
        time.sleep(1)    # delay to simulate streaming

@app.get("/numbers")
def stream_numbers():
    return StreamingResponse(number_stream(), media_type="text/plain")