def celsius_to_fahrenheit_and_kelvin(celsius):
    """
    Convert Celsius temperature to both Fahrenheit and Kelvin.

    Parameters:
    celsius (float or int): Temperature in Celsius.

    Returns:
    tuple: (fahrenheit, kelvin)
    """
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

# Example usage
if __name__ == "__main__":
    try:
        c = float(input("Enter temperature in Celsius: "))
        f, k = celsius_to_fahrenheit_and_kelvin(c)
        print(f"{c}°C is {f}°F and {k}K")
    except ValueError:
        print("Please enter a valid number for Celsius temperature.")
