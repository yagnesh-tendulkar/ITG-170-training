from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from auth.jwt_handler import verify_token

bearer_scheme = HTTPBearer(auto_error=False)


def verify_auth(
    credentials: HTTPAuthorizationCredentials | None = Security(bearer_scheme),
):
    if credentials and credentials.scheme.lower() == "bearer":
        return verify_token(credentials.credentials)

    raise HTTPException(status_code=401, detail="Authentication required")
