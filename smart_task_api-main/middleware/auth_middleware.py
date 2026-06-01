from fastapi.responses import JSONResponse

async def auth_middleware(
    request,
    call_next
):

    token = request.headers.get(
        "Authorization"
    )

    if not token:
        return JSONResponse(
            status_code=401,
            content={
                "message":"Unauthorized"
            }
        )

    response = await call_next(request)

    return response