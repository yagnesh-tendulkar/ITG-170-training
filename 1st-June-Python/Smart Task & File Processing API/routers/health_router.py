from fastapi import APIRouter

from sqlalchemy import text

from database.session import SessionLocal

router = APIRouter(
    prefix="/api/health",
    tags=["Health"]
)


@router.get("/")
def health():

    return {
        "status": "UP",
        "service": "Smart Task API"
    }


@router.get("/db")
def db_health():

    try:

        db = SessionLocal()

        db.execute(
            text("SELECT 1")
        )

        return {
            "database": "UP"
        }

    except Exception:

        return {
            "database": "DOWN"
        }

    finally:

        db.close()