# Type hints example
def max_number(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:

# Complete docstring with examples
"""
Calculate the area of a rectangle.

Args:
    length (Union[int, float]): Length of the rectangle
    width (Union[int, float]): Width of the rectangle

Returns:
    Union[int, float]: Area of the rectangle

Raises:
    TypeError: If inputs are not numeric
    ValueError: If dimensions are negative

Example:
    >>> rectangle_area(4, 5)
    20
"""

# Error handling
if not isinstance(length, (int, float)):
    raise TypeError("❌ Length and width must be numbers")
