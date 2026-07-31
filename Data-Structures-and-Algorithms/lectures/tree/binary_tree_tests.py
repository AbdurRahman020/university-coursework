from binary_tree import *

# %% BinaryNode tests


def test_binary_node_creation():
    """Test basic node creation and initialization"""
    print("\nTEST: BinaryNode Creation\n")

    node = BinaryNode(10)
    print(f"Created node with item: {node.item}")
    print(f"Left child: {node.left}")
    print(f"Right child: {node.right}")
    print(f"Parent: {node.parent}")

    assert node.item == 10
    assert node.left is None
    assert node.right is None
    assert node.parent is None
    print("All assertions passed!\n")


def test_binary_node_manual_tree():
    """Test manual tree construction and traversal"""
    print("\nTEST: BinaryNode Manual Tree Construction\n")

    # create a simple tree:
    #       5
    #      / \
    #     3   7
    #    /   / \
    #   1   6   9

    root = BinaryNode(5)
    root.left = BinaryNode(3)
    root.right = BinaryNode(7)
    root.left.parent = root
    root.right.parent = root

    root.left.left = BinaryNode(1)
    root.left.left.parent = root.left

    root.right.left = BinaryNode(6)
    root.right.right = BinaryNode(9)
    root.right.left.parent = root.right
    root.right.right.parent = root.right

    print("Tree structure:")
    print("       5")
    print("      / \\")
    print("     3   7")
    print("    /   / \\")
    print("   1   6   9")
    print()

    # test in-order traversal
    print("In-order traversal:")
    items = [node.item for node in root.subtree_iter()]
    print(f"Items: {items}")
    assert items == [1, 3, 5, 6, 7, 9]
    print("In-order traversal correct!\n")

    # test subtree_first and subtree_last
    first = root.subtree_first()
    last = root.subtree_last()
    print(f"First (leftmost) node: {first.item}")
    print(f"Last (rightmost) node: {last.item}")
    assert first.item == 1
    assert last.item == 9
    print("First/Last methods correct!\n")


def test_binary_node_successor_predecessor():
    """Test successor and predecessor methods"""
    print("\nTEST: BinaryNode Successor and Predecessor\n")

    # create tree: 1-3-5-6-7-9
    root = BinaryNode(5)
    root.left = BinaryNode(3)
    root.right = BinaryNode(7)
    root.left.parent = root
    root.right.parent = root

    root.left.left = BinaryNode(1)
    root.left.left.parent = root.left

    root.right.left = BinaryNode(6)
    root.right.right = BinaryNode(9)
    root.right.left.parent = root.right
    root.right.right.parent = root.right

    # test successors
    node3 = root.left
    succ = node3.successor()
    print(f"Successor of 3: {succ.item if succ else None}")
    assert succ.item == 5

    node5 = root
    succ = node5.successor()
    print(f"Successor of 5: {succ.item if succ else None}")
    assert succ.item == 6

    node9 = root.right.right
    succ = node9.successor()
    print(f"Successor of 9: {succ}")
    assert succ is None
    print("Successor tests passed!\n")

    # Test predecessors
    node7 = root.right
    pred = node7.predecessor()
    print(f"Predecessor of 7: {pred.item if pred else None}")
    assert pred.item == 6

    node5 = root
    pred = node5.predecessor()
    print(f"Predecessor of 5: {pred.item if pred else None}")
    assert pred.item == 3

    node1 = root.left.left
    pred = node1.predecessor()
    print(f"Predecessor of 1: {pred}")
    assert pred is None
    print("Predecessor tests passed!\n")


def test_binary_node_insert_operations():
    """Test insert_before and insert_after methods"""
    print("\nTEST: BinaryNode Insert Operations\n")

    # start with a simple tree
    root = BinaryNode(5)
    root.left = BinaryNode(3)
    root.right = BinaryNode(7)
    root.left.parent = root
    root.right.parent = root

    print("Initial tree (in-order): ", end="")
    items = [node.item for node in root.subtree_iter()]
    print(items)

    # insert 4 after 3
    new_node = BinaryNode(4)
    root.left.subtree_insert_after(new_node)
    print("After inserting 4 after 3: ", end="")
    items = [node.item for node in root.subtree_iter()]
    print(items)
    assert items == [3, 4, 5, 7]

    # insert 2 before 3
    new_node = BinaryNode(2)
    root.left.subtree_insert_before(new_node)
    print("After inserting 2 before 3: ", end="")
    items = [node.item for node in root.subtree_iter()]
    print(items)
    assert items == [2, 3, 4, 5, 7]

    print("Insert operations passed!\n")


def test_binary_node_delete():
    """Test node deletion"""
    print("\nTEST: BinaryNode Delete Operation\n")

    # create tree
    root = BinaryNode(5)
    root.left = BinaryNode(3)
    root.right = BinaryNode(7)
    root.left.parent = root
    root.right.parent = root

    root.left.left = BinaryNode(1)
    root.left.left.parent = root.left

    print("Initial tree (in-order): ", end="")
    items = [node.item for node in root.subtree_iter()]
    print(items)

    # delete leaf node (1)
    deleted = root.left.left.subtree_delete()
    print(f"Deleted node with item: {deleted.item}")
    print("After deleting 1: ", end="")
    items = [node.item for node in root.subtree_iter()]
    print(items)
    assert items == [3, 5, 7]

    print("Delete operation passed!\n")

# %% BinaryTree tests


def test_binary_tree_creation():
    """Test BinaryTree creation and basic operations"""
    print("\nTEST: BinaryTree Creation\n")

    tree = BinaryTree()
    print("Created empty tree")
    print(f"Size: {len(tree)}")
    print(f"Root: {tree.root}")

    assert len(tree) == 0
    assert tree.root is None
    print("Empty tree creation passed!\n")


def test_binary_tree_build():
    """Test building a balanced tree from a list"""
    print("\nTEST: BinaryTree Build Method\n")

    tree = BinaryTree()
    items = [1, 2, 3, 4, 5, 6, 7]
    tree.build(items)

    print(f"Built tree from: {items}")
    print(f"Tree size: {len(tree)}")
    print(f"Root item: {tree.root.item}")

    result = list(tree)
    print(f"In-order traversal: {result}")

    assert len(tree) == 7
    assert tree.root.item == 4  # Middle element
    assert result == items
    print("Build method passed!\n")


def test_binary_tree_iteration():
    """Test tree iteration"""
    print("\nTEST: BinaryTree Iteration\n")

    tree = BinaryTree()
    items = [10, 20, 30, 40, 50]
    tree.build(items)

    print(f"Built tree from: {items}")
    print("Iterating through tree:")
    for i, item in enumerate(tree):
        print(f"  Item {i}: {item}")

    result = list(tree)
    assert result == items
    print("Iteration passed!\n")


def test_binary_tree_empty_build():
    """Test building tree with empty list"""

    print("\nTEST: BinaryTree Empty Build\n")

    tree = BinaryTree()
    tree.build([])

    print("Built tree from empty list")
    print(f"Size: {len(tree)}")
    print(f"Root: {tree.root}")

    # Note: This will cause IndexError due to build_subtree(items, 0, -1)
    # This is a bug in the original code when building from empty list
    print("Warning: Building from empty list causes issues\n")


def test_binary_tree_single_element():
    """Test building tree with single element"""
    print("\nTEST: BinaryTree Single Element\n")

    tree = BinaryTree()
    tree.build([42])

    print("Built tree from: [42]")
    print(f"Size: {len(tree)}")
    print(f"Root item: {tree.root.item}")
    print(f"Root left: {tree.root.left}")
    print(f"Root right: {tree.root.right}")

    assert len(tree) == 1
    assert tree.root.item == 42
    assert tree.root.left is None
    assert tree.root.right is None
    print("Single element build passed!\n")

# %% BST_Node tests


class Item:
    """Helper class for BST testing"""

    def __init__(self, key, value=None):
        self.key = key
        self.value = value if value is not None else key

    def __repr__(self):
        return f"Item(key={self.key}, value={self.value})"


def test_bst_node_find():
    """Test BST find operation"""
    print("\nTEST: BST_Node Find\n")

    # Create BST
    root = BST_Node(Item(5))
    root.left = BST_Node(Item(3))
    root.right = BST_Node(Item(7))
    root.left.parent = root
    root.right.parent = root

    root.left.left = BST_Node(Item(1))
    root.left.left.parent = root.left
    root.right.right = BST_Node(Item(9))
    root.right.right.parent = root.right

    print("BST structure (keys): 1, 3, 5, 7, 9")

    # test finding existing keys
    node = root.subtree_find(3)
    print(f"Find key 3: {node.item if node else None}")
    assert node and node.item.key == 3

    node = root.subtree_find(9)
    print(f"Find key 9: {node.item if node else None}")
    assert node and node.item.key == 9

    # Test finding non-existing key
    node = root.subtree_find(6)
    print(f"Find key 6: {node}")
    assert node is None

    print("Find tests passed!\n")


def test_bst_node_find_next():
    """Test BST find_next operation"""
    print("\nTEST: BST_Node Find Next\n")

    # create BST with keys: 1, 3, 5, 7, 9
    root = BST_Node(Item(5))
    root.left = BST_Node(Item(3))
    root.right = BST_Node(Item(7))
    root.left.parent = root
    root.right.parent = root

    root.left.left = BST_Node(Item(1))
    root.left.left.parent = root.left
    root.right.right = BST_Node(Item(9))
    root.right.right.parent = root.right

    print("BST keys: 1, 3, 5, 7, 9")

    # find next after 2 (should be 3)
    node = root.subtree_find_next(2)
    print(f"Next after 2: {node.item.key if node else None}")
    assert node and node.item.key == 3

    # find next after 5 (should be 7)
    node = root.subtree_find_next(5)
    print(f"Next after 5: {node.item.key if node else None}")
    assert node and node.item.key == 7

    # find next after 9 (should be None)
    node = root.subtree_find_next(9)
    print(f"Next after 9: {node}")
    assert node is None

    print("Find next tests passed!\n")


def test_bst_node_find_prev():
    """Test BST find_prev operation"""
    print("\nTEST: BST_Node Find Prev\n")

    # create BST with keys: 1, 3, 5, 7, 9
    root = BST_Node(Item(5))
    root.left = BST_Node(Item(3))
    root.right = BST_Node(Item(7))
    root.left.parent = root
    root.right.parent = root

    root.left.left = BST_Node(Item(1))
    root.left.left.parent = root.left
    root.right.right = BST_Node(Item(9))
    root.right.right.parent = root.right

    print("BST keys: 1, 3, 5, 7, 9")

    # find prev before 8 (should be 7)
    node = root.subtree_find_prev(8)
    print(f"Prev before 8: {node.item.key if node else None}")
    assert node and node.item.key == 7

    # find prev before 5 (should be 3)
    node = root.subtree_find_prev(5)
    print(f"Prev before 5: {node.item.key if node else None}")
    assert node and node.item.key == 3

    # find prev before 1 (should be None)
    node = root.subtree_find_prev(1)
    print(f"Prev before 1: {node}")
    assert node is None

    print("Find prev tests passed!\n")


def test_bst_node_insert():
    """Test BST insert operation"""
    print("\nTEST: BST_Node Insert\n")

    # create initial BST
    root = BST_Node(Item(5))

    print("Initial BST: [5]")

    # insert nodes
    root.subtree_insert(BST_Node(Item(3)))
    print("After inserting 3: ", end="")
    keys = [node.item.key for node in root.subtree_iter()]
    print(keys)

    root.subtree_insert(BST_Node(Item(7)))
    print("After inserting 7: ", end="")
    keys = [node.item.key for node in root.subtree_iter()]
    print(keys)

    root.subtree_insert(BST_Node(Item(1)))
    print("After inserting 1: ", end="")
    keys = [node.item.key for node in root.subtree_iter()]
    print(keys)

    root.subtree_insert(BST_Node(Item(9)))
    print("After inserting 9: ", end="")
    keys = [node.item.key for node in root.subtree_iter()]
    print(keys)

    assert keys == [1, 3, 5, 7, 9]
    print("Insert tests passed!\n")

# %% SetBinaryTree tests


def test_set_binary_tree_creation():
    """Test SetBinaryTree creation"""
    print("\nTEST: SetBinaryTree Creation\n")

    bst = SetBinaryTree()
    print("Created empty SetBinaryTree")
    print(f"Size: {len(bst)}")
    print(f"Root: {bst.root}")

    assert len(bst) == 0
    assert bst.root is None
    print("Creation passed!\n")


def test_set_binary_tree_insert():
    """Test SetBinaryTree insert operation"""
    print("\nTEST: SetBinaryTree Insert\n")

    bst = SetBinaryTree()

    # insert items
    items_to_insert = [Item(5), Item(3), Item(7), Item(1), Item(9)]
    print(f"Inserting items with keys: {
          [item.key for item in items_to_insert]}")

    for item in items_to_insert:
        result = bst.insert(item)
        print(f"  Inserted key {item.key}: {result}")

    print(f"Tree size after insertions: {len(bst)}")

    keys = [item.key for item in bst.iter_order()]
    print(f"In-order traversal: {keys}")

    assert len(bst) == 5
    assert keys == [1, 3, 5, 7, 9]
    print("Insert tests passed!\n")


def test_set_binary_tree_find_operations():
    """Test SetBinaryTree find operations"""
    print("\nTEST: SetBinaryTree Find Operations\n")

    bst = SetBinaryTree()
    bst.build([Item(i) for i in [5, 3, 7, 1, 9, 4, 6, 8]])

    keys = [item.key for item in bst.iter_order()]
    print(f"BST keys: {keys}")

    # test find
    item = bst.find(5)
    print(f"Find key 5: {item.key if item else None}")
    assert item and item.key == 5

    item = bst.find(10)
    print(f"Find key 10 (not exists): {item}")
    assert item is None

    # test find_min and find_max
    min_item = bst.find_min()
    max_item = bst.find_max()
    print(f"Minimum key: {min_item.key if min_item else None}")
    print(f"Maximum key: {max_item.key if max_item else None}")
    assert min_item.key == 1
    assert max_item.key == 9

    # test find_next
    next_item = bst.find_next(5)
    print(f"Next after key 5: {next_item.key if next_item else None}")
    assert next_item.key == 6

    # test find_prev
    prev_item = bst.find_prev(5)
    print(f"Prev before key 5: {prev_item.key if prev_item else None}")
    assert prev_item.key == 4

    print("Find operations passed!\n")


def test_set_binary_tree_delete():
    """Test SetBinaryTree delete operation"""
    print("\nTEST: SetBinaryTree Delete\n")

    bst = SetBinaryTree()
    bst.build([Item(i) for i in [5, 3, 7, 1, 9]])

    print("Initial BST keys: ", end="")
    keys = [item.key for item in bst.iter_order()]
    print(keys)
    print(f"Size: {len(bst)}")

    # delete a leaf node
    deleted = bst.delete(1)
    print(f"\nDeleted key: {deleted.key}")
    keys = [item.key for item in bst.iter_order()]
    print(f"After deleting 1: {keys}")
    print(f"Size: {len(bst)}")
    assert len(bst) == 4
    assert keys == [3, 5, 7, 9]

    # delete a node with children
    deleted = bst.delete(5)
    print(f"\nDeleted key: {deleted.key}")
    keys = [item.key for item in bst.iter_order()]
    print(f"After deleting 5: {keys}")
    print(f"Size: {len(bst)}")
    assert len(bst) == 3

    print("Delete tests passed!\n")


def test_set_binary_tree_duplicate_insert():
    """Test inserting duplicate keys"""
    print("\nTEST: SetBinaryTree Duplicate Insert\n")

    bst = SetBinaryTree()

    # insert first item
    result = bst.insert(Item(5, "first"))
    print(f"Insert key 5 (first time): {result}")
    print(f"Size: {len(bst)}")
    assert result is True
    assert len(bst) == 1

    # insert duplicate with different value
    result = bst.insert(Item(5, "second"))
    print(f"Insert key 5 (duplicate): {result}")
    print(f"Size: {len(bst)}")

    # find and check value
    item = bst.find(5)
    print(f"Value for key 5: {item.value}")

    # Note: The size increases even for duplicates (potential bug)
    print(f"Final size: {len(bst)}")
    print("Note: Duplicate inserts still increment size\n")


def test_set_binary_tree_comprehensive():
    """Comprehensive test with various operations"""
    print("\nTEST: SetBinaryTree Comprehensive\n")

    bst = SetBinaryTree()

    # build tree
    items = [Item(i) for i in [50, 30, 70, 20, 40, 60, 80]]
    print(f"Building tree with keys: {[item.key for item in items]}")
    bst.build(items)

    print(f"Tree size: {len(bst)}")
    keys = [item.key for item in bst.iter_order()]
    print(f"In-order: {keys}")

    # test all operations
    print(f"\nMin: {bst.find_min().key}")
    print(f"Max: {bst.find_max().key}")
    print(f"Find 40: {bst.find(40).key if bst.find(40) else None}")
    print(f"Next after 40: {bst.find_next(
        40).key if bst.find_next(40) else None}")
    print(f"Prev before 40: {bst.find_prev(
        40).key if bst.find_prev(40) else None}")

    # delete middle node
    bst.delete(50)
    keys = [item.key for item in bst.iter_order()]
    print(f"\nAfter deleting 50: {keys}")
    print(f"Size: {len(bst)}")

    assert len(bst) == 6
    assert 50 not in keys
    print("Comprehensive test passed!\n")

# %%


def run_all_tests():
    """Run all test functions"""
    print("RUNNING ALL TESTS")

    # BinaryNode tests
    test_binary_node_creation()
    test_binary_node_manual_tree()
    test_binary_node_successor_predecessor()
    test_binary_node_insert_operations()
    test_binary_node_delete()

    # BinaryTree tests
    test_binary_tree_creation()
    test_binary_tree_build()
    test_binary_tree_iteration()
    test_binary_tree_single_element()

    # BST_Node tests
    test_bst_node_find()
    test_bst_node_find_next()
    test_bst_node_find_prev()
    test_bst_node_insert()

    # SetBinaryTree tests
    test_set_binary_tree_creation()
    test_set_binary_tree_insert()
    test_set_binary_tree_find_operations()
    test_set_binary_tree_delete()
    test_set_binary_tree_duplicate_insert()
    test_set_binary_tree_comprehensive()

    print("ALL TESTS COMPLETED!")


if __name__ == "__main__":
    run_all_tests()
