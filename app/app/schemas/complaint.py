from pydantic import BaseModel

class ComplaintCreate(BaseModel):
    title: str
    description: str
    priority: str

class ComplaintUpdate(BaseModel):
    title: str
    description: str
    status: str
    priority: str