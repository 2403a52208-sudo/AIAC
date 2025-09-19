from task1 import is_valid_email
def test_email_validation():
    # 15 test cases with expected results
    test_cases = [
        # Valid emails (should return True)
        ("supriyagoud123@gmail.com", True),
        ("sriharsha45@gmail.com", True),
        ("dririsri90@gmail.com", True),
        ("12deeksha123@gmail.com", True),
        ("user@example.com", True),
        ("test.email@domain.co.uk", True),
        ("user_name@example.org", True),
        ("user123@test.io", True),
        
        # Invalid emails (should return False)
        (".harsha.123@gmail.com", False),  # starts with dot
        ("@gmail.com", False),  # starts with @
        ("user@gmail", False),  # no dot in domain
        ("user@.com", False),  # domain starts with dot
        ("", False),  # empty string
        ("user@domain.", False),  # domain ends with dot
        ("user.@gmail.com", False),  # local ends with dot
    ]
    
    print("Testing email validation function...")
    print("=" * 50)
    
    all_passed = True
    passed_count = 0
    failed_count = 0
    
    for i, (email, expected) in enumerate(test_cases, 1):
        result = is_valid_email(email)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        
        if result == expected:
            passed_count += 1
        else:
            failed_count += 1
            all_passed = False
            
        print(f"Test {i:2d}: {email:<25} Expected: {expected:<5} Got: {result:<5} {status}")
    
    print("=" * 50)
    print(f"Results: {passed_count} passed, {failed_count} failed")
    
    if all_passed:
        print("okay all correct")
    else:
        print("some tests failed")

if __name__ == "__main__":
    test_email_validation()
