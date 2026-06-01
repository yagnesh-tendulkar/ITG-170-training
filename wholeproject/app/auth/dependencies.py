from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

SECRET_KEY = "mysecretkey123"
ALGORITHM = "HS256"
#oauth2 password barrier --->it expects a tokenb in the request header 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")

#reads token from the request and it depends into the function 
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(            #decoding the jwt 
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email: str = payload.get("sub")    #search for the user email 

        if email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,    #raises exception 
                detail="Invalid token"
            )

        return email    # if founds return the email

    except JWTError:
        raise HTTPException(               # we can handle  jwt exception 
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )