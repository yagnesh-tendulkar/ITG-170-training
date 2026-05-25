from datetime import datetime
def generate_password(fname: str, lname: str, joining_date: datetime) -> str:
    """
    Format:
    last 2 letters of first name +
    first 2 letters of last name +
    hour + minute + day

    Example:
    Amrita Pattanayak, 10:00 24th -> tapa100024
    
    """

    return (
        fname[-2:].lower()
        + lname[:2].lower()
        + joining_date.strftime("%H%M%d")
    )