class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value if value is not None else key
        self.right = None
        self.left = None

    def insert(self, key, value=None):
        """Insert a node in BST."""
        if self.key == key:
            return

        if self.key < key:
            if self.right is None:
                self.right = BSTNode(key, value)
            else:
                self.right.insert(key, value)
        else:
            if self.left is None:
                self.left = BSTNode(key, value)
            else:
                self.left.insert(key, value)

    def search(self, key):
        """Helper method to search for a node with given key."""
        if self.key == key:
            return self

        if self.key < key:
            if self.right is None:
                return None
            return self.right.search(key)

        if self.left is None:
            return None

        return self.left.search(key)

    def inorder_traversal(self):
        """Helper method to get inorder traversal (sorted order)."""
        result = []

        if self.left:
            result.extend(self.left.inorder_traversal())

        result.append(self.key)

        if self.right:
            result.extend(self.right.inorder_traversal())

        return result

    def count_nodes(self):
        """Helper method to count total nodes."""
        count = 1

        if self.left:
            count += self.left.count_nodes()

        if self.right:
            count += self.right.count_nodes()

        return count

    def delete(self, key):
        """Helper method to delete a node."""
        if key < self.key:
            if self.left:
                self.left = self.left.delete(key)
        elif key > self.key:
            if self.right:
                self.right = self.right.delete(key)
        else:
            if not self.left:
                return self.right

            if not self.right:
                return self.left

            temp_node = self.right

            while temp_node.left:
                temp_node = temp_node.left

            self.key, self.value = temp_node.key, temp_node.value
            self.right = self.right.delete(temp_node.key)

        return self

    # https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
    def display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate
        of the root."""
        # no child
        if self.right is None and self.left is None:
            line = '< ' + str(self.key) + ' , ' + str(self.value) + ' >'
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # only left child.
        if self.right is None:
            lines, n, p, x = self.left.display_aux()
            s = '< ' + str(self.key) + ' , ' + str(self.value) + ' >'
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # only right child.
        if self.left is None:
            lines, n, p, x = self.right.display_aux()
            s = '< ' + str(self.key) + ' , ' + str(self.value) + ' >'
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # two children.
        left, n, p, x = self.left.display_aux()
        right, m, q, y = self.right.display_aux()
        s = '< ' + str(self.key) + ' , ' + str(self.value) + ' >'
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

    def display(self):
        """Display BST."""
        lines, *_ = self.display_aux()
        for line in lines:
            print(line)
        print()
