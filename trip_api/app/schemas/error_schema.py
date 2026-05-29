# app/schemas/error_schema.py
from pydantic import BaseModel, Field

class APIErrorResponse(BaseModel):
    """
    Unified error communication layout returned to the client 
    whenever a processing rule fails.
    """
    status_code: int = Field(..., description="The matching HTTP status code")
    error_summary: str = Field(..., description="A short, high-level summary of the issue")
    detail: str = Field(..., description="Deep specific detail about why it failed")