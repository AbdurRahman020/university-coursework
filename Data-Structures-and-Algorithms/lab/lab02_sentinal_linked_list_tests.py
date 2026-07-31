from lab02_sentinal_linked_list import SLList

# %% Testing Sentinely Linked List


def test_initial_state():
    """Test 1: Initial state of SLList"""
    print("\nTest 1: Initial State")
    sll = SLList()

    print(f"Initial: {sll}")
    assert len(sll) == 0
    assert sll.get_first() is None
    return sll


def test_insert_first():
    """Test 2: insert_first method"""
    print("\nTest 2: insert_first")
    sll = SLList()

    sll.insert_first(10)
    sll.insert_first(20)
    sll.insert_first(30)

    print(f"After 3 inserts: {sll}")
    assert len(sll) == 3
    assert sll.to_list() == [30, 20, 10]
    assert sll.get_first() == 30
    return sll


def test_insert_last():
    """Test 3: insert_last method"""
    print("\nTest 3: insert_last")
    sll = SLList()

    sll.insert_last(10)
    sll.insert_last(20)
    sll.insert_last(30)

    print(f"After 3 inserts: {sll}")
    assert len(sll) == 3
    assert sll.to_list() == [10, 20, 30]
    assert sll.get_first() == 10
    return sll


def test_insert_at():
    """Test 4: insert_at method"""
    print("\nTest 4: insert_at")
    sll = SLList()

    sll.insert_last(10)
    sll.insert_last(30)
    sll.insert_at(1, 20)

    print(f"After insert_at(1, 20): {sll}")
    assert len(sll) == 3
    assert sll.to_list() == [10, 20, 30]
    assert sll.get_at(1) == 20
    return sll


def test_get_first():
    """Test 5: get_first method"""
    print("\nTest 5: get_first")
    sll = SLList()

    sll.insert_last(10)
    sll.insert_last(20)
    sll.insert_last(30)
    first = sll.get_first()

    print(f"get_first(): {first}")
    assert first == 10
    return sll


def test_get_at():
    """Test 6: get_at method"""
    print("\nTest 6: get_at")
    sll = SLList()

    for i in range(1, 6):
        sll.insert_last(i * 10)

    print(f"get_at(0): {sll.get_at(0)}")
    print(f"get_at(2): {sll.get_at(2)}")
    print(f"get_at(4): {sll.get_at(4)}")

    assert sll.get_at(0) == 10
    assert sll.get_at(2) == 30
    assert sll.get_at(4) == 50
    return sll


def test_delete_first():
    """Test 7: delete_first method"""
    print("\nTest 7: delete_first")
    sll = SLList()

    for i in range(1, 6):
        sll.insert_last(i * 10)

    sll.delete_first()
    print(f"After delete_first: {sll}")

    assert len(sll) == 4
    assert sll.to_list() == [20, 30, 40, 50]
    assert sll.get_first() == 20
    return sll


def test_delete_last():
    """Test 8: delete_last method"""
    print("\nTest 8: delete_last")
    sll = SLList()

    for i in range(1, 6):
        sll.insert_last(i * 10)

    sll.delete_last()
    print(f"After delete_last: {sll}")

    assert len(sll) == 4
    assert sll.to_list() == [10, 20, 30, 40]
    return sll


def test_delete_from():
    """Test 9: delete_from method"""
    print("\nTest 9: delete_from")
    sll = SLList()

    for i in range(1, 6):
        sll.insert_last(i * 10)

    sll.delete_from(2)
    print(f"After delete_from(2): {sll}")

    assert len(sll) == 4
    assert sll.to_list() == [10, 20, 40, 50]
    return sll


def test_edge_cases():
    """Test 10: Edge cases"""
    print("\nTest 10: Edge Cases")
    sll = SLList()

    # get_first on empty
    result = sll.get_first()
    print(f"get_first() on empty: {result}")
    assert result is None

    # get_at out of bounds
    sll.insert_last(10)
    result = sll.get_at(5)
    print(f"get_at(5) out of bounds: {result}")
    assert result is None


def test_error_handling():
    """Test 11: Error handling"""
    print("\nTest 11: Error Handling")
    sll = SLList()

    # delete_first on empty
    try:
        sll.delete_first()
        assert False, "Should raise IndexError"
    except IndexError as e:
        print(f"delete_first on empty: {e}")

    # delete_last on empty
    try:
        sll.delete_last()
        assert False, "Should raise IndexError"
    except IndexError as e:
        print(f"delete_last on empty: {e}")

    # insert_at out of bounds
    sll.insert_last(10)
    try:
        sll.insert_at(10, 20)
        assert False, "Should raise IndexError"
    except IndexError as e:
        print(f"insert_at out of bounds: {e}")


if __name__ == "__main__":
    """Run all test cases"""
    test_initial_state()
    test_insert_first()
    test_insert_last()
    test_insert_at()
    test_get_first()
    test_get_at()
    test_delete_first()
    test_delete_last()
    test_delete_from()
    test_edge_cases()
    test_error_handling()

    print("\nAll tests passed!\n")
