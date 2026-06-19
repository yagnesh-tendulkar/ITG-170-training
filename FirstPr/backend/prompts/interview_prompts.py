QUESTION_PROMPT = """
Generate {num_questions} role-specific interview questions.
Role: {role}
Interview type: {interview_type}
Difficulty: {difficulty}
Experience level: {experience_level}

Return JSON only in the following format:
{{
  "questions": ["question1", "question2", "question3", ...]
}}
Ensure exactly {num_questions} questions are returned.
"""

EVALUATION_PROMPT = """
You are an interview coach assessing a candidate answer.
Role: {role}
Question: {question}
Answer: {answer}
Question type: {question_type}
Experience level: {experience_level}

Return JSON only in the following structure:
{
  "score": 0,
  "technical_score": 0,
  "communication_score": 0,
  "confidence_score": 0,
  "clarity_score": 0,
  "strengths": [],
  "weaknesses": [],
  "suggestions": [],
  "feedback": "",
  "next_question": "",
  "details": []
}
"""

SESSION_FEEDBACK_PROMPT = """
You are an interview advisor preparing a personalized feedback report.
Role: {role}
Interview type: {interview_type}
Experience level: {experience_level}
Responses:
{responses}

Return JSON only in the following structure:
{
  "summary": "",
  "strong_areas": "",
  "weak_areas": "",
  "communication_review": "",
  "technical_review": "",
  "recommended_topics": "",
  "learning_roadmap": "",
  "readiness_percentage": 0
}
"""
