from typing import Dict

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database.connection import get_db

router = APIRouter(prefix="/health", tags=["health"])


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
)
def health_check() -> Dict[str, str]:
    """
    Basic health check endpoint to verify the application is running.

    Returns:
        dict: Status information with service name and health status.
    """
    return {
        "status": "healthy",
        "service": "employee-hr-api",
    }


@router.get(
    "/db",
    status_code=status.HTTP_200_OK,
)
def database_health_check(
    db: Session = Depends(get_db),
) -> Dict[str, str]:
    """
    Database health check endpoint to verify database connectivity.

    Args:
        db: SQLAlchemy session dependency for database operations.

    Returns:
        dict: Database connection status.

    Raises:
        HTTPException: 503 if database connection fails.
    """
    try:
        db.execute(text("SELECT 1"))
        return {
            "status": "healthy",
            "database": "connected",
        }
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database connection failed.",
        ) from exc
