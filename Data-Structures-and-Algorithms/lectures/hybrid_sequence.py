# Hybrid Sequence Data Structure (Deque with O(1) indexing)

class HybridSequence:
    """
    A hybrid data structure combining the benefits of arrays and linked lists.

    Features:
    - O(1) worst-case indexing (like arrays)
    - O(1) amortized insertion/removal at both ends (like deques)
    - O(n) space for n items

    Implementation Strategy:
    Uses two dynamic arrays (front and back) with the following invariants:
    - back array stores elements from middle to end (normal order)
    - front array stores elements from start to middle (reversed order)
    - Rebalancing occurs when one array becomes too large

    This is similar to the approach discussed in CLRS for amortized analysis.
    """

    def __init__(self):
        """Initialize empty sequence"""
        self.front = []  # stores first half in reverse
        self.back = []   # stores second half normally
        self._size = 0

    def __len__(self):
        """Return number of items. O(1) time."""
        return self._size

    def __getitem__(self, index):
        """
        Get item at index in O(1) worst-case time.

        Algorithm:
            if index < 0 or index >= size
                raise IndexError
            if index < len(front)
                return front[len(front) - 1 - index]  # Reverse indexing
            else
                return back[index - len(front)]
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")

        front_size = len(self.front)

        if index < front_size:
            # index is in front array (stored reversed)
            return self.front[front_size - 1 - index]
        else:
            # index is in back array
            return self.back[index - front_size]

    def __setitem__(self, index, value):
        """Set item at index in O(1) worst-case time."""
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")

        front_size = len(self.front)

        if index < front_size:
            self.front[front_size - 1 - index] = value
        else:
            self.back[index - front_size] = value

    def insert_first(self, value):
        """
        Insert at the beginning in O(1) amortized time.

        Algorithm:
            front.append(value)
            size ← size + 1
            if len(front) > 2 × len(back) + 1
                rebalance()
        """
        self.front.append(value)
        self._size += 1
        self._rebalance_if_needed()

    def insert_last(self, value):
        """
        Insert at the end in O(1) amortized time.
        """
        self.back.append(value)
        self._size += 1
        self._rebalance_if_needed()

    def delete_first(self):
        """
        Remove and return first item in O(1) amortized time.

        Algorithm:
            if size = 0
                raise IndexError
            if front is not empty
                value ← front.pop()
            else
                value ← back.pop(0)
            size ← size - 1
            rebalance_if_needed()
            return value
        """
        if self._size == 0:
            raise IndexError("Cannot delete from empty sequence")

        if self.front:
            value = self.front.pop()
        else:
            value = self.back.pop(0)

        self._size -= 1
        self._rebalance_if_needed()

        return value

    def delete_last(self):
        """Remove and return last item in O(1) amortized time."""
        if self._size == 0:
            raise IndexError("Cannot delete from empty sequence")

        if self.back:
            value = self.back.pop()
        else:
            value = self.front.pop(0)

        self._size -= 1
        self._rebalance_if_needed()

        return value

    def _rebalance_if_needed(self):
        """
        Rebalance if one array becomes too large relative to the other.

        Invariant: |len(front) - len(back)| ≤ n/2

        This ensures O(1) amortized time for all operations.
        Rebalancing takes O(n) time but happens infrequently.

        Amortized Analysis (Accounting Method):
        - Charge $3 per insert/delete operation
        - $1 for the actual operation
        - $2 saved as credit for future rebalancing
        - When rebalancing (O(n) cost), we have accumulated O(n) credit
        """
        if self._size <= 1:
            return

        front_size = len(self.front)
        back_size = len(self.back)

        # rebalance if imbalance is too large
        if front_size > 2 * back_size + 1 or back_size > 2 * front_size + 1:
            # merge both arrays
            all_items = []

            # get items in order
            for i in range(self._size):
                all_items.append(self[i])

            # split evenly
            mid = self._size // 2
            self.front = all_items[:mid][::-1]  # Reverse for front
            self.back = all_items[mid:]

    def __str__(self):
        """String representation"""
        if self._size == 0:
            return "[]"

        items = [str(self[i]) for i in range(self._size)]

        return "[" + ", ".join(items) + "]"


# %% test cases

print("HYBRID SEQUENCE DATA STRUCTURE\n")

print("Test: Basic Operations")
seq = HybridSequence()

print("Insert at front: 1, 2, 3")
seq.insert_first(3)
seq.insert_first(2)
seq.insert_first(1)
print(f"Sequence: {seq}")
print(f"Length: {len(seq)}\n")

print("Insert at back: 4, 5, 6")
seq.insert_last(4)
seq.insert_last(5)
seq.insert_last(6)
print(f"Sequence: {seq}\n")

print("Indexing (O(1) access):")
for i in range(len(seq)):
    print(f"  seq[{i}] = {seq[i]}")

print("\nModify seq[2] = 99")
seq[2] = 99
print(f"Sequence: {seq}\n")

print("Delete from front:")
print(f"  Removed: {seq.delete_first()}")
print(f"  Sequence: {seq}\n")

print("Delete from back:")
print(f"  Removed: {seq.delete_last()}")
print(f"  Sequence: {seq}\n")

print("Test: Stress test with many operations")
seq2 = HybridSequence()

print("Inserting 100 elements alternating front/back...")
for i in range(50):
    seq2.insert_first(i)
    seq2.insert_last(i + 50)

print(f"Length: {len(seq2)}")
print(f"First 10: {[seq2[i] for i in range(10)]}")
print(f"Last 10: {[seq2[len(seq2) - 10 + i] for i in range(10)]}")

print("\nDeleting 50 elements from front...")

for _ in range(50):
    seq2.delete_first()

print(f"Length after deletions: {len(seq2)}")


print("""
\nCOMPLEXITY ANALYSIS - Hybrid Sequence:
----------------------------------------
Time Complexity:
  - Indexing (__getitem__, __setitem__): O(1) worst-case
  - Insert/delete at ends: O(1) amortized
  - Rebalancing: O(n) worst-case, but amortized O(1)

Space Complexity: O(n) for n items

Amortized Analysis (Accounting Method from CLRS Ch. 17):
  - Each operation charged $3
  - $1 for immediate work
  - $2 saved for rebalancing
  - Rebalancing costs O(n) but happens after Ω(n) operations
  - Therefore, amortized cost is O(1)

This achieves the best of both worlds:
  O(1) indexing (like arrays)
  O(1) amortized insert/delete at both ends (like linked lists)
  O(n) space usage
""")
