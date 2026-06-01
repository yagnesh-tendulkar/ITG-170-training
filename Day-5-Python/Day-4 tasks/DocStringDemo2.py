def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Parameters:
        numbers (list): A list containing integer or float values.

    Returns:
        float: The average of all numbers in the list.

    Raises:
        ValueError: If the list is empty.

    Example:
        >>> calculate_average([10, 20, 30])
        20.0
    """

    if not numbers:
        raise ValueError("List cannot be empty")

    return sum(numbers) / len(numbers)


print(calculate_average([10, 20, 30]))