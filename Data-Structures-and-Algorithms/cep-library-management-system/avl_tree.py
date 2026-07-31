"""
AVL Tree Implementation
Based on standard AVL algorithms (MIT 6.006, CLRS textbook)
Adapted for UET Library Management System
"""


class AVLNode:
    """AVL tree node for storing book information.

    Attributes:
        isbn (str): Unique ISBN identifier used as the key for indexing.
        book_data (dict): Metadata associated with the book (title, author, etc.).
        left (AVLNode): Pointer to the left child node.
        right (AVLNode): Pointer to the right child node.
        height (int): Height of the node in the tree, used for balancing.
    """

    def __init__(self, isbn, book_data):
        # ISBN acts as the node key for BST ordering
        self.isbn = isbn
        # stores book-related information payload
        self.book_data = book_data
        # left subtree reference
        self.left = None
        # right subtree reference
        self.right = None
        # initial height (leaf node starts at 0)
        self.height = 0

    def update_height(self):
        """Recomputes and updates the node height using child node heights.

        The height is calculated as:
            1 + max(height of left subtree, height of right subtree)
        If a child does not exist, its height is considered -1.
        """
        # height of left child subtree; -1 if absent
        left_height = self.left.height if self.left else -1
        # height of right child subtree; -1 if absent
        right_height = self.right.height if self.right else -1
        # update node height based on taller subtree
        self.height = 1 + max(left_height, right_height)

    def get_balance_factor(self):
        """Computes and returns the node's balance factor.

        Balance Factor Formula:
            height(left subtree) - height(right subtree)

        Returns:
            int: The balance factor indicating tree skew.
                 >1  → Left heavy
                 <-1 → Right heavy
                 0,1,-1 → Balanced
        """
        # height of left subtree; -1 if absent
        left_height = self.left.height if self.left else -1
        # height of right subtree; -1 if absent
        right_height = self.right.height if self.right else -1

        # return balance factor to determine rotation needs
        return left_height - right_height


class AVLTree:
    """Self-balancing AVL Tree for book catalog indexed by ISBN.

    This tree maintains:
        - O(log n) insertion
        - O(log n) search
        - O(log n) deletion
    by performing rotations when imbalance is detected.

    Attributes:
        root (AVLNode): The root node of the AVL tree.
        size (int): Tracks the total number of books stored.
    """

    def __init__(self):
        # root of the AVL tree
        self.root = None
        # number of nodes/books in the tree
        self.size = 0

    def __len__(self):
        """Returns the number of books stored in the catalog.

        Returns:
            int: Size of the AVL tree.
        """
        return self.size

    def insert(self, isbn, book_data):
        """Adds a new book record into the AVL tree catalog.

        Args:
            isbn (str): ISBN key for indexing.
            book_data (dict): Book metadata payload.

        Returns:
            bool: True if insertion succeeds, False if ISBN already exists.
        """
        if self.root is None:
            # if tree is empty, insert first node as root
            self.root = AVLNode(isbn, book_data)
            # increment size counter
            self.size += 1
            return True

        # perform recursive BST insert + rebalancing
        node = self._insert_recursive(self.root, isbn, book_data)

        if node is None:
            # duplicate ISBN detected, insertion failed
            return False

        # successfully inserted, increment tree size
        self.size += 1
        return True

    def _insert_recursive(self, node, isbn, book_data):
        """Performs recursive insertion into BST and triggers rebalancing.

        Args:
            node (AVLNode): Current subtree root during recursion.
            isbn (str): ISBN key to insert.
            book_data (dict): Associated book payload.

        Returns:
            AVLNode: Inserted node reference or None if duplicate ISBN exists.
        """
        if isbn < node.isbn:
            # insert into left subtree if key is smaller
            if node.left is None:
                # create new left child if vacant
                node.left = AVLNode(isbn, book_data)
                inserted_node = node.left
            else:
                # continue recursive descent into left subtree
                inserted_node = self._insert_recursive(
                    node.left, isbn, book_data)

        elif isbn > node.isbn:
            # insert into right subtree if key is larger
            if node.right is None:
                # create new right child if vacant
                node.right = AVLNode(isbn, book_data)
                inserted_node = node.right
            else:
                # continue recursive descent into right subtree
                inserted_node = self._insert_recursive(
                    node.right, isbn, book_data)

        else:
            # ISBN already exists in tree → reject insertion
            return None

        if inserted_node:
            # rebalance current ancestor node if needed
            self._rebalance(node)

        # return reference to inserted node
        return inserted_node

    def search(self, isbn):
        """Retrieves book metadata by ISBN key lookup.

        Args:
            isbn (str): ISBN key to search.

        Returns:
            dict or None: Book data if found, else None.
        """
        # perform recursive search for matching ISBN node
        node = self._search_node(self.root, isbn)

        # return payload if node exists
        return node.book_data if node else None

    def _search_node(self, node, isbn):
        """Performs recursive BST search.

        Args:
            node (AVLNode): Current subtree node.
            isbn (str): ISBN lookup key.

        Returns:
            AVLNode or None: Node reference if found, else None.
        """
        if node is None or node.isbn == isbn:
            # return node if null or key match is found
            return node

        if isbn < node.isbn:
            # search left subtree if key is smaller
            return self._search_node(node.left, isbn)

        # otherwise search right subtree
        return self._search_node(node.right, isbn)

    def delete(self, isbn):
        """Removes a book entry from the catalog using ISBN key.

        Args:
            isbn (str): ISBN key of the book to remove.

        Returns:
            dict or None: Deleted book payload if successful, else None.
        """
        if self.root is None:
            # if tree is empty, nothing to delete
            return None

        # perform recursive deletion + rebalancing
        deleted_data = self._delete_recursive(self.root, isbn)

        if deleted_data is not None:
            # if deletion succeeded, decrement tree size
            self.size -= 1

        # return removed book payload
        return deleted_data

    def _delete_recursive(self, node, isbn):
        """Recursively deletes a node and restores AVL balance.

        Args:
            node (AVLNode): Current subtree node.
            isbn (str): ISBN key to delete.

        Returns:
            dict or None: Deleted book payload or None if not found.
        """
        if node is None:
            # key not found in tree
            return None

        deleted_data = None

        if isbn < node.isbn:
            # traverse into left subtree if key is smaller
            deleted_data = self._delete_recursive(node.left, isbn)
        elif isbn > node.isbn:
            # traverse into right subtree if key is larger
            deleted_data = self._delete_recursive(node.right, isbn)
        else:
            # node with matching ISBN found → delete this node
            deleted_data = node.book_data

            if node.left is None:
                # if left child is absent, transplant right subtree
                self._transplant(node, node.right)
            elif node.right is None:
                # if right child is absent, transplant left subtree
                self._transplant(node, node.left)
            else:
                # node has two children → replace with inorder successor (minimum of right subtree)
                successor = self._find_minimum(node.right)
                node.isbn = successor.isbn
                node.book_data = successor.book_data
                # delete successor node recursively from right subtree
                self._delete_recursive(node.right, successor.isbn)

        if node:
            # rebalance after deletion if subtree still exists
            self._rebalance(node)

        # return deleted book payload
        return deleted_data

    def _transplant(self, old_node, new_node):
        """Replaces an existing node reference with a new subtree reference.

        Args:
            old_node (AVLNode): Node to replace.
            new_node (AVLNode or None): New subtree root to attach.
        """
        if old_node == self.root:
            # if deleting root, update root reference
            self.root = new_node
        else:
            # find parent and replace appropriate child pointer
            parent = self._get_parent(old_node)
            if parent.left == old_node:
                parent.left = new_node
            else:
                parent.right = new_node

    def _get_parent(self, node):
        """Retrieves parent node reference of the given node.

        Args:
            node (AVLNode): Target node.

        Returns:
            AVLNode or None: Parent node reference or None if root or not found.
        """
        return self._find_parent(self.root, node)

    def _find_parent(self, current, target):
        """Recursively finds parent of the target node.

        Args:
            current (AVLNode): Current subtree root.
            target (AVLNode): Node whose parent is being searched.

        Returns:
            AVLNode or None: Parent node reference or None if not found.
        """
        if current is None or current == target:
            # root node or null subtree has no parent
            return None

        if current.left == target or current.right == target:
            # direct parent found
            return current

        if target.isbn < current.isbn:
            # search left subtree
            return self._find_parent(current.left, target)

        # search right subtree otherwise
        return self._find_parent(current.right, target)

    def _find_minimum(self, node):
        """Finds the node with the smallest ISBN key in a subtree.

        Args:
            node (AVLNode): Subtree root.

        Returns:
            AVLNode: The minimum key node.
        """
        while node.left:
            # keep moving left until smallest key is found
            node = node.left

        # return node with minimum ISBN
        return node

    def inorder_traversal(self):
        """Returns all book records in ascending sorted order by ISBN.

        This is useful for displaying the full catalog in indexed order.

        Returns:
            list: A list of tuples (isbn, book_data) in sorted order.
        """
        result = []
        # perform recursive inorder traversal
        self._inorder_helper(self.root, result)

        # return final sorted result
        return result

    def _inorder_helper(self, node, result):
        """Recursive helper to perform inorder traversal.

        Args:
            node (AVLNode): Current subtree root.
            result (list): Accumulator list for storing sorted records.
        """
        if node:
            # visit left subtree
            self._inorder_helper(node.left, result)
            # append current node data (sorted position)
            result.append((node.isbn, node.book_data))
            # visit right subtree
            self._inorder_helper(node.right, result)

    def _rotate_left(self, node):
        """Executes a left rotation around the given node.

        Rotation Case:
            Right-heavy imbalance (balance factor < -1)

        Args:
            node (AVLNode): The node to rotate.
        """
        # New subtree root after rotation
        y = node.right
        # Temporarily hold left subtree of y
        B = y.left
        # Perform rotation
        y.left = node
        node.right = B
        # Update heights after pointer changes
        node.update_height()
        y.update_height()

        if node == self.root:
            # Update root if rotation is at top
            self.root = y
        else:
            # Fix parent-child relationship post rotation
            parent = self._get_parent(node)
            if parent.left == node:
                parent.left = y
            else:
                parent.right = y

    def _rotate_right(self, node):
        """Executes a right rotation around the given node.

        Rotation Case:
            Left-heavy imbalance (balance factor > 1)

        Args:
            node (AVLNode): The node to rotate.
        """
        # New subtree root after rotation
        x = node.left
        # Temporarily hold right subtree of x
        B = x.right
        # Perform rotation
        x.right = node
        node.left = B
        # Update heights after pointer changes
        node.update_height()
        x.update_height()

        if node == self.root:
            # Update root if rotation is at top
            self.root = x
        else:
            # Fix parent-child relationship post rotation
            parent = self._get_parent(node)
            if parent.left == node:
                parent.left = x
            else:
                parent.right = x

    def _rebalance(self, node):
        """Checks imbalance and applies necessary rotations to restore AVL property.

        Args:
            node (AVLNode): Node to rebalance.
        """
        # Refresh height before checking balance
        node.update_height()
        # Compute balance factor to detect skew
        balance_factor = node.get_balance_factor()

        # Left-Left Case → Single Right Rotation
        if balance_factor > 1 and node.left.get_balance_factor() >= 0:
            self._rotate_right(node)

        # Left-Right Case → Left Rotation on child, then Right Rotation
        elif balance_factor > 1 and node.left.get_balance_factor() < 0:
            self._rotate_left(node.left)
            self._rotate_right(node)

        # Right-Right Case → Single Left Rotation
        elif balance_factor < -1 and node.right.get_balance_factor() <= 0:
            self._rotate_left(node)

        # Right-Left Case → Right Rotation on child, then Left Rotation
        elif balance_factor < -1 and node.right.get_balance_factor() > 0:
            self._rotate_right(node.right)
            self._rotate_left(node)

    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate
        of the root for visual tree display.

        Args:
            node (AVLNode): The node to display.

        Returns:
            tuple: (lines, width, height, middle)
        """
        # no child
        if node.right is None and node.left is None:
            line = str(node.isbn)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # only left child
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = str(node.isbn)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # only right child
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = str(node.isbn)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # two children
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = str(node.isbn)
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
