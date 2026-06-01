from datetime import datetime, timedelta  #used to set the expiration time 
from jose import jwt  #creates and decodes jwt tokens
from passlib.context import CryptContext # handles password hasing securely 

SECRET_KEY = "mysecretkey123"#secret password for signing tokens
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(
    schemes=["bcrypt"],   #password hashing we are using bycrpt algorithm 
    deprecated="auto"
)

# hash password
def hash_password(password: str):
    return pwd_context.hash(password)

# verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# create JWT token
def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )