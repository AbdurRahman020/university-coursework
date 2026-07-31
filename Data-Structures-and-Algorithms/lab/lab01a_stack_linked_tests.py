from lab01a_stack_linked import LinkedStack

# %% test Linked Stack


def test_initial_state_linked_stack():
    """Test 1: Initial state of LinkedStack"""
    print("\nTest 1: Initial State")
    stack = LinkedStack()

    print(f"Stack: {stack}")
    print(f"Length: {len(stack)}")
    print(f"is_empty: {stack.is_empty()}")
    assert len(stack) == 0
    assert stack.is_empty() is True
    return stack


def test_push_linked_stack():
    """Test 2: push method"""
    print("\nTest 2: push")
    stack = LinkedStack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(f"Stack: {stack}")
    print(f"After 3 pushes: length = {len(stack)}")
    assert len(stack) == 3
    assert stack.top() == 30
    return stack


def test_pop_linked_stack():
    """Test 3: pop method"""
    print("\nTest 3: pop")
    stack = LinkedStack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(f"Before pop: {stack}")
    popped = stack.pop()
    print(f"Popped value: {popped}")
    print(f"After pop: {stack}")
    print(f"Length: {len(stack)}")

    assert popped == 30
    assert len(stack) == 2
    assert stack.top() == 20
    return stack


def test_top_linked_stack():
    """Test 4: top method"""
    print("\nTest 4: top")
    stack = LinkedStack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(f"Stack: {stack}")
    top_val = stack.top()
    print(f"top(): {top_val}")
    print(f"Length after top: {len(stack)}")

    assert top_val == 30
    assert len(stack) == 3
    return stack


def test_is_empty_linked_stack():
    """Test 5: is_empty method"""
    print("\nTest 5: is_empty")
    stack = LinkedStack()

    print(f"Empty stack: {stack}")
    print(f"is_empty(): {stack.is_empty()}")
    assert stack.is_empty() is True

    stack.push(10)
    print(f"After push: {stack}")
    print(f"is_empty(): {stack.is_empty()}")
    assert stack.is_empty() is False

    stack.pop()
    print(f"After pop: {stack}")
    print(f"is_empty(): {stack.is_empty()}")
    assert stack.is_empty() is True
    return stack


def test_multiple_operations_linked_stack():
    """Test 6: Multiple operations"""
    print("\nTest 6: Multiple operations")
    stack = LinkedStack()

    for i in range(1, 6):
        stack.push(i * 10)

    print(f"Stack: {stack}")
    print(f"After 5 pushes: length = {len(stack)}, top = {stack.top()}")
    assert len(stack) == 5
    assert stack.top() == 50

    stack.pop()
    stack.pop()
    print(f"After 2 pops: {stack}")
    print(f"Length = {len(stack)}, top = {stack.top()}")
    assert len(stack) == 3
    assert stack.top() == 30
    return stack


def test_edge_cases_linked_stack():
    """Test 7: Edge cases"""
    print("\nTest 7: Edge Cases")
    stack = LinkedStack()

    stack.push(10)
    print(f"After push: {stack}")
    stack.pop()
    print(f"After pop: {stack}")

    print(f"Length: {len(stack)}")
    assert len(stack) == 0
    assert stack.is_empty() is True


def test_error_handling_linked_stack():
    """Test 8: Error handling"""
    print("\nTest 8: Error Handling")
    stack = LinkedStack()

    # pop on empty stack
    try:
        stack.pop()
        assert False, "Should raise IndexError"
    except IndexError as e:
        print(f"pop on empty stack: {e}")

    # top on empty stack
    try:
        stack.top()
        assert False, "Should raise IndexError"
    except IndexError as e:
        print(f"top on empty stack: {e}")


if __name__ == "__main__":
    """Run all test cases"""
    test_initial_state_linked_stack()
    test_push_linked_stack()
    test_pop_linked_stack()
    test_top_linked_stack()
    test_is_empty_linked_stack()
    test_multiple_operations_linked_stack()
    test_edge_cases_linked_stack()
    test_error_handling_linked_stack()

    print("\nAll tests passed!")
