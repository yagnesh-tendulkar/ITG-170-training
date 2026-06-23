# ─────────────────────────────────────────────
# tests/test_ai_service.py
#
# LEARNING NOTE:
# These are pure "unit tests" — they test a single function in isolation,
# with all external dependencies mocked out.
#
# Unlike integration tests (which test the full stack), unit tests:
#   - Are much faster (no DB, no network)
#   - Pinpoint exactly what broke when they fail
#   - Test edge cases that are hard to trigger through the API
#
# We use pytest.mark.asyncio to test async functions.
# ─────────────────────────────────────────────

import pytest
import json
from unittest.mock import AsyncMock, MagicMock, patch


class TestAnalyzeCode:
    """Unit tests for the analyze_code() AI service function"""

    @pytest.mark.asyncio
    async def test_analyze_with_valid_api_key(self):
        """
        When Gemini returns valid JSON, analyze_code should parse and return it.
        We mock the model object to return a controlled response.
        """
        mock_response_text = json.dumps({
            "bugs": [{"description": "Null pointer", "line_hint": "L5", "severity": "high"}],
            "optimizations": [{"description": "Use cache", "impact": "high"}],
            "best_practices": [{"description": "Add types", "category": "Safety"}],
            "overall_score": 80,
            "summary": "Pretty good code.",
        })

        mock_model = MagicMock()
        mock_model.generate_content.return_value = MagicMock(text=mock_response_text)

        # Patch the module-level 'model' variable in ai_service
        with patch("services.ai_service.model", mock_model):
            from services.ai_service import analyze_code
            result = await analyze_code("Python", "def foo(): pass")

        assert result["overall_score"] == 80
        assert len(result["bugs"]) == 1
        assert result["bugs"][0]["severity"] == "high"
        assert result["summary"] == "Pretty good code."

    @pytest.mark.asyncio
    async def test_analyze_strips_markdown_fences(self):
        """
        Gemini sometimes wraps JSON in ```json ... ``` fences.
        The service must handle this gracefully.
        """
        mock_response_text = """```json
{
    "bugs": [],
    "optimizations": [],
    "best_practices": [],
    "overall_score": 90,
    "summary": "Clean code!"
}
```"""
        mock_model = MagicMock()
        mock_model.generate_content.return_value = MagicMock(text=mock_response_text)

        with patch("services.ai_service.model", mock_model):
            from services.ai_service import analyze_code
            result = await analyze_code("Python", "def clean(): return True")

        # Should successfully parse despite the markdown fences
        assert result["overall_score"] == 90
        assert result["summary"] == "Clean code!"

    @pytest.mark.asyncio
    async def test_analyze_falls_back_on_bad_json(self):
        """
        If Gemini returns unparseable text, the service should NOT crash.
        It should gracefully fall back to mock data.
        """
        mock_model = MagicMock()
        mock_model.generate_content.return_value = MagicMock(
            text="Sorry, I cannot review this code."  # Not JSON!
        )

        with patch("services.ai_service.model", mock_model):
            from services.ai_service import analyze_code
            result = await analyze_code("Python", "def foo(): pass")

        # Should return the mock fallback — not raise an exception
        assert "bugs" in result
        assert "overall_score" in result
        assert isinstance(result["bugs"], list)

    @pytest.mark.asyncio
    async def test_analyze_uses_mock_when_no_model(self):
        """
        When model is None (no API key), analyze_code should return mock data.
        This ensures the app works even without a Gemini key.
        """
        with patch("services.ai_service.model", None):
            from services.ai_service import analyze_code
            result = await analyze_code("JavaScript", "function add(a, b) { return a+b; }")

        # Mock data should still be structured correctly
        assert "bugs" in result
        assert "optimizations" in result
        assert "best_practices" in result
        assert "overall_score" in result
        assert "summary" in result
        assert isinstance(result["overall_score"], (int, float))


class TestGenerateDocumentation:
    """Unit tests for the generate_documentation() AI service function"""

    @pytest.mark.asyncio
    async def test_generate_docs_success(self):
        """Happy path: Gemini returns valid documented code"""
        mock_response_text = json.dumps({
            "documented_code": "def foo():\n    '''Does foo stuff.'''\n    pass",
            "explanation": "This function does foo stuff.",
        })

        mock_model = MagicMock()
        mock_model.generate_content.return_value = MagicMock(text=mock_response_text)

        with patch("services.ai_service.model", mock_model):
            from services.ai_service import generate_documentation
            result = await generate_documentation("Python", "def foo(): pass", "google")

        assert "'''Does foo stuff.'''" in result["documented_code"]
        assert result["explanation"] == "This function does foo stuff."

    @pytest.mark.asyncio
    async def test_generate_docs_fallback_when_no_model(self):
        """Without a model, docs generation returns mock output"""
        with patch("services.ai_service.model", None):
            from services.ai_service import generate_documentation
            result = await generate_documentation("Python", "def foo(): pass", "google")

        assert "documented_code" in result
        assert "explanation" in result


class TestAuthUtils:
    """Unit tests for auth utility functions"""

    def test_password_hash_is_not_plaintext(self):
        """Hashed password should not equal the original"""
        from auth import hash_password
        hashed = hash_password("mysecretpassword")
        assert hashed != "mysecretpassword"
        assert len(hashed) > 20  # bcrypt hashes are long

    def test_password_verification_correct(self):
        """Correct password verifies successfully"""
        from auth import hash_password, verify_password
        hashed = hash_password("correct_password")
        assert verify_password("correct_password", hashed) is True

    def test_password_verification_wrong(self):
        """Wrong password fails verification"""
        from auth import hash_password, verify_password
        hashed = hash_password("correct_password")
        assert verify_password("wrong_password", hashed) is False

    def test_create_access_token_returns_string(self):
        """Token creation should return a non-empty string"""
        from auth import create_access_token
        token = create_access_token(data={"sub": "user@example.com"})
        assert isinstance(token, str)
        assert len(token) > 50

    def test_decode_token_returns_email(self):
        """Decoded token should return the original email"""
        from auth import create_access_token, decode_token
        email = "decode_test@example.com"
        token = create_access_token(data={"sub": email})
        decoded = decode_token(token)
        assert decoded == email

    def test_decode_invalid_token_returns_none(self):
        """Tampered/invalid token should return None, not raise an exception"""
        from auth import decode_token
        result = decode_token("this.is.garbage")
        assert result is None

    def test_decode_empty_token_returns_none(self):
        """Empty token should return None"""
        from auth import decode_token
        result = decode_token("")
        assert result is None
