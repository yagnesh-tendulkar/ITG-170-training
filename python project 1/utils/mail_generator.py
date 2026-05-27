def generate_corporate_email(fname: str, lname: str) -> str:
    """
    Format: first letter of fname + lastname@miraclesoft.com
    Example: Amrita Pattanayak -> apattanayak@miraclesoft.com
    """

    return f"{fname[0].lower()}{lname.lower()}@miraclesoft.com"