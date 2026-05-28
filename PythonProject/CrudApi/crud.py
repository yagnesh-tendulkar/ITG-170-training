

from fastapi import FastAPI, Request, Depends,HTTPException

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


from   pydanticmodel import User,UpdateUser,PatchUser
from sqlalchemy.exc import SQLAlchemyError
from fastapi.middleware.cors import CORSMiddleware



app=FastAPI(title="User CRUD Operations.")
origins = [
        "http://localhost",
        "http://localhost:3000",
    ]

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


DATABASE_URL = "mysql+pymysql://root:M1racle%40123@localhost/fastapi"
engine=create_engine(DATABASE_URL,pool_size=10,max_overflow=20)
Session=sessionmaker(bind=engine,autoflush=False,autocommit=False)
def get_db():
    db=Session()
    try:
        yield db
    finally:
        db.close()


@app.post("/create",status_code=201)
def create_user(user: User, db: Session = Depends(get_db)):
    query = text("""
        INSERT INTO user (name, age, email)
        VALUES (:name, :age, :email)
    """)
    try:
        db.execute(query, user.model_dump())
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500,detail=str(e))
    return{"message":"data inserted sucessfully"}



@app.get("/users",)
def get_users(db: Session = Depends(get_db)):
   query = text("SELECT * FROM user")

   try:
       result = db.execute(query)
       rows = result.fetchall()
       if not rows:
           raise HTTPException(status_code=404, detail="users not found")
   except HTTPException as e:
       print(e.args)
       raise
   except SQLAlchemyError as e:
       raise HTTPException(status_code=500,detail=str(e))
   return [dict(row._mapping) for row in rows]


@app.put("/update/{email}")
def update_user(user:UpdateUser,email:str, db: Session = Depends(get_db)):
    query = text("""
        UPDATE user
        SET name = :name, age = :age
        WHERE email = :email
    """)
    try:
      result=db.execute(query,{"name":user.name,"age":user.age,"email":email})
      if result.rowcount==0:
          raise HTTPException(status_code=404,detail="user is not updated")
      db.commit()
    except  HTTPException as e:
       print(e.args)
       raise
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500,detail=str(e))
    return {"message": "user updated sucessfully"}

@app.delete("/user/{email}")
def delete_user(email: str, db: Session = Depends(get_db)):
    query = text("DELETE FROM user WHERE email = :email")

    try:
        result= db.execute(query, {"email": email})

        if result.rowcount==0:
            raise HTTPException(status_code=404,detail="user not found")
        db.commit()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500,detail=str(e))


    return {"message": "Deleted"}


@app.patch("/user/{email}")
def patch_user(email: str, user: PatchUser, db: Session = Depends(get_db)):
    update_fields = []
    values = {"email": email}

    if user.name is not None:
        update_fields.append("name = :name")
        values["name"] = user.name

    if user.age is not None:
        update_fields.append("age = :age")
        values["age"] = user.age

    if not update_fields:
        raise HTTPException(
            status_code=400,
            detail="No fields provided for update"
        )

    query = text(f"""
        UPDATE user
        SET {", ".join(update_fields)}
        WHERE email = :email
    """)

    try:
        result = db.execute(query, values)

        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found")

        db.commit()

        return {
            "message": "User partially updated successfully"
        }

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

