class BinaryNode:
    def __init__(self, x):
        """
        Initialize a binary tree node with an item and null pointers.

        Args:
            x: The value to store in this node
        """
        self.item = x          # store the node's value
        self.left = None       # pointer to left child
        self.right = None      # pointer to right child
        self.parent = None     # pointer to parent node

    def subtree_iter(self):
        """
        In-order traversal iterator of the subtree rooted at this node.
        Yields nodes in sorted order (left subtree, root, right subtree).

        Time complexity: O(n) where n is the number of nodes in subtree
        """
        # recursively yield all nodes from left subtree
        if self.left:
            yield from self.left.subtree_iter()

        # yield the current node
        yield self

        # recursively yield all nodes from right subtree
        if self.right:
            yield from self.right.subtree_iter()

    def subtree_first(self):
        """
        Find the leftmost (minimum) node in the subtree rooted at this node.

        Time complexity: O(h) where h is the height of the subtree
        Returns: The leftmost node
        """
        # keep going left until we can't go any further
        if self.left:
            return self.left.subtree_first()
        else:
            return self

    def subtree_last(self):
        """
        Find the rightmost (maximum) node in the subtree rooted at this node.

        Time complexity: O(h) where h is the height of the subtree
        Returns: The rightmost node
        """
        # keep going right until we can't go any further
        if self.right:
            return self.right.subtree_last()
        else:
            return self

    def successor(self):
        """
        Find the in-order successor of this node (next larger node).

        Time complexity: O(h) where h is the height of the tree
        Returns: The successor node, or None if this is the maximum node
        """
        # if right subtree exists, successor is its minimum
        if self.right:
            return self.right.subtree_first()

        # otherwise, go up until we find a parent where we came from the left
        # (meaning we're transitioning from a left subtree to its parent)
        node = self
        while node.parent and (node is node.parent.right):
            node = node.parent

        return node.parent

    def predecessor(self):
        """
        Find the in-order predecessor of this node (next smaller node).

        Time complexity: O(h) where h is the height of the tree
        Returns: The predecessor node, or None if this is the minimum node
        """
        # if left subtree exists, predecessor is its maximum
        if self.left:
            return self.left.subtree_last()

        # otherwise, go up until we find a parent where we came from the right
        # (meaning we're transitioning from a right subtree to its parent)
        node = self
        while node.parent and (node is node.parent.left):
            node = node.parent

        return node.parent

    def subtree_insert_before(self, new_node):
        """
        Insert node new_node immediately before node self in in-order traversal.
        new_node becomes self's predecessor.

        Args:
            new_node: The node to insert
        """
        # if self has a left child, insert new_node at the rightmost position of left subtree
        if self.left:
            node = self.left.subtree_last()
            node.right, new_node.parent = new_node, node
        else:
            # otherwise, new_node becomes self's left child directly
            self.left, new_node.parent = new_node, self

    def subtree_insert_after(self, new_node):
        """
        Insert node new_node immediately after node self in in-order traversal.
        new_node becomes self's successor.

        Args:
            new_node: The node to insert
        """
        # if self has a right child, insert new_node at the leftmost position of right subtree
        if self.right:
            node = self.right.subtree_first()
            node.left, new_node.parent = new_node, node
        else:
            # otherwise, new_node becomes self's right child directly
            self.right, new_node.parent = new_node, self

    def subtree_delete(self):
        """
        Delete this node from the tree while maintaining BST properties.
        If the node has children, swap with predecessor/successor first,
        then delete the swapped node (which will be a leaf or have one child).

        Returns: The actually deleted node (which may be different from self after swapping)
        """
        # if node has at least one child, swap with predecessor or successor
        if self.left or self.right:
            # choose predecessor if left child exists, otherwise successor
            if self.left:
                other_node = self.predecessor()
            else:
                other_node = self.successor()

            # swap items (not the actual nodes, just their values)
            self.item, other_node.item = other_node.item, self.item

            # recursively delete the swapped node (other_node), which is now in a simpler position
            return other_node.subtree_delete()

        # node is a leaf - just remove it from parent's pointer
        if self.parent:
            if self.parent.left is self:
                self.parent.left = None
            else:
                self.parent.right = None

        return self

# %%


class BST_Node(BinaryNode):
    def subtree_find(self, k):
        """
        Find a node with key k in the subtree rooted at this node.

        Args:
            k: The key to search for

        Returns: The node with key k, or None if not found
        """
        if k < self.item.key:
            if self.left:
                return self.left.subtree_find(k)
        elif k > self.item.key:
            if self.right:
                return self.right.subtree_find(k)
        else:
            return self

        return None

    def subtree_find_next(self, k):
        """
        Find the node with the smallest key greater than k.

        Args:
            k: The key threshold

        Returns: The node with smallest key > k, or None if no such node exists
        """
        if self.item.key <= k:
            if self.right:
                return self.right.subtree_find_next(k)
            else:
                return None
        elif self.left:
            result = self.left.subtree_find_next(k)
            if result:
                return result

        return self

    def subtree_find_prev(self, k):
        """
        Find the node with the largest key less than k.

        Args:
            k: The key threshold

        Returns: The node with largest key < k, or None if no such node exists
        """
        if self.item.key >= k:
            if self.left:
                return self.left.subtree_find_prev(k)
            else:
                return None
        elif self.right:
            result = self.right.subtree_find_prev(k)
            if result:
                return result

        return self

    def subtree_insert(self, new_node):
        """
        Insert a new node into the BST subtree rooted at this node.

        Args:
            new_node: The node to insert
        """
        if new_node.item.key < self.item.key:
            if self.left:
                self.left.subtree_insert(new_node)
            else:
                self.subtree_insert_before(new_node)
        elif new_node.item.key > self.item.key:
            if self.right:
                self.right.subtree_insert(new_node)
            else:
                self.subtree_insert_after(new_node)
        else:
            self.item = new_node.item

# %%


class BinaryTree:
    def __init__(self, Node_Type=BinaryNode):
        """
        Initialize an empty binary tree.

        Args:
            Node_Type: The class to use for creating nodes (default: BinaryNode)
        """
        self.root = None                # root node of the tree
        self.size = 0                   # number of nodes in the tree
        self.Node_Type = Node_Type      # node class to instantiate

    def __len__(self):
        """
        Return the number of nodes in the tree.

        Returns: The size of the tree
        """
        return self.size

    def __iter__(self):
        """
        Iterator over items in the tree (in-order traversal).

        Yields: Item values from nodes in in-order sequence
        """
        if self.root:
            for node in self.root.subtree_iter():
                yield node.item

    def build(self, X):
        """
        Build a balanced binary tree from a sequence of items.
        Creates a complete binary tree structure.

        Args:
            X: Iterable of items to insert into the tree
        """
        # convert input to list
        items = [x for x in X]

        def build_subtree(items, i, j):
            """
            Recursively build a balanced subtree from array slice items[i:j+1].

            Args:
                items: Array of items
                i: Start index (inclusive)
                j: End index (inclusive)

            Returns: Root node of the constructed subtree
            """
            # find middle index
            c = (i + j) // 2
            # create node with middle item
            root = self.Node_Type(items[c])

            if i < c:
                # build left subtree from left half
                root.left = build_subtree(items, i, c - 1)
                root.left.parent = root

            if c < j:
                # build right subtree from right half
                root.right = build_subtree(items, c + 1, j)
                root.right.parent = root

            return root

        self.root = build_subtree(items, 0, len(items) - 1)
        self.size = len(items)

# %%


class SetBinaryTree(BinaryTree):
    def __init__(self):
        super().__init__(BST_Node)

    def iter_order(self):
        yield from self

    def build(self, X):
        for x in X:
            self.insert(x)

    def find_min(self):
        if self.root:
            return self.root.subtree_first().item

    def find_max(self):
        if self.root:
            return self.root.subtree_last().item

    def find(self, k):
        if self.root:
            node = self.root.subtree_find(k)
            if node:
                return node.item

    def find_next(self, k):
        if self.root:
            node = self.root.subtree_find_next(k)
            if node:
                return node.item

    def find_prev(self, k):
        if self.root:
            node = self.root.subtree_find_prev(k)
            if node:
                return node.item

    def insert(self, x):
        new_node = self.Node_Type(x)
        if self.root:
            self.root.subtree_insert(new_node)
            if new_node.parent is None:
                return False
        else:
            self.root = new_node

        self.size += 1

        return True

    def delete(self, k):
        assert self.root
        node = self.root.subtree_find(k)
        assert node
        ext = node.subtree_delete()

        if ext.parent is None:
            self.root = None

        self.size -= 1

        return ext.item
