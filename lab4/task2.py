def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 0  # As per your example: 0! = 0
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Example usage
num = int(input("Enter a number: "))
print(f"{num}! =", factorial(num))