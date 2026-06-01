from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.core.security import create_access_token

from app.models.user import User


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
):

    payload = create_access_token(token)

    if payload is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    user_id = payload.get("sub")

    user = db.query(User).filter(
        User.id == int(user_id)
    ).first()

    if not user:

        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user