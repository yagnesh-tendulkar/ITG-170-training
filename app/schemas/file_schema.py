from pydantic import BaseModel
from datetime import datetime


class FileResponse(BaseModel):

    id: int
    filename: str
    filepath: str
    uploaded_at: datetime
    user_id: int

    class Config:
        from_attributes = True