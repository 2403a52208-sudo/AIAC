# Readability Enhancement  the code with descriptive variable names, 
# inline comments, and clear formatting with types hints

"""Module for calculating percentage with enhanced readability."""

from typing import Union
def calculate_percentage(principal_amount: Union[int, float], percentage_rate: Union[int, float]) -> float:
    """
    Calculate the percentage value of a given amount.
    This function computes what percentage of the principal amount represents
    based on the given percentage rate.
    Args:
        principal_amount: The base amount to calculate percentage from.
        percentage_rate: The percentage rate to apply (e.g., 15 for 15%).
    Returns:
        float: The calculated percentage value.
        
    Example:
        >>> calculate_percentage(200, 15)
        30.0
    """
    # Calculate percentage: (principal_amount * percentage_rate) / 100
    percentage_value = principal_amount * percentage_rate / 100
    
    return percentage_value
if __name__ == "__main__":
    # Example usage with descriptive variable names
    base_amount = 200      # The principal amount
    rate_percentage = 15   # The percentage rate (15%)
    
    # Calculate and display the percentage value
    result = calculate_percentage(base_amount, rate_percentage)
    print(f"Percentage calculation: {base_amount} * {rate_percentage}% = {result}")
