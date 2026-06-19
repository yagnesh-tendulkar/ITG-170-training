import json
import os
import time
from typing import Any, Dict, IO, List

import requests

try:
    import openai
except ImportError:
    openai = None

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-pro-mini")
GEMINI_API_URL = os.getenv(
    "GEMINI_API_URL",
    f"https://generativelanguage.googleapis.com/v1beta2/models/{GEMINI_MODEL}:generateText",
)

from backend.prompts.interview_prompts import EVALUATION_PROMPT, QUESTION_PROMPT, SESSION_FEEDBACK_PROMPT


def _parse_json(text: str) -> Dict[str, Any]:
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise RuntimeError("AI response was not valid JSON:\n" + text) from exc


def _extract_gemini_text(payload: Dict[str, Any]) -> str:
    candidates = payload.get("candidates") or []
    if candidates:
        candidate = candidates[0]
        if isinstance(candidate, dict):
            nested = candidate.get("output") or candidate.get("content") or candidate.get("text")
            if isinstance(nested, str):
                return nested.strip()
            if isinstance(nested, dict):
                return nested.get("text", "").strip()
            if isinstance(nested, list) and nested:
                first = nested[0]
                if isinstance(first, dict):
                    return first.get("text", "").strip()
                return str(first).strip()
    if isinstance(payload.get("output"), str):
        return payload["output"].strip()
    if isinstance(payload.get("content"), str):
        return payload["content"].strip()
    raise RuntimeError("Gemini returned an unexpected response format: %s" % payload)


def _call_gemini(prompt_text: str, max_tokens: int = 512) -> str:
    if not GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY is not configured")

    headers = {"Content-Type": "application/json"}
    params = {"key": GEMINI_API_KEY}
    payload = {
        "prompt": {"text": prompt_text},
        "temperature": 0.35,
        "maxOutputTokens": max_tokens,
        "candidateCount": 1,
    }

    for attempt in range(3):
        response = requests.post(
            GEMINI_API_URL,
            headers=headers,
            params=params,
            json=payload,
            timeout=30,
        )
        response.raise_for_status()
        data = response.json()
        text = _extract_gemini_text(data)
        if text:
            return text
        time.sleep(1.5 * attempt)

    raise RuntimeError("Gemini did not return usable output")


def _call_openai(prompt_text: str, max_tokens: int = 512) -> str:
    if not OPENAI_API_KEY or openai is None:
        raise RuntimeError("OpenAI SDK is not installed or OPENAI_API_KEY is not configured")

    openai.api_key = OPENAI_API_KEY
    completion = openai.ChatCompletion.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": "You are an interview coach generating structured interview content."},
            {"role": "user", "content": prompt_text},
        ],
        temperature=0.4,
        max_tokens=max_tokens,
    )
    return completion.choices[0].message.content.strip()


def _call_ai(prompt_text: str, max_tokens: int = 512) -> str:
    if GEMINI_API_KEY:
        try:
            return _call_gemini(prompt_text, max_tokens=max_tokens)
        except Exception:
            pass
    return _call_openai(prompt_text, max_tokens=max_tokens)


def ai_generate_questions(
    role: str,
    difficulty: str = "Technical",
    interview_type: str = "Technical",
    experience_level: str = "Mid",
    num_questions: int = 5,
) -> List[str]:
    prompt = QUESTION_PROMPT.format(
        role=role,
        interview_type=interview_type,
        difficulty=difficulty,
        experience_level=experience_level,
        num_questions=num_questions,
    )
    max_tokens = 200 + (num_questions * 60)
    text = _call_ai(prompt, max_tokens=max_tokens)
    payload = _parse_json(text)
    questions = payload.get("questions")
    if not isinstance(questions, list):
        raise RuntimeError("AI returned invalid question payload: " + text)
    return [str(question) for question in questions[:num_questions]]


def ai_evaluate_answer(
    role: str,
    question: str,
    response: str,
    question_type: str = "Technical",
    experience_level: str = "Mid",
) -> Dict[str, Any]:
    prompt = EVALUATION_PROMPT.format(
        role=role,
        question=question,
        answer=response,
        question_type=question_type,
        experience_level=experience_level,
    )
    text = _call_ai(prompt, max_tokens=420)
    payload = _parse_json(text)

    technical_score = int(payload.get("technical_score", 0))
    communication_score = int(payload.get("communication_score", 0))
    confidence_score = int(payload.get("confidence_score", 0))
    clarity_score = int(payload.get("clarity_score", 0))
    score = int(payload.get("score", (technical_score + communication_score + confidence_score + clarity_score) // 4))

    return {
        "score": score,
        "technical_score": technical_score,
        "communication_score": communication_score,
        "confidence_score": confidence_score,
        "clarity_score": clarity_score,
        "feedback": str(payload.get("feedback", "")),
        "strengths": payload.get("strengths", []),
        "weaknesses": payload.get("weaknesses", []),
        "suggestions": payload.get("suggestions", []),
        "next_question": str(payload.get("next_question", "")),
        "details": payload.get("details", []),
    }


def ai_generate_feedback_report(
    role: str,
    interview_type: str,
    experience_level: str,
    responses: List[Dict[str, Any]],
) -> Dict[str, Any]:
    responses_payload = json.dumps(responses, ensure_ascii=False, indent=2)
    prompt = SESSION_FEEDBACK_PROMPT.format(
        role=role,
        interview_type=interview_type,
        experience_level=experience_level,
        responses=responses_payload,
    )
    text = _call_ai(prompt, max_tokens=520)
    payload = _parse_json(text)

    return {
        "summary": str(payload.get("summary", "")),
        "strong_areas": str(payload.get("strong_areas", "")),
        "weak_areas": str(payload.get("weak_areas", "")),
        "communication_review": str(payload.get("communication_review", "")),
        "technical_review": str(payload.get("technical_review", "")),
        "recommended_topics": str(payload.get("recommended_topics", "")),
        "learning_roadmap": str(payload.get("learning_roadmap", "")),
        "readiness_percentage": int(payload.get("readiness_percentage", 0)),
    }


def ai_transcribe_audio(audio_file: IO[bytes]) -> str:
    if not OPENAI_API_KEY or openai is None:
        raise RuntimeError("OPENAI transcription requires OPENAI_API_KEY and the OpenAI SDK")

    openai.api_key = OPENAI_API_KEY
    if hasattr(openai.Audio, "transcriptions"):
        transcription = openai.Audio.transcriptions.create(model="gpt-4o-transcribe", file=audio_file)
        return getattr(transcription, "text", transcription.get("text", ""))

    if hasattr(openai.Audio, "transcribe"):
        transcription = openai.Audio.transcribe(model="gpt-4o-transcribe", file=audio_file)
        return transcription.get("text", "")

    raise RuntimeError("Audio transcription is not supported by the installed OpenAI SDK version")
