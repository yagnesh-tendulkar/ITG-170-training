from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.core.database import Base
from app.core.database import engine

Base.metadata.create_all(bind=engine)

class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String(100),
        unique=True,
        nullable=False
    )

    email = Column(
        String(255),
        unique=True,
        nullable=False
    )

    password = Column(
        String(500),
        nullable=False
    )

    tasks = relationship(
        "Task",
        back_populates="owner",
        cascade="all, delete"
    )

    files = relationship(
        "File",
        back_populates="owner",
        cascade="all, delete"
    )