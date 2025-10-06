import math

# Define separate functions for each shape
def area_rectangle(length, width):
    return length * width

def area_square(side):
    return side * side

def area_circle(radius):
    return math.pi * radius * radius

# Dictionary mapping shape names to functions
area_functions = {
    "rectangle": area_rectangle,
    "square": area_square,
    "circle": area_circle
}

# Function to calculate area using dictionary-based dispatch
def calculate_area(shape, x, y=0):
    shape = shape.lower()
    # Check if shape is rectangle - requires both length and width
    if shape == "rectangle":
        return area_functions[shape](x, y)
    # Check if shape is square or circle - requires only one dimension
    elif shape in ["square", "circle"]:
        return area_functions[shape](x)
    # Handle invalid shape input
    else:
        raise ValueError("Unknown shape! Please enter rectangle, square, or circle.")

# Main function to take user input
def main():
    print("Shapes available: rectangle, square, circle")
    shape = input("Enter shape: ").strip()
    # Get dimensions for rectangle (length and width)
    if shape.lower() == "rectangle":
        x = float(input("Enter length: "))
        y = float(input("Enter width: "))
    # Get single dimension for square (side) or circle (radius)
    elif shape.lower() in ["square", "circle"]:
        x = float(input("Enter side/radius: "))
        y = 0
    # Exit if invalid shape is entered
    else:
        print("Unknown shape! Exiting.")
        return

    # Calculate and display the area, handling any errors
    try:
        area = calculate_area(shape, x, y)
        print(f"The area of the {shape} is: {area:.2f}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
