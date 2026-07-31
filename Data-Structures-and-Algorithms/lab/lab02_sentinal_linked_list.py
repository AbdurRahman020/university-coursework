from typing import Optional, Any, List


class Node:
    """
    A node in a singly linked list.

    Attributes:
        _val: The value stored in the node.
        _next: Reference to the next node in the list.
    """
    # limit attributes to save memory (no __dict__ created)
    __slots__ = '_val', '_next'

    def __init__(self, item: Any, next_node: Optional['Node'] = None) -> None:
        """
        Initialize a singly linked list node.

        Args:
            item: The value to store in the node.
            next_node: Reference to the next node (default: None).
        """
        self._val = item
        self._next = next_node

    @property
    def next(self) -> Optional['Node']:
        """Public access to the next node (getter)."""
        return self._next

    @next.setter
    def next(self, new_next: Optional['Node']) -> None:
        """Public access to set the next node (setter)."""
        self._next = new_next

    @property
    def value(self) -> Any:
        """Public access to the stored value (getter)."""
        return self._val

    @value.setter
    def value(self, new_val: Any) -> None:
        """Public access to set the stored value (setter)."""
        self._val = new_val


class SLList:
    """
    Singly linked list with a sentinel node.

    The sentinel node simplifies insertion and deletion.
    Tracks the number of elements separately in 'size'.
    """

    def __init__(self) -> None:
        """
        Initialize an empty singly linked list.

        Creates a sentinel node and sets the initial size to zero.
        """
        self._sentinel: Node = Node(None)
        self._size = 0

    @property
    def sentinel(self) -> Node:
        """Public access to the sentinel node (getter)."""
        return self._sentinel

    @property
    def size(self) -> int:
        """Public access to the size of the linked list (getter)."""
        return self._size

    @size.setter
    def size(self, new_size: int) -> None:
        """Public access to set the size of the linked list (setter)."""
        self._size = new_size

    def insert_first(self, item: Any) -> None:
        """Insert the first node, after sentinel"""
        # start from sentinel node
        curr_node: Node = self.sentinel

        # create new node that points to the current first element
        new_node: Node = Node(item, curr_node.next)
        # update sentinel to point to new first element
        curr_node.next = new_node

        # increment the size counter
        self.size += 1

    def insert_last(self, item: Any) -> None:
        """Insert a node at the end"""
        # create new node with no next pointer (will be last)
        new_node: Node = Node(item)

        # start from sentinel node
        curr_node: Node = self.sentinel

        # traverse to the last node
        while curr_node.next is not None:
            curr_node = curr_node.next

        # link the last node to our new node
        curr_node.next = new_node

        # increment the size counter
        self.size += 1

    def insert_at(self, pos: int, item: Any) -> None:
        """Insert a node at specific index"""
        # special case: inserting at beginning
        if pos == 0:
            self.insert_first(item)
            return

        # start from sentinel node
        curr_node: Node = self.sentinel

        # move to the node just before the insertion position
        for _ in range(pos):
            if curr_node is None:
                raise IndexError("Index out of range")
            curr_node = curr_node.next

        # check if we've gone past the end of the list
        if curr_node is None:
            raise IndexError("Index out of range")

        # create new node that points to the next node
        new_node = Node(item, curr_node.next)
        # link current node to our new node
        curr_node.next = new_node

        # increment the size counter
        self.size += 1

    def delete_first(self) -> None:
        """Delete the first node"""
        # check if list is empty
        if self.size == 0:
            raise IndexError("empty linked list")

        # start from sentinel node
        curr_node: Node = self.sentinel

        # delete the first element
        curr_node.next = (curr_node.next).next

        # decrement the size counter
        self.size -= 1

    def delete_last(self) -> None:
        """Delete the last node"""
        # check if list is empty
        if self.size == 0:
            raise IndexError("empty linked list")

        # start from sentinel node
        curr_node: Node = self.sentinel

        # traverse to the second-to-last node
        while curr_node.next and (curr_node.next).next:
            curr_node = curr_node.next

        # now curr_node is the second-to-last node
        curr_node.next = None

        # decrement the size counter
        self.size -= 1

    def delete_from(self, pos: int) -> None:
        """Delete a node from specified position"""
        # check if pos is valid first
        if pos < 0 or pos >= self.size:
            raise IndexError("Index out of range")

        # special case: deleting from the beginning
        if pos == 0:
            self.delete_first()
            return

        # start from the sentinel node
        curr_node: Node = self.sentinel

        # move to the node just before the position to delete
        for _ in range(pos):
            curr_node = curr_node.next

        # curr_node is now the node just before the one we want to delete
        curr_node.next = (curr_node.next).next

        # decrement the size counter
        self.size -= 1

    def get_first(self) -> Any:
        """Return the value of first actual node"""
        # check if list is not empty
        if self.size != 0:
            # return value of first actual node (skip sentinel)
            return self.sentinel.next.value
        # return None for empty list
        return None

    def get_at(self, pos: int) -> Any:
        """Return the value of a node at specified postion"""
        # check if pos is within valid range
        if pos < 0 or pos >= self.size:
            return None

        # start from the first actual node
        curr_node: Node = self.sentinel.next

        for _ in range(pos):
            curr_node = curr_node.next

        return curr_node.value

    def to_list(self) -> List[Any]:
        """Return the list version of SLList"""
        # create empty list to store values
        list_for_node_vals: List[Any] = []

        dummy_node = self.sentinel
        # start at first actual node
        curr_node: Node = dummy_node.next

        # traverse until we reach sentinel again
        while curr_node is not None:
            list_for_node_vals.append(curr_node.value)
            curr_node = curr_node.next

        return list_for_node_vals

    def __len__(self) -> int:
        """Return the current size of the linked list"""
        return self.size

    def __str__(self) -> str:
        return f"SLList(size = {self.size}, items = {self.to_list()})"
