from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from ..database.connection import get_database_session
from ..models.developer import DeveloperProfile
from ..services.developer_service import (
    create_developer,
    delete_developer,
    get_developer_by_id,
    get_developer_by_username,
    list_all_developers,
    update_developer,
)

router = APIRouter()


@router.post("/register", response_model=DeveloperProfile, status_code=status.HTTP_201_CREATED)
def register_developer(profile: DeveloperProfile, db: Session = Depends(get_database_session)):
    existing_user = get_developer_by_username(db, profile.username)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This username is already taken. Try another one!",
        )
    return create_developer(db, profile)


@router.get("/developers", response_model=list[DeveloperProfile])
def list_developers(db: Session = Depends(get_database_session)):
    return list_all_developers(db)


@router.patch("/developers/{developer_id}", response_model=DeveloperProfile)
def update_developer_profile(
    developer_id: int,
    updated_fields: dict,
    db: Session = Depends(get_database_session),
):
    db_profile = get_developer_by_id(db, developer_id)
    if not db_profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="We couldn't find a developer profile with that ID.",
        )
    return update_developer(db, db_profile, updated_fields)


@router.delete("/developers/{developer_id}", status_code=status.HTTP_200_OK)
def delete_developer_profile(developer_id: int, db: Session = Depends(get_database_session)):
    db_profile = get_developer_by_id(db, developer_id)
    if not db_profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Delete failed. No profile found with that specific ID.",
        )
    delete_developer(db, db_profile)
    return {"message": f"Profile for ID {developer_id} has been permanently deleted from the registry."}
