from pydantic import BaseModel

class EvaluationResponse(BaseModel):
    score: int
    technical_score: int
    communication_score: int
    feedback: str
    strengths: list[str]
    weaknesses: list[str]
    suggestions: list[str]
    next_question: str
