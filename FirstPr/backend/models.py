import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from backend.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=False)
    email = Column(String(256), unique=True, index=True, nullable=False)
    hashed_password = Column(String(256), nullable=False)

    responses = relationship("ResponseRecord", back_populates="user")
    sessions = relationship("InterviewSession", back_populates="user")


class ResponseRecord(Base):
    __tablename__ = "responses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    session_id = Column(String(36), nullable=False, index=True, default=lambda: str(uuid.uuid4()))
    role = Column(String(128), nullable=False)
    question_type = Column(String(64), nullable=False, default="Technical")
    question = Column(String(512), nullable=False)
    response = Column(Text, nullable=False)
    feedback = Column(Text, nullable=False)
    score = Column(Integer, nullable=False, default=0)
    technical_score = Column(Integer, nullable=False, default=0)
    communication_score = Column(Integer, nullable=False, default=0)
    confidence_score = Column(Integer, nullable=False, default=0)
    clarity_score = Column(Integer, nullable=False, default=0)
    duration_seconds = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="responses")


class InterviewSession(Base):
    __tablename__ = "interview_sessions"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(36), unique=True, nullable=False, index=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    role = Column(String(128), nullable=False)
    interview_type = Column(String(64), nullable=False, default="Technical")
    difficulty = Column(String(64), nullable=False, default="Medium")
    experience_level = Column(String(64), nullable=False, default="Mid")
    duration_seconds = Column(Integer, nullable=True)
    started_at = Column(DateTime, default=datetime.utcnow)
    ended_at = Column(DateTime, nullable=True)
    total_score = Column(Integer, nullable=True)
    total_technical_score = Column(Integer, nullable=True)
    total_communication_score = Column(Integer, nullable=True)
    status = Column(String(32), nullable=False, default="in_progress")

    user = relationship("User", back_populates="sessions")
    responses = relationship("InterviewResponse", back_populates="session", cascade="all, delete-orphan")
    feedback_report = relationship("FeedbackReport", uselist=False, back_populates="session", cascade="all, delete-orphan")


class InterviewResponse(Base):
    __tablename__ = "interview_responses"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("interview_sessions.id"), nullable=False)
    question = Column(String(512), nullable=False)
    response = Column(Text, nullable=False)
    question_type = Column(String(64), nullable=False, default="Technical")
    duration_seconds = Column(Integer, nullable=True)
    technical_score = Column(Integer, nullable=False, default=0)
    communication_score = Column(Integer, nullable=False, default=0)
    confidence_score = Column(Integer, nullable=False, default=0)
    clarity_score = Column(Integer, nullable=False, default=0)
    score = Column(Integer, nullable=False, default=0)
    feedback = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    session = relationship("InterviewSession", back_populates="responses")


class FeedbackReport(Base):
    __tablename__ = "feedback_reports"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("interview_sessions.id"), nullable=False, unique=True)
    summary = Column(Text, nullable=False)
    strong_areas = Column(Text, nullable=False)
    weak_areas = Column(Text, nullable=False)
    communication_review = Column(Text, nullable=False)
    technical_review = Column(Text, nullable=False)
    recommended_topics = Column(Text, nullable=False)
    learning_roadmap = Column(Text, nullable=False)
    readiness_percentage = Column(Integer, nullable=False)
    generated_at = Column(DateTime, default=datetime.utcnow)

    session = relationship("InterviewSession", back_populates="feedback_report")
