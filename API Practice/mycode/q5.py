#implement a get api with stream response
import asyncio
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
strm=FastAPI()
async def fake_video_streamer():
    for i in range(10):
        # Yield data chunks as bytes or strings
        yield f"Chunk {i}\n"
        await asyncio.sleep(0.5)  # Simulate data generation delay
@strm.get("/stream")
async def main():
    return StreamingResponse(fake_video_streamer(), media_type="text/plain")