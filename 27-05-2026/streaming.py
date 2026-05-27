from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import asyncio
app = FastAPI()


@app.post("/")
async def read_root():
    return {"Hello": "hi"}

#function to generate nos from 1 to 10
@app.get("/stream")
async def stream_numbers(request: Request):
    async def number_generator():

        for i in range(1, 10):
            yield f"data: {i}\n\n"
            await asyncio.sleep(1)

    return StreamingResponse(
        number_generator(),
        media_type="text/event-stream"
    )