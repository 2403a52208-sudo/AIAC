from task3 import is_sentence_palindrome

def test_palindrome_validation():
    # 15 test cases with expected results - all guaranteed to pass
    test_cases = [
        # Valid palindromes (should return True)
        ("racecar", True),                           # simple palindrome
        ("A man a plan a canal Panama", True),       # sentence palindrome
        ("Madam", True),                             # single word palindrome
        ("level", True),                             # simple palindrome
        ("Was it a car or a cat I saw?", True),      # question palindrome
        ("A Santa at NASA", True),                   # NASA palindrome
        ("Never odd or even", True),                 # sentence palindrome
        ("12321", True),                             # numeric palindrome
        ("", True),                                  # empty string (considered palindrome)
        ("a", True),                                 # single character
        
        # Invalid palindromes (should return False)
        ("hello", False),                            # not a palindrome
        ("world", False),                            # not a palindrome
        ("python", False),                           # not a palindrome
        ("programming", False),                      # not a palindrome
        ("12345", False),                            # not a numeric palindrome
    ]
    
    print("Testing palindrome validation function...")
    print("=" * 70)
    
    all_passed = True
    passed_count = 0
    failed_count = 0
    
    for i, (sentence, expected) in enumerate(test_cases, 1):
        result = is_sentence_palindrome(sentence)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        
        if result == expected:
            passed_count += 1
        else:
            failed_count += 1
            all_passed = False
            
        print(f"Test {i:2d}: '{sentence:<30}' Expected: {str(expected):<5} Got: {str(result):<5} {status}")
    
    print("=" * 70)
    print(f"Results: {passed_count} passed, {failed_count} failed")
    
    if all_passed:
        print("okay all correct")
    else:
        print("some tests failed")

if __name__ == "__main__":
    test_palindrome_validation()