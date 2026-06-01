from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from DBConnection import get_db, Base


class UserSchema(BaseModel):
    id:int
    name:str
    age:int

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)


app = FastAPI()

@app.get("/user")
def get_users(db:Session= Depends(get_db)):
    users= db.query(User).all()
    return users

@app.get("/user/{id}")
def get_user(id: int, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post('/user')
def create_user(User: UserSchema, db:Session = Depends(get_db)):
    db.add(User)
    db.commit()
    db.refresh(User)
    return User

@app.put("/user/{id}")
def update_user(id: int, User: UserSchema, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).update(User)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.commit()
    db.refresh(User)
    return User

@app.delete("/user/{id}")
def delete_user(id: int, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted"}

