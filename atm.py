def rectangle_area(length: float | int, width: float | int) -> float:
    """
    Calculate the area of a rectangle.

    Args:
        length (float | int): Length of the rectangle (must be non-negative)
        width (float | int): Width of the rectangle (must be non-negative)

    Returns:
        float: Area of the rectangle

    Raises:
        TypeError: If inputs are not numeric (int or float)
        ValueError: If any dimension is negative

    Example:
        >>> rectangle_area(4, 5)
        20
    """

    # Type validation
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError("Length and width must be numbers (int or float)")

    # Value validation
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")

    return float(length * width)
