from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate,UserUpdate

def create_user(db:Session, user:UserCreate):
    new_user = User(
    name = user.name,
    email =user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db:Session):
    return db.query(User).all()
def get_user_by_id(db:Session,user_id:int):
    return db.query(User).filter(User.id == user_id).first()


def update_user(db:Session, user_id:int,user:UserUpdate):
    existing_user = db.query(User).filter(User.id == user_id).first()
    if not existing_user:
        return None
    if user.name is not None:
        existing_user.name = user.name
    if user.email is not None:
        existing_user.email = user.email
    if user.is_active is not None:
        existing_user.is_active = user.is_active
    db.commit()
    db.refresh(existing_user)
    return existing_user
def delete_user(db:Session,user_id:int):
    existing_user =db.query(User).filter(User.id == user_id).first()
    if not existing_user:
        return None
    db.delete(existing_user)
    db.commit()
    return {"mesage":"user deleted successfully"}


