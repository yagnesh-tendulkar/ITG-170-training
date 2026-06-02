from pydantic import BaseModel


class FileResponse(BaseModel):
    id: int
    filename: str
    mime_type: str
    file_size: int

    model_config = {
        "from_attributes": True
    }