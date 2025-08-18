def calculate_electricity_bill(units):
    """
    Calculate the total electricity bill based on units consumed.
    Slabs:
    - For first 100 units: Rs. 1.5/unit
    - For next 100 units (101-200): Rs. 2.5/unit
    - For next 100 units (201-300): Rs. 4/unit
    - Above 300 units: Rs. 6/unit
    """
    if units < 0:
        raise ValueError("Units consumed cannot be negative.")

    bill = 0.0
    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = (100 * 1.5) + ((units - 100) * 2.5)
    elif units <= 300:
        bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4)
    else:
        bill = (100 * 1.5) + (100 * 2.5) + (100 * 4) + ((units - 300) * 6)
    return bill

if __name__ == "__main__":
    try:
        units = float(input("Enter the number of electricity units consumed: "))
        if units < 0:
            print("Units consumed cannot be negative.")
        else:
            total_bill = calculate_electricity_bill(units)
            print(f"Total electricity bill for {units} units: Rs. {total_bill:.2f}")
    except ValueError:
        print("Please enter a valid number for units consumed.")
