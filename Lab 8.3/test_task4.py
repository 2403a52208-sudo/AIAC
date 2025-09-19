from task4 import ShoppingCart

def test_shopping_cart():
    # 15 test cases with expected results
    print("Testing ShoppingCart class...")
    print("=" * 70)
    
    all_passed = True
    passed_count = 0
    failed_count = 0
    
    # Test 1: Create empty cart
    cart = ShoppingCart()
    expected_items = {}
    actual_items = cart.items
    status = "✓ PASS" if actual_items == expected_items else "✗ FAIL"
    if actual_items == expected_items:
        passed_count += 1
    else:
        failed_count += 1
        all_passed = False
    print(f"Test  1: Empty cart creation                    Expected: {expected_items} Got: {actual_items} {status}")
    
    # Test 2: Add single item
    cart = ShoppingCart()
    cart.add_item("apple", 1.50)
    expected_items = {"apple": {"price": 1.50, "quantity": 1}}
    actual_items = cart.items
    status = "✓ PASS" if actual_items == expected_items else "✗ FAIL"
    if actual_items == expected_items:
        passed_count += 1
    else:
        failed_count += 1
        all_passed = False
    print(f"Test  2: Add single item                        Expected: {expected_items} Got: {actual_items} {status}")
    
    # Test 3: Add same item again (quantity should increase)
    cart.add_item("apple", 1.50)
    expected_items = {"apple": {"price": 1.50, "quantity": 2}}
    actual_items = cart.items
    status = "✓ PASS" if actual_items == expected_items else "✗ FAIL"
    if actual_items == expected_items:
        passed_count += 1
    else:
        failed_count += 1
        all_passed = False
    print(f"Test  3: Add same item again                    Expected: {expected_items} Got: {actual_items} {status}")
    
    # Test 4: Add different item
    cart.add_item("banana", 0.75)
    expected_items = {"apple": {"price": 1.50, "quantity": 2}, "banana": {"price": 0.75, "quantity": 1}}
    actual_items = cart.items
    status = "✓ PASS" if actual_items == expected_items else "✗ FAIL"
    if actual_items == expected_items:
        passed_count += 1
    else:
        failed_count += 1
        all_passed = False
    print(f"Test  4: Add different item                      Expected: {expected_items} Got: {actual_items} {status}")
    
    # Test 5: Calculate total cost
    expected_total = 3.75  # (1.50 * 2) + (0.75 * 1)
    actual_total = cart.total_cost()
    status = "✓ PASS" if actual_total == expected_total else "✗ FAIL"
    if actual_total == expected_total:
        passed_count += 1
    else:
        failed_count += 1
        all_passed = False
    print(f"Test  5: Calculate total cost                   Expected: {expected_total} Got: {actual_total} {status}")
    
    # Test 6: Remove item with quantity > 1
    cart.remove_item("apple")
    expected_items = {"apple": {"price": 1.50, "quantity": 1}, "banana": {"price": 0.75, "quantity": 1}}
    actual_items = cart.items
    status = "✓ PASS" if actual_items == expected_items else "✗ FAIL"
    if actual_items == expected_items:
        passed_count += 1
    else:
        failed_count += 1
        all_passed = False
    print(f"Test  6: Remove item (qty > 1)                  Expected: {expected_items} Got: {actual_items} {status}")
    
    # Test 7: Remove item with quantity = 1 (should be deleted)
    cart.remove_item("banana")
    expected_items = {"apple": {"price": 1.50, "quantity": 1}}
    actual_items = cart.items
    status = "✓ PASS" if actual_items == expected_items else "✗ FAIL"
    if actual_items == expected_items:
        passed_count += 1
    else:
        failed_count += 1
        all_passed = False
    print(f"Test  7: Remove item (qty = 1)                   Expected: {expected_items} Got: {actual_items} {status}")
    
    # Test 8: Remove non-existent item
    cart.remove_item("orange")
    expected_items = {"apple": {"price": 1.50, "quantity": 1}}
    actual_items = cart.items
    status = "✓ PASS" if actual_items == expected_items else "✗ FAIL"
    if actual_items == expected_items:
        passed_count += 1
    else:
        failed_count += 1
        all_passed = False
    print(f"Test  8: Remove non-existent item               Expected: {expected_items} Got: {actual_items} {status}")
    
    # Test 9: Empty cart total cost
    cart.remove_item("apple")
    expected_total = 0
    actual_total = cart.total_cost()
    status = "✓ PASS" if actual_total == expected_total else "✗ FAIL"
    if actual_total == expected_total:
        passed_count += 1
    else:
        failed_count += 1
        all_passed = False
    print(f"Test  9: Empty cart total cost                  Expected: {expected_total} Got: {actual_total} {status}")
    
    # Test 10: Add multiple different items
    cart = ShoppingCart()
    cart.add_item("book", 10.00)
    cart.add_item("pen", 2.50)
    cart.add_item("notebook", 5.00)
    expected_items = {"book": {"price": 10.00, "quantity": 1}, "pen": {"price": 2.50, "quantity": 1}, "notebook": {"price": 5.00, "quantity": 1}}
    actual_items = cart.items
    status = "✓ PASS" if actual_items == expected_items else "✗ FAIL"
    if actual_items == expected_items:
        passed_count += 1
    else:
        failed_count += 1
        all_passed = False
    print(f"Test 10: Add multiple items                     Expected: {expected_items} Got: {actual_items} {status}")
    
    # Test 11: Multiple quantities of same item
    cart.add_item("book", 10.00)
    cart.add_item("book", 10.00)
    expected_items = {"book": {"price": 10.00, "quantity": 3}, "pen": {"price": 2.50, "quantity": 1}, "notebook": {"price": 5.00, "quantity": 1}}
    actual_items = cart.items
    status = "✓ PASS" if actual_items == expected_items else "✗ FAIL"
    if actual_items == expected_items:
        passed_count += 1
    else:
        failed_count += 1
        all_passed = False
    print(f"Test 11: Multiple quantities                    Expected: {expected_items} Got: {actual_items} {status}")
    
    # Test 12: Total cost with multiple quantities
    expected_total = 37.50  # (10.00 * 3) + (2.50 * 1) + (5.00 * 1)
    actual_total = cart.total_cost()
    status = "✓ PASS" if actual_total == expected_total else "✗ FAIL"
    if actual_total == expected_total:
        passed_count += 1
    else:
        failed_count += 1
        all_passed = False
    print(f"Test 12: Total with multiple quantities         Expected: {expected_total} Got: {actual_total} {status}")
    
    # Test 13: Remove all quantities of an item
    cart.remove_item("book")
    cart.remove_item("book")
    cart.remove_item("book")
    expected_items = {"pen": {"price": 2.50, "quantity": 1}, "notebook": {"price": 5.00, "quantity": 1}}
    actual_items = cart.items
    status = "✓ PASS" if actual_items == expected_items else "✗ FAIL"
    if actual_items == expected_items:
        passed_count += 1
    else:
        failed_count += 1
        all_passed = False
    print(f"Test 13: Remove all quantities                  Expected: {expected_items} Got: {actual_items} {status}")
    
    # Test 14: Add item with decimal price
    cart.add_item("chocolate", 3.99)
    expected_items = {"pen": {"price": 2.50, "quantity": 1}, "notebook": {"price": 5.00, "quantity": 1}, "chocolate": {"price": 3.99, "quantity": 1}}
    actual_items = cart.items
    status = "✓ PASS" if actual_items == expected_items else "✗ FAIL"
    if actual_items == expected_items:
        passed_count += 1
    else:
        failed_count += 1
        all_passed = False
    print(f"Test 14: Add item with decimal price             Expected: {expected_items} Got: {actual_items} {status}")
    
    # Test 15: Final total cost
    expected_total = 11.49  # (2.50 * 1) + (5.00 * 1) + (3.99 * 1)
    actual_total = cart.total_cost()
    status = "✓ PASS" if actual_total == expected_total else "✗ FAIL"
    if actual_total == expected_total:
        passed_count += 1
    else:
        failed_count += 1
        all_passed = False
    print(f"Test 15: Final total cost                       Expected: {expected_total} Got: {actual_total} {status}")
    
    print("=" * 70)
    print(f"Results: {passed_count} passed, {failed_count} failed")
    
    if all_passed:
        print("okay all correct")
    else:
        print("some tests failed")

if __name__ == "__main__":
    test_shopping_cart()
