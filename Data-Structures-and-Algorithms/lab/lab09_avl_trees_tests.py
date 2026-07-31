from lab09_avl_trees import AVLTree
import random
import math

# %% test cases


def test_basic_insertion():
    """Test basic insertion operations."""
    print("\nTEST 1: Basic Insertion")

    tree = AVLTree()
    keys = [10, 20, 30, 40, 50, 25]

    print(f"Inserting keys: {keys}")
    for key in keys:
        tree.insert(key)

    print(f"\nTree size: {len(tree)}")
    print(f"Tree height: {tree.get_height()}")
    print(f"Is balanced: {tree.is_balanced()}")
    print(f"Rotations performed: {tree.get_rotation_count()}")
    print("\nTree structure:")
    tree.print_tree()


def test_worst_case_bst():
    """Test insertion of sorted sequence (worst case for regular BST)."""
    print("\nTEST 2: Worst Case BST (Sorted Insertion)")

    tree = AVLTree()
    keys = [1, 2, 3, 4, 5, 6, 7]

    print(f"Inserting sorted keys: {keys}")
    for key in keys:
        tree.insert(key)

    print(f"\nTree size: {len(tree)}")
    print(f"Tree height: {tree.get_height()}")
    print(f"Expected height for balanced tree: ~{
          int(__import__('math').log2(len(tree)))}")
    print(f"Is balanced: {tree.is_balanced()}")
    print(f"Rotations performed: {tree.get_rotation_count()}")
    print("\nTree structure:")
    tree.print_tree()


def test_search_operations():
    """Test search, minimum, and maximum operations."""
    print("\nTEST 3: Search Operations")

    tree = AVLTree()
    keys = [15, 10, 20, 8, 12, 17, 25]

    print(f"Building tree with keys: {keys}")
    for key in keys:
        tree.insert(key)

    print("\nSearch operations:")
    test_keys = [12, 17, 100, 8]
    for key in test_keys:
        result = tree.search(key)
        print(f"  Search({key}): {'Found' if result else 'Not found'}")

    print(f"\nMinimum key: {tree.find_minimum()}")
    print(f"Maximum key: {tree.find_maximum()}")


def test_deletion():
    """Test deletion operations."""
    print("\nTEST 4: Deletion Operations")

    tree = AVLTree()
    keys = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 65]

    print(f"Building tree with keys: {keys}")
    for key in keys:
        tree.insert(key)

    print("\nInitial tree:")
    tree.print_tree()

    tree.reset_rotation_count()
    delete_keys = [20, 30, 50]
    print(f"\nDeleting keys: {delete_keys}")
    for key in delete_keys:
        tree.delete(key)
        print(f"  Deleted {key}")

    print(f"\nTree size after deletion: {len(tree)}")
    print(f"Is balanced: {tree.is_balanced()}")
    print(f"Rotations during deletion: {tree.get_rotation_count()}")
    print("\nTree after deletions:")
    tree.print_tree()


def test_all_rotation_cases():
    """Test all four rotation cases."""
    print("\nTEST 5: All Rotation Cases")

    # left-left Case
    print("\n--- Left-Left Case ---")
    tree = AVLTree()
    tree.insert(30)
    tree.insert(20)
    tree.insert(10)
    print("Inserted: 30, 20, 10")
    tree.print_tree()

    # right-right Case
    print("\n--- Right-Right Case ---")
    tree = AVLTree()
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    print("Inserted: 10, 20, 30")
    tree.print_tree()

    # left-right Case
    print("\n--- Left-Right Case ---")
    tree = AVLTree()
    tree.insert(30)
    tree.insert(10)
    tree.insert(20)
    print("Inserted: 30, 10, 20")
    tree.print_tree()

    # right-left Case
    print("\n--- Right-Left Case ---")
    tree = AVLTree()
    tree.insert(10)
    tree.insert(30)
    tree.insert(20)
    print("Inserted: 10, 30, 20")
    tree.print_tree()


def test_inorder_traversal():
    """Test in-order traversal."""
    print("\nTEST 6: In-order Traversal")

    tree = AVLTree()
    keys = [50, 30, 70, 20, 40, 60, 80]

    print(f"Inserting keys: {keys}")
    for key in keys:
        tree.insert(key)

    print("\nIn-order traversal (should be sorted):")
    print(f"  {list(tree)}")


def test_large_dataset():
    """Test with a larger dataset."""
    print("\nTEST 7: Large Dataset Performance")

    tree = AVLTree()
    n = 100
    keys = list(range(1, n + 1))
    random.shuffle(keys)

    print(f"Inserting {n} random keys...")
    for key in keys:
        tree.insert(key)

    print(f"\nTree size: {len(tree)}")
    print(f"Tree height: {tree.get_height()}")
    print(f"Theoretical minimum height: ~{int(math.log2(n))}")
    print(f"Is balanced: {tree.is_balanced()}")
    print(f"Total rotations: {tree.get_rotation_count()}")
    print(f"Average rotations per insertion: {
          tree.get_rotation_count() / n:.2f}")


def test_duplicate_insertion():
    """Test insertion of duplicate keys."""
    print("\nTEST 8: Duplicate Key Insertion")

    tree = AVLTree()
    keys = [50, 30, 70, 30, 50, 70]

    print(f"Inserting keys (with duplicates): {keys}")
    for key in keys:
        result = tree.insert(key, f"value_{key}")
        if not result:
            print(f"  Key {key} already exists (value updated)")

    print(f"\nTree size: {len(tree)} (should be 3, not 6)")
    print(f"Is balanced: {tree.is_balanced()}")
    print("\nTree structure:")
    tree.print_tree()


def test_sequential_deletion():
    """Test sequential deletion of all nodes."""
    print("\nTEST 9: Sequential Deletion of All Nodes")

    tree = AVLTree()
    keys = [50, 25, 75, 10, 30, 60, 80, 5, 15, 27, 55, 65, 85]

    print(f"Building tree with keys: {keys}")
    for key in keys:
        tree.insert(key)

    print("\nInitial tree:")
    tree.print_tree()

    print("\nDeleting all nodes one by one...")
    for key in keys:
        tree.delete(key)
        print(f"  Deleted {key}, size: {
              len(tree)}, balanced: {tree.is_balanced()}")

    print(f"\nFinal tree size: {len(tree)}")
    print(f"Tree is empty: {len(tree) == 0}")


def test_alternating_operations():
    """Test alternating insertions and deletions."""
    print("\nTEST 10: Alternating Insert/Delete Operations")

    tree = AVLTree()

    print("Phase 1: Insert 5 nodes")
    for i in [10, 5, 15, 3, 7]:
        tree.insert(i)
    print(f"  Size: {len(tree)}, Height: {tree.get_height()}")
    tree.print_tree()

    print("Phase 2: Delete 2 nodes")
    tree.delete(3)
    tree.delete(15)
    print(f"  Size: {len(tree)}, Height: {tree.get_height()}")
    tree.print_tree()

    print("Phase 3: Insert 4 more nodes")
    for i in [20, 1, 8, 12]:
        tree.insert(i)
    print(f"  Size: {len(tree)}, Height: {tree.get_height()}")
    tree.print_tree()

    print("Phase 4: Delete 3 nodes")
    tree.delete(10)
    tree.delete(5)
    tree.delete(20)
    print(f"  Size: {len(tree)}, Height: {tree.get_height()}")
    tree.print_tree()

    print(f"Is balanced: {tree.is_balanced()}")


def test_edge_cases():
    """Test various edge cases."""
    print("\nTEST 11: Edge Cases")

    # empty tree operations
    print("Testing empty tree operations:")
    tree = AVLTree()
    print(f"  Search in empty tree: {tree.search(10)}")
    print(f"  Delete from empty tree: {tree.delete(10)}")
    print(f"  Min in empty tree: {tree.find_minimum()}")
    print(f"  Max in empty tree: {tree.find_maximum()}")
    print(f"  Height of empty tree: {tree.get_height()}")

    # single node tree
    print("\nTesting single node tree:")
    tree.insert(42)
    print(f"  Size: {len(tree)}")
    print(f"  Height: {tree.get_height()}")
    print(f"  Min: {tree.find_minimum()}")
    print(f"  Max: {tree.find_maximum()}\n")
    tree.print_tree()

    # delete single node
    print("Deleting the only node:")
    tree.delete(42)
    print(f"  Size after deletion: {len(tree)}")
    print(f"  Tree is empty: {len(tree) == 0}")

    # two node tree
    print("\nTesting two node tree:")
    tree.insert(10)
    tree.insert(20)
    tree.print_tree()
    print(f"  Height: {tree.get_height()}")


def test_negative_numbers():
    """Test tree with negative numbers."""
    print("\nTEST 12: Negative Numbers")

    tree = AVLTree()
    keys = [-50, -30, -70, 10, -20, -60, 30, -80, 20]

    print(f"Inserting keys with negatives: {keys}")
    for key in keys:
        tree.insert(key)

    print(f"\nTree size: {len(tree)}")
    print(f"Tree height: {tree.get_height()}")
    print(f"Is balanced: {tree.is_balanced()}")
    print("\nTree structure:")
    tree.print_tree()

    print(f"\nMinimum: {tree.find_minimum()}")
    print(f"Maximum: {tree.find_maximum()}")
    print(f"In-order traversal: {list(tree)}")


def test_string_keys():
    """Test AVL tree with string keys."""
    print("\nTEST 13: String Keys")

    tree = AVLTree()
    words = ["dog", "cat", "bird", "elephant", "ant", "fox", "zebra"]

    print(f"Inserting words: {words}")
    for word in words:
        tree.insert(word)

    print(f"\nTree size: {len(tree)}")
    print(f"Tree height: {tree.get_height()}")
    print(f"Is balanced: {tree.is_balanced()}")

    print(f"\nMinimum word: {tree.find_minimum()}")
    print(f"Maximum word: {tree.find_maximum()}")
    print(f"Alphabetically sorted: {list(tree)}")

    print("\nSearching for words:")
    for word in ["cat", "lion", "fox"]:
        result = tree.search(word)
        print(f"  Search('{word}'): {'Found' if result else 'Not found'}")


def test_complete_tree():
    """Test building a complete binary tree."""
    print("\nTEST 14: Complete Binary Tree")

    tree = AVLTree()
    # insert in level order to create complete tree: 15 nodes (height 3)
    keys = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]

    print(f"Inserting {len(keys)} nodes to form complete tree")
    for key in keys:
        tree.insert(key)

    print(f"\nTree size: {len(tree)}")
    print(f"Tree height: {tree.get_height()}")
    print(f"Is balanced: {tree.is_balanced()}")
    print(f"Rotations performed: {tree.get_rotation_count()}")
    print("\nTree structure:")
    tree.print_tree()


def test_deletion_leaf_nodes():
    """Test deletion of only leaf nodes."""
    print("\nTEST 15: Deletion of Leaf Nodes")

    tree = AVLTree()
    keys = [50, 25, 75, 10, 30, 60, 80]

    print(f"Building tree with keys: {keys}")
    for key in keys:
        tree.insert(key)

    print("\nInitial tree:")
    tree.print_tree()

    leaf_nodes = [10, 30, 60, 80]
    print(f"\nDeleting leaf nodes: {leaf_nodes}")
    for key in leaf_nodes:
        tree.delete(key)
        print(f"  After deleting {key}:")
        tree.print_tree()

    print(f"Is balanced: {tree.is_balanced()}")


def test_deletion_internal_nodes():
    """Test deletion of internal nodes with children."""
    print("\nTEST 16: Deletion of Internal Nodes")

    tree = AVLTree()
    keys = [50, 25, 75, 10, 30, 60, 80, 5, 15, 27, 35, 55, 65, 77, 85]

    print(f"Building tree with keys: {keys}")
    for key in keys:
        tree.insert(key)

    print("\nInitial tree:")
    tree.print_tree()

    # delete nodes with 2 children
    internal_nodes = [25, 75]
    print(f"\nDeleting internal nodes with 2 children: {internal_nodes}")
    for key in internal_nodes:
        print(f"\n  Deleting {key}:")
        tree.delete(key)
        tree.print_tree()

    print(f"Is balanced: {tree.is_balanced()}")


def test_stress_random_operations():
    """Stress test with random operations."""
    print("\nTEST 17: Stress Test - Random Operations")

    tree = AVLTree()
    operations = []
    inserted_keys = set()

    print("Performing 200 random insert/delete operations...")

    for i in range(200):
        if random.random() < 0.7 or len(inserted_keys) == 0:  # 70% insert
            key = random.randint(1, 100)
            tree.insert(key)
            inserted_keys.add(key)
            operations.append(f"Insert({key})")
        else:  # 30% delete
            key = random.choice(list(inserted_keys))
            tree.delete(key)
            inserted_keys.remove(key)
            operations.append(f"Delete({key})")

    print(f"\nFinal tree size: {len(tree)}")
    print(f"Final tree height: {tree.get_height()}")
    print(f"Is balanced: {tree.is_balanced()}")
    print(f"Total rotations: {tree.get_rotation_count()}")

    # verify all remaining keys are searchable
    all_found = all(tree.search(key) is not None for key in inserted_keys)
    print(f"All remaining keys searchable: {all_found}")

    # verify in-order traversal is sorted
    traversal = list(tree)
    is_sorted = traversal == sorted(traversal)
    print(f"In-order traversal is sorted: {is_sorted}")


def test_height_balance_verification():
    """Verify height and balance properties."""
    print("\nTEST 18: Height and Balance Verification")

    tree = AVLTree()
    sizes = [10, 50, 100]

    for n in sizes:
        tree = AVLTree()
        keys = list(range(1, n + 1))

        print(f"\nInserting {n} sequential keys...")
        for key in keys:
            tree.insert(key)

        theoretical_min_height = math.ceil(math.log2(n + 1)) - 1
        theoretical_max_height = math.floor(1.44 * math.log2(n + 2))

        actual_height = tree.get_height()

        print(f"  Actual height: {actual_height}")
        print(f"  Theoretical min height: {theoretical_min_height}")
        print(f"  Theoretical max AVL height: {theoretical_max_height}")
        print(f"  Height is optimal: {
              theoretical_min_height <= actual_height <= theoretical_max_height}")
        print(f"  Is balanced: {tree.is_balanced()}")


def test_key_value_pairs():
    """Test storing and retrieving key-value pairs."""
    print("\nTEST 19: Key-Value Pairs")

    tree = AVLTree()

    students = [
        (101, "Alice"),
        (105, "Bob"),
        (103, "Charlie"),
        (108, "Diana"),
        (102, "Eve")
    ]

    print("Inserting student records (ID, Name):")
    for student_id, name in students:
        tree.insert(student_id, name)
        print(f"  ID {student_id}: {name}")

    print("\nTree structure (showing IDs):")
    tree.print_tree()

    print("\nRetrieving student names:")
    for student_id in [101, 103, 108, 999]:
        name = tree.search(student_id)
        if name:
            print(f"  ID {student_id}: {name}")
        else:
            print(f"  ID {student_id}: Not found")

    print("\nUpdating value for existing key:")
    tree.insert(103, "Charlotte")  # update Charlie to Charlotte
    print(f"  ID 103: {tree.search(103)}")


def test_boundary_rotations():
    """Test rotations at tree boundaries (root and leaves)."""
    print("\nTEST 20: Boundary Rotations")

    # root rotation
    print("Testing root rotation (LL case):")
    tree = AVLTree()
    tree.insert(3)
    tree.insert(2)
    tree.insert(1)
    print("  After inserting 3, 2, 1:")
    tree.print_tree()

    # deep rotation
    print("\nTesting deep tree rotation:")
    tree = AVLTree()
    for key in [50, 25, 75, 12, 30, 60, 80, 5, 15]:
        tree.insert(key)

    print("  Before inserting 1 (will cause rotation):")
    tree.print_tree()

    tree.insert(1)
    print("  After inserting 1:")
    tree.print_tree()

    print(f"Is balanced: {tree.is_balanced()}")


def run_all_tests():
    """Run all test cases"""
    test_basic_insertion()
    test_worst_case_bst()
    test_search_operations()
    test_deletion()
    test_all_rotation_cases()
    test_inorder_traversal()
    test_large_dataset()
    test_duplicate_insertion()
    test_sequential_deletion()
    test_alternating_operations()
    test_edge_cases()
    test_negative_numbers()
    test_string_keys()
    test_complete_tree()
    test_deletion_leaf_nodes()
    test_deletion_internal_nodes()
    test_stress_random_operations()
    test_height_balance_verification()
    test_key_value_pairs()
    test_boundary_rotations()

    print("\nALL TESTS COMPLETED!")


if __name__ == "__main__":
    run_all_tests()
