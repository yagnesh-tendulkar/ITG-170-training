from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from ..database.db import get_session
from ..models.user_model import User
from ..schemas.user_schema import UserCreate

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# CREATE USER
@router.post("/")
def create_user(
    user: UserCreate,
    session: Session = Depends(get_session)
):

    db_user = User(**user.model_dump())

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user

# GET USERS
@router.get("/")
def get_users(
    session: Session = Depends(get_session)
):

    users = session.exec(select(User)).all()

    return users