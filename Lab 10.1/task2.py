def area_of_rectangle(length: int, breadth: int) -> int:
    """
    Calculate the area of a rectangle using integer values.

    Args:
        length (int): The length of the rectangle (integer).
        breadth (int): The breadth (width) of the rectangle (integer).

    Returns:
        int: The area of the rectangle as an integer.

    Example:
        >>> area_of_rectangle(5, 3)
        15
    """
    # Multiply length by breadth to get the area (integers only)
    return length * breadth

# Hint: Use area_of_rectangle(length, breadth) with integer arguments to compute the area.
# Example usage:
print(area_of_rectangle(10, 20))  # Output: 200