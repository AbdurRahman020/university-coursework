class AVLNode:
    """
    AVL tree node with self-balancing capabilities.
    Maintains height information and supports rotations.
    """

    def __init__(self, key, value=None):
        """
        Initialize an AVL tree node.

        Args:
            key: The key to store in this node
            value: Optional value associated with the key
        """
        self.key = key
        self.value = value if value is not None else key
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0

    def get_height(self):
        """Get the height of this node."""
        return self.height

    def update_height(self):
        """Update the height of this node based on its children."""
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1
        self.height = 1 + max(left_height, right_height)

    def get_balance_factor(self):
        """
        Calculate the balance factor of this node.
        Balance Factor (skew) = height(left) - height(right)

        Returns:
            The balance factor (positive means left-heavy, negative means
                                right-heavy)
        """
        left_height = self.left.height if self.left else -1
        right_height = self.right.height if self.right else -1

        return left_height - right_height


class AVLTree:
    """
    AVL Tree implementation with automatic balancing.
    Provides O(log n) operations for insertion, deletion, and search.
    """

    def __init__(self):
        """Initialize an empty AVL tree."""
        self.root = None
        self.size = 0
        self.rotation_count = 0

    def __len__(self):
        """Return the number of nodes in the tree."""
        return self.size

    def _inorder_traversal(self, node):
        """
        Perform in-order traversal of the tree.

        Args:
            node: The root node of the subtree to traverse
        """
        if node:
            yield from self._inorder_traversal(node.left)
            yield node.key
            yield from self._inorder_traversal(node.right)

    def __iter__(self):
        """Iterator over items in the tree (in-order traversal)."""
        yield from self._inorder_traversal(self.root)

    def insert(self, key, value=None):
        """
        Insert a key-value pair into the AVL tree.

        Args:
            key: The key to insert
            value: Optional value associated with the key

        Returns:
            True if insertion was successful, False if key already exists
        """
        if self.root is None:
            self.root = AVLNode(key, value)
            self.size += 1
            return True

        # perform standard BST insertion
        node = self._insert_recursive(self.root, key, value)

        if node is None:
            # key already exists
            return False

        self.size += 1
        return True

    def _insert_recursive(self, node, key, value):
        """
        Recursively insert a node and rebalance the tree.

        Args:
            node: Current node in the recursion
            key: Key to insert
            value: Value to insert

        Returns:
            The inserted node or None if key already exists
        """
        # standard BST insertion
        if key < node.key:
            if node.left is None:
                node.left = AVLNode(key, value)
                node.left.parent = node
                inserted_node = node.left
            else:
                inserted_node = self._insert_recursive(node.left, key, value)
        elif key > node.key:
            if node.right is None:
                node.right = AVLNode(key, value)
                node.right.parent = node
                inserted_node = node.right
            else:
                inserted_node = self._insert_recursive(node.right, key, value)
        else:
            # key already exists, update value
            node.value = value if value is not None else key
            return None

        # update height and rebalance
        if inserted_node:
            self._rebalance(node)

        return inserted_node

    def delete(self, key):
        """
        Delete a node with the given key from the AVL tree.

        Args:
            key: The key to delete

        Returns:
            The value of the deleted node, or None if key not found
        """
        if self.root is None:
            return None

        deleted_value = self._delete_recursive(self.root, key)

        if deleted_value is not None:
            self.size -= 1

        return deleted_value

    def _delete_recursive(self, node, key):
        """
        Recursively delete a node and rebalance the tree.

        Args:
            node: Current node in the recursion
            key: Key to delete

        Returns:
            The value of the deleted node or None if not found
        """
        if node is None:
            return None

        deleted_value = None

        # search for the node to delete
        if key < node.key:
            deleted_value = self._delete_recursive(node.left, key)
        elif key > node.key:
            deleted_value = self._delete_recursive(node.right, key)
        else:
            # node found, perform deletion
            deleted_value = node.value

            # case 1: node with only one child or no child
            if node.left is None:
                self._transplant(node, node.right)
            elif node.right is None:
                self._transplant(node, node.left)
            else:
                # case 2: node with two children
                # get the inorder successor (minimum in right subtree)
                successor = self._find_minimum(node.right)

                # copy the successor's data to this node
                node.key = successor.key
                node.value = successor.value

                # delete the successor
                self._delete_recursive(node.right, successor.key)

        # rebalance the tree
        if node:
            self._rebalance(node)

        return deleted_value

    def _transplant(self, old_node, new_node):
        """
        Replace old_node with new_node in the tree.

        Args:
            old_node: Node to be replaced
            new_node: Node to replace with
        """
        if old_node.parent is None:
            self.root = new_node
        elif old_node == old_node.parent.left:
            old_node.parent.left = new_node
        else:
            old_node.parent.right = new_node

        if new_node:
            new_node.parent = old_node.parent

    def _find_minimum(self, node):
        """
        Find the node with minimum key in the subtree.

        Args:
            node: Root of the subtree

        Returns:
            The node with minimum key
        """
        while node.left:
            node = node.left

        return node

    def _find_maximum(self, node):
        """
        Find the node with maximum key in the subtree.

        Args:
            node: Root of the subtree

        Returns:
            The node with maximum key
        """
        while node.right:
            node = node.right

        return node

    def search(self, key):
        """
        Search for a key in the AVL tree.

        Args:
            key: The key to search for

        Returns:
            The value associated with the key, or None if not found
        """
        node = self._search_node(self.root, key)

        return node.value if node else None

    def _search_node(self, node, key):
        """
        Recursively search for a node with the given key.

        Args:
            node: Current node in the recursion
            key: Key to search for

        Returns:
            The node if found, None otherwise
        """
        if node is None or node.key == key:
            return node

        if key < node.key:
            return self._search_node(node.left, key)

        return self._search_node(node.right, key)

    def find_minimum(self):
        """Find and return the minimum key in the tree."""
        if self.root is None:
            return None

        return self._find_minimum(self.root).key

    def find_maximum(self):
        """Find and return the maximum key in the tree."""
        if self.root is None:
            return None
        return self._find_maximum(self.root).key

    def get_height(self):
        """Get the height of the tree."""
        return self.root.height if self.root else -1

    def get_rotation_count(self):
        """Get the total number of rotations performed."""
        return self.rotation_count

    def reset_rotation_count(self):
        """Reset the rotation counter to zero."""
        self.rotation_count = 0

    def _rotate_left(self, node):
        """
        Perform a left rotation on the given node.

        Before:     x          After:      y
                   / \                    / \
                  A   y                  x   C
                     / \                / \
                    B   C              A   B

        Args:
            node: The node to rotate (x in the diagram)
        """
        y = node.right
        B = y.left

        # perform rotation
        y.left = node
        node.right = B

        # update parents
        y.parent = node.parent
        node.parent = y
        if B:
            B.parent = node

        # update the parent's child pointer
        if y.parent is None:
            self.root = y
        elif node == y.parent.left:
            y.parent.left = y
        else:
            y.parent.right = y

        # update heights
        node.update_height()
        y.update_height()

        self.rotation_count += 1

    def _rotate_right(self, node):
        """
        Perform a right rotation on the given node.

        Before:     y          After:      x
                   / \                    / \
                  x   C                  A   y
                 / \                        / \
                A   B                      B   C

        Args:
            node: The node to rotate (y in the diagram)
        """
        x = node.left
        B = x.right

        # perform rotation
        x.right = node
        node.left = B

        # update parents
        x.parent = node.parent
        node.parent = x
        if B:
            B.parent = node

        # update the parent's child pointer
        if x.parent is None:
            self.root = x
        elif node == x.parent.left:
            x.parent.left = x
        else:
            x.parent.right = x

        # update heights
        node.update_height()
        x.update_height()

        self.rotation_count += 1

    def _rebalance(self, node):
        """
        Rebalance the tree starting from the given node.
        Performs appropriate rotations based on balance factor.

        Args:
            node: The node to rebalance
        """
        node.update_height()
        balance_factor = node.get_balance_factor()

        # left-left Case (LL)
        if balance_factor > 1 and node.left.get_balance_factor() >= 0:
            self._rotate_right(node)

        # left-right Case (LR)
        elif balance_factor > 1 and node.left.get_balance_factor() < 0:
            self._rotate_left(node.left)
            self._rotate_right(node)

        # right-right Case (RR)
        elif balance_factor < -1 and node.right.get_balance_factor() <= 0:
            self._rotate_left(node)

        # right-left Case (RL)
        elif balance_factor < -1 and node.right.get_balance_factor() > 0:
            self._rotate_right(node.right)
            self._rotate_left(node)

    def is_balanced(self):
        """
        Check if the tree is balanced (AVL property holds).

        Returns:
            True if balanced, False otherwise
        """
        return self._check_balance(self.root)

    def _check_balance(self, node):
        """
        Recursively check if subtree is balanced.

        Args:
            node: Root of the subtree to check

        Returns:
            True if balanced, False otherwise
        """
        if node is None:
            return True

        balance_factor = node.get_balance_factor()

        if abs(balance_factor) > 1:
            return False

        return self._check_balance(node.left) and self._check_balance(
            node.right)

    def _display_aux(self, node):
        """
        Returns list of strings, width, height, and horizontal coordinate
        of the root for visual tree display.

        Args:
            node: The node to display

        Returns:
            Tuple of (lines, width, height, middle)
        """
        # no child
        if node.right is None and node.left is None:
            line = str(node.key)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # only left child
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = str(node.key)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # only right child
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = str(node.key)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # two children
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = str(node.key)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '

        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)

        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def print_tree(self):
        """Display the AVL tree in a visual format."""
        if self.root is None:
            print("Empty tree")
            return

        lines, *_ = self._display_aux(self.root)
        for line in lines:
            print(line)
        print()
