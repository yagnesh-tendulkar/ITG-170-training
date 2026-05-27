# app/main.py
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.exceptions import RideSharingException
from app.schemas.error_schema import APIErrorResponse
from app.api.v1.rides import router as rides_router

app = FastAPI(
    title="Production Ride-Sharing Dispatch Core Engine",
    version="2.0.0"
)

# Central Global Interceptor Exception Handler
@app.exception_handler(RideSharingException)
async def core_ride_exception_handler(request: Request, exc: RideSharingException):
    """
    Catches RideSharingException globally and forces the output 
    to exactly match our custom error response blueprint class.
    """
    error_instance = APIErrorResponse(
        status_code=exc.status_code,
        error_summary=exc.error_summary,
        detail=exc.detail
    )
    
    return JSONResponse(
        status_code=exc.status_code,
        content=error_instance.model_dump()
    )

# Include the routes
app.include_router(rides_router, prefix="/rides", tags=["Ride Operations Management"])

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)