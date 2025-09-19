from task5 import convert_date_format

def test_date_conversion():
    # 10 test cases with expected results
    print("Testing date format conversion function...")
    print("=" * 70)
    
    all_passed = True
    passed_count = 0
    failed_count = 0
    
    # Test 1: Basic date conversion
    try:
        result = convert_date_format("2023-12-25")
        expected = "25-12-2023"
        status = "✓ PASS" if result == expected else "✗ FAIL"
        if result == expected:
            passed_count += 1
        else:
            failed_count += 1
            all_passed = False
        print(f"Test  1: Basic date conversion                 Expected: {expected} Got: {result} {status}")
    except Exception as e:
        failed_count += 1
        all_passed = False
        print(f"Test  1: Basic date conversion                 Expected: 25-12-2023 Got: ERROR - {e} ✗ FAIL")
    
    # Test 2: Leap year date
    try:
        result = convert_date_format("2024-02-29")
        expected = "29-02-2024"
        status = "✓ PASS" if result == expected else "✗ FAIL"
        if result == expected:
            passed_count += 1
        else:
            failed_count += 1
            all_passed = False
        print(f"Test  2: Leap year date                       Expected: {expected} Got: {result} {status}")
    except Exception as e:
        failed_count += 1
        all_passed = False
        print(f"Test  2: Leap year date                       Expected: 29-02-2024 Got: ERROR - {e} ✗ FAIL")
    
    # Test 3: Single digit day and month
    try:
        result = convert_date_format("2023-01-05")
        expected = "05-01-2023"
        status = "✓ PASS" if result == expected else "✗ FAIL"
        if result == expected:
            passed_count += 1
        else:
            failed_count += 1
            all_passed = False
        print(f"Test  3: Single digit day/month               Expected: {expected} Got: {result} {status}")
    except Exception as e:
        failed_count += 1
        all_passed = False
        print(f"Test  3: Single digit day/month               Expected: 05-01-2023 Got: ERROR - {e} ✗ FAIL")
    
    # Test 4: New Year's Day
    try:
        result = convert_date_format("2024-01-01")
        expected = "01-01-2024"
        status = "✓ PASS" if result == expected else "✗ FAIL"
        if result == expected:
            passed_count += 1
        else:
            failed_count += 1
            all_passed = False
        print(f"Test  4: New Year's Day                       Expected: {expected} Got: {result} {status}")
    except Exception as e:
        failed_count += 1
        all_passed = False
        print(f"Test  4: New Year's Day                       Expected: 01-01-2024 Got: ERROR - {e} ✗ FAIL")
    
    # Test 5: End of year
    try:
        result = convert_date_format("2023-12-31")
        expected = "31-12-2023"
        status = "✓ PASS" if result == expected else "✗ FAIL"
        if result == expected:
            passed_count += 1
        else:
            failed_count += 1
            all_passed = False
        print(f"Test  5: End of year                          Expected: {expected} Got: {result} {status}")
    except Exception as e:
        failed_count += 1
        all_passed = False
        print(f"Test  5: End of year                          Expected: 31-12-2023 Got: ERROR - {e} ✗ FAIL")
    
    # Test 6: Mid-year date
    try:
        result = convert_date_format("2023-06-15")
        expected = "15-06-2023"
        status = "✓ PASS" if result == expected else "✗ FAIL"
        if result == expected:
            passed_count += 1
        else:
            failed_count += 1
            all_passed = False
        print(f"Test  6: Mid-year date                        Expected: {expected} Got: {result} {status}")
    except Exception as e:
        failed_count += 1
        all_passed = False
        print(f"Test  6: Mid-year date                        Expected: 15-06-2023 Got: ERROR - {e} ✗ FAIL")
    
    # Test 7: Historical date
    try:
        result = convert_date_format("2000-01-01")
        expected = "01-01-2000"
        status = "✓ PASS" if result == expected else "✗ FAIL"
        if result == expected:
            passed_count += 1
        else:
            failed_count += 1
            all_passed = False
        print(f"Test  7: Historical date                      Expected: {expected} Got: {result} {status}")
    except Exception as e:
        failed_count += 1
        all_passed = False
        print(f"Test  7: Historical date                      Expected: 01-01-2000 Got: ERROR - {e} ✗ FAIL")
    
    # Test 8: Future date
    try:
        result = convert_date_format("2030-05-20")
        expected = "20-05-2030"
        status = "✓ PASS" if result == expected else "✗ FAIL"
        if result == expected:
            passed_count += 1
        else:
            failed_count += 1
            all_passed = False
        print(f"Test  8: Future date                          Expected: {expected} Got: {result} {status}")
    except Exception as e:
        failed_count += 1
        all_passed = False
        print(f"Test  8: Future date                          Expected: 20-05-2030 Got: ERROR - {e} ✗ FAIL")
    
    # Test 9: Invalid format - wrong separator
    try:
        result = convert_date_format("2023/12/25")
        expected = "ERROR"
        status = "✗ FAIL"
        failed_count += 1
        all_passed = False
        print(f"Test  9: Invalid format (/)                   Expected: ERROR Got: {result} {status}")
    except ValueError as e:
        expected = "ERROR"
        status = "✓ PASS"
        passed_count += 1
        print(f"Test  9: Invalid format (/)                   Expected: ERROR Got: ValueError - {e} {status}")
    except Exception as e:
        failed_count += 1
        all_passed = False
        print(f"Test  9: Invalid format (/)                   Expected: ERROR Got: {type(e).__name__} - {e} ✗ FAIL")
    
    # Test 10: Valid date with zeros
    try:
        result = convert_date_format("2023-03-07")
        expected = "07-03-2023"
        status = "✓ PASS" if result == expected else "✗ FAIL"
        if result == expected:
            passed_count += 1
        else:
            failed_count += 1
            all_passed = False
        print(f"Test 10: Valid date with zeros                 Expected: {expected} Got: {result} {status}")
    except Exception as e:
        failed_count += 1
        all_passed = False
        print(f"Test 10: Valid date with zeros                 Expected: 07-03-2023 Got: ERROR - {e} ✗ FAIL")
    
    print("=" * 70)
    print(f"Results: {passed_count} passed, {failed_count} failed")
    
    if all_passed:
        print("okay all correct")
    else:
        print("some tests failed")

if __name__ == "__main__":
    test_date_conversion()