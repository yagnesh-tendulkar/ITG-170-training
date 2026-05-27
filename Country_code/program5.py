# ?implement get api and stream the response (use generators)
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
app = FastAPI()
def Gene():
    for i in range(1,8):
        yield f"{i *2}\n"
@app.get("/users")
def read_items():
    return StreamingResponse(Gene(),media_type="text/plain")