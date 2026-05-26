from sqlalchemy.orm import Session
from model import User
import schemas


# CREATE USER
def create_user(db: Session, user: schemas.UserCreate):
    new_user = User(
        first_name=user.first_name,
        last_name=user.last_name
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# GET USER
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


# GET ALL USERS
def get_users(db: Session):
    return db.query(User).all()


# DELETE USER
def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user