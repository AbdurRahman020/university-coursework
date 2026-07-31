from typing import Any, Optional, List


class Node:
    """
    A node in a doubly linked list.

    Attributes:
        _val: The value stored in the node.
        _prev: Reference to the previous node in the list.
        _next: Reference to the next node in the list.
    """
    # limit attributes to save memory (no __dict__ created)
    __slots__ = '_val', '_prev', '_next'

    def __init__(self, item: Any,
                 prev_node: Optional['Node'] = None,
                 next_node: Optional['Node'] = None) -> None:
        """
        Initialize a doubly linked list node.

        Args:
            item: The value to store in the node.
            prev_node: Reference to the previous node (default: None).
            next_node: Reference to the next node (default: None).
        """
        # store the value
        self._val: Any = item
        # reference to the previous node
        self._prev: Optional['Node'] = prev_node
        # reference to the next node
        self._next: Optional['Node'] = next_node

    @property
    def next(self) -> Optional['Node']:
        """Public access to the next node (getter)."""
        return self._next

    @next.setter
    def next(self, new_next: Optional['Node']) -> None:
        """Public access to set the next node (setter)."""
        self._next = new_next

    @property
    def prev(self) -> Optional['Node']:
        """Public access to the previous node (getter)."""
        return self._prev

    @prev.setter
    def prev(self, new_prev: Optional['Node']) -> None:
        """Public access to set the previous node (setter)."""
        self._prev = new_prev

    @property
    def value(self) -> Any:
        """Public access to the stored value (getter)."""
        return self._val

    @value.setter
    def value(self, new_val: Any) -> None:
        """Public access to set the stored value (setter)."""
        self._val = new_val


class DLList:
    """
    Doubly linked list with a sentinel node.

    The sentinel node simplifies insertion and deletion at the head and tail.
    Tracks the number of elements separately in 'size'.
    """

    def __init__(self) -> None:
        """
        Initialize an empty doubly linked list.

        Creates a sentinel node whose _next and _prev point to itself.
        Sets the initial size of the list to zero.
        """
        self.sentinel: Node = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        self.size: int = 0

    def insert_first(self, item: Any) -> None:
        """Insert a node after sentinel node"""
        dummy_node: Node = self.sentinel

        # create a new node between sentinel and current first node
        new_node: Node = Node(item, dummy_node, dummy_node.next)
        # update old first node to point back to new node
        dummy_node.next.prev = new_node
        # update sentinel to point to new node
        dummy_node.next = new_node

        # increment the size counter
        self.size += 1

    def insert_last(self, item: Any) -> None:
        """Insert a node before sentincal node"""
        dummy_node: Node = self.sentinel

        # create a new node between current last node and sentinel
        new_node: Node = Node(item, dummy_node.prev, dummy_node)
        # update old last node to point to new node
        dummy_node.prev.next = new_node
        # update sentinel to point back to new node
        dummy_node.prev = new_node

        # increment the size counter
        self.size += 1

    def insert_at(self, pos: int, item: Any) -> None:
        """Insert a node at a specific position"""
        # check boundary conditions
        if pos < 0 or pos > self.size:
            raise IndexError("Index out of range")

        # edge case (I)
        if pos == 0:
            self.insert_first(item)
            return
        # edge case (II)
        if pos == self.size:
            self.insert_last(item)
            return

        dummy_node: Node = self.sentinel

        curr_node = dummy_node
        # find the node before insertion point
        for _ in range(pos):
            curr_node = curr_node.next

        # create and link new node
        new_node = Node(item, curr_node, curr_node.next)
        curr_node.next.prev = new_node
        curr_node.next = new_node

        # increment the size counter
        self.size += 1

    def delete_first(self) -> None:
        """Delete the first node after sentinel node"""
        if self.size == 0:
            raise IndexError("Empty DLL")

        dummy_node: Node = self.sentinel

        # get the first node
        first_node: Node = dummy_node.next
        # link sentinel to second to first node
        dummy_node.next = first_node.next
        # link second to first node to sentinel
        first_node.next.prev = dummy_node

        # decrement the size counter
        self.size -= 1

    def delete_last(self) -> None:
        """Delete the first node before sentinel node"""
        if self.size == 0:
            raise IndexError("Empty DLL")

        dummy_node: Node = self.sentinel

        # get the last node
        last_node: Node = dummy_node.prev
        # link sentinel to second to last node
        dummy_node.prev = last_node.prev
        # link second to last node to sentinel
        last_node.prev.next = dummy_node

        # decrement the size counter
        self.size -= 1

    def delete_from(self, pos: int) -> Any:
        """Delete a node from a specific position"""
        # check boundary conditions
        if pos < 0 or pos >= self.size:
            raise IndexError("Index out of range")

        # edge case (I)
        if pos == 0:
            val = self.sentinel.next.value
            self.delete_first()
            return val
        # edge case (II)
        if pos == self.size - 1:
            val = self.sentinel.prev.value
            self.delete_last()
            return val

        dummy_node: Node = self.sentinel

        curr_node = dummy_node
        # find the node before deletion point
        for _ in range(pos):
            curr_node = curr_node.next

        node_to_be_deleted: Node = curr_node.next
        # bypass the node to delete
        curr_node.next = node_to_be_deleted.next
        node_to_be_deleted.next.prev = curr_node

        # decrement the size counter
        self.size -= 1

        return node_to_be_deleted.value

    def get_value_at(self, pos: int) -> Any:
        """Return the value at the given index"""
        # check if position is out of bounds
        if pos < 0 or pos >= self.size:
            raise IndexError("Out of Range")

        dummy_node: Node = self.sentinel
        # start at first actual node
        curr_node: Node = dummy_node.next

        # move forward pos times
        for _ in range(pos):
            curr_node = curr_node.next

        # return the value at this position
        return curr_node.value

    def to_list(self) -> List[Any]:
        """Return the list version of DLL"""
        # create empty list to store values
        list_for_node_vals: List[Any] = []

        dummy_node = self.sentinel
        # start at first actual node
        curr_node: Node = dummy_node.next

        # traverse until we reach sentinel again
        while curr_node != dummy_node:
            list_for_node_vals.append(curr_node.value)
            curr_node = curr_node.next

        return list_for_node_vals

    def is_empty(self) -> bool:
        """Checks if the DLL is empty"""
        return self.size == 0

    def __len__(self) -> int:
        """Return the number of elements in DLL"""
        return self.size

    def __iter__(self):
        """Can use loop on DLL"""
        dummy_node: Node = self.sentinel
        # start at first actual node
        curr_node: Node = dummy_node.next

        while curr_node != dummy_node:
            yield curr_node.value
            curr_node = curr_node.next

    def __reversed__(self):
        """Can use loop in reverse direction on DLL"""
        dummy_node: Node = self.sentinel
        # start at last actual node
        curr_node: Node = dummy_node.prev

        while curr_node != dummy_node:
            yield curr_node.value
            curr_node = curr_node.prev

    def __str__(self) -> str:
        """String representation"""
        return f"DLList(size = {self.size}, items = {self.to_list()})"
