from typing import List
def legacy_search(items: List[int], target: int) -> bool:
    """
    Legacy approach using a loop to find target in items.
    """
    found = False
    for value in items:
        if value == target:
            found = True
            break
    return found
def refactored_search(items: List[int], target: int) -> bool:
    """
    Refactored approach using Python's `in` for membership testing.
    """
    return target in items
def get_user_list_and_target() -> (List[int], int):
    """
    Get a list of integers and a target integer from the user.
    Defaults chosen to match example: items=[10,20,30,40,50], target=30.
    """
    print("Enter numbers separated by spaces (default: 10 20 30 40 50):")
    items_input = input().strip()
    if not items_input:
        items = [10, 20, 30, 40, 50]
    else:
        try:
            items = [int(x) for x in items_input.split()]
        except Exception:
            print("Invalid list. Using default: 10 20 30 40 50")
            items = [10, 20, 30, 40, 50]

    print("Enter target integer to search (default: 30):")
    target_input = input().strip()
    if not target_input:
        target = 30
    else:
        try:
            target = int(target_input)
        except Exception:
            print("Invalid target. Using default: 30")
            target = 30

    return items, target
def main():
    print("=== Optimized Search Demo ===")
    print("This program compares manual loop search vs Python's `in`.")
    print()

    items, target = get_user_list_and_target()
    print(f"\nInputs -> items: {items}, target: {target}")

    legacy_result = legacy_search(items, target)
    refactored_result = refactored_search(items, target)

    print("Legacy:", "Found" if legacy_result else "Not Found")
    print("Refactored:", "Found" if refactored_result else "Not Found")

    if legacy_result == refactored_result:
        print(" Results match.")
    else:
        print(" Results differ - there may be an issue.")

    if items == [10, 20, 30, 40, 50] and target == 30:
        print("Expected Output:\nFound")
if __name__ == "__main__":
    main()


