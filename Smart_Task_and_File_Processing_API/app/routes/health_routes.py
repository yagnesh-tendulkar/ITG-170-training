import os
import platform
from datetime import datetime

from fastapi import APIRouter


router = APIRouter(
    prefix="",
    tags=["Health & Metrics"]
)


APPLICATION_START_TIME = datetime.utcnow()


@router.get("/health")
def health_check():
    """
    Basic health check endpoint.
    """

    return {
        "success": True,
        "status": "healthy",
        "service": "Smart Task API",
        "timestamp": datetime.utcnow()
    }


@router.get("/metrics")
def get_metrics():
    """
    Application metrics endpoint.
    """

    uptime = (
        datetime.utcnow() -
        APPLICATION_START_TIME
    ).total_seconds()

    return {
        "success": True,
        "metrics": {
            "uptime_seconds": uptime,
            "python_version": platform.python_version(),
            "platform": platform.system(),
            "cpu_count": os.cpu_count()
        }
    }


@router.get("/readiness")
def readiness_check():
    """
    Readiness probe.
    """

    return {
        "success": True,
        "ready": True,
        "message": "Application is ready to accept requests"
    }


@router.get("/liveness")
def liveness_check():
    """
    Liveness probe.
    """

    return {
        "success": True,
        "alive": True,
        "message": "Application is running"
    }