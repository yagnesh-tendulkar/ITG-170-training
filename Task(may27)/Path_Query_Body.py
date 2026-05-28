from fastapi import FastAPI, Depends, HTTPException, Query
from pydantic import BaseModel, Field, EmailStr
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session


DATABASE_URL = "mysql+pymysql://root:M1racle%40123@localhost/fastapi_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    age = Column(Integer)
    email = Column(String(100), unique=True)

Base.metadata.create_all(bind=engine)


class UserCreate(BaseModel):
    name: str = Field(..., min_length=3)
    age: int = Field(..., ge=18, le=60)
    email: EmailStr

class UserUpdate(BaseModel):
    name: str | None = None
    age: int | None = None

class UserResponse(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr

    class Config:
        from_attributes = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI(title="CRUD with Path, Query, Body Separation")

@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = UserDB(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/", response_model=list[UserResponse])
def get_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(5, le=20),
    db: Session = Depends(get_db)
):
    return db.query(UserDB).offset(skip).limit(limit).all()

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,  # PATH
    user_update: UserUpdate,  # BODY
    db: Session = Depends(get_db)
):
    user = db.query(UserDB).filter(UserDB.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user_update.name:
        user.name = user_update.name

    if user_update.age:
        user.age = user_update.age

    db.commit()
    db.refresh(user)
    return user


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": "User deleted"}