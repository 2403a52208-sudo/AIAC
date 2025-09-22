def grade(score: int) -> str:
    """
    Return the letter grade for a given score.

    Args:
        score (int): The numeric score (0-100).

    Returns:
        str: The letter grade ("A", "B", "C", "D", or "F").
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Get user input and print the grade
try:
    user_score = int(input("Enter the score (0-100): "))
    if 0 <= user_score <= 100:
        print(f"Grade: {grade(user_score)}")
    else:
        print("Please enter a score between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter an integer value.")