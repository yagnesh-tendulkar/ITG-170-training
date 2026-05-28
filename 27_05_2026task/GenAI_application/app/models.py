from pydantic import BaseModel, Field
class ChatRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=1,
        max_length=500
    )
    max_tokens: int = Field(
        default=50,
        gt=10,
        le=200
    )
