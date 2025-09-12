def add_numbers():
    """
    Function to add two numbers entered by the user.
    Returns the sum of the two numbers.
    """
    # Get first number from user input
    print("Enter the first number:")
    num1 = float(input())  # Convert input to float to handle decimals
    
    # Get second number from user input
    print("Enter the second number:")
    num2 = float(input())  # Convert input to float to handle decimals
    
    # Calculate and return the sum
    result = num1 + num2
    return result

def subtract_numbers():
    """
    Function to subtract two numbers entered by the user.
    Returns the difference of the two numbers.
    """
    # Get first number from user input
    print("Enter the first number:")
    num1 = float(input())  # Convert input to float to handle decimals
    
    # Get second number from user input
    print("Enter the second number:")
    num2 = float(input())  # Convert input to float to handle decimals
    
    # Calculate and return the difference
    result = num1 - num2
    return result

def multiply_numbers():
    """
    Function to multiply two numbers entered by the user.
    Returns the product of the two numbers.
    """
    # Get first number from user input
    print("Enter the first number:")
    num1 = float(input())  # Convert input to float to handle decimals
    
    # Get second number from user input
    print("Enter the second number:")
    num2 = float(input())  # Convert input to float to handle decimals
    
    # Calculate and return the product
    result = num1 * num2
    return result

def divide_numbers():
    """
    Function to divide two numbers entered by the user.
    Returns the quotient of the two numbers.
    Handles division by zero error.
    """
    # Get first number from user input
    print("Enter the first number:")
    num1 = float(input())  # Convert input to float to handle decimals
    
    # Get second number from user input
    print("Enter the second number:")
    num2 = float(input())  # Convert input to float to handle decimals
    
    # Check for division by zero
    if num2 == 0:
        print("Error: Cannot divide by zero!")
        return None  # Return None to indicate error
    
    # Calculate and return the quotient
    result = num1 / num2
    return result

# Main program execution
if __name__ == "__main__":
    # Display calculator menu
    print("=" * 30)
    print("SIMPLE CALCULATOR")
    print("=" * 30)
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("=" * 30)
    
    # Get user choice
    choice = input("Enter choice (1/2/3/4): ").strip()
    
    # Perform operation based on user choice
    if choice == "1":
        # Call add function and display result
        result = add_numbers()
        print(f"Result: {result}")
    elif choice == "2":
        # Call subtract function and display result
        result = subtract_numbers()
        print(f"Result: {result}")
    elif choice == "3":
        # Call multiply function and display result
        result = multiply_numbers()
        print(f"Result: {result}")
    elif choice == "4":
        # Call divide function and display result
        result = divide_numbers()
        if result is not None:  # Check if division was successful
            print(f"Result: {result}")
    else:
        # Display error message for invalid choice
        print("Invalid choice! Please enter 1, 2, 3, or 4.")

