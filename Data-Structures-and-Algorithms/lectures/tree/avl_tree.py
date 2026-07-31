"""
AVL Tree — Self-Balancing Binary Search Tree

This code is based on the lecture materials from:
    MIT OpenCourseWare — 6.006 Introduction to Algorithms (Spring 2020)
    https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/

The original implementation was taken from the course and updated with
additional structure, comments, and test cases.
"""

from binary_tree import BinaryTree


def height(node):
    """
    Get the height of a node.

    Args:
        node: The node to get height from

    Returns:
        Height of the node, or -1 if node is None
    """
    if node:
        return node.height
    return -1


class Binary_Node:
    """
    AVL tree node with self-balancing capabilities.
    Maintains height information and supports rotations.
    """

    def __init__(self, x):  # O(1)
        """
        Initialize an AVL tree node.

        Args:
            x: The value to store in this node
        """
        self.item = x
        self.left = None
        self.right = None
        self.parent = None
        self.subtree_update()

    def subtree_update(self):  # O(1)
        """
        Update the height of this node based on its children.
        Height is defined as 1 + max(left_height, right_height).
        """
        self.height = 1 + max(height(self.left), height(self.right))

    def skew(self):  # O(1)
        """
        Calculate the balance factor (skew) of this node.
        Skew = right_height - left_height

        Returns:
            The skew value (positive means right-heavy, negative means left-heavy)
        """
        return height(self.right) - height(self.left)

    def subtree_iter(self):  # O(n)
        """
        In-order traversal iterator of the subtree rooted at this node.

        Yields:
            Nodes in sorted order (left subtree, root, right subtree)
        """
        if self.left:
            yield from self.left.subtree_iter()

        yield self

        if self.right:
            yield from self.right.subtree_iter()

    def subtree_first(self):  # O(log n)
        """
        Find the leftmost (minimum) node in the subtree rooted at this node.

        Returns:
            The leftmost node
        """
        if self.left:
            return self.left.subtree_first()
        return self

    def subtree_last(self):  # O(log n)
        """
        Find the rightmost (maximum) node in the subtree rooted at this node.

        Returns:
            The rightmost node
        """
        if self.right:
            return self.right.subtree_last()

        return self

    def successor(self):  # O(log n)
        """
        Find the in-order successor of this node (next larger node).

        Returns:
            The successor node, or None if this is the maximum node
        """
        if self.right:
            return self.right.subtree_first()

        while self.parent and (self is self.parent.right):
            self = self.parent

        return self.parent

    def predecessor(self):  # O(log n)
        """
        Find the in-order predecessor of this node (next smaller node).

        Returns:
            The predecessor node, or None if this is the minimum node
        """
        if self.left:
            return self.left.subtree_last()

        while self.parent and (self is self.parent.left):
            self = self.parent

        return self.parent

    def subtree_insert_before(self, new_node):  # O(log n)
        """
        Insert new_node immediately before this node in in-order traversal.
        Then rebalance the tree from the insertion point upward.

        Args:
            new_node: The node to insert
        """
        if self.left:
            self = self.left.subtree_last()
            self.right, new_node.parent = new_node, self
        else:
            self.left, new_node.parent = new_node, self

        self.maintain()

    def subtree_insert_after(self, new_node):  # O(log n)
        """
        Insert new_node immediately after this node in in-order traversal.
        Then rebalance the tree from the insertion point upward.

        Args:
            new_node: The node to insert
        """
        if self.right:
            self = self.right.subtree_first()
            self.left, new_node.parent = new_node, self
        else:
            self.right, new_node.parent = new_node, self

        self.maintain()

    def subtree_delete(self):  # O(log n)
        """
        Delete this node from the tree while maintaining AVL properties.
        If the node has children, swap with predecessor/successor first,
        then delete the swapped node and rebalance.

        Returns:
            The actually deleted node (which may be different from self after swapping)
        """
        if self.left or self.right:
            if self.left:
                other_node = self.predecessor()
            else:
                other_node = self.successor()
            self.item, other_node.item = other_node.item, self.item
            return other_node.subtree_delete()

        if self.parent:
            if self.parent.left is self:
                self.parent.left = None
            else:
                self.parent.right = None
            self.parent.maintain()

        return self

    def subtree_rotate_right(self):  # O(1)
        """
        Perform a right rotation on this node.
        This operation is used to rebalance left-heavy trees.

        Before:     D          After:      B
                   / \                    / \
                  B   E                  A   D
                 / \                        / \
                A   C                      C   E
        """
        assert self.left
        D = self

        B, E = D.left, D.right
        A, C = B.left, B.right
        D, B = B, D
        D.item, B.item = B.item, D.item
        B.left, B.right = A, D
        D.left, D.right = C, E

        if A:
            A.parent = B
        if E:
            E.parent = D

        B.subtree_update()
        D.subtree_update()

    def subtree_rotate_left(self):  # O(1)
        """
        Perform a left rotation on this node.
        This operation is used to rebalance right-heavy trees.

        Before:     B          After:      D
                   / \                    / \
                  A   D                  B   E
                     / \                / \
                    C   E              A   C
        """
        assert self.right
        B = self

        A, D = B.left, B.right
        C, E = D.left, D.right
        B, D = D, B
        B.item, D.item = D.item, B.item
        D.left, D.right = B, E
        B.left, B.right = A, C

        if A:
            A.parent = B
        if E:
            E.parent = D

        B.subtree_update()
        D.subtree_update()

    def rebalance(self):  # O(1)
        """
        Rebalance this node if it violates AVL property (|skew| > 1).
        Performs appropriate rotations based on the skew pattern.
        """
        if self.skew() == 2:
            if self.right.skew() < 0:
                self.right.subtree_rotate_right()
            self.subtree_rotate_left()
        elif self.skew() == -2:
            if self.left.skew() > 0:
                self.left.subtree_rotate_left()
            self.subtree_rotate_right()

    def maintain(self):  # O(log n)
        """
        Maintain AVL property by rebalancing and updating height,
        then recursively maintain parent nodes up to the root.
        """
        self.rebalance()
        self.subtree_update()

        if self.parent:
            self.parent.maintain()


class Size_Node(Binary_Node):
    """
    AVL tree node that also maintains subtree size information.
    Extends Binary_Node with size tracking for efficient indexing.
    """

    def subtree_update(self):  # O(1)
        """
        Update both height and size of this node based on its children.
        Size is defined as 1 + left_size + right_size.
        """
        super().subtree_update()

        self.size = 1

        if self.left:
            self.size += self.left.size

        if self.right:
            self.size += self.right.size

    def subtree_at(self, i):  # O(h)
        """
        Find the node at index i in the in-order traversal of this subtree.

        Args:
            i: The index to find (0-indexed)

        Returns:
            The node at index i
        """
        assert 0 <= i
        if self.left:
            L_size = self.left.size
        else:
            L_size = 0

        if i < L_size:
            return self.left.subtree_at(i)
        elif i > L_size:
            return self.right.subtree_at(i - L_size - 1)
        else:
            return self


class Seq_Binary_Tree(BinaryTree):
    """
    Sequence data structure implemented as an AVL tree.
    Supports O(log n) operations for insertion, deletion, and indexing.
    """

    def __init__(self):
        """Initialize an empty sequence AVL tree."""
        super().__init__(Size_Node)

    def build(self, X):
        """
        Build a balanced AVL tree from a sequence of items.

        Args:
            X: Iterable of items to insert into the tree

        Time complexity: O(n)
        """
        def build_subtree(X, i, j):
            """
            Recursively build a balanced subtree from array slice X[i:j+1].

            Args:
                X: Array of items
                i: Start index (inclusive)
                j: End index (inclusive)

            Returns:
                Root node of the constructed subtree
            """
            c = (i + j) // 2
            root = self.Node_Type(X[c])

            if i < c:
                root.left = build_subtree(X, i, c - 1)
                root.left.parent = root

            if c < j:
                root.right = build_subtree(X, c + 1, j)
                root.right.parent = root
            root.subtree_update()
            return root

        self.root = build_subtree(X, 0, len(X) - 1)
        self.size = self.root.size

    def get_at(self, i):
        """
        Get the item at index i.

        Args:
            i: The index to access

        Returns:
            The item at index i

        Time complexity: O(log n)
        """
        assert self.root
        return self.root.subtree_at(i).item

    def set_at(self, i, x):
        """
        Set the item at index i to x.

        Args:
            i: The index to modify
            x: The new value

        Time complexity: O(log n)
        """
        assert self.root
        self.root.subtree_at(i).item = x

    def insert_at(self, i, x):
        """
        Insert item x at index i.

        Args:
            i: The index to insert at
            x: The item to insert

        Time complexity: O(log n)
        """
        new_node = self.Node_Type(x)

        if i == 0:
            if self.root:
                node = self.root.subtree_first()
                node.subtree_insert_before(new_node)
            else:
                self.root = new_node
        else:
            node = self.root.subtree_at(i - 1)
            node.subtree_insert_after(new_node)

        self.size += 1

    def delete_at(self, i):
        """
        Delete and return the item at index i.

        Args:
            i: The index to delete

        Returns:
            The deleted item

        Time complexity: O(log n)
        """
        assert self.root
        node = self.root.subtree_at(i)
        ext = node.subtree_delete()

        if ext.parent is None:
            self.root = None
        self.size -= 1

        return ext.item

    def insert_first(self, x):
        """Insert item x at the beginning of the sequence."""
        self.insert_at(0, x)

    def delete_first(self):
        """Delete and return the first item in the sequence."""
        return self.delete_at(0)

    def insert_last(self, x):
        """Insert item x at the end of the sequence."""
        self.insert_at(len(self), x)

    def delete_last(self):
        """Delete and return the last item in the sequence."""
        return self.delete_at(len(self) - 1)
