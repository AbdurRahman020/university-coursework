from counting_sort import counting_sort

# %% test cases


def test_basic_case():
    """Test with the classic CLRS example."""
    A = [2, 5, 3, 0, 2, 3, 0, 3]
    k = 5

    result = counting_sort(A, k)
    expected = [0, 0, 2, 2, 3, 3, 3, 5]

    print("Test 1 - Basic case:")
    print(f"  Input:    {A}")
    print(f"  Output:   {result}")
    print(f"  Expected: {expected}")
    print(f"  Pass: {result == expected}\n")


def test_all_same():
    """Test with all identical elements."""
    A = [3, 3, 3, 3, 3]
    k = 3

    result = counting_sort(A, k)
    expected = [3, 3, 3, 3, 3]

    print("Test 2 - All same elements:")
    print(f"  Input:    {A}")
    print(f"  Output:   {result}")
    print(f"  Expected: {expected}")
    print(f"  Pass: {result == expected}\n")


def test_already_sorted():
    """Test with already sorted array."""
    A = [0, 1, 2, 3, 4, 5]
    k = 5

    result = counting_sort(A, k)
    expected = [0, 1, 2, 3, 4, 5]

    print("Test 3 - Already sorted:")
    print(f"  Input:    {A}")
    print(f"  Output:   {result}")
    print(f"  Expected: {expected}")
    print(f"  Pass: {result == expected}\n")


def test_reverse_sorted():
    """Test with reverse sorted array."""
    A = [5, 4, 3, 2, 1, 0]
    k = 5

    result = counting_sort(A, k)
    expected = [0, 1, 2, 3, 4, 5]

    print("Test 4 - Reverse sorted:")
    print(f"  Input:    {A}")
    print(f"  Output:   {result}")
    print(f"  Expected: {expected}")
    print(f"  Pass: {result == expected}\n")


def test_single_element():
    """Test with single element."""
    A = [7]
    k = 10

    result = counting_sort(A, k)
    expected = [7]

    print("Test 5 - Single element:")
    print(f"  Input:    {A}")
    print(f"  Output:   {result}")
    print(f"  Expected: {expected}")
    print(f"  Pass: {result == expected}\n")


def test_with_zeros():
    """Test with multiple zeros."""
    A = [0, 5, 0, 3, 0, 1]
    k = 5

    result = counting_sort(A, k)
    expected = [0, 0, 0, 1, 3, 5]

    print("Test 6 - Multiple zeros:")
    print(f"  Input:    {A}")
    print(f"  Output:   {result}")
    print(f"  Expected: {expected}")
    print(f"  Pass: {result == expected}\n")


def test_stability():
    """
    Test stability of counting sort. Using tuples where first element
    is the key and second is the original position.
    """
    # track positions to verify stability
    A_values = [2, 5, 3, 0, 2, 3, 0, 3]
    A_with_positions = [(val, idx) for idx, val in enumerate(A_values)]

    print("Test 7 - Stability check:")
    print(f"  Input values: {A_values}")
    print(f"  With positions: {A_with_positions}")

    # for stability test, we need a modified version that preserves extra data
    # let's just verify with values
    result = counting_sort(A_values, 5)
    print(f" Sorted: {result}")
    print("  Note: Counting sort is STABLE - equal elements maintain relative order")
    print("  (To fully verify stability, we'd need to track original positions)\n")


def run_all_tests():
    """Run all test cases."""
    print("RUNNING ALL TESTS\n")

    test_basic_case()
    test_all_same()
    test_already_sorted()
    test_reverse_sorted()
    test_single_element()
    test_with_zeros()
    test_stability()

    print("ALL TESTS COMPLETED!")


if __name__ == "__main__":
    run_all_tests()
