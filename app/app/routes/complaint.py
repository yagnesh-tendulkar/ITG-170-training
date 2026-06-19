from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.complaint import Complaint
from app.schemas.complaint import ComplaintCreate, ComplaintUpdate

router = APIRouter()


# DATABASE CONNECTION
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE COMPLAINT
@router.post("/complaints")
def create_complaint(
    complaint: ComplaintCreate,
    db: Session = Depends(get_db)
):

    new_complaint = Complaint(
        title=complaint.title,
        description=complaint.description,
        priority=complaint.priority
    )

    db.add(new_complaint)
    db.commit()
    db.refresh(new_complaint)

    return new_complaint


# GET ALL COMPLAINTS
@router.get("/complaints")
def get_complaints(
    db: Session = Depends(get_db)
):

    complaints = db.query(Complaint).all()

    return complaints


# GET SINGLE COMPLAINT
@router.get("/complaints/{complaint_id}")
def get_complaint(
    complaint_id: int,
    db: Session = Depends(get_db)
):

    complaint = db.query(Complaint).filter(
        Complaint.id == complaint_id
    ).first()

    if not complaint:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    return complaint


# UPDATE COMPLAINT
@router.put("/complaints/{complaint_id}")
def update_complaint(
    complaint_id: int,
    complaint: ComplaintUpdate,
    db: Session = Depends(get_db)
):

    db_complaint = db.query(Complaint).filter(
        Complaint.id == complaint_id
    ).first()

    if not db_complaint:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    db_complaint.title = complaint.title
    db_complaint.description = complaint.description
    db_complaint.status = complaint.status
    db_complaint.priority = complaint.priority

    db.commit()
    db.refresh(db_complaint)

    return db_complaint


# DELETE COMPLAINT
@router.delete("/complaints/{complaint_id}")
def delete_complaint(
    complaint_id: int,
    db: Session = Depends(get_db)
):

    complaint = db.query(Complaint).filter(
        Complaint.id == complaint_id
    ).first()

    if not complaint:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found"
        )

    db.delete(complaint)
    db.commit()

    return {
        "message": "Complaint deleted successfully"
    }