import array
from typing import List

# %% Array Sequence


class ArrSeq:
    """Array Sequence with optimized memory usage"""

    # limit attributes to save memory (no __dict__ created)
    __slots__ = 'capacity', 'curr_size', 'items'

    # default initial capacity and minimum capacity threshold
    DEFAULT_CAPACITY = 5

    def __init__(self, capacity: int = DEFAULT_CAPACITY) -> None:
        self.capacity = capacity
        self.curr_size: int = 0
        self.items: List[int] = array.array("l", [0] * capacity)

    def _resize(self, new_capacity) -> None:
        """Create a new array with new_capacity and transfer all elements
        from old array"""
        # create new array with new capacity
        new_items: List[int] = array.array("l", [0] * new_capacity)

        # transfer all elements from old array to new array
        for i in range(self.curr_size):
            new_items[i] = self.items[i]

        # update the array and capacity
        self.items = new_items
        self.capacity = new_capacity

    def _check_resize_up(self) -> None:
        """Check and resize array if full"""
        if self.curr_size >= self.capacity:
            new_capacity = self.capacity * 2
            self._resize(new_capacity)

    def _check_resize_down(self) -> None:
        """Check and resize array if utilization falls below 25%"""
        # check if we need to shrink the array
        if self.curr_size > 0 and (
                self.curr_size / self.capacity < 0.25 and
                self.capacity > self.DEFAULT_CAPACITY):
            # reduce capacity to half and maintain minimum capacity
            # of DEFAULT_CAPACITY
            new_capacity = max(self.DEFAULT_CAPACITY, self.capacity // 2)

            self._resize(new_capacity)

    def _validate_index(self, idx: int, allow_equal: bool = False) -> None:
        """Validate index bounds"""
        upper = self.curr_size if allow_equal else self.curr_size - 1
        if idx < 0 or idx > upper:
            raise IndexError("Index out of bounds")

    def insert_first(self, val: int) -> None:
        """Insert element at the 0 index. Resize array if full"""
        # check if array is full
        self._check_resize_up()

        # shift elements right, starting from the end
        for i in range(self.curr_size - 1, -1, -1):
            self.items[i + 1] = self.items[i]

        # insert the element at the start
        self.items[0] = val
        # increment the size counter
        self.curr_size += 1

    def insert_last(self, val: int) -> None:
        """Insert element at the end. _resize array if full"""
        # check if array is full
        self._check_resize_up()

        # insert the element at the end
        self.items[self.curr_size] = val
        # increment the size counter
        self.curr_size += 1

    def insert_at(self, val: int, idx: int) -> None:
        """Insert element at specified index. Resize array if full"""
        self._validate_index(idx, allow_equal=True)
        self._check_resize_up()

        # shift elements right from idx onwards
        for i in range(self.curr_size - 1, idx - 1, -1):
            self.items[i + 1] = self.items[i]

        # insert the element at idx
        self.items[idx] = val
        # increment the size counter
        self.curr_size += 1

    def delete_first(self) -> int:
        """Delete first element. Resize array if utilization falls below 25%"""
        if self.curr_size == 0:
            raise IndexError("Array is empty")

        # retrieve the value to return
        val = self.items[0]

        # shift elements left from index 1 onwards
        for i in range(1, self.curr_size):
            self.items[i - 1] = self.items[i]

        # decrement the size counter
        self.curr_size -= 1
        # clear the last position
        self.items[self.curr_size] = 0

        # check if we need to shrink the array
        self._check_resize_down()

        return val

    def delete_last(self) -> None:
        """Delete last element. Resize array if utilization falls below 25%"""
        if self.curr_size == 0:
            raise IndexError("Array is empty")

        # decrement the size counter
        self.curr_size -= 1
        # delete the last element
        self.items[self.curr_size] = 0

        self._check_resize_down()

    def delete_at(self, idx: int) -> int:
        """Delete element at specified index. Resize array if utilization
        falls below 25%"""
        self._validate_index(idx)

        # retrieve the value to return
        val = self.items[idx]

        # shift elements left from idx+1 onwards
        for i in range(idx, self.curr_size - 1):
            self.items[i] = self.items[i + 1]

        # derement the size counter
        self.curr_size -= 1
        # clear the last position
        self.items[self.curr_size] = 0

        # check if we need to shrink the array
        self._check_resize_down()

        return val

    def get_last(self) -> int:
        """Get the last element"""
        if self.curr_size == 0:
            return None
        return self.items[self.curr_size - 1]

    def get_at(self, idx: int) -> int:
        """Get element at index idx"""
        if idx < 0 or idx >= self.curr_size:
            raise IndexError("Index out of bounds")
        return self.items[idx]

    def __len__(self) -> int:
        """Return the current size of the array"""
        return self.curr_size

    def __str__(self) -> str:
        """String representation"""
        return (
            f"ArraySeq(size={self.curr_size}, capacity={self.capacity}, "
            f"items={[self.get_at(i) for i in range(self.curr_size)]})"
            )
