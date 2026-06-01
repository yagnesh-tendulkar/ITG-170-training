"""
Reusable validation utilities for the Employee HR Management System.

This module provides small, testable functions suitable for use in Pydantic
validators, service-layer checks, and route guards.

Design goals:
- Fast, deterministic checks using compiled regexes where appropriate.
- Clear, typed return values (`bool`) so functions are easy to compose.
- Defensive handling of edge-cases (None, wrong types, invalid formats).
"""
from __future__ import annotations

import logging
import math
import re
from datetime import date, datetime
from typing import Any, Optional, Union

import numbers

logger = logging.getLogger("app.validators")

# Pre-compiled regex patterns for performance and reuse
_EMAIL_REGEX = re.compile(r"^[A-Za-z0-9_.+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9-.]+$")
_PHONE_REGEX = re.compile(r"^\+?\d{10,15}$")
_UPPERCASE_REGEX = re.compile(r"[A-Z]")
_LOWERCASE_REGEX = re.compile(r"[a-z]")
_DIGIT_REGEX = re.compile(r"\d")
_SPECIAL_CHAR_REGEX = re.compile(r"[^A-Za-z0-9]")


def validate_email(email: str) -> bool:
    """
    Validate an email address using a conservative regex.

    This function intentionally uses a pragmatic regex rather than a full
    RFC5322 implementation because most applications only need a
    reasonably strict format check; complex email validation should be
    delegated to a delivery/verification step or a dedicated library.

    Args:
        email: Email address to validate.

    Returns:
        True if `email` looks like a valid address, False otherwise.
    """
    if not email or not isinstance(email, str):
        return False
    try:
        return _EMAIL_REGEX.match(email) is not None
    except Exception:
        logger.exception("Unexpected error validating email: %s", email)
        return False


def validate_phone(phone: str) -> bool:
    """
    Validate international phone numbers with optional leading plus.

    Rules:
    - Optional leading '+'
    - 10 to 15 digits total (typical range for international numbers)

    Args:
        phone: Phone string to validate (may include leading '+').

    Returns:
        True if phone matches pattern, False otherwise.
    """
    if not phone or not isinstance(phone, str):
        return False
    try:
        normalized = phone.strip()
        return _PHONE_REGEX.match(normalized) is not None
    except Exception:
        logger.exception("Unexpected error validating phone: %s", phone)
        return False


def validate_password_strength(password: str) -> bool:
    """
    Enforce password strength rules.

    Requirements:
    - Minimum 8 characters
    - At least 1 uppercase letter
    - At least 1 lowercase letter
    - At least 1 digit
    - At least 1 special character (non-alphanumeric)

    Args:
        password: The plain-text password to validate.

    Returns:
        True if password meets all requirements, False otherwise.
    """
    if not password or not isinstance(password, str):
        return False

    if len(password) < 8:
        return False

    try:
        if _UPPERCASE_REGEX.search(password) is None:
            return False
        if _LOWERCASE_REGEX.search(password) is None:
            return False
        if _DIGIT_REGEX.search(password) is None:
            return False
        if _SPECIAL_CHAR_REGEX.search(password) is None:
            return False
        return True
    except Exception:
        logger.exception("Unexpected error validating password strength")
        return False


def _to_date(obj: Union[date, datetime, str]) -> Optional[date]:
    """
    Helper to coerce supported types to a `date` object.

    Accepts `date`, `datetime`, or ISO-formatted `str`.
    Returns None for unsupported or unparsable values.
    """
    if obj is None:
        return None
    if isinstance(obj, date) and not isinstance(obj, datetime):
        return obj
    if isinstance(obj, datetime):
        return obj.date()
    if isinstance(obj, str):
        try:
            # Accept ISO 8601-ish strings
            parsed = datetime.fromisoformat(obj)
            return parsed.date()
        except Exception:
            # Fallback: try parsing as YYYY-MM-DD
            try:
                parts = obj.split("-")
                if len(parts) == 3:
                    y, m, d = map(int, parts)
                    return date(y, m, d)
            except Exception:
                return None
    return None


def validate_date_range(start_date: Union[date, datetime, str], end_date: Union[date, datetime, str]) -> bool:
    """
    Validate that `start_date` is not after `end_date`.

    Accepts date/datetime objects or ISO-formatted strings. Returns False
    for unparsable inputs.

    Args:
        start_date: Start date (date, datetime, or ISO string).
        end_date: End date (date, datetime, or ISO string).

    Returns:
        True if start_date <= end_date, False otherwise.
    """
    s = _to_date(start_date)
    e = _to_date(end_date)
    if s is None or e is None:
        return False
    return s <= e


def validate_positive_number(value: Union[int, float]) -> bool:
    """
    Validate that a number is positive (>= 0) and finite.

    Args:
        value: Numeric value to check.

    Returns:
        True if value is a real number and >= 0; False otherwise.
    """
    if value is None:
        return False
    if not isinstance(value, numbers.Real):
        return False
    # Reject NaN and infinities
    try:
        if not math.isfinite(value):
            return False
    except Exception:
        return False
    return value >= 0


__all__ = [
    "validate_email",
    "validate_phone",
    "validate_password_strength",
    "validate_date_range",
    "validate_positive_number",
]
