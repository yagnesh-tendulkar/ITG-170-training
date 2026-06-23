# ─────────────────────────────────────────────
# schemas.py
#
# LEARNING NOTE:
# Pydantic "schemas" define the shape of data coming IN (requests)
# and going OUT (responses) of our API. They are different from
# SQLAlchemy models — models describe the DB, schemas describe the API.
#
# FastAPI uses schemas to:
#   1. Automatically validate incoming request data
#   2. Serialize (convert) Python objects to JSON for responses
#   3. Generate automatic API documentation at /docs
# ─────────────────────────────────────────────

from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, List


# ── Auth Schemas ────────────────────────────────────────────────

class UserRegister(BaseModel):
    """Data required to register a new user"""
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr                        # EmailStr validates it looks like an email
    password: str = Field(..., min_length=6)


class UserLogin(BaseModel):
    """Data required to log in"""
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    """What we return when someone asks about a user (never include the password!)"""
    id: int
    username: str
    email: str
    is_active: bool
    created_at: datetime

    # This tells Pydantic to read from SQLAlchemy model attributes (not just dicts)
    model_config = {"from_attributes": True}


class TokenResponse(BaseModel):
    """The JWT token returned after successful login"""
    access_token: str
    token_type: str = "bearer"
    user: UserResponse


# ── Review Schemas ────────────────────────────────────────────────

class ReviewCreate(BaseModel):
    """Data sent when requesting a new code review"""
    title: str = Field(..., min_length=1, max_length=200)
    language: str = Field(..., description="e.g. Python, JavaScript, Java")
    code_snippet: str = Field(..., min_length=10, description="The code to review")


class BugItem(BaseModel):
    """A single bug found by AI"""
    description: str
    line_hint: Optional[str] = None
    severity: str = "medium"  # low | medium | high


class OptimizationItem(BaseModel):
    """A single optimization suggestion from AI"""
    description: str
    impact: str = "medium"  # low | medium | high


class BestPracticeItem(BaseModel):
    """A single best practice suggestion from AI"""
    description: str
    category: str = "general"


class ReviewResponse(BaseModel):
    """Full review result returned to the frontend"""
    id: int
    title: str
    language: str
    code_snippet: str
    bugs: List[BugItem]
    optimizations: List[OptimizationItem]
    best_practices: List[BestPracticeItem]
    summary: str
    overall_score: float
    created_at: datetime

    model_config = {"from_attributes": True}


class ReviewSummary(BaseModel):
    """Lightweight review info for listing in history (no full code)"""
    id: int
    title: str
    language: str
    overall_score: float
    bug_count: int
    created_at: datetime

    model_config = {"from_attributes": True}


# ── Docs Generator Schemas ────────────────────────────────────────────────

class DocsRequest(BaseModel):
    """Request to generate documentation for code"""
    code: str = Field(..., min_length=10)
    language: str = Field(..., description="e.g. Python, JavaScript")
    doc_style: str = Field(default="google", description="google | numpy | jsdoc")


class DocsResponse(BaseModel):
    """Generated documentation"""
    original_code: str
    documented_code: str
    explanation: str


# ── Dashboard Stats ────────────────────────────────────────────────

class DashboardStats(BaseModel):
    """Statistics shown on the dashboard"""
    total_reviews: int
    average_score: float
    most_used_language: Optional[str]
    total_bugs_found: int
    recent_reviews: List[ReviewSummary]
