from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import time

router = APIRouter(
    prefix="/logs",
    tags=["Logs"]
)


def generate_logs():

    logs = [
        "HR Login Successful",
        "JWT Token Generated",
        "Token Verification Started",
        "Token Verified",
        "Employee Creation Started",
        "Employee Data Validated",
        "Employee Saved Successfully",
        "Request Logged",
        "Response Generated",
        "Process Completed"
    ]

    for log in logs:
        yield f"{log}\n"
        time.sleep(1)


@router.get("/stream")
def stream_logs():

    return StreamingResponse(
        generate_logs(),
        media_type="text/plain"
    )