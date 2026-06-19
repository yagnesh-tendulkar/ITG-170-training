import os
from backend.services.interview_service import evaluate_response


def test_evaluate_response_returns_expected_fields():
    os.environ.pop("OPENAI_API_KEY", None)
    result = evaluate_response(
        "Frontend Developer",
        "Explain the difference between React state and props.",
        "State is mutable and local to a component while props are passed from parent to child. For example, I use state to track form values.",
    )

    assert result["technical_score"] >= 0
    assert result["communication_score"] >= 0
    assert isinstance(result["strengths"], list)
    assert isinstance(result["weaknesses"], list)
    assert isinstance(result["suggestions"], list)
    assert result["next_question"].startswith("Explain one project")
