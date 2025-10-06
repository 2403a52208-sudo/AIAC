def main():
    """
    Takes user input for numbers and prints their squares using list comprehension.
    """

    try:
        # Take user input (comma-separated numbers)
        user_input = input("Enter numbers separated by commas: ").strip()
        if not user_input:
            print("No input provided.")
            return
        
        # Convert input string to list of integers
        nums = [int(x.strip()) for x in user_input.split(",") if x.strip() != ""]

        if not nums:
            print("No numbers provided.")
            return

        # Efficient way using list comprehension
        squares = [n * n for n in nums]

        print(f"\nOriginal Numbers: {nums}")
        print(f"Squares: {squares}")

    except ValueError:
        print("Invalid input! Please enter only numbers separated by commas.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
