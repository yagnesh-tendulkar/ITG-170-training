from sqlalchemy.orm import Session
from app.models.user import User

from app.schemas.user import UserCreate,Update,UserResponse

from app.utils.password import hash_password


def create_user(
    db: Session,
    user_data: UserCreate
):

    hashed_password = hash_password(
        user_data.password
    )

    new_user = User(
        full_name=user_data.full_name,
        email=user_data.email,
        password=hashed_password
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return new_user


def get_user(
    db: Session,
    user_id: int
):

    return db.query(User).filter(
        User.id == user_id
    ).first()


def get_all_users(db: Session):

    return db.query(User).all()


def update_user(
    db: Session,
    user_id: int,
    user_data: Update
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        return None

    user.full_name = user_data.full_name

    user.email = user_data.email

    db.commit()

    db.refresh(user)

    return user


def delete_user(
    db: Session,
    user_id: int
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        return None

    db.delete(user)

    db.commit()

    return user