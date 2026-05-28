from fastapi import Request

async def log_requests(request : Request, call_next):
    print(request.url)
    print(request.method)
    response = await call_next(request)

    return response

