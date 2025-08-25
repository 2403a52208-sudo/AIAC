def is_valid_indian_mobile(number: str) -> bool:
    """
    Validates an Indian mobile number.
    Checks if the number starts with 6, 7, 8, or 9 and has exactly 10 digits.
    """
    return (
        len(number) == 10 and
        number.isdigit() and
        number[0] in {'6', '7', '8', '9'}
    )

# Example usage:
user_number = input("Enter an Indian mobile number: ")
if is_valid_indian_mobile(user_number):
    print("Valid Indian mobile number.")
else:
    print("Invalid Indian mobile number.")