"""
Hash Table with Chaining
Based on standard hash table algorithms (MIT 6.006)
Hash function: Polynomial rolling hash (common in Java, Python)
Adapted for UET Library Management System
"""


class Node:
    """Node for chaining in hash table (linked-list bucket storage).

    This node structure is used for collision resolution via chaining.

    Attributes:
        key (Any): Key stored in the hash table.
        val (Any): Optional value associated with the key.
        next (Node): Pointer to the next node in the same bucket chain.
    """

    def __init__(self, key, val=None, next_ptr=None):
        # Primary key stored in this node
        self.key = key
        # Associated value (default: None)
        self.val = val
        # Pointer to next node in chain for this bucket
        self.next = next_ptr


class HashTable:
    """Hash Table implementation using chaining for collision resolution.

    Uses a linked-list per bucket to handle hash collisions efficiently.

    Performance:
        - Average case insert/search/delete: O(1)
        - Worst case (heavy collisions): O(n) in a single bucket

    Attributes:
        table (list): Internal bucket array storing head pointers of chains.
        m (int): Number of buckets (table capacity).
        n (int): Number of stored key-value entries.
        load_factor (float): Current load factor (n/m), used for resizing decisions.
    """

    def __init__(self, m=10):
        # Initialize bucket array with None (empty chains)
        self.table = [None] * m
        # Store capacity (number of buckets)
        self.m = m
        # Entry count initialized to 0
        self.n = 0
        # Load factor tracking for dynamic resizing
        self.load_factor = 0.0

    def hash_function(self, key):
        """Compute bucket index using polynomial rolling hash for strings,
        otherwise fallback to built-in hash.

        Polynomial Rolling Hash Properties:
            - Base prime = 31 (commonly used for uniform distribution)
            - Converts each character into an integer contribution

        Args:
            key (Any): Input key to hash.

        Returns:
            int: Valid bucket index in range [0, m−1]
        """
        if isinstance(key, str):
            # Compute rolling polynomial hash for string keys
            hash_value = 0
            prime = 31  # Base multiplier prime for polynomial hash
            for char in key:
                hash_value = hash_value * prime + ord(char)

            # Map computed hash into bucket range
            return hash_value % self.m

        # Fallback hashing for non-string keys
        return hash(key) % self.m

    def insert(self, key, val=None):
        """Insert or update a key-value entry in the hash table.

        - If key exists → updates its value
        - If key is new → inserts at bucket head (LIFO chaining)

        Resizes table when load factor exceeds 0.75

        Args:
            key (Any): Key to insert.
            val (Any): Optional value payload.
        """
        # Compute target bucket index
        idx = self.hash_function(key)
        # Pointer to current chain head at that bucket
        curr = self.table[idx]

        # Traverse chain to check for existing key
        while curr:
            if curr.key == key:
                # Key already exists → update value only
                curr.val = val
                return
            curr = curr.next

        # Key not found → create new node and insert at bucket head
        new_node = Node(key, val, self.table[idx])
        self.table[idx] = new_node
        # Increment entry count
        self.n += 1

        # Update load factor after insertion
        self.load_factor = self.n / self.m
        # Trigger resize if threshold exceeded
        if self.load_factor > 0.75:
            self.resize()

    def search(self, key):
        """Retrieve value associated with a key.

        Args:
            key (Any): Key to lookup.

        Returns:
            Any or None: Value if found, otherwise None.
        """
        # Compute bucket index for key
        idx = self.hash_function(key)
        # Traverse bucket chain
        curr = self.table[idx]

        while curr:
            if curr.key == key:
                # Key found → return stored value
                return curr.val
            curr = curr.next

        # Key not found in chain
        return None

    def delete(self, key):
        """Remove a key-value entry from the table if present.

        Chain pointers are updated to preserve bucket integrity.

        Args:
            key (Any): Key to remove.

        Returns:
            Any or None: Deleted value if successful, else None if key doesn't exist.
        """
        # Compute bucket index for key
        idx = self.hash_function(key)
        # Traverse bucket chain to locate key
        curr = self.table[idx]
        prev = None  # Tracks previous node for pointer updates

        while curr:
            if curr.key == key:
                # Key found → remove node from chain
                if prev is None:
                    # If deleting head, update bucket pointer
                    self.table[idx] = curr.next
                else:
                    # Otherwise bypass node in chain
                    prev.next = curr.next
                # Decrement entry count
                self.n -= 1
                # Update load factor after deletion
                self.load_factor = self.n / self.m
                return curr.val
            # Advance chain traversal
            prev = curr
            curr = curr.next

        # Key not found → deletion failed
        return None

    def resize(self):
        """Dynamically resizes the hash table to double its current capacity.

        Rehashes all existing entries by reinserting them into the new bucket array.
        """
        # Backup reference to existing table
        old_table = self.table
        # Double bucket capacity
        self.m = self.m * 2
        # Create new empty bucket array
        self.table = [None] * self.m
        # Reset entry counter before reinsertion
        self.n = 0
        # Reset load factor before reinsertion
        self.load_factor = 0.0

        # Reinsert all nodes from old table into new table (rehashing)
        for bucket_head in old_table:
            curr = bucket_head
            while curr:
                # Reinsert each node using updated hash indices
                self.insert(curr.key, curr.val)
                curr = curr.next

    def get_all_keys(self):
        """Extracts all keys stored in the hash table.

        Traverses each bucket chain and aggregates keys.

        Returns:
            list: All stored keys (order depends on chaining insertion pattern).
        """
        keys = []
        # Iterate through all buckets
        for bucket_head in self.table:
            curr = bucket_head
            # Traverse chain for this bucket
            while curr:
                keys.append(curr.key)
                curr = curr.next

        # Return aggregated key list
        return keys
