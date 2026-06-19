from backend.services.interview_service import generate_questions


def test_generate_questions_fallback():
    questions = generate_questions("Backend Developer", "Technical")
    assert isinstance(questions, list)
    assert len(questions) >= 3
    assert "RESTful" in questions[0] or "HTTP status" in questions[0]


def test_generate_questions_unknown_role_uses_default():
    questions = generate_questions("Unknown Role", "Behavioral")
    assert isinstance(questions, list)
    assert len(questions) > 0
