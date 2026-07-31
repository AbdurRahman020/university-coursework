from typing import Any, List

# %% Stack using List


class Stack:
    def __init__(self) -> None:
        # Initialize the stack with an empty list
        self._items: List[Any] = []

    @property
    def items(self) -> List[Any]:
        """Public access to the stack items (getter)."""
        return self._items

    @items.setter
    def items(self, new_items: List[Any]) -> None:
        """Public access to set the stack items (setter)."""
        self._items = new_items

    def push(self, item: Any) -> None:
        """Add the item to the top of the stack"""
        self._items.append(item)

    def is_empty(self) -> bool:
        """Check if the stack is empty"""
        return len(self._items) == 0

    def pop(self) -> Any:
        """Remove and return the top item from the stack"""
        if self.is_empty():
            raise IndexError("It's an empty Stack")
        return self._items.pop()

    def peek(self) -> Any:
        """Return the top item without removing it"""
        if self.is_empty():
            raise IndexError("It's an empty Stack")
        return self._items[-1]

    def __len__(self) -> int:
        """Return the number of items in the stack"""
        return len(self._items)

    def __str__(self) -> str:
        """String representation"""
        return f'Stack: {self._items}'
