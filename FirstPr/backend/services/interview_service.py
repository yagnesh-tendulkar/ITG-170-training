import os
import logging
from typing import Dict, List

from backend.services.ai_service import (
    build_personalized_feedback,
    evaluate_candidate_answer,
    generate_role_questions,
)

logger = logging.getLogger(__name__)


def generate_questions(
    role: str,
    question_type: str = "Technical",
    difficulty: str = "Medium",
    experience_level: str = "Mid",
    num_questions: int = 5,
) -> List[str]:
    try:
        return generate_role_questions(role, question_type, difficulty, experience_level, num_questions)
    except Exception as exc:
        logger.warning("Question generation fallback active: %s", exc)

    return [
        "Provide a strong foundation for the candidate to speak to their experience.",
        "Ask for details on tools, architecture, or frameworks used.",
        "Prompt a scenario that helps reveal the candidate's problem-solving approach.",
    ]


def evaluate_response(
    role: str,
    question: str,
    response: str,
    question_type: str = "Technical",
    experience_level: str = "Mid",
) -> Dict[str, object]:
    try:
        return evaluate_candidate_answer(role, question, response, question_type, experience_level)
    except Exception as exc:
        logger.warning("AI evaluation fallback active: %s", exc)

    technical_score = 70
    communication_score = 70
    confidence_score = 70
    clarity_score = 70
    strengths: List[str] = [
        "The answer shows role awareness and a structured approach.",
        "You kept the response focused on the core problem."
    ]
    weaknesses: List[str] = [
        "Add a concrete example to strengthen the answer.",
        "Make the technical reasoning clearer and more specific."
    ]
    suggestions: List[str] = [
        "Highlight implementation details and trade-offs.",
        "Summarize the final recommendation in one sentence.",
    ]

    lower_response = response.strip().lower()
    if len(response.strip()) < 40:
        technical_score -= 20
        communication_score -= 20
        confidence_score -= 15
        clarity_score -= 20
        strengths = ["The response requires more details to fully assess the candidate."]
        weaknesses.append("The answer is too short for a complete evaluation.")
    if "because" in lower_response or "for example" in lower_response:
        technical_score += 10
        clarity_score += 10
        strengths.append("Strong use of explanation and supporting examples.")

    technical_score = max(0, min(100, technical_score))
    communication_score = max(0, min(100, communication_score))
    confidence_score = max(0, min(100, confidence_score))
    clarity_score = max(0, min(100, clarity_score))
    overall_score = round((technical_score + communication_score + confidence_score + clarity_score) / 4)

    return {
        "score": overall_score,
        "technical_score": technical_score,
        "communication_score": communication_score,
        "confidence_score": confidence_score,
        "clarity_score": clarity_score,
        "feedback": (
            "The response is constructive, but it will benefit from deeper examples and sharper clarity "
            "aligned to the role context."
        ),
        "strengths": strengths,
        "weaknesses": weaknesses,
        "suggestions": suggestions,
        "next_question": f"Explain one project you worked on as a {role}.",
        "details": [
            "Focus on action, results, and the impact for the team or product.",
            "Use precise language rather than high-level descriptions."
        ],
    }


def build_feedback_report(
    role: str,
    question_type: str,
    experience_level: str,
    responses: List[Dict[str, object]],
) -> Dict[str, object]:
    try:
        return build_personalized_feedback(role, question_type, experience_level, responses)
    except Exception as exc:
        logger.warning("Personalized feedback fallback active: %s", exc)

    return {
        "summary": (
            "The candidate demonstrated strong role awareness but can improve technical depth "
            "and communication clarity in their interview responses."
        ),
        "strong_areas": "Role alignment, organized responses, and positive tone.",
        "weak_areas": "More precise evidence, structured examples, and concise delivery.",
        "communication_review": (
            "The candidate communicates ideas clearly but should tighten the narrative to avoid diluting key points."
        ),
        "technical_review": (
            "The responses are correct at a high level, but adding implementation details will improve scores."
        ),
        "recommended_topics": "Core architecture patterns, performance optimization, and team collaboration examples.",
        "learning_roadmap": (
            "Review common role-specific interview questions, practice using metrics, and prepare a short summary for each scenario."
        ),
        "readiness_percentage": 72,
    }
