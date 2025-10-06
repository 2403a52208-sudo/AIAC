from typing import Dict, Optional
def legacy_lookup(student_scores: Dict[str, int], name: str) -> str:
    """
    Legacy approach using explicit membership check and direct indexing.
    Returns score as string, or "Not Found" if the key is missing.
    """
    if name in student_scores:
        return str(student_scores[name])
    else:
        return "Not Found"
def refactored_lookup(student_scores: Dict[str, int], name: str) -> str:
    """
    Refactored approach using dict.get() with a default value.
    Returns score as string, or "Not Found" if the key is missing.
    """
    value: Optional[int] = student_scores.get(name)
    return str(value) if value is not None else "Not Found"
def get_student_name() -> str:
    """
    Prompt user for a student name. If empty input is provided, use a default
    that is not in the dictionary to demonstrate the graceful fallback.
    """
    print("Enter a student name to look up (e.g., Alice, Bob, Charlie):")
    user_input = input().strip()
    if not user_input:
        print("No name provided. Using default: Charlie")
        return "Charlie"
    return user_input
def main():
    print("=== Safe Dictionary Access Demo ===")
    print("This program shows how to use dict.get() to avoid KeyError.")
    print()
    # Example dataset (can be extended as needed)
    student_scores: Dict[str, int] = {"Alice": 85, "Bob": 90}
    name = get_student_name()
    print(f"\nLooking up: {name}")

    legacy_result = legacy_lookup(student_scores, name)
    refactored_result = refactored_lookup(student_scores, name)

    print(f"Legacy lookup result: {legacy_result}")
    print(f"Refactored lookup result: {refactored_result}")
    # Both methods should match
    if legacy_result == refactored_result:
        print(" Results match.")
    else:
        print(" Results differ - there may be an issue.")
    # For the case when name is 'Charlie', expected output is 'Not Found'
    if name == "Charlie":
        print("Expected Output:\nNot Found")
if __name__ == "__main__":
    main()


