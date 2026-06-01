from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import BigInteger

from database.base import Base


class UploadedFile(Base):

    __tablename__ = "uploaded_files"

    id = Column(
        Integer,
        primary_key=True
    )

    file_name = Column(
        String(255)
    )

    file_path = Column(
        String(500)
    )

    user_id = Column(
        BigInteger,
        ForeignKey("users.id"),
        nullable=False
    )