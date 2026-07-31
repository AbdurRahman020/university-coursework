from lab08_binary_search_tree import BSTNode
import random

# %% test BST


def test_single_node():
    """Test BST with a single node."""
    print("Test 1: Single Node")
    bst = BSTNode(50)
    assert bst.key == 50
    assert bst.value == 50
    assert bst.left is None
    assert bst.right is None
    assert bst.count_nodes() == 1
    print("Single node test passed\n")


def test_insert_right():
    """Test inserting nodes to the right."""
    print("Test 2: Insert Right")
    bst = BSTNode(50)
    bst.insert(60)
    bst.insert(70)
    assert bst.right is not None
    assert bst.right.key == 60
    assert bst.right.right.key == 70
    assert bst.count_nodes() == 3
    print("Insert right test passed\n")


def test_insert_left():
    """Test inserting nodes to the left."""
    print("Test 3: Insert Left")
    bst = BSTNode(50)
    bst.insert(40)
    bst.insert(30)
    assert bst.left is not None
    assert bst.left.key == 40
    assert bst.left.left.key == 30
    assert bst.count_nodes() == 3
    print("Insert left test passed\n")


def test_insert_both_sides():
    """Test inserting nodes on both sides."""
    print("Test 4: Insert Both Sides")
    bst = BSTNode(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)
    assert bst.left.key == 30
    assert bst.right.key == 70
    assert bst.left.left.key == 20
    assert bst.left.right.key == 40
    assert bst.right.left.key == 60
    assert bst.right.right.key == 80
    assert bst.count_nodes() == 7
    print("Insert both sides test passed\n")


def test_insert_duplicate():
    """Test inserting duplicate keys (should not insert)."""
    print("Test 5: Insert Duplicate")
    bst = BSTNode(50)
    bst.insert(30)
    bst.insert(70)
    initial_count = bst.count_nodes()
    bst.insert(50)  # duplicate
    bst.insert(30)  # duplicate
    assert bst.count_nodes() == initial_count
    print("Insert duplicate test passed\n")


def test_inorder_traversal():
    """Test that inorder traversal returns sorted order."""
    print("Test 6: Inorder Traversal (Sorted Order)")
    bst = BSTNode(50)
    values = [30, 70, 20, 40, 60, 80, 10, 25, 35, 45]
    for val in values:
        bst.insert(val)

    result = bst.inorder_traversal()
    expected = sorted([50] + values)
    assert result == expected, f"Expected {expected}, got {result}"
    print(f"Inorder traversal test passed: {result}\n")


def test_search():
    """Test searching for nodes."""
    print("Test 7: Search")
    bst = BSTNode(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)

    found = bst.search(30)
    assert found is not None
    assert found.key == 30

    found = bst.search(40)
    assert found is not None
    assert found.key == 40

    found = bst.search(100)
    assert found is None

    print("Search test passed\n")


def test_custom_values():
    """Test BST with custom key-value pairs."""
    print("Test 8: Custom Key-Value Pairs")
    bst = BSTNode(50, "fifty")
    bst.insert(30, "thirty")
    bst.insert(70, "seventy")

    assert bst.value == "fifty"
    assert bst.left.value == "thirty"
    assert bst.right.value == "seventy"
    print("Custom values test passed\n")


def test_large_random_tree():
    """Test with a larger random tree."""
    print("Test 9: Large Random Tree")
    random.seed(42)  # for reproducibility
    bst = BSTNode(50)
    inserted_values = {50}

    for _ in range(100):
        val = random.randint(0, 200)
        bst.insert(val)
        inserted_values.add(val)

    # check that all unique values are in the tree
    inorder = bst.inorder_traversal()
    assert len(inorder) == len(inserted_values)
    assert set(inorder) == inserted_values

    # check that inorder traversal is sorted
    assert inorder == sorted(inorder)

    print(f"Large random tree test passed (inserted {
          len(inserted_values)} unique values)\n")


def test_display_output():
    """Test that display methods run without errors."""
    print("Test 10: Display Output")
    bst = BSTNode(50, 'uet')
    bst.insert(30, 'uet')
    bst.insert(70, 'uet')
    bst.insert(20, 'uet')
    bst.insert(40, 'uet')
    bst.insert(75, 'uet')
    bst.insert(10, 'uet')
    bst.insert(65, 'uet')
    bst.insert(60, 'uet')
    bst.insert(35, 'uet')

    try:
        lines, width, height, _ = bst.display_aux()
        assert len(lines) > 0
        assert width > 0
        assert height > 0
        print("Display aux executed successfully")

        print("\nTree visualization:")
        bst.display()
        print("Display output test passed\n")
    except Exception as e:
        assert False, f"Display failed with error: {e}"


def test_delete_leaf_node():
    """Test deleting a leaf node."""
    print("Test 11: Delete Leaf Node")
    bst = BSTNode(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.display()
    bst.delete(20)
    bst.display()
    assert bst.search(20) is None
    assert bst.count_nodes() == 4
    assert bst.inorder_traversal() == [30, 40, 50, 70]
    print("Delete leaf node test passed\n")


def test_delete_node_with_one_child():
    """Test deleting a node with one child."""
    print("Test 12: Delete Node with One Child")
    bst = BSTNode(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(60)
    bst.display()
    bst.delete(70)  # has only left child (60)
    bst.display()
    assert bst.search(70) is None
    assert bst.search(60) is not None
    assert bst.count_nodes() == 4
    assert bst.inorder_traversal() == [20, 30, 50, 60]
    print("Delete node with one child test passed\n")


def test_delete_node_with_two_children():
    """Test deleting a node with two children."""
    print("Test 13: Delete Node with Two Children")
    bst = BSTNode(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)
    bst.display()
    bst.delete(30)  # has two children
    bst.display()
    assert bst.search(30) is None
    assert bst.count_nodes() == 6
    assert bst.inorder_traversal() == [20, 40, 50, 60, 70, 80]
    print("Delete node with two children test passed\n")


def test_delete_root():
    """Test deleting the root node."""
    print("Test 14: Delete Root")
    bst = BSTNode(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.display()
    bst = bst.delete(50)
    bst.display()
    assert bst.search(50) is None
    assert bst.count_nodes() == 5
    assert bst.inorder_traversal() == [20, 30, 40, 60, 70]
    print("Delete root test passed\n")


def test_delete_nonexistent():
    """Test deleting a non-existent key."""
    print("Test 15: Delete Non-existent Key")
    bst = BSTNode(50)
    bst.insert(30)
    bst.insert(70)

    initial_count = bst.count_nodes()
    bst.delete(100)  # doesn't exist
    assert bst.count_nodes() == initial_count
    assert bst.inorder_traversal() == [30, 50, 70]
    print("Delete non-existent key test passed\n")


def test_delete_multiple():
    """Test deleting multiple nodes."""
    print("Test 16: Delete Multiple Nodes")
    bst = BSTNode(50)
    values = [30, 70, 20, 40, 60, 80, 10, 25]
    for val in values:
        bst.insert(val)

    bst.delete(20)
    bst.delete(70)
    bst = bst.delete(50)

    remaining = [10, 25, 30, 40, 60, 80]
    assert bst.inorder_traversal() == remaining
    assert bst.count_nodes() == len(remaining)
    print("Delete multiple nodes test passed\n")


def run_all_tests():
    """Run all test cases"""
    test_single_node()
    test_insert_right()
    test_insert_left()
    test_insert_both_sides()
    test_insert_duplicate()
    test_inorder_traversal()
    test_search()
    test_custom_values()
    test_large_random_tree()
    test_display_output()
    test_delete_leaf_node()
    test_delete_node_with_one_child()
    test_delete_node_with_two_children()
    test_delete_root()
    test_delete_nonexistent()
    test_delete_multiple()

    print("All tests passed!")


if __name__ == "__main__":
    run_all_tests()
