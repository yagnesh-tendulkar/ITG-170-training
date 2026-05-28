from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, Field, EmailStr
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi.middleware.cors import CORSMiddleware

# DATABASE CONFIG
allow_origins=[
    "http://localhost:3000",
    "https://yourfrontend.com"
]
DATABASE_URL = "mysql+pymysql://root:M1racle%40123@localhost/fastapi_db"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


# DB MODEL

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    age = Column(Integer)
    email = Column(String(100), unique=True)

Base.metadata.create_all(bind=engine)


# Pydantic Schemas

class UserCreate(BaseModel):
    name: str = Field(..., min_length=3)
    age: int = Field(..., gt=17, lt=100)
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


app = FastAPI(title="Production Ready CRUD API")

app = FastAPI(title="Production Ready CRUD API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ for testing only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = UserDB(**user.dict())
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
    user = db.query(UserDB).filter(UserDB.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user_update.name is not None:
        user.name = user_update.name

    if user_update.age is not None:
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

    return {"message": "User deleted successfully"}