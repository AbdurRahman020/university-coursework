from avl_tree import *

# %% test cases


def test_binary_node_creation():
    """Test basic AVL node creation and initialization"""
    print("\nTEST: Binary_Node Creation\n")

    node = Binary_Node(10)
    print(f"Created node with item: {node.item}")
    print(f"Height: {node.height}")
    print(f"Left child: {node.left}")
    print(f"Right child: {node.right}")
    print(f"Parent: {node.parent}")

    assert node.item == 10
    assert node.height == 0  # Leaf node has height 0 (1 + max(-1, -1) = 0)
    assert node.left is None
    assert node.right is None
    assert node.parent is None
    print("All assertions passed!\n")


def test_binary_node_height_update():
    """Test height calculation after building a tree"""
    print("\nTEST: Binary_Node Height Update\n")

    # create a simple tree manually
    root = Binary_Node(5)
    root.left = Binary_Node(3)
    root.right = Binary_Node(7)
    root.left.parent = root
    root.right.parent = root

    root.subtree_update()

    print(f"Root height: {root.height}")
    print(f"Left child height: {root.left.height}")
    print(f"Right child height: {root.right.height}")

    assert root.height == 1  # 1 + max(0, 0) = 1
    assert root.left.height == 0  # Leaf node
    assert root.right.height == 0  # Leaf node
    print("Height update correct!\n")


def test_binary_node_skew():
    """Test skew calculation"""
    print("\nTEST: Binary_Node Skew Calculation\n")

    # balanced tree
    root = Binary_Node(5)
    root.left = Binary_Node(3)
    root.right = Binary_Node(7)
    root.left.parent = root
    root.right.parent = root

    print(f"Balanced tree skew: {root.skew()}")
    assert root.skew() == 0

    # right-heavy tree
    root2 = Binary_Node(5)
    root2.right = Binary_Node(7)
    root2.right.parent = root2
    root2.right.right = Binary_Node(9)
    root2.right.right.parent = root2.right
    root2.right.subtree_update()
    root2.subtree_update()

    print(f"Right-heavy tree skew: {root2.skew()}")
    assert root2.skew() == 2
    print("Skew calculation correct!\n")


def test_binary_node_rotations():
    """Test left and right rotations"""
    print("\nTEST: Binary_Node Rotations\n")

    # test right rotation
    root = Binary_Node(5)
    root.left = Binary_Node(3)
    root.left.parent = root
    root.left.left = Binary_Node(1)
    root.left.left.parent = root.left

    print("Before right rotation:")
    items = [node.item for node in root.subtree_iter()]
    print(f"In-order: {items}")

    root.subtree_rotate_right()

    print("After right rotation:")
    items = [node.item for node in root.subtree_iter()]
    print(f"In-order: {items}")
    assert items == [1, 3, 5]
    print("Right rotation maintains in-order!\n")


def test_size_node_creation():
    """Test Size_Node creation and size tracking"""
    print("\nTEST: Size_Node Creation and Size Tracking\n")

    node = Size_Node(10)
    print(f"Created node with item: {node.item}")
    print(f"Height: {node.height}")
    print(f"Size: {node.size}")

    assert node.item == 10
    assert node.height == 0  # Leaf node has height 0
    assert node.size == 1

    # add children
    node.left = Size_Node(5)
    node.right = Size_Node(15)
    node.left.parent = node
    node.right.parent = node
    node.subtree_update()

    print(f"After adding children, root size: {node.size}")
    assert node.size == 3
    print("Size tracking correct!\n")


def test_size_node_subtree_at():
    """Test indexing with subtree_at"""
    print("\nTEST: Size_Node subtree_at\n")

    # build a tree: 1, 2, 3, 4, 5
    root = Size_Node(3)
    root.left = Size_Node(2)
    root.right = Size_Node(4)
    root.left.parent = root
    root.right.parent = root

    root.left.left = Size_Node(1)
    root.left.left.parent = root.left

    root.right.right = Size_Node(5)
    root.right.right.parent = root.right

    # update sizes bottom-up
    root.left.left.subtree_update()
    root.right.right.subtree_update()
    root.left.subtree_update()
    root.right.subtree_update()
    root.subtree_update()

    print("Tree in-order: [1, 2, 3, 4, 5]")

    for i in range(5):
        node = root.subtree_at(i)
        print(f"Index {i}: {node.item}")
        assert node.item == i + 1

    print("Indexing correct!\n")


def test_seq_binary_tree_creation():
    """Test Seq_Binary_Tree creation"""
    print("\nTEST: Seq_Binary_Tree Creation\n")

    tree = Seq_Binary_Tree()
    print("Created empty Seq_Binary_Tree")
    print(f"Size: {len(tree)}")
    print(f"Root: {tree.root}")

    assert len(tree) == 0
    assert tree.root is None
    print("Creation passed!\n")


def test_seq_binary_tree_build():
    """Test building a sequence tree"""
    print("\nTEST: Seq_Binary_Tree Build\n")

    tree = Seq_Binary_Tree()
    items = [1, 2, 3, 4, 5, 6, 7]
    tree.build(items)

    print(f"Built tree from: {items}")
    print(f"Tree size: {len(tree)}")
    print(f"Root item: {tree.root.item}")

    result = list(tree)
    print(f"In-order traversal: {result}")

    assert len(tree) == 7
    assert tree.root.item == 4
    assert result == items
    print("Build method passed!\n")


def test_seq_binary_tree_get_set():
    """Test get_at and set_at operations"""

    print("\nTEST: Seq_Binary_Tree Get/Set\n")

    tree = Seq_Binary_Tree()
    tree.build([10, 20, 30, 40, 50])

    print("Initial tree: [10, 20, 30, 40, 50]")

    # test get
    for i in range(5):
        item = tree.get_at(i)
        print(f"Get index {i}: {item}")
        assert item == (i + 1) * 10

    # test set
    tree.set_at(2, 35)
    print("\nAfter set_at(2, 35):")
    result = list(tree)
    print(f"Tree: {result}")
    assert result == [10, 20, 35, 40, 50]
    print("Get/Set operations passed!\n")


def test_seq_binary_tree_insert():
    """Test insert_at operations"""
    print("\nTEST: Seq_Binary_Tree Insert\n")

    tree = Seq_Binary_Tree()
    tree.build([10, 30, 50])

    print("Initial tree: [10, 30, 50]")

    tree.insert_at(1, 20)
    result = list(tree)
    print(f"After insert_at(1, 20): {result}")
    assert result == [10, 20, 30, 50]

    tree.insert_at(4, 60)
    result = list(tree)
    print(f"After insert_at(4, 60): {result}")
    assert result == [10, 20, 30, 50, 60]

    tree.insert_at(0, 5)
    result = list(tree)
    print(f"After insert_at(0, 5): {result}")
    assert result == [5, 10, 20, 30, 50, 60]

    print("Insert operations passed!\n")


def test_seq_binary_tree_delete():
    """Test delete_at operations"""

    print("\nTEST: Seq_Binary_Tree Delete\n")

    tree = Seq_Binary_Tree()
    tree.build([10, 20, 30, 40, 50])

    print("Initial tree: [10, 20, 30, 40, 50]")

    deleted = tree.delete_at(2)
    result = list(tree)
    print(f"After delete_at(2): {result}, deleted: {deleted}")
    assert deleted == 30
    assert result == [10, 20, 40, 50]

    deleted = tree.delete_at(0)
    result = list(tree)
    print(f"After delete_at(0): {result}, deleted: {deleted}")
    assert deleted == 10
    assert result == [20, 40, 50]

    print("Delete operations passed!\n")


def test_seq_binary_tree_first_last():
    """Test insert_first, delete_first, insert_last, delete_last"""
    print("\nTEST: Seq_Binary_Tree First/Last Operations\n")

    tree = Seq_Binary_Tree()
    tree.build([30, 40, 50])

    print("Initial tree: [30, 40, 50]")

    tree.insert_first(20)
    result = list(tree)
    print(f"After insert_first(20): {result}")
    assert result == [20, 30, 40, 50]

    tree.insert_last(60)
    result = list(tree)
    print(f"After insert_last(60): {result}")
    assert result == [20, 30, 40, 50, 60]

    deleted = tree.delete_first()
    result = list(tree)
    print(f"After delete_first(): {result}, deleted: {deleted}")
    assert deleted == 20
    assert result == [30, 40, 50, 60]

    deleted = tree.delete_last()
    result = list(tree)
    print(f"After delete_last(): {result}, deleted: {deleted}")
    assert deleted == 60
    assert result == [30, 40, 50]

    print("First/Last operations passed!\n")


def test_seq_binary_tree_comprehensive():
    """Comprehensive test with various operations"""
    print("\nTEST: Seq_Binary_Tree Comprehensive\n")

    tree = Seq_Binary_Tree()

    # build from empty
    tree.insert_first(50)
    print(f"After insert_first(50): {list(tree)}")

    # add more elements
    tree.insert_at(0, 40)
    tree.insert_at(0, 30)
    tree.insert_last(60)
    tree.insert_last(70)
    result = list(tree)
    print(f"After multiple inserts: {result}")
    assert result == [30, 40, 50, 60, 70]

    # modify middle element
    tree.set_at(2, 55)
    result = list(tree)
    print(f"After set_at(2, 55): {result}")
    assert result == [30, 40, 55, 60, 70]

    # delete from various positions
    tree.delete_at(1)
    tree.delete_at(2)
    result = list(tree)
    print(f"After deleting index 1 and 2: {result}")
    assert result == [30, 55, 70]

    print(f"Final tree size: {len(tree)}")
    assert len(tree) == 3
    print("Comprehensive test passed!\n")


def run_all_tests():
    """Run all test functions"""
    print("RUNNING ALL TESTS")

    # Binary_Node tests
    test_binary_node_creation()
    test_binary_node_height_update()
    test_binary_node_skew()
    test_binary_node_rotations()

    # Size_Node tests
    test_size_node_creation()
    test_size_node_subtree_at()

    # Seq_Binary_Tree tests
    test_seq_binary_tree_creation()
    test_seq_binary_tree_build()
    test_seq_binary_tree_get_set()
    test_seq_binary_tree_insert()
    test_seq_binary_tree_delete()
    test_seq_binary_tree_first_last()
    test_seq_binary_tree_comprehensive()

    print("ALL TESTS COMPLETED!")


if __name__ == "__main__":
    run_all_tests()
