def sort_numbers(numbers):
    """
    Sort a list of numbers in ascending order.

    Parameters:
    numbers (list): A list of numbers to sort.

    Returns:
    list: A new list containing the sorted numbers.
    """
    return sorted(numbers)

if __name__ == "__main__":
    # Example input-output prompt
    example_input = [5, 2, 9, 1, 5, 6]
    print("Input:", example_input)
    print("Output:", sort_numbers(example_input))
