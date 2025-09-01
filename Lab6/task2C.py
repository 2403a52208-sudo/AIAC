def print_multiples_for_loop(number):
    print("Using For Loop:")
    print("First 10 multiples of", number, "are:")
    for i in range(1, 11):
        multiple = number * i
        print(number, "x", i, "=", multiple)
def print_multiples_while_loop(number):
    print("\nUsing While Loop:")
    print("First 10 multiples of", number, "are:")
    i = 1
    while i <= 10:
        multiple = number * i
        print(number, "x", i, "=", multiple)
        i = i + 1
# Main program
if __name__ == "__main__":
    print("Welcome to Multiples Calculator!")
    print("This program will show you the first 10 multiples of any number.")
    # Get input from user
    number = int(input("Enter a number: "))
    print()
    print("=" * 30)
    # Call function with for loop
    print_multiples_for_loop(number)
    # Call function with while loop
    print_multiples_while_loop(number)
    print("=" * 30)
    print("Program completed!")
