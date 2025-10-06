"""
Task 1: Square Numbers Calculator
This program demonstrates two approaches to calculate squares of numbers:
1. Legacy approach using a for loop
2. Refactored approach using list comprehension
"""
from typing import List
def legacy_task1(nums: List[int]) -> List[int]:
    """
    Calculate squares using traditional for loop approach.
    
    Args:
        nums (List[int]): List of integers to square
        
    Returns:
        List[int]: List of squared numbers
    """
    squares = []
    for i in nums:
        squares.append(i * i)
    return squares

def refactored_task1(nums: List[int]) -> List[int]:
    """
    Calculate squares using Pythonic list comprehension.
    More concise and readable approach.
    
    Args:
        nums (List[int]): List of integers to square
        
    Returns:
        List[int]: List of squared numbers
    """
    return [x * x for x in nums]

def get_user_input() -> List[int]:
    """
    Get a list of numbers from user input.
   
    Returns:
        List[int]: List of integers entered by user
    """
    print("Enter numbers separated by spaces (e.g., 1 2 3 4 5):")
    try:
        # Get input from user and convert to list of integers
        user_input = input().strip()
        if not user_input:
            print("No input provided. Using default numbers: 1, 2, 3, 4, 5")
            return [1, 2, 3, 4, 5]
        
        # Split input by spaces and convert each to integer
        nums = [int(x) for x in user_input.split()]
        return nums
    except ValueError:
        print("Invalid input. Please enter only numbers separated by spaces.")
        print("Using default numbers: 1, 2, 3, 4, 5")
        return [1, 2, 3, 4, 5]

def main():
    """
    Main function to run the square calculator program.
    """
    print("=== Square Numbers Calculator ===")
    print("This program calculates the square of each number you provide.")
    print()
    
    # Get numbers from user
    numbers = get_user_input()
    
    # Calculate squares using both methods
    print(f"\nInput numbers: {numbers}")
    
    # Using legacy approach
    legacy_result = legacy_task1(numbers)
    print(f"Squares (Legacy method): {legacy_result}")
    
    # Using refactored approach
    refactored_result = refactored_task1(numbers)
    print(f"Squares (Refactored method): {refactored_result}")
    
    # Verify both methods give the same result
    if legacy_result == refactored_result:
        print(" Both methods produce identical results!")
    else:
        print(" Methods produce different results - there's an issue!")

# Run the program when this file is executed
if __name__ == "__main__":
    main()
