from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.user import (
    UserCreate,
    Update,
    UserResponse
)

from app.services.user_service import (
    create_user,
    get_user,
    get_all_users,
    update_user,
    delete_user
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_user(
    payload: UserCreate,
    db: Session = Depends(get_db)
):

    user = create_user(
        db=db,
        user_data=payload
    )

    return user


@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user_by_id(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = get_user(
        db=db,
        user_id=user_id
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.get(
    "/",
    response_model=list[UserResponse]
)
def get_users(
    db: Session = Depends(get_db)
):

    return get_all_users(db=db)


@router.put(
    "/{user_id}",
    response_model=UserResponse
)
def update_existing_user(
    user_id: int,
    payload: Update,
    db: Session = Depends(get_db)
):

    user = update_user(
        db=db,
        user_id=user_id,
        user_data=payload
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_200_OK
)
def delete_existing_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = delete_user(
        db=db,
        user_id=user_id
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "User deleted successfully"
    }