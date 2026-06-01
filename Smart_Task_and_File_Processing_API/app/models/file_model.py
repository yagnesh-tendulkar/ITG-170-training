from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    BigInteger,
    ForeignKey
)

from sqlalchemy.orm import relationship

from core.database import Base


class File(Base):

    __tablename__ = "files"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    original_filename = Column(
        String(255),
        nullable=False
    )

    stored_filename = Column(
        String(255),
        nullable=False,
        unique=True
    )

    file_path = Column(
        String(500),
        nullable=False
    )

    content_type = Column(
        String(100),
        nullable=False
    )

    file_size = Column(
        BigInteger,
        nullable=False
    )

    upload_status = Column(
        String(20),
        nullable=False,
        default="uploaded"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    user = relationship(
        "User",
        backref="files"
    )