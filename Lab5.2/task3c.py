def fibonacci_iterative(n):
    """
    Calculate the nth Fibonacci number using an iterative approach.

    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).

    Returns:
        int: The nth Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# Example usage with other numbers:
print(fibonacci_iterative(7))  # Output: 13
print(fibonacci_iterative(10))  # Output: 55
