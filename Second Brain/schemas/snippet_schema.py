from pydantic import BaseModel


class Snippet(BaseModel):
    id: int
    title: str
    language: str
    code: str