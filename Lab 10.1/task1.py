# Calculate average score of a student
def calc_average(marks):
    """
    Calculate the average score from a list of marks.
    
    Args:
        marks: List of numeric scores
        
    Returns:
        float: Average score
    """
    total = 0
    for m in marks:
        total += m
    average = total / len(marks)
    return average  # Fixed typo: 'avrage' -> 'average'

marks = [85, 90, 78, 92]
print("Average Score is", calc_average(marks))  # Added missing closing parenthesis)

