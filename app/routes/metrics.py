from fastapi import APIRouter

router = APIRouter(
    tags=["Metrics"]
)


@router.get("/metrics")
def metrics():
    return {
        "requests": 100,
        "status": "ok"
    }