from task2 import assign_grade

def test_grade_validation():
    # 15 test cases with expected results
    test_cases = [
        # Valid scores with expected grades
        (95, "A"),      # A grade (90-100)
        (90, "A"),      # A grade boundary
        (85, "B"),      # B grade (80-89)
        (80, "B"),      # B grade boundary
        (75, "C"),      # C grade (70-79)
        (70, "C"),      # C grade boundary
        (65, "D"),      # D grade (60-69)
        (60, "D"),      # D grade boundary
        (45, "F"),      # F grade (0-59)
        (0, "F"),       # F grade boundary
        
        # Invalid inputs (should return error messages)
        ("abc", "Invalid input: not a number"),           # non-numeric string
        ("", "Invalid input: not a number"),              # empty string
        (None, "Invalid input: not a number"),            # None value
        (-5, "Invalid input: score must be between 0 and 100"),  # negative score
        (105, "Invalid input: score must be between 0 and 100"), # score above 100
    ]
    
    print("Testing grade assignment function...")
    print("=" * 60)
    
    all_passed = True
    passed_count = 0
    failed_count = 0
    
    for i, (score, expected) in enumerate(test_cases, 1):
        result = assign_grade(score)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        
        if result == expected:
            passed_count += 1
        else:
            failed_count += 1
            all_passed = False
            
        print(f"Test {i:2d}: Score: {str(score):<10} Expected: {str(expected):<35} Got: {str(result):<35} {status}")
    
    print("=" * 60)
    print(f"Results: {passed_count} passed, {failed_count} failed")
    
    if all_passed:
        print("okay all correct")
    else:
        print("some tests failed")

if __name__ == "__main__":
    test_grade_validation()
