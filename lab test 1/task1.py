def factorial_febo(n):
    # Calculate factorial of n
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    # Generate Fibonacci series up to n terms
    fibo_series = []
    a, b = 0, 1
    for _ in range(n):
        fibo_series.append(a)
        a, b = b, a + b

    return factorial, fibo_series

# Example call
n = 5
result = factorial_febo(n)
print(f"Factorial of {n}: {result[0]}")
print(f"Fibonacci series up to {n} terms: {result[1]}")
