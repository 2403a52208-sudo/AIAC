def is_sentence_palindrome(sentence):
    """
    Checks if the given sentence is a palindrome, ignoring case, punctuation, and spaces.

    Args:
        sentence (str): The sentence to check.

    Returns:
        bool: True if the sentence is a palindrome, False otherwise.
    """
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in sentence if char.isalnum())
    return cleaned == cleaned[::-1]
#run test cases
test_cases = [
    ("A man, a plan, a canal, Panama", True),
    ("racecar", True),
    ("hello world", False),
    ("", True),
    ("12321", True),
    ("12321", True),
]
for sentence, expected in test_cases:
    result = is_sentence_palindrome(sentence)
    print(f"Sentence: {sentence:<25} Expected: {expected:<5} Got: {result:<5} {'✓ PASS' if result == expected else '✗ FAIL'}")
    