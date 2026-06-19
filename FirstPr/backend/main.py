import json
import os
import uuid
from datetime import datetime
from typing import List, Optional

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, File, HTTPException, Request, UploadFile, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from sqlalchemy.orm import Session

load_dotenv()

from backend.auth import (
    authenticate_user,
    create_access_token,
    get_current_user,
    get_current_user_optional,
    get_password_hash,
)
from backend.ai_client import ai_transcribe_audio
from backend.database import Base, engine, SessionLocal
from backend.models import (
    FeedbackReport,
    InterviewResponse,
    InterviewSession,
    ResponseRecord,
    User,
)
from backend.schemas import (
    AnalyticsResponse,
    DashboardResponse,
    EvaluateRequest,
    EvaluateResponse,
    InterviewResponseCreate,
    InterviewSessionCreate,
    InterviewSessionRead,
    PersonalizedFeedbackRead,
    ProgressResponse,
    QuestionListResponse,
    ReportRequest,
    ResponseRecordRead,
    TokenRequest,
    TokenResponse,
    UserCreate,
    UserRead,
)
from backend.services import build_feedback_report, evaluate_response, generate_questions
from backend.utils.pdf_generator import create_interview_report

# Create tables at startup (simple approach for small projects)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Interview Preparation API",
    description="A FastAPI backend for role-specific interview question generation, evaluation, mock interview sessions, analytics, and personalized feedback.",
    version="0.2.0",
)

# Configure CORS from environment; default allows local dev frontends
cors_env = os.getenv("CORS_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173")
allow_origins = [o.strip() for o in cors_env.split(",") if o.strip()]
if not allow_origins:
    allow_origins = ["http://localhost:5173", "http://127.0.0.1:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    if isinstance(exc, HTTPException):
        raise exc
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Something went wrong. Please try again later."},
    )


def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_or_create_guest_user(db: Session) -> User:
    user = db.query(User).filter(User.email == "guest@interviewprep.local").first()
    if user is None:
        user = User(name="Guest User", email="guest@interviewprep.local", hashed_password="")
        db.add(user)
        db.commit()
        db.refresh(user)
    return user


@app.get("/api/health")
def health_check():
    return {"status": "ok", "message": "Interview prep backend is healthy"}


@app.post("/api/auth/register", response_model=UserRead)
def register_user(user: UserCreate, db: Session = Depends(get_db_session)):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")

    hashed_password = get_password_hash(user.password)
    new_user = User(name=user.name, email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.post("/api/auth/login", response_model=TokenResponse)
def login_user(credentials: TokenRequest, db: Session = Depends(get_db_session)):
    user = authenticate_user(db, credentials.email, credentials.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}


@app.get("/api/auth/me", response_model=UserRead)
def current_user_profile(current_user: User = Depends(get_current_user)):
    return current_user


@app.post("/api/interview/session", response_model=InterviewSessionRead)
def create_interview_session(
    payload: InterviewSessionCreate,
    db: Session = Depends(get_db_session),
    current_user: Optional[User] = Depends(get_current_user_optional),
):
    user = current_user or get_or_create_guest_user(db)
    session_id = str(uuid.uuid4())
    session = InterviewSession(
        session_id=session_id,
        user_id=user.id,
        role=payload.role,
        interview_type=payload.question_type or "Technical",
        difficulty=payload.difficulty or "Medium",
        experience_level=payload.experience_level or "Mid",
        duration_seconds=(payload.duration_minutes or 30) * 60,
    )
    db.add(session)
    db.commit()
    db.refresh(session)
    return session


@app.get("/api/questions", response_model=QuestionListResponse)
def list_questions(
    role: str = "Frontend Developer",
    question_type: str = "Technical",
    difficulty: str = "Medium",
    experience_level: str = "Mid",
    num_questions: int = 5,
):
    num_questions = max(1, min(num_questions, 20))
    questions = generate_questions(role, question_type, difficulty, experience_level, num_questions)
    return {"role": role, "questions": questions}


@app.post("/api/evaluate", response_model=EvaluateResponse)
def evaluate_answer(
    payload: EvaluateRequest,
    db: Session = Depends(get_db_session),
    current_user: Optional[User] = Depends(get_current_user_optional),
):
    feedback_payload = evaluate_response(
        payload.role,
        payload.question,
        payload.response,
        payload.question_type or "Technical",
    )

    user = current_user or get_or_create_guest_user(db)
    session_id = payload.session_id or str(uuid.uuid4())
    record = ResponseRecord(
        user_id=user.id,
        session_id=session_id,
        role=payload.role,
        question_type=payload.question_type or "Technical",
        question=payload.question,
        response=payload.response,
        feedback=feedback_payload["feedback"],
        score=feedback_payload.get("score", 0),
        technical_score=feedback_payload.get("technical_score", 0),
        communication_score=feedback_payload.get("communication_score", 0),
        confidence_score=feedback_payload.get("confidence_score", 0),
        clarity_score=feedback_payload.get("clarity_score", 0),
        duration_seconds=payload.duration_seconds,
    )
    db.add(record)
    db.commit()
    db.refresh(record)

    return EvaluateResponse(
        score=feedback_payload.get("score", 0),
        technical_score=feedback_payload.get("technical_score", 0),
        communication_score=feedback_payload.get("communication_score", 0),
        confidence_score=feedback_payload.get("confidence_score", 0),
        clarity_score=feedback_payload.get("clarity_score", 0),
        feedback=feedback_payload["feedback"],
        strengths=feedback_payload.get("strengths", []),
        weaknesses=feedback_payload.get("weaknesses", []),
        suggestions=feedback_payload.get("suggestions", []),
        next_question=feedback_payload.get("next_question", ""),
        details=feedback_payload.get("details", []),
    )


@app.post("/api/interview/session/{session_id}/answer", response_model=EvaluateResponse)
def submit_interview_answer(
    session_id: str,
    payload: InterviewResponseCreate,
    db: Session = Depends(get_db_session),
    current_user: Optional[User] = Depends(get_current_user_optional),
):
    session = db.query(InterviewSession).filter(InterviewSession.session_id == session_id).first()
    if not session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Interview session not found")
    if session.status != "in_progress":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Interview session is already completed")

    feedback_payload = evaluate_response(
        session.role,
        payload.question,
        payload.response,
        payload.question_type or session.interview_type,
    )

    response_record = InterviewResponse(
        session_id=session.id,
        question=payload.question,
        response=payload.response,
        question_type=payload.question_type or session.interview_type,
        duration_seconds=payload.duration_seconds,
        technical_score=feedback_payload.get("technical_score", 0),
        communication_score=feedback_payload.get("communication_score", 0),
        confidence_score=feedback_payload.get("confidence_score", 0),
        clarity_score=feedback_payload.get("clarity_score", 0),
        score=feedback_payload.get("score", 0),
        feedback=feedback_payload["feedback"],
    )
    db.add(response_record)
    session.total_score = (session.total_score or 0) + feedback_payload.get("score", 0)
    session.total_technical_score = (session.total_technical_score or 0) + feedback_payload.get("technical_score", 0)
    session.total_communication_score = (session.total_communication_score or 0) + feedback_payload.get("communication_score", 0)
    db.commit()
    db.refresh(response_record)
    db.refresh(session)

    return EvaluateResponse(
        score=feedback_payload.get("score", 0),
        technical_score=feedback_payload.get("technical_score", 0),
        communication_score=feedback_payload.get("communication_score", 0),
        confidence_score=feedback_payload.get("confidence_score", 0),
        clarity_score=feedback_payload.get("clarity_score", 0),
        feedback=feedback_payload["feedback"],
        strengths=feedback_payload.get("strengths", []),
        weaknesses=feedback_payload.get("weaknesses", []),
        suggestions=feedback_payload.get("suggestions", []),
        next_question=feedback_payload.get("next_question", ""),
        details=feedback_payload.get("details", []),
    )


@app.post("/api/interview/session/{session_id}/complete", response_model=PersonalizedFeedbackRead)
def complete_interview_session(
    session_id: str,
    db: Session = Depends(get_db_session),
    current_user: Optional[User] = Depends(get_current_user_optional),
):
    session = db.query(InterviewSession).filter(InterviewSession.session_id == session_id).first()
    if not session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Interview session not found")
    if session.status == "completed":
        report = db.query(FeedbackReport).filter(FeedbackReport.session_id == session.id).first()
        if report:
            return report
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Feedback report not found")

    responses = [
        {
            "question": response.question,
            "answer": response.response,
            "technical_score": response.technical_score,
            "communication_score": response.communication_score,
            "confidence_score": response.confidence_score,
            "clarity_score": response.clarity_score,
            "feedback": response.feedback,
        }
        for response in session.responses
    ]

    report_payload = build_feedback_report(session.role, session.interview_type, session.experience_level, responses)
    report = FeedbackReport(
        session_id=session.id,
        summary=report_payload.get("summary", ""),
        strong_areas=report_payload.get("strong_areas", ""),
        weak_areas=report_payload.get("weak_areas", ""),
        communication_review=report_payload.get("communication_review", ""),
        technical_review=report_payload.get("technical_review", ""),
        recommended_topics=report_payload.get("recommended_topics", ""),
        learning_roadmap=report_payload.get("learning_roadmap", ""),
        readiness_percentage=report_payload.get("readiness_percentage", 0),
    )
    session.status = "completed"
    session.ended_at = datetime.utcnow()
    if session.duration_seconds is None:
        session.duration_seconds = int((session.ended_at - session.started_at).total_seconds())

    db.add(report)
    db.commit()
    db.refresh(report)
    db.refresh(session)

    return report


@app.get("/api/interview/session/{session_id}", response_model=InterviewSessionRead)
def get_interview_session(
    session_id: str,
    db: Session = Depends(get_db_session),
    current_user: Optional[User] = Depends(get_current_user_optional),
):
    session = (
        db.query(InterviewSession)
        .filter(InterviewSession.session_id == session_id)
        .first()
    )
    if not session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Interview session not found")
    return session


@app.get("/api/history", response_model=List[ResponseRecordRead])
def get_user_history(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db_session),
):
    records = (
        db.query(ResponseRecord)
        .filter(ResponseRecord.user_id == current_user.id)
        .order_by(ResponseRecord.created_at.desc())
        .limit(40)
        .all()
    )
    return records


@app.get("/api/analytics/dashboard", response_model=DashboardResponse)
def get_analytics_dashboard(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db_session),
):
    sessions = (
        db.query(InterviewSession)
        .filter(InterviewSession.user_id == current_user.id, InterviewSession.status == "completed")
        .order_by(InterviewSession.started_at.asc())
        .all()
    )

    total_sessions = len(sessions)
    if total_sessions == 0:
        return {
            "total_sessions": 0,
            "total_questions": 0,
            "average_score": 0.0,
            "best_score": 0.0,
            "improvement_percentage": 0.0,
            "average_technical_score": 0.0,
            "average_communication_score": 0.0,
            "weekly_progress": [],
            "monthly_progress": [],
        }

    session_scores = [
        session.total_score / len(session.responses) if session.responses else 0
        for session in sessions
    ]
    best_score = max(session_scores)
    average_score = sum(session_scores) / total_sessions
    total_questions = sum(len(session.responses) for session in sessions)
    average_technical = sum(session.total_technical_score or 0 for session in sessions) / total_sessions
    average_communication = sum(session.total_communication_score or 0 for session in sessions) / total_sessions
    improvement_percentage = 0.0
    if total_sessions >= 2:
        improvement_percentage = round(
            ((session_scores[-1] - session_scores[0]) / max(1, session_scores[0])) * 100,
            1,
        )

    weekly_progress = []
    monthly_progress = []
    weekly_map: dict[str, List[float]] = {}
    monthly_map: dict[str, List[float]] = {}
    for session in sessions:
        week_label = session.started_at.strftime("%Y-W%U")
        month_label = session.started_at.strftime("%Y-%m")
        weekly_map.setdefault(week_label, []).append(
            session.total_score / len(session.responses) if session.responses else 0
        )
        monthly_map.setdefault(month_label, []).append(
            session.total_score / len(session.responses) if session.responses else 0
        )

    for week, scores in weekly_map.items():
        weekly_progress.append(
            {
                "label": week,
                "average_score": round(sum(scores) / len(scores), 1),
                "average_technical_score": 0.0,
                "average_communication_score": 0.0,
                "sessions": len(scores),
            }
        )
    for month, scores in monthly_map.items():
        monthly_progress.append(
            {
                "label": month,
                "average_score": round(sum(scores) / len(scores), 1),
                "average_technical_score": 0.0,
                "average_communication_score": 0.0,
                "sessions": len(scores),
            }
        )

    return {
        "total_sessions": total_sessions,
        "total_questions": total_questions,
        "average_score": round(average_score, 1),
        "best_score": round(best_score, 1),
        "improvement_percentage": improvement_percentage,
        "average_technical_score": round(average_technical, 1),
        "average_communication_score": round(average_communication, 1),
        "weekly_progress": weekly_progress,
        "monthly_progress": monthly_progress,
    }


@app.get("/api/analytics/progress", response_model=ProgressResponse)
def get_analytics_progress(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db_session),
):
    sessions = (
        db.query(InterviewSession)
        .filter(InterviewSession.user_id == current_user.id, InterviewSession.status == "completed")
        .order_by(InterviewSession.started_at.asc())
        .all()
    )

    weekly_map: dict[str, List[float]] = {}
    monthly_map: dict[str, List[float]] = {}
    for session in sessions:
        week_label = session.started_at.strftime("%Y-W%U")
        month_label = session.started_at.strftime("%Y-%m")
        weekly_map.setdefault(week_label, []).append(
            session.total_score / len(session.responses) if session.responses else 0
        )
        monthly_map.setdefault(month_label, []).append(
            session.total_score / len(session.responses) if session.responses else 0
        )

    weekly = [
        {
            "label": key,
            "average_score": round(sum(values) / len(values), 1),
            "average_technical_score": 0.0,
            "average_communication_score": 0.0,
            "sessions": len(values),
        }
        for key, values in weekly_map.items()
    ]
    monthly = [
        {
            "label": key,
            "average_score": round(sum(values) / len(values), 1),
            "average_technical_score": 0.0,
            "average_communication_score": 0.0,
            "sessions": len(values),
        }
        for key, values in monthly_map.items()
    ]

    return {"weekly": weekly, "monthly": monthly}


@app.post("/api/report")
def generate_report(payload: ReportRequest):
    filename = f"/tmp/interview-report-{uuid.uuid4().hex}.pdf"
    create_interview_report(
        filename=filename,
        candidate_name=payload.candidate_name,
        role=payload.role,
        question=payload.question,
        response=payload.response,
        technical_score=payload.technical_score,
        communication_score=payload.communication_score,
        feedback=payload.feedback,
        suggestions=payload.suggestions,
    )
    return FileResponse(filename, media_type="application/pdf", filename="Interview Report.pdf")


@app.post("/api/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    try:
        transcription = ai_transcribe_audio(file.file)
        return {"text": transcription}
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exc))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
