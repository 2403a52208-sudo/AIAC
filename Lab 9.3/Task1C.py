def sum_even_odd_numbers():
    """
    Function to calculate the sum of even and odd numbers in a list.
    Takes user input for the list elements.
    Returns a tuple containing (sum_of_even, sum_of_odd).
    """
    # Get user input for the list
    print("Enter numbers separated by spaces:")
    user_input = input().strip()
    
    # Convert input string to list of integers
    try:
        numbers = [int(x) for x in user_input.split()]
    except ValueError:
        print("Error: Please enter only valid integers.")
        return None, None
    
    # Initialize sums
    sum_even = 0
    sum_odd = 0
    
    # Calculate sums
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    
    return sum_even, sum_odd

# Example usage
if __name__ == "__main__":
    even_sum, odd_sum = sum_even_odd_numbers()
    
    if even_sum is not None and odd_sum is not None:
        print(f"Sum of even numbers: {even_sum}")
        print(f"Sum of odd numbers: {odd_sum}")
        print(f"Total sum: {even_sum + odd_sum}")
