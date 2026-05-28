from sqlmodel import SQLModel,Field,create_engine,Session,select
#creation of sqlmodel class
class Hero(SQLModel,table=True):
    id :int |None = Field(default=None,primary_key=True)
    name:str
    secret_name:str
    age:int

#creation of rows
hero1=Hero(name="Deadpond",secret_name="Diver",age=30)
hero2=Hero(name="Spider-Boy",secret_name="Miles Morales",age=16)
hero3=Hero(name="Kevin",secret_name="Kevineleven",age=45)

#writing into database
engine=create_engine("sqlite:///databse.db")
SQLModel.metadata.create_all(engine)
with Session(engine) as session:
    session.add(hero1)
    session.add(hero2)
    session.add(hero3)
    session.commit()

#reading from database
    statement=select(Hero).where(Hero.name=="Deadpond")
    hero=session.exec(statement).first()
    print(hero)
    print( " ------------------")
    s1=select(Hero).where(Hero.age>20)
    res=session.exec(s1).all()
    for i in res:
        print(i.name,i.secret_name,i.age)
    print(" ")

