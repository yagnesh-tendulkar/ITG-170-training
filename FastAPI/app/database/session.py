from sqlalchemy.orm import sessionmaker
from app.database.database import engine


sessionfactory = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db():
    db = sessionfactory()
    try:
        yield db
    finally:
        db.close()