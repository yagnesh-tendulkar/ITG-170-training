from app.database.connection import engine, Base
from app.models.user import User
from app.models.task import Task


def init_db():
    Base.metadata.create_all(bind=engine)