import os

from sqlalchemy.orm import Session

from app.models.uploaded_file import File

from app.exceptions.custom_exception import (
    ResourceNotFoundException,
    UnauthorizedAccessException
)


def save_file_record(
        db: Session,
        filename: str,
        filepath: str,
        user_id: int
):

    file_record = File(
        filename=filename,
        filepath=filepath,
        user_id=user_id
    )

    db.add(file_record)

    db.commit()

    db.refresh(file_record)

    return file_record


def get_user_files(
        db: Session,
        user_id: int
):

    return db.query(File).filter(
        File.user_id == user_id
    ).all()


def get_file_by_id(
        db: Session,
        file_id: int,
        user_id: int
):

    file_record = db.query(File).filter(
        File.id == file_id
    ).first()

    if not file_record:
        raise ResourceNotFoundException(
            "File Not Found"
        )

    if file_record.user_id != user_id:
        raise UnauthorizedAccessException(
            "Unauthorized Access"
        )

    return file_record


def delete_file_record(
        db: Session,
        file_id: int,
        user_id: int
):

    file_record = get_file_by_id(
        db,
        file_id,
        user_id
    )

    if os.path.exists(
            file_record.filepath
    ):
        os.remove(
            file_record.filepath
        )

    db.delete(file_record)

    db.commit()

    return True