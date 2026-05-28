# from fastapi import FastAPI
# from sqlalchemy import create_engine, text
#
# app = FastAPI()
#
# DATABASE_URL = "mysql+pymysql://root:M1racle%40123@localhost/fastapi_db"
#
# engine = create_engine(DATABASE_URL)
#
#
# @app.get("/")
# def test_db():
#     try:
#         with engine.connect() as connection:
#             result = connection.execute(text("SELECT 1"))
#             return {"message": "DB Connected ✅"}
#     except Exception as e:
#         return {"error": str(e)}

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, Field, EmailStr, field_validator
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy.exc import SQLAlchemyError
from passlib.context import CryptContext
import re

#
DATABASE_URL = "mysql+pymysql://root:M1racle%40123@localhost/fastapi_db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# PASSWORD HASHING
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)


class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    age = Column(Integer)
    email = Column(String(100), unique=True)
    password = Column(String(255))  # hashed password

Base.metadata.create_all(bind=engine)

class UserCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    age: int = Field(..., ge=18, le=60)
    email: EmailStr
    password: str = Field(..., min_length=8)

    @field_validator("name")
    def validate_name(cls, v):
        if not re.match("^[A-Za-z ]+$", v):
            raise ValueError("Name must contain only letters")
        return v

class UserUpdate(BaseModel):
    name: str | None = Field(None, min_length=3)
    age: int | None = Field(None, ge=18, le=60)

class UserResponse(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr

    class Config:
        from_attributes = True

 get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user_or_404(user_id: int, db: Session):
    user = db.query(UserDB).filter(UserDB.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


app = FastAPI(title="Production Ready CRUD API")


@app.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        # Check duplicate email
        existing = db.query(UserDB).filter(UserDB.email == user.email).first()
        if existing:
            raise HTTPException(status_code=400, detail="Email already registered")

        db_user = UserDB(
            name=user.name,
            age=user.age,
            email=user.email,
            password=hash_password(user.password)
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")


@app.get("/users/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(UserDB).all()


@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return get_user_or_404(user_id, db)


@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    try:
        user = get_user_or_404(user_id, db)

        if user_update.name is not None:
            user.name = user_update.name

        if user_update.age is not None:
            user.age = user_update.age

        db.commit()
        db.refresh(user)
        return user

    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        user = get_user_or_404(user_id, db)

        db.delete(user)
        db.commit()

        return {"message": "User deleted successfully"}

    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")