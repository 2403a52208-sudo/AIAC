def convert_temperature():
    """
    Convert temperature between Celsius and Fahrenheit based on user input.
    Prompts the user for the temperature value and the conversion direction.
    """
    try:
        value = float(input("Enter the temperature value: "))
        direction = input("Convert from (C)elsius or (F)ahrenheit? Enter 'C' or 'F': ").strip().upper()
        if direction == 'C':
            fahrenheit = (value * 9/5) + 32
            print(f"{value}°C is {fahrenheit}°F")
        elif direction == 'F':
            celsius = (value - 32) * 5/9
            print(f"{value}°F is {celsius}°C")
        else:
            print("Invalid conversion direction. Please enter 'C' or 'F'.")
    except ValueError:
        print("Please enter a valid number for the temperature value.")

if __name__ == "__main__":
    convert_temperature()
