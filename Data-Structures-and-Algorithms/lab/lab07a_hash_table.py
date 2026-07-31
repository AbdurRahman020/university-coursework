class Node:
    def __init__(self, key, val=None, next_ptr=None):
        # initialize the key of the node
        self.key = key
        # initialize the value of the node
        self.val = val
        # initialize the next pointer to the next node
        self.next = next_ptr


class HashT:
    def __init__(self, m=10):
        # initialize an array (list) of empty buckets
        self.table = [[]] * m
        # store total number of buckets (m)
        self.m = m
        # initialize number of inserted items (n)
        self.n = 0
        # initialize the load factor
        self.load_factor = 0.0

    def hash_function(self, key):
        """Compute hash index for a given key"""
        # if the key is an integer, return its value modulo m
        if isinstance(key, int):
            return key % self.m
        # if the key is a string, calculate a numeric hash
        # sum up the ASCII values of all characters in the string
        if isinstance(key, str):
            hash_val = sum(ord(char) for char in key)
            # compute the final index using modulo operator
            idx = hash_val % self.m
            # return the computed index
            return idx

        # for other types, use python's built-in hash function
        return hash(key) % self.m

    def insert(self, key, val=None):
        """Insert a key-value pair into the hash table"""
        # compute hash index for the key
        idx = self.hash_function(key)
        # access the corresponding bucket
        bucket = self.table[idx]

        # check if key already exists in bucket, if it does, update the value
        curr = bucket
        while curr:
            if curr.key == key:
                curr.val = val
                return
            curr = curr.next

        # if key is new, insert it at the beginning of the bucket
        new_node = Node(key, val, self.table[idx])
        self.table[idx] = new_node
        self.n += 1

        # compute load factor
        self.load_factor = self.n / self.m
        # if load factor exceeds 0.75, resize the table
        if self.load_factor > 0.75:
            self.resize()

    def resize(self):
        """Resize the hash table when load factor exceeds threshold"""
        old_table = self.table
        self.m = self.m * 2
        self.table = [[]] * self.m
        self.n = 0
        self.load_factor = 0.0

        # rehash all existing items
        for bucket in old_table:
            curr = bucket
            while curr:
                self.insert(curr.key, curr.val)
                curr = curr.next

    def contains(self, key):
        """Check if a key exists in the hash table"""
        # compute the hash index for the given key
        index = self.hash_function(key)
        # access the corresponding bucket
        bucket = self.table[index]

        # traverse the bucket to search for the key and return True if found
        curr = bucket
        while curr:
            if curr.key == key:
                return True
            curr = curr.next

        # if not found, return False
        return False

    def display(self):
        """Display the hash table"""
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: ", end="")
            if isinstance(bucket, list):
                if bucket:
                    print([f"({node.key}, {node.val})" for node in bucket])
                else:
                    print("[]")
            else:
                curr = bucket
                items = []
                while curr:
                    items.append(f"({curr.key}, {curr.val})")
                    curr = curr.next
                print(items if items else "[]")
