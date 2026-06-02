from sqlalchemy import Column, ForeignKey, Integer, String

from app.models import Base


class UploadedFile(Base):
    __tablename__ = "uploaded_files"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String, nullable=False)

    stored_filename = Column(String, nullable=False)

    mime_type = Column(String)

    file_size = Column(Integer)

    task_id = Column(Integer, ForeignKey("tasks.id"))