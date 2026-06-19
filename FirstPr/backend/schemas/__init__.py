from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, EmailStr
from backend.schemas.ai_schema import EvaluationResponse


class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True


class TokenRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class EvaluateRequest(BaseModel):
    role: str
    question: str
    response: str
    question_type: Optional[str] = "Technical"
    duration_seconds: Optional[int] = None
    session_id: Optional[str] = None


class InterviewSessionCreate(BaseModel):
    role: str
    question_type: Optional[str] = "Technical"
    difficulty: Optional[str] = "Medium"
    experience_level: Optional[str] = "Mid"
    duration_minutes: Optional[int] = 30


class InterviewResponseCreate(BaseModel):
    question: str
    response: str
    question_type: Optional[str] = "Technical"
    duration_seconds: Optional[int] = None


class InterviewResponseRead(BaseModel):
    id: int
    question: str
    response: str
    question_type: str
    duration_seconds: Optional[int] = None
    technical_score: int
    communication_score: int
    confidence_score: int
    clarity_score: int
    score: int
    feedback: str
    created_at: datetime

    class Config:
        orm_mode = True


class PersonalizedFeedbackRead(BaseModel):
    summary: str
    strong_areas: str
    weak_areas: str
    communication_review: str
    technical_review: str
    recommended_topics: str
    learning_roadmap: str
    readiness_percentage: int
    generated_at: datetime

    class Config:
        orm_mode = True


class InterviewSessionRead(BaseModel):
    session_id: str
    role: str
    interview_type: str
    difficulty: str
    experience_level: str
    duration_seconds: Optional[int]
    started_at: datetime
    ended_at: Optional[datetime]
    total_score: Optional[int]
    total_technical_score: Optional[int]
    total_communication_score: Optional[int]
    status: str
    responses: List[InterviewResponseRead] = []
    feedback_report: Optional[PersonalizedFeedbackRead] = None

    class Config:
        orm_mode = True


class DashboardPoint(BaseModel):
    label: str
    average_score: float
    average_technical_score: float
    average_communication_score: float
    sessions: int


class DashboardResponse(BaseModel):
    total_sessions: int
    total_questions: int
    average_score: float
    best_score: float
    improvement_percentage: float
    average_technical_score: float
    average_communication_score: float
    weekly_progress: List[DashboardPoint]
    monthly_progress: List[DashboardPoint]


class ProgressResponse(BaseModel):
    weekly: List[DashboardPoint]
    monthly: List[DashboardPoint]


class ReportRequest(BaseModel):
    candidate_name: str
    role: str
    question: str
    response: str
    technical_score: int
    communication_score: int
    feedback: str
    suggestions: List[str]


class EvaluateResponse(EvaluationResponse):
    confidence_score: int = 0
    clarity_score: int = 0
    details: List[str] = []


class ResponseRecordRead(BaseModel):
    id: int
    role: str
    question_type: str
    question: str
    response: str
    feedback: str
    score: int
    technical_score: int
    communication_score: int
    confidence_score: int
    clarity_score: int
    duration_seconds: Optional[int] = None
    created_at: datetime

    class Config:
        orm_mode = True


class AnalyticsResponse(BaseModel):
    total_responses: int
    avg_score: float
    avg_technical_score: float
    avg_communication_score: float
    recent_trend: List[Dict[str, Any]]
    role_breakdown: Dict[str, int]


class QuestionListResponse(BaseModel):
    role: str
    questions: List[str]
