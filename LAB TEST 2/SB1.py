def parse_time(time_str):
    """Parses HH:MM string and returns (hour, minute) as integers."""
    try:
        hour, minute = map(int, time_str.strip().split(":"))
        if 0 <= hour < 24 and 0 <= minute < 60:
            return hour, minute
        else:
            raise ValueError
    except Exception:
        print("Invalid time format. Please enter time as HH:MM in 24-hour format.")
        return None

def is_surge(hour, minute):
    """Returns True if time is after 18:00 strictly."""
    return (hour > 18) or (hour == 18 and minute > 0)

def main():
    base_per_km = 10

    time_str = input("Enter ride time (HH:MM, 24-hour format): ")
    parsed_time = parse_time(time_str)
    while parsed_time is None:
        time_str = input("Enter ride time (HH:MM, 24-hour format): ")
        parsed_time = parse_time(time_str)
    hour, minute = parsed_time

    while True:
        km_str = input("Enter distance in km: ")
        try:
            km = float(km_str)
            if km < 0:
                print("Distance cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid distance. Please enter a number.")

    if is_surge(hour, minute):
        surgeMultiplier = 2
    else:
        surgeMultiplier = 1

    fare = km * base_per_km * surgeMultiplier
    print(f"Fare: {fare:.2f}")

if __name__ == "__main__":
    main()

