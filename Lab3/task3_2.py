def calculate_electricity_bill(units, rate_per_unit):
    """
    Calculate the total electricity bill based on units consumed and a fixed rate per unit.

    Parameters:
    units (float or int): Number of electricity units consumed.
    rate_per_unit (float): Fixed rate per unit.

    Returns:
    float: Total electricity bill.
    """
    if units < 0:
        raise ValueError("Units consumed cannot be negative.")
    if rate_per_unit < 0:
        raise ValueError("Rate per unit cannot be negative.")
    return units * rate_per_unit

if __name__ == "__main__":
    try:
        units = float(input("Enter the number of electricity units consumed: "))
        rate = float(input("Enter the fixed rate per unit: "))
        if units < 0 or rate < 0:
            print("Units and rate per unit must be non-negative.")
        else:
            total_bill = calculate_electricity_bill(units, rate)
            print(f"Total electricity bill for {units} units at Rs. {rate} per unit: Rs. {total_bill:.2f}")
    except ValueError:
        print("Please enter valid numbers for units and rate per unit.")
