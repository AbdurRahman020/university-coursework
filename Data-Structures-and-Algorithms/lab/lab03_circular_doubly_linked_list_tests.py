from lab03_circular_doubly_linked_list import DLList

# %% Testing sentinel (Circular) Doubly Linked List


def test_initial_state():
    """Test 1: Initial state of DLList"""
    print("\nTest 1: Initial State")
    dll = DLList()

    print(f"Initial: {dll}")
    assert len(dll) == 0
    assert dll.is_empty() is True
    return dll


def test_insert_first():
    """Test 2: insert_first method"""
    print("\nTest 2: insert_first")
    dll = DLList()

    dll.insert_first(10)
    dll.insert_first(20)
    dll.insert_first(30)

    print(f"After 3 inserts: {dll}")
    assert len(dll) == 3
    assert dll.to_list() == [30, 20, 10]
    assert dll.get_value_at(0) == 30
    return dll


def test_insert_last():
    """Test 3: insert_last method"""
    print("\nTest 3: insert_last")
    dll = DLList()

    dll.insert_last(10)
    dll.insert_last(20)
    dll.insert_last(30)

    print(f"After 3 inserts: {dll}")
    assert len(dll) == 3
    assert dll.to_list() == [10, 20, 30]
    assert dll.get_value_at(2) == 30
    return dll


def test_insert_at():
    """Test 4: insert_at method"""
    print("\nTest 4: insert_at")
    dll = DLList()

    dll.insert_last(10)
    dll.insert_last(30)
    dll.insert_at(1, 20)

    print(f"After insert_at(1, 20): {dll}")
    assert len(dll) == 3
    assert dll.to_list() == [10, 20, 30]
    return dll


def test_get_value_at():
    """Test 5: get_value_at method"""
    print("\nTest 5: get_value_at")
    dll = DLList()

    for i in range(1, 6):
        dll.insert_last(i * 10)

    print(f"get_value_at(0): {dll.get_value_at(0)}")
    print(f"get_value_at(2): {dll.get_value_at(2)}")
    print(f"get_value_at(4): {dll.get_value_at(4)}")

    assert dll.get_value_at(0) == 10
    assert dll.get_value_at(2) == 30
    assert dll.get_value_at(4) == 50
    return dll


def test_delete_first():
    """Test 6: delete_first method"""
    print("\nTest 6: delete_first")
    dll = DLList()

    for i in range(1, 6):
        dll.insert_last(i * 10)

    dll.delete_first()
    print(f"After delete_first: {dll}")

    assert len(dll) == 4
    assert dll.to_list() == [20, 30, 40, 50]
    return dll


def test_delete_last():
    """Test 7: delete_last method"""
    print("\nTest 7: delete_last")
    dll = DLList()

    for i in range(1, 6):
        dll.insert_last(i * 10)

    dll.delete_last()
    print(f"After delete_last: {dll}")

    assert len(dll) == 4
    assert dll.to_list() == [10, 20, 30, 40]
    return dll


def test_delete_from():
    """Test 8: delete_from method"""
    print("\nTest 8: delete_from")
    dll = DLList()

    for i in range(1, 6):
        dll.insert_last(i * 10)

    deleted_val = dll.delete_from(2)
    print(f"After delete_from(2): {dll}")
    print(f"Deleted value: {deleted_val}")

    assert len(dll) == 4
    assert deleted_val == 30
    assert dll.to_list() == [10, 20, 40, 50]
    return dll


def test_iteration():
    """Test 9: Iteration"""
    print("\nTest 9: Iteration")
    dll = DLList()

    for i in range(1, 4):
        dll.insert_last(i * 10)

    forward = list(dll)
    backward = list(reversed(dll))

    print(f"Forward iteration: {forward}")
    print(f"Backward iteration: {backward}")

    assert forward == [10, 20, 30]
    assert backward == [30, 20, 10]
    return dll


def test_error_handling():
    """Test 10: Error handling"""
    print("\nTest 10: Error Handling")
    dll = DLList()

    # delete_first on empty
    try:
        dll.delete_first()
        assert False, "Should raise IndexError"
    except IndexError as e:
        print(f"delete_first on empty: {e}")

    # get_value_at out of bounds
    dll.insert_last(10)
    try:
        dll.get_value_at(5)
        assert False, "Should raise IndexError"
    except IndexError as e:
        print(f"get_value_at out of bounds: {e}")

    # insert_at out of bounds
    try:
        dll.insert_at(10, 20)
        assert False, "Should raise IndexError"
    except IndexError as e:
        print(f"insert_at out of bounds: {e}")


if __name__ == "__main__":
    """Run all test cases"""
    test_initial_state()
    test_insert_first()
    test_insert_last()
    test_insert_at()
    test_get_value_at()
    test_delete_first()
    test_delete_last()
    test_delete_from()
    test_iteration()
    test_error_handling()

    print("\nAll tests passed!")
