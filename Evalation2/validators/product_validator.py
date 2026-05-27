import re


def validate_product_name(value: str):
    if len(value.strip()) < 3:
        raise ValueError("Product name must contain at least 3 characters")

    if not re.match(r"^[A-Za-z0-9 ]+$", value):
        raise ValueError("Special characters are not allowed in product name")

    return value