from lab01a_stack import Stack

# %% test list based Stack


def test_initial_state():
    """Test 1: Initial state of Stack"""
    print("\nTest 1: Initial State")
    stack = Stack()

    print(f"Initial: {stack}")
    print(f"Length: {len(stack)}")
    assert len(stack) == 0
    assert stack.is_empty() is True
    return stack


def test_push():
    """Test 2: push method"""
    print("\nTest 2: push")
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print(f"After 3 pushes: {stack}")
    assert len(stack) == 3
    assert stack.peek() == 30
    return stack


def test_pop():
    """Test 3: pop method"""
    print("\nTest 3: pop")
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    popped = stack.pop()
    print(f"After pop: {stack}")
    print(f"Popped value: {popped}")

    assert popped == 30
    assert len(stack) == 2
    assert stack.peek() == 20
    return stack


def test_peek():
    """Test 4: peek method"""
    print("\nTest 4: peek")
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    top = stack.peek()
    print(f"peek(): {top}")
    print(f"Stack after peek: {stack}")

    assert top == 30
    assert len(stack) == 3
    return stack


def test_is_empty():
    """Test 5: is_empty method"""
    print("\nTest 5: is_empty")
    stack = Stack()

    print(f"Empty stack is_empty(): {stack.is_empty()}")
    assert stack.is_empty() is True

    stack.push(10)
    print(f"After push is_empty(): {stack.is_empty()}")
    assert stack.is_empty() is False

    stack.pop()
    print(f"After pop is_empty(): {stack.is_empty()}")
    assert stack.is_empty() is True
    return stack


def test_multiple_operations():
    """Test 6: Multiple operations"""
    print("\nTest 6: Multiple operations")
    stack = Stack()

    for i in range(1, 6):
        stack.push(i * 10)

    print(f"After 5 pushes: {stack}")
    assert len(stack) == 5

    stack.pop()
    stack.pop()
    print(f"After 2 pops: {stack}")
    assert len(stack) == 3
    assert stack.peek() == 30
    return stack


def test_edge_cases():
    """Test 7: Edge cases"""
    print("\nTest 7: Edge Cases")
    stack = Stack()

    stack.push(10)
    stack.pop()

    print(f"After push and pop: {stack}")
    assert len(stack) == 0
    assert stack.is_empty() is True


def test_error_handling():
    """Test 8: Error handling"""
    print("\nTest 8: Error Handling")
    stack = Stack()

    # pop on empty stack
    try:
        stack.pop()
        assert False, "Should raise IndexError"
    except IndexError as e:
        print(f"pop on empty stack: {e}")

    # peek on empty stack
    try:
        stack.peek()
        assert False, "Should raise IndexError"
    except IndexError as e:
        print(f"peek on empty stack: {e}")


if __name__ == "__main__":
    """Run all test cases"""
    test_initial_state()
    test_push()
    test_pop()
    test_peek()
    test_is_empty()
    test_multiple_operations()
    test_edge_cases()
    test_error_handling()

    print("\nAll tests passed!")
