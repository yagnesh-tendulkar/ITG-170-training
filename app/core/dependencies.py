from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.core.security import verify_token

from app.models.user import User


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
):

    payload = verify_token(token)

    if not payload:

        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    user = db.query(User).filter(
        User.id == payload["user_id"]
    ).first()

    if not user:

        raise HTTPException(
            status_code=401,
            detail="User Not Found"
        )

    return user