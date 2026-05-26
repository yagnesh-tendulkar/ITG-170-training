import random
import string

def generate_email(first_name: str, last_name: str) -> str:
    """Generate company email"""
    return f"{first_name.lower()}.{last_name.lower()}@company.com"

def generate_password(first_name: str, last_name: str) -> str:
    """Generate temporary password"""
    base = (first_name[:3] + last_name[:3]).lower()
    digits = ''.join(random.choices(string.digits, k=4))
    return base + digits + "@2025"