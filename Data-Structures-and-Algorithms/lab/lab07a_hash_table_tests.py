from lab07a_hash_table import HashT

# %% test HashT class


def test_initial_state():
    """Test 1: initial state of HashT"""
    print("\nTest 1: Initial State")
    ht = HashT()

    print(f"Initial number of buckets (m): {ht.m}")
    print(f"Initial number of items (n): {ht.n}")
    print(f"Initial load factor: {ht.load_factor}")

    assert ht.m == 10
    assert ht.n == 0
    assert ht.load_factor == 0.0
    return ht


def test_insert():
    """Test 2: insert method"""
    print("\nTest 2: insert")
    ht = HashT()

    ht.insert(7, "seven")
    ht.insert(16, "sixteen")
    ht.insert(25, "twenty-five")

    print("After 3 insertions:")
    ht.display()
    print(f"Number of items: {ht.n}")
    print(f"Load factor: {ht.load_factor}")

    assert ht.n == 3
    assert ht.contains(7) is True
    assert ht.contains(16) is True
    assert ht.contains(25) is True
    return ht


def test_insert_with_strings():
    """Test 3: insert with string keys"""
    print("\nTest 3: insert with string keys")
    ht = HashT()

    ht.insert("apple", 100)
    ht.insert("banana", 200)
    ht.insert("cherry", 300)

    print("After inserting string keys:")
    ht.display()
    print(f"Number of items: {ht.n}")

    assert ht.n == 3
    assert ht.contains("apple") is True
    assert ht.contains("banana") is True
    assert ht.contains("cherry") is True
    return ht


def test_update_existing_key():
    """Test 4: update existing key"""
    print("\nTest 4: update existing key")
    ht = HashT()

    ht.insert(10, "ten")
    ht.insert(20, "twenty")
    print("Before update:")
    ht.display()

    ht.insert(10, "TEN_UPDATED")
    print("After updating key 10:")
    ht.display()
    print(f"Number of items (should remain same): {ht.n}")

    assert ht.n == 2
    assert ht.contains(10) is True
    return ht


def test_contains():
    """Test 5: contains method"""
    print("\nTest 5: contains method")
    ht = HashT()

    ht.insert(5, "five")
    ht.insert(15, "fifteen")
    ht.insert(25, "twenty-five")

    print(f"Contains 5: {ht.contains(5)}")
    print(f"Contains 15: {ht.contains(15)}")
    print(f"Contains 99: {ht.contains(99)}")

    assert ht.contains(5) is True
    assert ht.contains(15) is True
    assert ht.contains(25) is True
    assert ht.contains(99) is False
    return ht


def test_collision_handling():
    """Test 6: collision handling (separate chaining)"""
    print("\nTest 6: collision handling")
    ht = HashT(m=5)  # small table to force collisions

    # these keys will collide (7 % 5 = 2, 12 % 5 = 2, 17 % 5 = 2)
    ht.insert(7, "seven")
    ht.insert(12, "twelve")
    ht.insert(17, "seventeen")

    print("After inserting colliding keys:")
    ht.display()

    assert ht.n == 3
    assert ht.contains(7) is True
    assert ht.contains(12) is True
    assert ht.contains(17) is True
    return ht


def test_load_factor_calculation():
    """Test 7: load factor calculation"""
    print("\nTest 7: load factor calculation")
    ht = HashT(m=10)

    for i in range(5):
        ht.insert(i, f"val_{i}")
        print(f"After inserting {i+1} items: load factor = {ht.load_factor}")

    assert ht.n == 5
    assert ht.load_factor == 0.5
    return ht


def test_resize():
    """Test 8: resize when load factor exceeds 0.75"""
    print("\nTest 8: resize")
    ht = HashT(m=4)  # small initial size

    print(f"Initial size: {ht.m}")

    # insert enough items to trigger resize (load factor > 0.75)
    for i in range(4):
        ht.insert(i, f"val_{i}")
        print(f"After inserting {
              i+1} items: n={ht.n}, m={ht.m}, load_factor={ht.load_factor}")

    print(f"\nFinal size after resize: {ht.m}")
    print(f"Final number of items: {ht.n}")

    # verify all items still exist after resize
    for i in range(4):
        assert ht.contains(i) is True

    return ht


def test_multiple_operations():
    """Test 9: multiple operations"""
    print("\nTest 9: multiple operations")
    ht = HashT()

    # insert multiple items
    for i in range(1, 6):
        ht.insert(i * 10, f"val_{i * 10}")

    print("After 5 insertions:")
    ht.display()
    print(f"Number of items: {ht.n}")

    # update some items
    ht.insert(20, "UPDATED_20")
    ht.insert(40, "UPDATED_40")

    print("\nAfter 2 updates:")
    ht.display()
    print(f"Number of items: {ht.n}")

    assert ht.n == 5
    assert ht.contains(10) is True
    assert ht.contains(50) is True
    return ht


def test_edge_cases():
    """Test 10: edge cases"""
    print("\nTest 10: edge cases")
    ht = HashT()

    # insert and check single item
    ht.insert(42, "answer")
    print(f"Single item inserted, contains 42: {ht.contains(42)}")
    assert ht.contains(42) is True
    assert ht.n == 1

    # check non-existent key
    print(f"Check non-existent key 99: {ht.contains(99)}")
    assert ht.contains(99) is False

    # insert None value
    ht.insert(100, None)
    print(f"Inserted key 100 with None value, contains 100: {
          ht.contains(100)}")
    assert ht.contains(100) is True


def test_hash_function():
    """Test 11: hash function"""
    print("\nTest 11: hash function")
    ht = HashT(m=10)

    # test integer key
    int_hash = ht.hash_function(25)
    print(f"Hash of integer 25: {int_hash}")
    assert int_hash == 25 % 10

    # test string key
    str_hash = ht.hash_function("hello")
    print(f"Hash of string 'hello': {str_hash}")
    assert 0 <= str_hash < 10

    print("Hash function works correctly for both integers and strings")


if __name__ == "__main__":
    """Run all test cases"""
    test_initial_state()
    test_insert()
    test_insert_with_strings()
    test_update_existing_key()
    test_contains()
    test_collision_handling()
    test_load_factor_calculation()
    test_resize()
    test_multiple_operations()
    test_edge_cases()
    test_hash_function()

    print("\nAll tests passed!")
