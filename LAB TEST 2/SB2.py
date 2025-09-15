def rolling_mean(xs, w):
    """
    Computes the rolling mean of list xs with window size w.
    Returns a list of means.
    """
    means = []
    # The correct range is len(xs) - w + 1 to include the last window
    for i in range(len(xs) - w + 1):
        window = xs[i:i+w]
        means.append(sum(window) / w)
    return means

# Get user input for the list of numbers
xs_input = input("Enter numbers separated by commas (e.g., 1,2,3,4): ")
xs = [float(x.strip()) for x in xs_input.split(",")]

# Get user input for window size
while True:
    try:
        w = int(input("Enter window size (positive integer): "))
        if w <= 0 or w > len(xs):
            print("Window size must be positive and less than or equal to the length of the list.")
            continue
        break
    except ValueError:
        print("Please enter a valid integer for window size.")

result = rolling_mean(xs, w)
print("Rolling means:", result)
