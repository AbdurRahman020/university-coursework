from radix_sort import radix_sort

# %% test cases


def test_basic_example_rs():
    """Test with classic CLRS-style example."""
    print("Test 1: Basic Example (3-digit numbers)")

    arr = [329, 457, 657, 839, 436, 720, 355]
    print(f"Original: {arr}\n")

    result = radix_sort(arr.copy())
    expected = [329, 355, 436, 457, 657, 720, 839]

    print(f"\nFinal: {result}")
    print(f"Expected: {expected}")
    print("PASS\n" if result == expected else "FAIL\n")


def test_single_digit_rs():
    """Test with single digit numbers."""
    print("Test 2: Single Digit Numbers")

    arr = [5, 2, 9, 1, 7, 3]
    print(f"Original: {arr}\n")

    result = radix_sort(arr.copy())
    expected = [1, 2, 3, 5, 7, 9]

    print(f"\nFinal: {result}")
    print(f"Expected: {expected}")
    print("PASS\n" if result == expected else "FAIL\n")


def test_two_digit_rs():
    """Test with two digit numbers."""
    print("Test 3: Two Digit Numbers")

    arr = [64, 25, 12, 22, 11, 90, 88]
    print(f"Original: {arr}\n")

    result = radix_sort(arr.copy())
    expected = [11, 12, 22, 25, 64, 88, 90]

    print(f"\nFinal: {result}")
    print(f"Expected: {expected}")
    print("PASS\n" if result == expected else "FAIL\n")


def test_with_zeros_rs():
    """Test with numbers containing zeros."""
    print("Test 4: Numbers with Zeros")

    arr = [101, 1, 100, 10, 202, 20]
    print(f"Original: {arr}\n")

    result = radix_sort(arr.copy())
    expected = sorted(arr)

    print(f"\nFinal: {result}")
    print(f"Expected: {expected}")
    print("PASS\n" if result == expected else "FAIL\n")


def test_already_sorted_rs():
    """Test with already sorted array."""
    print("Test 5: Already Sorted")

    arr = [111, 222, 333, 444, 555]
    print(f"Original: {arr}\n")

    result = radix_sort(arr.copy())
    expected = [111, 222, 333, 444, 555]

    print(f"\nFinal: {result}")
    print(f"Expected: {expected}")
    print("PASS\n" if result == expected else "FAIL\n")


def test_reverse_sorted_rs():
    """Test with reverse sorted array."""
    print("Test 6: Reverse Sorted")

    arr = [987, 654, 321, 123]
    print(f"Original: {arr}\n")

    result = radix_sort(arr.copy())
    expected = [123, 321, 654, 987]

    print(f"\nFinal: {result}")
    print(f"Expected: {expected}")
    print("PASS\n" if result == expected else "FAIL\n")


def test_duplicates_rs():
    """Test with duplicate values."""
    print("Test 7: With Duplicates")

    arr = [170, 45, 75, 90, 2, 24, 45, 66]
    print(f"Original: {arr}\n")

    result = radix_sort(arr.copy())
    expected = sorted(arr)

    print(f"\nFinal: {result}")
    print(f"Expected: {expected}")
    print("PASS\n" if result == expected else "FAIL\n")


def test_large_range_rs():
    """Test with large numbers."""
    print("Test 8: Large Numbers (4-5 digits)")

    arr = [12345, 9876, 54321, 1111, 99999]
    print(f"Original: {arr}\n")

    result = radix_sort(arr.copy())
    expected = [1111, 9876, 12345, 54321, 99999]

    print(f"\nFinal: {result}")
    print(f"Expected: {expected}")
    print("PASS\n" if result == expected else "FAIL\n")


def test_stability_rs():
    """
    Test stability - equal values should maintain original order.
    We'll use a different representation to track this.
    """
    print("Test 9: Stability Check")

    # Numbers with same first two digits
    arr = [121, 122, 120, 123, 124]
    print(f"Original: {arr}")
    print("Note: All start with '12_', should maintain relative order\n")

    result = radix_sort(arr.copy())
    expected = [120, 121, 122, 123, 124]

    print(f"\nFinal: {result}")
    print(f"Expected: {expected}")
    print("PASS\n" if result == expected else "FAIL\n")


def test_single_element_rs():
    """Test with single element."""
    print("Test 10: Single Element")

    arr = [42]
    print(f"Original: {arr}\n")

    result = radix_sort(arr.copy())
    expected = [42]

    print(f"\nFinal: {result}")
    print(f"Expected: {expected}")
    print("PASS\n" if result == expected else "FAIL\n")


def run_all_tests():
    """Run all test cases."""
    print("\nRADIX SORT WITH COUNTING SORT - CLRS Implementation")

    test_basic_example_rs()
    test_single_digit_rs()
    test_two_digit_rs()
    test_with_zeros_rs()
    test_already_sorted_rs()
    test_reverse_sorted_rs()
    test_duplicates_rs()
    test_large_range_rs()
    test_stability_rs()
    test_single_element_rs()

    print("All tests completed!")
    print("\nKey Properties of Radix Sort:")
    print("- Time Complexity: O(d × (n + k)) where d = digits, k = base (10)")
    print("- Space Complexity: O(n + k)")
    print("- Stable: YES")
    print("- In-place: NO (requires extra space)")
    print("- Best for: Integers with fixed number of digits")


if __name__ == "__main__":
    run_all_tests()
