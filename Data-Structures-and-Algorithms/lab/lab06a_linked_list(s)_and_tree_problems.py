from typing import Optional, List

# %% Nodes definitions


class SNode:
    """Node for singly linked list."""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return f"SNode({self.data})"


class DNode:
    """Node for doubly linked list."""

    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev = prev_node
        self.next = next_node

    def __str__(self):
        return f"DNode({self.data})"


# %%

def count_occurrences(head: 'SNode', target: int) -> int:
    """
    Count how many times target appears in the list.

    Args:
        head: Head of singly linked list
        target: Value to count
    Returns:
        int: Number of occurrences
    """
    count = 0

    curr_node = head

    while curr_node:
        if curr_node.data == target:
            count += 1
        curr_node = curr_node.next

    return count


def test_count():
    """Test for count_occurrence function"""
    head = SNode(1, SNode(2, SNode(2, SNode(3, SNode(2)))))

    assert count_occurrences(head, 2) == 3
    assert count_occurrences(head, 1) == 1
    assert count_occurrences(head, 5) == 0
    assert count_occurrences(None, 1) == 0
    print("count_occurrences() tests passed!")


if __name__ == "__main__":
    test_count()

# %%


def reverse_list(head: 'SNode') -> 'SNode':
    """
    Reverse a singly linked list iteratively.

    Args:
        head: Head of singly linked list
    Returns:
        New head of reversed list
    """
    if head is None:
        return None

    # initialize a pointer to hold the reversed part of the list
    rev_head = None

    # traverse the list until all nodes are processed
    while head:
        # temporarily store the current head node
        curr_node = head

        # move the head pointer to the next node before changing links
        head = head.next

        # reverse the link: point current node to the already reversed part
        curr_node.next = rev_head

        # update the reversed list's head to the current node
        rev_head = curr_node

    # return the new head of the reversed list
    return rev_head


def test_reverse():
    """Test for reverse_list function"""
    head = SNode(1, SNode(2, SNode(3)))

    reverse_head = reverse_list(head)

    assert reverse_head.data == 3
    assert reverse_head.next.data == 2
    assert reverse_head.next.next.data == 1
    assert reverse_head.next.next.next is None

    assert reverse_list(None) is None

    single = SNode(5)
    assert reverse_list(single).data == 5

    print("reverse_list() test passed!")


if __name__ == "__main__":
    test_reverse()

# %%


def reverse_dll(head: 'DNode') -> 'DNode':
    """
    Reverse a doubly linked list

    Args:
        head: Head of doubly linked list
    Returns:
        New head of reversed list
    """
    if head is None:
        return None

    # start traversal from the head node
    curr_node = head

    # this will hold the new head of the reversed list
    rev_head = None

    # traverse through the entire list
    while curr_node:
        # swap the prev and next pointers for the current node
        curr_node.prev, curr_node.next = curr_node.next, curr_node.prev

        # update rev_head to the current node (it will become the new head at
        # the end)
        rev_head = curr_node

        # move to the next node in the original sequence (which is now
        # curr_node.prev after swapping)
        curr_node = curr_node.prev

    # return the new head of the reversed list
    return rev_head


def test_reverse_dll():
    """Test for reverse_dll function"""
    node1 = DNode(1)
    node2 = DNode(2)
    node3 = DNode(3)

    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2

    reversed_head = reverse_dll(node1)

    assert reversed_head.data == 3
    assert reversed_head.next.data == 2
    assert reversed_head.next.next.data == 1
    assert reversed_head.next.next.next is None

    assert reversed_head.prev is None
    assert reversed_head.next.prev.data == 3
    assert reversed_head.next.next.prev.data == 2

    print("rreverse_dll() tests passed!")


if __name__ == "__main__":
    test_reverse_dll()

# %%


def remove_duplicates_dll(head: 'DNode') -> 'DNode':
    """
    Remove duplicates from sorted doubly linked list.

    Args:
        head: Head of sorted doubly linked list
    Returns:
        Head of list with duplicates removed
    """
    if head is None:
        return None

    # start traversal from the head node
    curr_node = head

    # traverse the list until the end
    while curr_node and curr_node.next:
        # if current node has the same data as the next node, it's a duplicate
        if curr_node.data == curr_node.next.data:
            # store the duplicate node temporarily
            dup_node = curr_node.next

            # skip the duplicate node by linking current node to the node after
            # the duplicate
            curr_node.next = dup_node.next

            # if there is a node after duplicate, fix its prev pointer
            if dup_node.next:
                dup_node.next.prev = curr_node

            # explicitly delete the duplicate node to free memory
            del dup_node
        else:
            # move to the next node if no duplicate found
            curr_node = curr_node.next

    # return the head of the modified list
    return head


def test_remove_duplicate_dll():
    """Test for remove_duplicates_dll function"""
    node1 = DNode(1)
    node2a = DNode(2)
    node2b = DNode(2)
    node3a = DNode(3)
    node3b = DNode(3)
    node3c = DNode(3)

    node1.next = node2a
    node2a.prev = node1
    node2a.next = node2b
    node2b.prev = node2a
    node2b.next = node3a
    node3a.prev = node2b
    node3a.next = node3b
    node3b.prev = node3a
    node3b.next = node3c
    node3c.prev = node3b

    result = remove_duplicates_dll(node1)

    assert result.data == 1
    assert result.next.data == 2
    assert result.next.next.data == 3
    assert result.next.next.next is None

    assert result.next.prev.data == 1
    assert result.next.next.prev.data == 2

    print("remove_duplicates_dll() tests passed!")


if __name__ == "__main__":
    test_remove_duplicate_dll()

# %% Merging of sorted linked list


def merge_sorted_lists(first_list: 'SNode', second_list: 'SNode') -> 'SNode':
    """
    Merge two sorted singly linked lists

    Args:
        first_list: Head of first sorted list
        second_list: Head of second sorted list
    Returns:
        Head of merged sorted list
    """
    # if the first list is empty, return the second list
    if not first_list:
        return second_list

    # if the second list is empty, return the first list
    if not second_list:
        return first_list

    # determine the head of the merged list (the smaller of the two starting
    # nodes)
    if first_list.data <= second_list.data:
        head = first_list
        first_list = first_list.next
    else:
        head = second_list
        second_list = second_list.next

    # current pointer for building the merged list
    curr_node = head

    # traverse both lists and attach the smaller node each time
    while first_list and second_list:
        if first_list.data <= second_list.data:
            # Attach node from list 1
            curr_node.next = first_list
            first_list = first_list.next
        else:
            # Attach node from list 2
            curr_node.next = second_list
            second_list = second_list.next

        # Move the current pointer forward
        curr_node = curr_node.next

    # if any nodes remain in list 1, attach them
    if first_list:
        curr_node.next = first_list

    # if any nodes remain in list 2, attach them
    if second_list:
        curr_node.next = second_list

    # return the head of the merged sorted list
    return head


def test_merge_sorted():
    """Test for merge_sorted_lists function"""
    first_list = SNode(1, SNode(3, SNode(5)))
    second_list = SNode(2, SNode(4, SNode(6)))

    merged = merge_sorted_lists(first_list, second_list)

    curr = merged
    expected = [1, 2, 3, 4, 5, 6]

    for val in expected:
        assert curr.data == val
        curr = curr.next
    assert curr is None

    assert merge_sorted_lists(None, None) is None
    assert merge_sorted_lists(SNode(1), None).data == 1
    assert merge_sorted_lists(None, SNode(1)).data == 1

    print("merge_sorted_lists() tests passed!")


if __name__ == "__main__":
    test_merge_sorted()

# %% Binary Seach Tree


class TreeNode:
    """
    A node in a binary tree.

    Attributes:
        data: The integer value stored in the node.
        left_node: Reference to the left child node (default: None).
        right_node: Reference to the right child node (default: None).
    """

    def __init__(self, data: int,
                 left_node: Optional['TreeNode'] = None,
                 right_node: Optional['TreeNode'] = None) -> None:
        self.data = data
        self.left = left_node
        self.right = right_node

    def __str__(self):
        return f"TreeNode({self.data})"


class SimpleBST:
    """
    A simple Binary Search Tree (BST) implementation.

    Attributes:
        root: Reference to the root node of the BST (default: None).
    """

    def __init__(self):
        self.root: Optional['TreeNode'] = None

    def insert(self, data: int) -> None:
        """Insert a value into the BST"""
        # handle the empty tree
        if self.root is None:
            self.root = TreeNode(data)
        else:
            curr_node = self.root
            while True:
                # go left if data is smaller
                if data < curr_node.data:
                    if curr_node.left is None:
                        curr_node.left = TreeNode(data)
                        return
                    curr_node = curr_node.left
                # go right if data is greater or equal (duplicates go right)
                else:
                    if curr_node.right is None:
                        curr_node.right = TreeNode(data)
                        return
                    curr_node = curr_node.right

    def search(self, data: int) -> bool:
        """Search for a value in the BST"""
        curr_node: 'TreeNode' = self.root
        while curr_node is not None:
            if data == curr_node.data:
                return True
            # go left if data is smaller
            if data < curr_node.data:
                curr_node = curr_node.left
                # go right if data is greater
            else:
                curr_node = curr_node.right
        return False

    def inorder_traversal(self, node: Optional['TreeNode'] = None,
                          result: List = None) -> List:
        """Return list of values in sorted order (left-root-right)"""
        # initialize on first call
        if result is None:
            result = []
            node = self.root

        if node is not None:
            # traverse left subtree
            self.inorder_traversal(node.left, result)
            # visit current node
            result.append(node.data)
            # traverse right subtree
            self.inorder_traversal(node.right, result)

        return result

    def find_min(self):
        """Find minimum value in the BST"""
        if self.root is None:
            return None

        # keep going left to find smallest value
        curr_node = self.root

        while curr_node.left is not None:
            curr_node = curr_node.left

        return curr_node.data

    def find_max(self):
        """Find maximum value in the BST"""
        if self.root is None:
            return None

        # keep going right to find largest value
        curr_node = self.root

        while curr_node.right is not None:
            curr_node = curr_node.right

        return curr_node.data

    def height(self):
        """Calculate height of the tree"""
        if self.root is None:
            return 0

        # use level-order traversal (BFS) to count levels
        queue = [self.root]
        height = 0

        while len(queue) > 0:
            level_size = len(queue)
            height += 1

            # process all nodes at current level
            for _ in range(level_size):
                node = queue.pop(0)

                # add children to queue for next level
                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

        return height


def test_simple_bst():
    """Test for search and inoder traversal in BST"""
    bst = SimpleBST()
    # insert values
    values = [5, 3, 7, 2, 4, 6, 8]
    for val in values:
        bst.insert(val)

    # test search
    assert bst.search(5) is True
    assert bst.search(3) is True
    assert bst.search(7) is True
    assert bst.search(2) is True
    assert bst.search(10) is False
    assert bst.search(1) is False

    # test inorder traversal (should be sorted)
    inorder = bst.inorder_traversal()
    assert inorder == [2, 3, 4, 5, 6, 7, 8]

    # test empty tree
    empty_bst = SimpleBST()
    assert empty_bst.search(5) is False
    assert empty_bst.inorder_traversal() == []

    # test duplicate insertion (optional behavior)
    bst.insert(5)  # duplicate
    inorder_with_duplicate = bst.inorder_traversal()
    # depending on implementation, duplicates might be allowed on right or left
    assert inorder_with_duplicate == [2, 3, 4, 5, 5, 6, 7, 8]

    print("BST tests passed!")


def test_bst_structure():
    """Test the actual BST structure"""
    bst = SimpleBST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)

    # verify tree structure
    assert bst.root.data == 5
    assert bst.root.left.data == 3
    assert bst.root.right.data == 7

    bst.insert(2)
    bst.insert(4)

    assert bst.root.left.left.data == 2
    assert bst.root.left.right.data == 4

    print("BST structure tests passed!")


def test_min_max():
    """Test the min and max methods of BST"""
    bst = SimpleBST()

    # test empty tree
    assert bst.find_min() is None
    assert bst.find_max() is None

    # insert values
    values = [5, 3, 7, 2, 4, 6, 8]
    for val in values:
        bst.insert(val)

    assert bst.find_min() == 2
    assert bst.find_max() == 8

    # test with different values
    bst2 = SimpleBST()
    bst2.insert(10)
    bst2.insert(15)
    bst2.insert(5)

    assert bst2.find_min() == 5
    assert bst2.find_max() == 15

    print("min()/max() tests passed!")


def test_height():
    """Test for height method of BST"""
    bst = SimpleBST()

    # test empty tree
    assert bst.height() == 0

    # test single node
    bst.insert(5)
    assert bst.height() == 1

    # test balanced tree
    bst.insert(3)
    bst.insert(7)
    assert bst.height() == 2

    # test unbalanced tree
    bst2 = SimpleBST()
    bst2.insert(1)
    bst2.insert(2)
    bst2.insert(3)
    bst2.insert(4)
    assert bst2.height() == 4

    print("height() tests passed!")


if __name__ == "__main__":
    test_simple_bst()
    test_bst_structure()
    test_min_max()
    test_height()

    print("\nAll tests passed successfully!")
