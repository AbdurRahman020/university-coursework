from typing import Any, Optional

# %% Linked Stack Implementation


class Node:
    """ Node class representing a single element in the stack."""

    # limit attributes to save memory (no __dict__ created)
    __slots__ = '_val', '_next_node'

    def __init__(self, item: Any, next_node: Optional['Node'] = None) -> None:
        # store the data of the node
        self._val: Any = item
        # reference to the next node
        self._next_node: Optional['Node'] = next_node

    @property
    def value(self) -> Any:
        """Public access to the node's value (getter)."""
        return self._val

    @value.setter
    def value(self, new_val: Any) -> None:
        """Public access to set the node's value (setter)."""
        self._val = new_val

    @property
    def next(self) -> Optional['Node']:
        """Public access to the next node (getter)."""
        return self._next_node

    @next.setter
    def next(self, new_next: Optional['Node']) -> None:
        """Public access to set the next node (setter)."""
        self._next_node = new_next


class LinkedStack:
    def __init__(self) -> None:
        # head points to the top of the stack
        self._head: Optional[Node] = None
        # initialize stack size to 0
        self._size: int = 0

    @property
    def head(self) -> Optional[Node]:
        """Public access to the head node (getter)."""
        return self._head

    @head.setter
    def head(self, new_head: Optional[Node]) -> None:
        """Public access to set the head node (setter)."""
        self._head = new_head

    @property
    def size(self) -> int:
        """Public access to the stack size (getter)."""
        return self._size

    @size.setter
    def size(self, new_size: int) -> None:
        """Public access to set the stack size (setter)."""
        self._size = new_size

    def __len__(self) -> int:
        """Returns the size of the stack"""
        return self.size

    def is_empty(self) -> bool:
        """Checks if the stack is empty"""
        return self.size == 0

    def __str__(self) -> str:
        """Returns string representation of the stack"""
        if self.is_empty():
            return "LinkedStack([])"

        items = []
        current = self.head
        while current is not None:
            items.append(str(current.value))  # use property
            current = current.next  # use property

        return f"LinkedStack([{', '.join(items)}])"

    def push(self, data: Any) -> None:
        """Pushes a new element onto the stack"""
        # create new node, point to current head
        self.head = Node(data, self.head)  # use property
        # increase stack size
        self.size += 1

    def top(self) -> Any:
        """Returns the top element of the stack without removing it"""
        if self.is_empty():
            raise IndexError("Stack is empty!")
        return self.head.value  # use property

    def pop(self) -> Any:
        """Removes and returns the top element of the stack"""
        if self.is_empty():
            raise IndexError("Stack is empty!")

        top_val: Any = self.head.value  # use property
        self.head = self.head.next  # use property
        self.size -= 1
        return top_val
