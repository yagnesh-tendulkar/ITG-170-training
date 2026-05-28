from sqlalchemy.orm import Session

from Pydantic.models.user import User

from Pydantic.schemas.user import (
    UserCreate,
    UserUpdate
)

from Pydantic.utils.password import (
    hash_password
)


# -----------------------------------------
# CREATE USER
# -----------------------------------------

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
        hashed_password=hashed_password
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return new_user


# -----------------------------------------
# GET USER BY ID
# -----------------------------------------

def get_user(
    db: Session,
    user_id: int
):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    return user


# -----------------------------------------
# GET ALL USERS
# -----------------------------------------

def get_all_users(
    db: Session,
    skip: int = 0,
    limit: int = 10
):

    users = db.query(User).offset(
        skip
    ).limit(
        limit
    ).all()

    return users


# -----------------------------------------
# UPDATE USER
# -----------------------------------------

def update_user(
    db: Session,
    user_id: int,
    user_data: UserUpdate
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


# -----------------------------------------
# DELETE USER
# -----------------------------------------

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