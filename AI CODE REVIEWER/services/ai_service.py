# ─────────────────────────────────────────────
# services/ai_service.py
#
# LEARNING NOTE:
# This is where we talk to the Gemini AI API.
#
# Key concepts:
#   - Prompt Engineering: carefully wording instructions so the AI
#     returns exactly what we need (structured JSON in our case)
#   - Structured Outputs: asking the AI to respond in a specific JSON
#     format that our app can reliably parse
#   - Graceful fallback: if no API key is provided, we return mock data
#     so the rest of the app still works for learning purposes
# ─────────────────────────────────────────────

import os
import json
import re
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# Only import and configure Gemini if we have an API key
if GEMINI_API_KEY:
    try:
        import google.generativeai as genai
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel("gemini-2.5-flash")
        print("[AI Service] Gemini AI connected ✅")
    except Exception as e:
        print(f"[AI Service] Gemini import failed: {e}. Using mock mode.")
        model = None
else:
    print("[AI Service] No GEMINI_API_KEY found — using mock mode")
    model = None


def _clean_json_response(text: str) -> str:
    """
    Remove markdown code fences (```json ... ```) that Gemini sometimes wraps around responses.
    We need pure JSON to parse it.
    """
    # Remove ```json ... ``` or ``` ... ``` wrappers
    text = re.sub(r"```(?:json)?\n?", "", text)
    text = text.strip().strip("`")
    return text


async def analyze_code(language: str, code: str) -> Dict[str, Any]:
    """
    Send code to Gemini AI and get back a structured review.

    The prompt is carefully engineered to return ONLY valid JSON
    in the exact shape our schemas expect.
    """

    # If no API key, return realistic mock data
    if not model:
        return _mock_review(language, code)

    # ── PROMPT ENGINEERING ────────────────────────────────────────
    # Notice how we:
    #  1. Set clear role/context ("You are an expert code reviewer")
    #  2. Specify exact output format (JSON schema)
    #  3. Give examples of severity values
    #  4. Tell it NOT to add extra commentary
    prompt = f"""You are an expert code reviewer. Analyze the following {language} code and return ONLY a valid JSON object — no markdown, no explanation, just the JSON.

The JSON must match this exact structure:
{{
  "bugs": [
    {{"description": "string", "line_hint": "string or null", "severity": "low|medium|high"}}
  ],
  "optimizations": [
    {{"description": "string", "impact": "low|medium|high"}}
  ],
  "best_practices": [
    {{"description": "string", "category": "string"}}
  ],
  "overall_score": <integer 0-100>,
  "summary": "2-3 sentence plain English summary of the code quality"
}}

Rules:
- overall_score: 100 = perfect, 0 = terrible. Be honest and calibrated.
- If there are no bugs/optimizations/practices, return empty arrays [].
- Return at most 5 items per category.
- line_hint should reference the relevant line number or function name if visible.

Code to review ({language}):
```
{code}
```"""

    try:
        response = model.generate_content(prompt)
        raw = _clean_json_response(response.text)
        result = json.loads(raw)
        return result
    except (json.JSONDecodeError, Exception) as e:
        # If the AI response is unparseable, return a fallback
        print(f"[AI Service] Error parsing Gemini response: {e}")
        return _mock_review(language, code)


async def generate_documentation(language: str, code: str, doc_style: str) -> Dict[str, Any]:
    """
    Ask Gemini to add documentation/docstrings to the provided code.
    """
    if not model:
        return _mock_docs(language, code)

    style_guide = {
        "google": "Google-style docstrings (for Python)",
        "numpy": "NumPy-style docstrings (for Python)",
        "jsdoc": "JSDoc comments (for JavaScript/TypeScript)",
    }.get(doc_style, "standard docstrings")

    prompt = f"""You are a technical documentation expert. Add {style_guide} to the following {language} code.

Return ONLY a JSON object with this exact structure:
{{
  "documented_code": "the full code with documentation added",
  "explanation": "1-2 sentences explaining what the code does"
}}

Original code:
```
{code}
```"""

    try:
        response = model.generate_content(prompt)
        raw = _clean_json_response(response.text)
        return json.loads(raw)
    except Exception as e:
        print(f"[AI Service] Documentation error: {e}")
        return _mock_docs(language, code)


# ── Mock Data (used when no API key is provided) ──────────────────

def _mock_review(language: str, code: str) -> Dict[str, Any]:
    """
    Returns realistic-looking mock review data.
    This lets you use and learn the full app without an API key.
    """
    return {
        "bugs": [
            {
                "description": "Potential null/undefined reference — always check if a value exists before using it.",
                "line_hint": "Line 5",
                "severity": "high"
            },
            {
                "description": "Missing error handling — exceptions from this block are not caught.",
                "line_hint": "Line 12",
                "severity": "medium"
            }
        ],
        "optimizations": [
            {
                "description": "Consider caching the result of this computation if it's called repeatedly.",
                "impact": "high"
            },
            {
                "description": "Use a list comprehension instead of a for loop for more Pythonic, faster code.",
                "impact": "low"
            }
        ],
        "best_practices": [
            {
                "description": "Add type hints to function parameters and return values for better readability.",
                "category": "Type Safety"
            },
            {
                "description": "Function is doing too many things — consider splitting into smaller, single-purpose functions.",
                "category": "SOLID Principles"
            },
            {
                "description": "Magic numbers (e.g., 42, 100) should be named constants for clarity.",
                "category": "Readability"
            }
        ],
        "overall_score": 62,
        "summary": f"This is a mock AI review (no Gemini API key found). The {language} code has a couple of common issues around error handling and null checks. With some refactoring it could be significantly more robust and maintainable."
    }


def _mock_docs(language: str, code: str) -> Dict[str, Any]:
    return {
        "documented_code": f"# Mock documentation (add GEMINI_API_KEY to .env for real docs)\n{code}",
        "explanation": "This is a mock documentation response. Add your Gemini API key to .env to get real AI-generated documentation."
    }
