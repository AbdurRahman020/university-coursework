import array
from typing import List

# %% Circualr Array Sequence


class CircularArraySeq:
    """Circular Array Sequence with optimized memory usage"""

    # limit attributes to save memory (no __dict__ created)
    __slots__ = 'items', 'capacity', 'curr_size', 'front_index', 'back_index'

    # default initial capacity and minimum capacity threshold
    DEFAULT_CAPACITY = 5

    def __init__(self, capacity: int = DEFAULT_CAPACITY,
                 front_index: int = 0,
                 back_index: int = 0) -> None:
        self.items: List[int] = array.array('l', [0] * capacity)
        self.capacity = capacity
        self.front_index = front_index
        self.back_index = back_index
        self.curr_size = 0

    def _resize(self, direction: str = 'up') -> None:
        """Resize the circular array up or down"""

        # calculate new capacity: double for 'up', halve for 'down'
        if direction == 'up':
            new_capacity = self.capacity * 2
        elif direction == 'down':
            new_capacity = max(self.capacity // 2, self.DEFAULT_CAPACITY)

        # allocate new array with updated capacity
        new_items = array.array('l', [0] * new_capacity)

        # copy elements sequentially, unwrapping circular structure
        for i in range(self.curr_size):
            new_items[i] = self.items[(self.front_index + i) % self.capacity]

        # update array reference and reset indices to linear layout
        self.items = new_items
        self.capacity = new_capacity
        self.front_index = 0
        self.back_index = self.curr_size

    def _check_resize_up(self) -> None:
        """Check and resize array if full"""
        if self.curr_size >= self.capacity:
            self._resize('up')

    def _check_resize_down(self) -> None:
        """Check and shrink array if utilization < 25%"""
        if self.curr_size > 0 and (
                self.curr_size < self.capacity * 0.25 and
                self.capacity > self.DEFAULT_CAPACITY):
            self._resize('down')

    def _check_not_empty(self) -> None:
        """Validate sequence is not empty"""
        if self.curr_size == 0:
            raise IndexError("Delete from empty sequence")

    def _validate_index(self, idx: int, allow_equal: bool = False) -> None:
        """Validate index bounds"""
        upper = self.curr_size if allow_equal else self.curr_size - 1
        if idx < 0 or idx > upper:
            raise IndexError("Index out of bounds")

    def _circular_index(self, idx: int) -> int:
        """Convert logical index to physical circular index"""
        return (self.front_index + idx) % self.capacity

    def insert_first(self, val: int) -> None:
        """Insert at the starting index"""
        self._check_resize_up()

        self.front_index = (self.front_index - 1) % self.capacity
        self.items[self.front_index] = val
        # increment the size counter
        self.curr_size += 1

    def insert_last(self, val: int) -> None:
        """Insert at the ending index"""
        self._check_resize_up()

        self.items[self.back_index] = val
        self.back_index = (self.back_index + 1) % self.capacity
        # increment the size counter
        self.curr_size += 1

    def insert_at(self, val: int, idx: int) -> None:
        """Insert at a specified index"""
        # make sure the index is valid for insertion
        self._validate_index(idx, allow_equal=True)
        # check if we need more space before inserting
        self._check_resize_up()

        # shift the smaller portion to minimize element moves
        if idx < self.curr_size // 2:
            # inserting closer to front, so shift front portion left
            self.front_index = (self.front_index - 1) % self.capacity
            # shift all elements before idx one position to the left
            for i in range(idx):
                from_idx = (self.front_index + i + 1) % self.capacity
                to_idx = (self.front_index + i) % self.capacity
                self.items[to_idx] = self.items[from_idx]
            # calculate where to place the new value
            actual_index = (self.front_index + idx) % self.capacity
        else:
            # inserting closer to back, so shift back portion right
            for i in range(self.curr_size, idx, -1):
                from_idx = (self.front_index + i - 1) % self.capacity
                to_idx = (self.front_index + i) % self.capacity
                self.items[to_idx] = self.items[from_idx]
            # update back pointer since we shifted right
            self.back_index = (self.back_index + 1) % self.capacity
            # calculate where to place the new value
            actual_index = (self.front_index + idx) % self.capacity

        # place the new value at the insertion point
        self.items[actual_index] = val
        # increment the size counter
        self.curr_size += 1

    def delete_first(self) -> int:
        """Delete from the starting index"""
        self._check_not_empty()

        val = self.items[self.front_index]
        self.front_index = (self.front_index + 1) % self.capacity
        # decrement the size counter
        self.curr_size -= 1

        self._check_resize_down()

        return val

    def delete_last(self) -> int:
        """Delete from the ending index"""
        self._check_not_empty()

        self.back_index = (self.back_index - 1) % self.capacity
        val = self.items[self.back_index]
        # dencrement the size counter
        self.curr_size -= 1

        self._check_resize_down()

        return val

    def delete_at(self, idx: int) -> int:
        """Delete element at a specified index"""
        # make sure the index is valid
        self._validate_index(idx)
        # find the actual position in the circular array
        actual_index = self._circular_index(idx)

        # grab the value before we shift things around
        val = self.items[actual_index]

        # shift the smaller portion to minimize element moves
        if idx < self.curr_size // 2:
            # deleting closer to front, so shift front portion right
            for i in range(idx, 0, -1):
                from_idx = (self.front_index + i - 1) % self.capacity
                to_idx = (self.front_index + i) % self.capacity
                self.items[to_idx] = self.items[from_idx]
            # move front pointer forward since we shifted right
            self.front_index = (self.front_index + 1) % self.capacity
        else:
            # deleting closer to back, so shift back portion left
            for i in range(idx, self.curr_size - 1):
                from_idx = (self.front_index + i + 1) % self.capacity
                to_idx = (self.front_index + i) % self.capacity
                self.items[to_idx] = self.items[from_idx]
            # move back pointer backward since we shifted left
            self.back_index = (self.back_index - 1) % self.capacity

        # decrement the size counter
        self.curr_size -= 1

        # check if we should shrink the array
        self._check_resize_down()

        return val

    def get_at(self, idx: int) -> int:
        """Get element at logical index"""
        self._validate_index(idx)
        return self.items[self._circular_index(idx)]

    def get_first(self) -> int | None:
        """Get the first element without removing it"""
        if self.curr_size == 0:
            return None
        return self.items[self.front_index]

    def get_last(self) -> int | None:
        """Get the last element without removing it"""
        if self.curr_size == 0:
            return None
        return self.items[(self.back_index - 1) % self.capacity]

    def set_at(self, idx: int, val: int) -> None:
        """Set element at logical index"""
        self._validate_index(idx)
        self.items[self._circular_index(idx)] = val

    def to_list(self) -> list:
        """Return the logical sequence as a list"""
        return [self.get_at(i) for i in range(self.curr_size)]

    def __len__(self) -> int:
        """Return the current size of the array"""
        return self.curr_size

    def is_empty(self) -> bool:
        """Check if the Circular Array Sequence is empty"""
        return self.curr_size == 0

    def __str__(self) -> str:
        """String representation"""
        return (
            f"CircularArraySeq(size={self.curr_size}, "
            f"capacity={self.capacity}, "
            f"items={[self.get_at(i) for i in range(self.curr_size)]})"
        )
