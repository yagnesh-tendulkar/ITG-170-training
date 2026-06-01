import os
import uuid

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


def generate_unique_filename(
        filename: str
):

    extension = filename.split(".")[-1]

    unique_name = (
        str(uuid.uuid4())
        + "."
        + extension
    )

    return unique_name