from lab05_circular_array_seq import CircularArraySeq

# %%


def test_initial_state():
    """Test 01: Initial state of CircularArraySeq"""
    print("\nTest 01: Initial State")
    seq = CircularArraySeq()

    print(f"Initial: {seq}")
    print(f"Length: {len(seq)}")
    assert len(seq) == 0
    assert seq.capacity == 5
    return seq


def test_insert_first():
    """Test 02: insert_first without triggering resize"""
    print("\nTest 02: insert_first (no resize)")
    seq = CircularArraySeq()

    seq.insert_first(20)
    seq.insert_first(50)
    seq.insert_first(80)

    print(f"After 3 inserts: {seq}")
    assert len(seq) == 3
    assert seq.capacity == 5
    assert seq.get_at(0) == 80
    assert seq.get_at(2) == 20
    return seq


def test_insert_first_with_resize():
    """Test 03: insert_first with resize trigger"""
    print("\nTest 03: insert_first (with resize)")
    seq = CircularArraySeq()

    for i in range(5):
        seq.insert_first((i + 1) * 10)

    print(f"After 5 inserts (full): {seq}")
    assert seq.capacity == 5

    seq.insert_first(60)
    print(f"After 6 inserts (resized): {seq}")
    assert seq.capacity == 10
    assert len(seq) == 6
    return seq


def test_insert_last_without_resize():
    """Test 04: insert_last without triggering resize"""
    print("\nTest 04: insert_last (no resize)")
    seq = CircularArraySeq()

    seq.insert_last(10)
    seq.insert_last(20)
    seq.insert_last(30)

    print(f"After 3 inserts: {seq}")
    assert len(seq) == 3
    assert seq.capacity == 5
    assert seq.get_at(0) == 10
    assert seq.get_at(2) == 30
    return seq


def test_insert_last_with_resize():
    """Test 05: insert_last with resize trigger"""
    print("\nTest 05: insert_last (with resize)")
    seq = CircularArraySeq()

    for i in range(5):
        seq.insert_last((i + 1) * 10)

    print(f"After 5 inserts (full): {seq}")
    assert seq.capacity == 5

    seq.insert_last(60)
    print(f"After 6 inserts (resized): {seq}")
    assert seq.capacity == 10
    assert len(seq) == 6
    return seq


def test_insert_at():
    """Test 06: insert_at method"""
    print("\nTest 06: insert_at")
    seq = CircularArraySeq()

    for i in range(5):
        seq.insert_last((i + 1) * 10)

    print(f"Before insert_at: {seq}")
    seq.insert_at(99, 2)
    print(f"After insert_at(99, 2): {seq}")

    assert seq.get_at(2) == 99
    assert seq.get_at(3) == 30
    assert len(seq) == 6
    return seq


def test_get_at():
    """Test 07: get_at method"""
    print("\nTest 07: get_at")
    seq = CircularArraySeq()

    for i in range(6):
        seq.insert_last((i + 1) * 10)

    print(f"get_at(0): {seq.get_at(0)}")
    print(f"get_at(3): {seq.get_at(3)}")
    print(f"get_at(5): {seq.get_at(5)}")

    assert seq.get_at(0) == 10
    assert seq.get_at(3) == 40
    assert seq.get_at(5) == 60
    return seq


def test_get_first_last():
    """Test 08: get_first and get_last methods"""
    print("\nTest 08: get_first and get_last")
    seq = CircularArraySeq()

    seq.insert_last(10)
    seq.insert_last(20)
    seq.insert_last(30)

    first = seq.get_first()
    last = seq.get_last()

    print(f"get_first(): {first}")
    print(f"get_last(): {last}")

    assert first == 10
    assert last == 30
    return seq


def test_delete_first_without_resize():
    """Test 09: delete_first without resize"""
    print("\nTest 09: delete_first (no resize)")
    seq = CircularArraySeq()

    for i in range(6):
        seq.insert_last((i + 1) * 10)

    initial_capacity = seq.capacity
    val = seq.delete_first()
    print(f"Deleted value: {val}")
    print(f"After 1 delete: {seq}")

    assert val == 10
    assert len(seq) == 5
    assert seq.capacity == initial_capacity
    return seq


def test_delete_last_without_resize():
    """Test 10: delete_last without resize"""
    print("\nTest 10: delete_last (no resize)")
    seq = CircularArraySeq()

    for i in range(6):
        seq.insert_last((i + 1) * 10)

    initial_capacity = seq.capacity
    val = seq.delete_last()
    print(f"Deleted value: {val}")
    print(f"After 1 delete: {seq}")

    assert val == 60
    assert len(seq) == 5
    assert seq.capacity == initial_capacity
    return seq


def test_delete_last_with_resize():
    """Test 11: delete_last with resize trigger"""
    print("\nTest 11: delete_last (with resize)")
    seq = CircularArraySeq()

    for i in range(10):
        seq.insert_last((i + 1) * 10)
    print(f"Before deletes: {seq}")

    for _ in range(8):
        seq.delete_last()
    print(f"After 8 deletes: {seq}")

    assert len(seq) == 2
    # after 8 deletes: size = 2, capacity should shrink from 10 to 5
    # because 2/10 = 0.2 < 0.25
    assert seq.capacity == 5
    return seq


def test_delete_at():
    """Test 12: delete_at method"""
    print("\nTest 12: delete_at")
    seq = CircularArraySeq()

    for i in range(5):
        seq.insert_last((i + 1) * 10)

    print(f"Before delete_at: {seq}")
    val = seq.delete_at(2)
    print(f"Deleted value: {val}")
    print(f"After delete_at(2): {seq}")

    assert val == 30
    assert seq.get_at(2) == 40
    assert len(seq) == 4
    return seq


def test_circular_wrap_around():
    """Test 13: Circular wrap-around behavior"""
    print("\nTest 13: Circular wrap-around")
    seq = CircularArraySeq()

    seq.insert_last(1)
    seq.insert_last(2)
    seq.insert_last(3)
    print(f"After insert_last: {seq}")

    seq.delete_first()
    seq.delete_first()
    print(f"After 2 delete_first: {seq}")

    seq.insert_last(4)
    seq.insert_last(5)
    seq.insert_first(0)
    print(f"After mixed operations: {seq}")

    assert seq.to_list() == [0, 3, 4, 5]
    return seq


def test_set_at():
    """Test 14: set_at method"""
    print("\nTest 14: set_at")
    seq = CircularArraySeq()

    for i in range(5):
        seq.insert_last((i + 1) * 10)

    print(f"Before set_at: {seq}")
    seq.set_at(2, 99)
    print(f"After set_at(2, 99): {seq}")
    print(f"get_at(2): {seq.get_at(2)}")

    assert seq.get_at(2) == 99
    return seq


def test_edge_cases():
    """Test 15: Edge cases"""
    print("\nTest 15: Edge Cases")
    seq = CircularArraySeq()

    # empty array get_first and get_last
    first = seq.get_first()
    last = seq.get_last()
    print(f"get_first() on empty: {first}")
    print(f"get_last() on empty: {last}")
    assert first is None
    assert last is None

    # Single element
    seq.insert_at(42, 0)
    print(f"After single insert_at: {seq}")
    assert seq.to_list() == [42]

    val = seq.delete_at(0)
    print(f"After delete_at: {val}")
    assert seq.is_empty()


def test_error_handling():
    """Test 16: Error handling"""
    print("\nTest 16: Error Handling")
    seq = CircularArraySeq()

    # delete_first on empty
    try:
        seq.delete_first()
        assert False, "Should raise IndexError"
    except IndexError as e:
        print(f"delete_first on empty: {e}")
        print("Caught expected error")

    # delete_last on empty
    try:
        seq.delete_last()
        assert False, "Should raise IndexError"
    except IndexError as e:
        print(f"delete_last on empty: {e}")
        print("Caught expected error")

    # get_at out of bounds
    seq.insert_last(10)
    try:
        seq.get_at(10)
        assert False, "Should raise IndexError"
    except IndexError as e:
        print(f"get_at out of bounds: {e}")
        print("Caught expected error")

    # insert_at out of bounds
    try:
        seq.insert_at(99, -1)
        assert False, "Should raise IndexError"
    except IndexError as e:
        print(f"insert_at negative index: {e}")
        print("Caught expected error")

    # delete_at out of bounds
    try:
        seq.delete_at(10)
        assert False, "Should raise IndexError"
    except IndexError as e:
        print(f"delete_at out of bounds: {e}")
        print("Caught expected error")


if __name__ == "__main__":
    """Run all test cases"""
    test_initial_state()
    test_insert_first()
    test_insert_first_with_resize()
    test_insert_last_without_resize()
    test_insert_last_with_resize()
    test_insert_at()
    test_get_at()
    test_get_first_last()
    test_delete_first_without_resize()
    test_delete_last_without_resize()
    test_delete_last_with_resize()
    test_delete_at()
    test_circular_wrap_around()
    test_set_at()
    test_edge_cases()
    test_error_handling()

    print("\nAll tests passed!")
