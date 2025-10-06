"""
Task 2: String Concatenation Simplification
This program demonstrates two approaches to build sentences from words:
1. Legacy approach using += operator in a loop
2. Refactored approach using " ".join() method for better efficiency and readability
"""
from typing import List
def legacy_string_concat(words: List[str]) -> str:
    """Build sentence using += operator (inefficient due to string immutability)"""
    sentence = ""
    for word in words:
        sentence += word + " "
    return sentence.strip()
def refactored_string_concat(words: List[str]) -> str:
    """Build sentence using join() method (more efficient and readable)"""
    return " ".join(words)

def get_user_words() -> List[str]:
    """Get words from user input with default fallback"""
    print("Enter words separated by spaces to build a sentence:")
    print("Example: AI helps in refactoring code")
    try:
        user_input = input().strip()
        if not user_input:
            print("No input provided. Using default words: AI, helps, in, refactoring, code")
            return ["AI", "helps", "in", "refactoring", "code"]
        
        words = user_input.split()
        return words
    except Exception:
        print("Error processing input. Using default words: AI, helps, in, refactoring, code")
        return ["AI", "helps", "in", "refactoring", "code"]
def main():
    """Main function to run the string concatenation program"""
    print("=== String Concatenation Simplification ===")
    print("This program demonstrates efficient vs inefficient string building methods.")
    print()
    # Get words from user
    words = get_user_words()
    print(f"\nInput words: {words}")
    # Compare both methods
    legacy_result = legacy_string_concat(words)
    refactored_result = refactored_string_concat(words)
    
    print(f"Sentence (Legacy method): {legacy_result}")
    print(f"Sentence (Refactored method): {refactored_result}")
    # Verify results match
    if legacy_result == refactored_result:
        print(" Both methods produce identical results!")
    else:
        print(" Methods produce different results - there's an issue!")

# Run the program when this file is executed
if __name__ == "__main__":
    main()
