from typing import Callable, Dict, Optional, Tuple
def legacy_calculate(operation: str, a: int, b: int) -> Optional[int]:
    """
    Legacy approach using an if-elif chain for basic arithmetic operations.
    """
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    else:
        return None
def refactored_calculate(operation: str, a: int, b: int) -> Optional[int]:
    """
    Refactored approach using a dictionary mapping of operation names to callables.
    Unknown operations return None.
    """
    operations: Dict[str, Callable[[int, int], int]] = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
    }
    func = operations.get(operation)
    return func(a, b) if func else None
def get_user_inputs() -> Tuple[str, int, int]:
    """
    Get operation and operands from user input with sensible defaults.
    Defaults chosen to match expected example: multiply 5 and 3 -> 15.
    """
    print("Enter operation (add, subtract, multiply). Press Enter for default: multiply")
    op = input().strip().lower()
    if not op:
        op = "multiply"

    print("Enter two integers separated by space. Press Enter for default: 5 3")
    nums = input().strip()
    if not nums:
        return op, 5, 3
    try:
        a_str, b_str = nums.split()
        a, b = int(a_str), int(b_str)
    except Exception:
        print("Invalid input. Using defaults: 5 3")
        a, b = 5, 3
    return op, a, b
def main():
    print("=== Operation Selector Refactor ===")
    print("This program compares if-elif vs dict mapping for operation dispatch.")
    print()

    operation, a, b = get_user_inputs()
    print(f"\nInputs -> operation: {operation}, a: {a}, b: {b}")

    legacy_result = legacy_calculate(operation, a, b)
    refactored_result = refactored_calculate(operation, a, b)

    print(f"Legacy result: {legacy_result}")
    print(f"Refactored result: {refactored_result}")

    if legacy_result == refactored_result:
        print(" Results match.")
    else:
        print(" Results differ - there may be an issue.")

    if operation == "multiply" and a == 5 and b == 3:
        print("Expected Output:\n15")
if __name__ == "__main__":
    main()


