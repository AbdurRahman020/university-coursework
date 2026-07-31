from lab04_array_seq import ArrSeq

# %% Test Modules


def test_initial_state():
    """Test 01: Initial state of ArraySeq"""
    print("\nTest 01: Initial State")
    arr = ArrSeq()

    print(f"Initial: {arr}")
    print(f"Length: {len(arr)}")
    assert len(arr) == 0
    assert arr.capacity == 5
    return arr


def test_insert_first():
    "Test 02: inser_first without triggering resize"
    print("\nTest 02: insert_first (no resize)")
    arr = ArrSeq()

    arr.insert_first(20)
    arr.insert_first(50)
    arr.insert_first(80)

    print(f"After 3 inserts: {arr}")
    assert len(arr) == 3
    assert arr.capacity == 5
    assert arr.get_at(0) == 80
    assert arr.get_at(2) == 20
    return arr


def test_insert_first_with_resize():
    """Test 03: insert_first with resize trigger"""
    print("\nTest 03: insert_first (with resize)")
    arr = ArrSeq()

    for i in range(5):
        arr.insert_first((i + 1) * 10)

    print(f"After 5 inserts (full): {arr}")
    assert arr.capacity == 5

    arr.insert_first(60)
    print(f"After 6 inserts (resized): {arr}")
    assert arr.capacity == 10
    assert len(arr) == 6
    return arr


def test_insert_without_resize():
    """Test 04: insert_last without triggering resize"""
    print("\nTest 04: insert_last (no resize)")
    arr = ArrSeq()

    arr.insert_last(10)
    arr.insert_last(20)
    arr.insert_last(30)

    print(f"After 3 inserts: {arr}")
    assert len(arr) == 3
    assert arr.capacity == 5
    assert arr.get_at(0) == 10
    assert arr.get_at(2) == 30
    return arr


def test_insert_with_resize():
    """Test 05: insert_last with resize trigger"""
    print("\nTest 05: insert_last (with resize)")
    arr = ArrSeq()

    for i in range(5):
        arr.insert_last((i + 1) * 10)

    print(f"After 5 inserts (full): {arr}")
    assert arr.capacity == 5

    arr.insert_last(60)
    print(f"After 6 inserts (resized): {arr}")
    assert arr.capacity == 10
    assert len(arr) == 6
    return arr


def test_insert_at_beginning():
    """Test 06: insert_at at beginning"""
    print("\nTest 06: insert_at (at beginning)")
    arr = ArrSeq()

    arr.insert_last(10)
    arr.insert_last(20)
    arr.insert_last(30)

    print(f"Before insert_at: {arr}")
    arr.insert_at(5, 0)
    print(f"After insert_at(5, 0): {arr}")

    assert arr.get_at(0) == 5
    assert arr.get_at(1) == 10
    assert len(arr) == 4
    return arr


def test_insert_at_middle():
    """Test 07: insert_at in the middle"""
    print("\nTest 07: insert_at (in middle)")
    arr = ArrSeq()

    for i in range(5):
        arr.insert_last((i + 1) * 10)

    print(f"Before insert_at: {arr}")
    arr.insert_at(99, 2)
    print(f"After insert_at(99, 2): {arr}")

    assert arr.get_at(2) == 99
    assert arr.get_at(3) == 30
    assert len(arr) == 6
    return arr


def test_insert_at_end():
    """Test 08: insert_at at end"""
    print("\nTest 08: insert_at (at end)")
    arr = ArrSeq()

    arr.insert_last(10)
    arr.insert_last(20)
    arr.insert_last(30)

    print(f"Before insert_at: {arr}")
    arr.insert_at(40, 3)
    print(f"After insert_at(40, 3): {arr}")

    assert arr.get_at(3) == 40
    assert len(arr) == 4
    return arr


def test_get_at():
    """Test 09: get_at method"""
    print("\nTest 09: get_at")
    arr = ArrSeq()

    for i in range(6):
        arr.insert_last((i + 1) * 10)

    print(f"get_at(0): {arr.get_at(0)}")
    print(f"get_at(3): {arr.get_at(3)}")
    print(f"get_at(5): {arr.get_at(5)}")

    assert arr.get_at(0) == 10
    assert arr.get_at(3) == 40
    assert arr.get_at(5) == 60
    return arr


def test_get_last():
    """Test 10: get_last method"""
    print("\nTest 10: get_last")
    arr = ArrSeq()

    arr.insert_last(10)
    arr.insert_last(20)
    arr.insert_last(30)
    last = arr.get_last()

    print(f"get_last(): {last}")
    assert last == 30
    return arr


def test_delete_without_resize():
    """Test 11: delete_last without resize"""
    print("\nTest 11: delete_last (no resize)")
    arr = ArrSeq()

    for i in range(6):
        arr.insert_last((i + 1) * 10)

    initial_capacity = arr.capacity
    arr.delete_last()
    print(f"After 1 delete: {arr}")

    assert len(arr) == 5
    assert arr.capacity == initial_capacity
    return arr


def test_delete_first_without_resize():
    """Test 12: delete_first without resize"""
    print("\nTest 12: delete_first (no resize)")
    arr = ArrSeq()

    for i in range(6):
        arr.insert_last((i + 1) * 10)

    initial_capacity = arr.capacity
    val = arr.delete_first()
    print(f"Deleted value: {val}")
    print(f"After 1 delete: {arr}")

    assert val == 10
    assert arr.get_at(0) == 20
    assert len(arr) == 5
    assert arr.capacity == initial_capacity
    return arr


def test_delete_first_with_resize():
    """Test 13: delete_first with resize trigger"""
    print("\nTest 13: delete_first (with resize)")
    arr = ArrSeq()

    for i in range(10):
        arr.insert_last((i + 1) * 10)
    print(f"Before deletes: {arr}")

    for _ in range(8):
        arr.delete_first()
    print(f"After 8 deletes: {arr}")

    assert len(arr) == 2
    # after 8 deletes: size = 2, capacity should shrink from 10 to 5
    assert arr.capacity == 5
    return arr


def test_delete_with_resize():
    """Test 14: delete_last with resize trigger"""
    print("\nTest 14: delete_last (with resize)")
    arr = ArrSeq()

    for i in range(10):
        arr.insert_last((i + 1) * 10)
    print(f"Before deletes: {arr}")

    for _ in range(8):
        arr.delete_last()
    print(f"After 8 deletes: {arr}")

    assert len(arr) == 2
    # after 8 deletes: size = 2, capacity should shrink from 10 to 5
    # because 2/10 = 0.2 which is < 0.25
    assert arr.capacity == 5
    return arr


def test_delete_at_beginning():
    """Test 15: delete_at at beginning"""
    print("\nTest 15: delete_at (at beginning)")
    arr = ArrSeq()

    for i in range(5):
        arr.insert_last((i + 1) * 10)

    print(f"Before delete_at: {arr}")
    val = arr.delete_at(0)
    print(f"Deleted value: {val}")
    print(f"After delete_at(0): {arr}")

    assert val == 10
    assert arr.get_at(0) == 20
    assert len(arr) == 4
    return arr


def test_delete_at_middle():
    """Test 16: delete_at in the middle"""
    print("\nTest 16: delete_at (in middle)")
    arr = ArrSeq()

    for i in range(5):
        arr.insert_last((i + 1) * 10)

    print(f"Before delete_at: {arr}")
    val = arr.delete_at(2)
    print(f"Deleted value: {val}")
    print(f"After delete_at(2): {arr}")

    assert val == 30
    assert arr.get_at(2) == 40
    assert len(arr) == 4
    return arr


def test_delete_at_end():
    """Test 17: delete_at at end"""
    print("\nTest 17: delete_at (at end)")
    arr = ArrSeq()

    for i in range(5):
        arr.insert_last((i + 1) * 10)

    print(f"Before delete_at: {arr}")
    val = arr.delete_at(4)
    print(f"Deleted value: {val}")
    print(f"After delete_at(4): {arr}")

    assert val == 50
    assert len(arr) == 4
    return arr


def test_delete_at_with_resize():
    """Test 18: delete_at with resize trigger"""
    print("\nTest 18: delete_at (with resize)")
    arr = ArrSeq()

    for i in range(10):
        arr.insert_last((i + 1) * 10)
    print(f"Before deletes: {arr}")

    for i in range(7, -1, -1):
        arr.delete_at(i)
    print(f"After 8 deletes: {arr}")

    assert len(arr) == 2
    # after 8 deletes: size = 2, capacity should shrink from 10 to 5
    assert arr.capacity == 5
    return arr


def test_edge_cases():
    """Test 19: Edge cases"""
    print("\nTest 19: Edge Cases")
    arr = ArrSeq()

    # empty array get_last
    result = arr.get_last()
    print(f"get_last() on empty: {result}")
    assert result is None


def test_error_handling():
    """Test 20: Error handling"""
    print("\nTest 20: Error Handling")
    arr = ArrSeq()

    # delete_last on empty
    try:
        arr.delete_last()
        assert False, "Should raise IndexError"
    except IndexError as e:
        print(f"delete_last on empty: {e}\nCaught expected error")

    # get_at out of bounds
    arr.insert_last(10)
    try:
        arr.get_at(10)
        assert False, "Should raise IndexError"
    except IndexError as e:
        print(f"get_at out of bounds: {e}\nCaught expected error")

    # insert_at out of bounds
    try:
        arr.insert_at(99, -1)
        assert False, "Should raise IndexError"
    except IndexError as e:
        print(f"insert_at out of bounds: {e}\nCaught expected error")

    # delete_at on empty
    arr2 = ArrSeq()
    try:
        arr2.delete_at(0)
        assert False, "Should raise IndexError"
    except IndexError as e:
        print(f"delete_at on empty: {e}\nCaught expected error")

    # delete_at out of bounds
    try:
        arr.delete_at(10)
        assert False, "Should raise IndexError"
    except IndexError as e:
        print(f"delete_at out of bounds: {e}\nCaught expected error")


if __name__ == "__main__":
    """Run all test cases"""
    test_initial_state()
    test_insert_first()
    test_insert_first_with_resize()
    test_insert_without_resize()
    test_insert_with_resize()
    test_insert_at_beginning()
    test_insert_at_middle()
    test_insert_at_end()
    test_get_at()
    test_get_last()
    test_delete_without_resize()
    test_delete_first_without_resize()
    test_delete_first_with_resize()
    test_delete_with_resize()
    test_delete_at_beginning()
    test_delete_at_middle()
    test_delete_at_end()
    test_delete_at_with_resize()
    test_edge_cases()
    test_error_handling()

    print("\nAll test passed!\n")
