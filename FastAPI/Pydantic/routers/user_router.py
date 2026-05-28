from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from sqlalchemy.orm import Session

from Pydantic.database.session import get_db

from Pydantic.models.user import User

from Pydantic.schemas.user import (
    UserCreate,
    UserUpdate,
    UserResponse,
    UserPathParams,
    UserQueryParams
)

from Pydantic.services.user_service import (
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


# -----------------------------------------
# CREATE USER
# -----------------------------------------

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


# -----------------------------------------
# GET USER BY ID
# -----------------------------------------

@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user_by_id(
    params: UserPathParams = Depends(),
    db: Session = Depends(get_db)
):

    user = get_user(
        db=db,
        user_id=params.user_id
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


# -----------------------------------------
# GET ALL USERS
# -----------------------------------------

@router.get(
    "/",
    response_model=list[UserResponse]
)
def get_users(
    query: UserQueryParams = Depends(),
    db: Session = Depends(get_db)
):

    users = get_all_users(
        db=db,
        skip=query.skip,
        limit=query.limit
    )

    return users


# -----------------------------------------
# UPDATE USER
# -----------------------------------------

@router.put(
    "/{user_id}",
    response_model=UserResponse
)
def update_existing_user(
    params: UserPathParams = Depends(),
    payload: UserUpdate = ...,
    db: Session = Depends(get_db)
):

    user = update_user(
        db=db,
        user_id=params.user_id,
        user_data=payload
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


# -----------------------------------------
# DELETE USER
# -----------------------------------------

@router.delete(
    "/{user_id}",
    status_code=status.HTTP_200_OK
)
def delete_existing_user(
    params: UserPathParams = Depends(),
    db: Session = Depends(get_db)
):

    user = delete_user(
        db=db,
        user_id=params.user_id
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "User deleted successfully"
    }