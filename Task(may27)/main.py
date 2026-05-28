from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Sample Database Model
class UserDB(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)

Base.metadata.create_all(bind=engine)

# Sample Pydantic Schemas
class UserCreate(BaseModel):
    email: EmailStr
    name: str

# FastAPI App Instance
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class AppError(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message

class ErrorCodes:
    USER_NOT_FOUND = (404, "User not found")
    EMAIL_EXISTS = (400, "Email already exists")
    DB_ERROR = (500, "Database error")



@app.exception_handler(AppError)
async def app_error_handler(request: Request, exc: AppError):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": exc.message
        }
    )


@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.id == user_id).first()

    if not user:
        # Unpacking tuples works perfectly here
        raise AppError(*ErrorCodes.USER_NOT_FOUND)

    return user


@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    existing = db.query(UserDB).filter(UserDB.email == user.email).first()
    if existing:
        raise AppError(*ErrorCodes.EMAIL_EXISTS)


    try:
        db_user = UserDB(**user.model_dump())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except SQLAlchemyError:
        db.rollback()
        raise AppError(*ErrorCodes.DB_ERROR)