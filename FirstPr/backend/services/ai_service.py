import json
import logging
import os
import time
from typing import Any, Dict, List

from backend.ai_client import ai_evaluate_answer, ai_generate_questions, ai_generate_feedback_report

logger = logging.getLogger(__name__)

DEFAULT_QUESTIONS = {
    "Frontend Developer": {
        "Technical": [
            "Explain the difference between React state and props.",
            "How do you optimize rendering in a React application?",
            "Describe the accessibility strategies you use in front-end development.",
        ],
        "Behavioral": [
            "Tell me about a time you fixed a production bug under pressure.",
            "How do you stay aligned with designers and backend engineers?",
            "Describe a project where you improved the user experience.",
        ],
        "Architecture": [
            "How would you design a scalable React application for a large team?",
            "What approach do you use for reusable component libraries?",
            "How do you structure CSS and component styles for maintainability?",
        ],
    },
    "Backend Developer": {
        "Technical": [
            "Explain RESTful API design and how you choose HTTP status codes.",
            "How do you manage database migrations in a production service?",
            "Describe how you secure an API endpoint and protect sensitive data.",
        ],
        "Behavioral": [
            "Tell me about a time you improved service reliability.",
            "How do you balance technical debt against feature delivery?",
            "Describe your process for collaborating with frontend teams.",
        ],
        "Architecture": [
            "How would you design a microservice architecture for a payment system?",
            "What caching strategies do you use for high-traffic APIs?",
            "How do you ensure data consistency across distributed services?",
        ],
    },
    "Data Scientist": {
        "Technical": [
            "How do you choose between classification and regression models?",
            "Explain cross-validation and its role in model selection.",
            "What is bias-variance tradeoff, and how do you manage it?",
        ],
        "Behavioral": [
            "Tell me about a data project that had business impact.",
            "How do you explain model results to non-technical stakeholders?",
            "Describe a time you handled incomplete or messy data.",
        ],
        "Architecture": [
            "How would you architect a production machine learning pipeline?",
            "What is your approach to model monitoring and retraining?",
            "How do you deploy models with reliable inference latency?",
        ],
    },
}


def _retry(fn, *args, attempts: int = 3, backoff: float = 1.5, **kwargs):
    last_exception = None
    for attempt in range(1, attempts + 1):
        try:
            return fn(*args, **kwargs)
        except Exception as exc:
            last_exception = exc
            logger.warning("AI service attempt %s failed: %s", attempt, exc)
            if attempt == attempts:
                break
            time.sleep(backoff * attempt)
    raise last_exception


def generate_role_questions(
    role: str,
    interview_type: str = "Technical",
    difficulty: str = "Medium",
    experience_level: str = "Mid",
    num_questions: int = 5,
) -> List[str]:
    if os.getenv("GEMINI_API_KEY") or os.getenv("OPENAI_API_KEY"):
        try:
            return _retry(
                ai_generate_questions,
                role=role,
                difficulty=difficulty,
                interview_type=interview_type,
                experience_level=experience_level,
                num_questions=num_questions,
                attempts=3,
            )
        except Exception as exc:
            logger.warning("AI question generation fallback active: %s", exc)

    role_set = DEFAULT_QUESTIONS.get(role, DEFAULT_QUESTIONS["Frontend Developer"])
    return role_set.get(interview_type, role_set["Technical"])[:num_questions]


def evaluate_candidate_answer(
    role: str,
    question: str,
    response: str,
    question_type: str = "Technical",
    experience_level: str = "Mid",
) -> Dict[str, Any]:
    if os.getenv("GEMINI_API_KEY") or os.getenv("OPENAI_API_KEY"):
        try:
            return _retry(
                ai_evaluate_answer,
                role=role,
                question=question,
                response=response,
                question_type=question_type,
                experience_level=experience_level,
                attempts=3,
            )
        except Exception as exc:
            logger.warning("AI evaluation failed, falling back to heuristic scoring: %s", exc)

    technical_score = 70
    communication_score = 70
    confidence_score = 70
    clarity_score = 70
    strengths = [
        "Your response shows awareness of the key role responsibilities.",
        "You maintain a calm and structured answer flow.",
    ]
    weaknesses = [
        "Add more specifics to improve the technical depth.",
        "Use a stronger closing statement in the answer.",
    ]
    suggestions = [
        "Include a concrete example with metrics.",
        "Clarify trade-offs and expected outcomes.",
    ]

    lower_answer = response.strip().lower()
    if len(response.strip()) < 40:
        technical_score -= 20
        communication_score -= 20
        confidence_score -= 20
        clarity_score -= 20
        strengths = ["The answer needs more detail to evaluate properly."]
        weaknesses.append("Length is too short to demonstrate experience.")
    if "because" in lower_answer or "for example" in lower_answer:
        technical_score += 10
        communication_score += 5
        clarity_score += 10
        strengths.append("Good use of examples and explanations.")
    if "i" in lower_answer and "we" not in lower_answer:
        confidence_score += 5

    technical_score = max(0, min(100, technical_score))
    communication_score = max(0, min(100, communication_score))
    confidence_score = max(0, min(100, confidence_score))
    clarity_score = max(0, min(100, clarity_score))
    score = round((technical_score + communication_score + confidence_score + clarity_score) / 4)

    return {
        "score": score,
        "technical_score": technical_score,
        "communication_score": communication_score,
        "confidence_score": confidence_score,
        "clarity_score": clarity_score,
        "feedback": (
            "The response is on the right track, but it would be stronger with a clearer example "
            "and better alignment to the target role."
        ),
        "strengths": strengths,
        "weaknesses": weaknesses,
        "suggestions": suggestions,
        "next_question": f"Explain one project you worked on as a {role}.",
        "details": [
            "Focus on measurable results and your direct contributions.",
            "Keep answers concise and anchor them to the role impact.",
        ],
    }


def build_personalized_feedback(
    role: str,
    interview_type: str,
    experience_level: str,
    responses: List[Dict[str, Any]],
) -> Dict[str, Any]:
    if os.getenv("GEMINI_API_KEY") or os.getenv("OPENAI_API_KEY"):
        try:
            return _retry(
                ai_generate_feedback_report,
                role=role,
                interview_type=interview_type,
                experience_level=experience_level,
                responses=responses,
                attempts=3,
            )
        except Exception as exc:
            logger.warning("AI feedback report failed, using fallback summary: %s", exc)

    summary = "The candidate has several strengths across the role but would benefit from deeper technical examples and clearer communication in answers."
    return {
        "summary": summary,
        "strong_areas": "Clear role understanding and structured answers.",
        "weak_areas": "More precise technical depth and examples needed.",
        "communication_review": "Overall communication is strong, but the answers can be more concise and confident.",
        "technical_review": "The candidate understands the domain, though some response areas lack concrete implementation details.",
        "recommended_topics": "API design, performance optimization, system architecture patterns.",
        "learning_roadmap": "Practice case studies, build sample projects, and rehearse concise explanations.",
        "readiness_percentage": 68,
    }
