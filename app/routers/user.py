from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import schemas, crud
from ..dependencies import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=schemas.UserResponse)
def create(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@router.get("/{user_id}", response_model=schemas.UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)


@router.get("/", response_model=list[schemas.UserResponse])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_users(db, skip, limit)


@router.put("/{user_id}", response_model=schemas.UserResponse)
def update(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    return crud.update_user(db, user_id, user)


@router.delete("/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)