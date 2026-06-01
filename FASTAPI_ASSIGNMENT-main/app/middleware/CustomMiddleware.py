from fastapi import Request
from datetime import datetime


async def log_requests(
    request: Request,
    call_next
):

    response = await call_next(request)

    with open("request_logs.txt", "a") as file:

        file.write(
            f"{datetime.now()} | "
            f"{request.method} | "
            f"{request.url.path} | "
            f"{response.status_code}\n"
        )

    return response