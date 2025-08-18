def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.

    Parameters:
    n (int): The number to compute the factorial of. Must be non-negative.

    Returns:
    int: The factorial of n.

    Raises:
    ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    try:
        num = int(input("Enter a number to calculate its factorial: "))
        print(f"The factorial of {num} is {factorial(num)}")
    except ValueError as e:
        print(f"Error: {e}")
