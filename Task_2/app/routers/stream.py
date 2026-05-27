from fastapi import APIRouter, File, UploadFile
from fastapi.responses import StreamingResponse

router = APIRouter()


@router.post("/stream")
async def generate_file(file: UploadFile = File(...)):

    def read():
        while True:
            line = file.file.readline()

            if not line:
                break

            yield line

    return StreamingResponse(read(), media_type="text/plain")