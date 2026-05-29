from typing import List
from sqlmodel import Session, select

from ..models.developer import DeveloperProfile


def get_developer_by_username(db: Session, username: str) -> DeveloperProfile | None:
    return db.exec(select(DeveloperProfile).where(DeveloperProfile.username == username)).first()


def get_developer_by_id(db: Session, developer_id: int) -> DeveloperProfile | None:
    return db.get(DeveloperProfile, developer_id)


def create_developer(db: Session, profile: DeveloperProfile) -> DeveloperProfile:
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile


def list_all_developers(db: Session) -> List[DeveloperProfile]:
    return db.exec(select(DeveloperProfile)).all()


def update_developer(db: Session, db_profile: DeveloperProfile, updated_fields: dict) -> DeveloperProfile:
    for key, value in updated_fields.items():
        if hasattr(db_profile, key):
            setattr(db_profile, key, value)

    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile


def delete_developer(db: Session, db_profile: DeveloperProfile) -> None:
    db.delete(db_profile)
    db.commit()
