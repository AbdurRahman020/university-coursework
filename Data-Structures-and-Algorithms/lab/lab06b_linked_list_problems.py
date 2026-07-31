from typing import Any, Optional, TYPE_CHECKING
from lab02_sentinal_linked_list import Node, SLList

# %%


def count(linked_list: 'SLList', target: int) -> int:
    """
    Count the number of times a given int occurs in the list.
    """
    occur = 0
    # start from the first actual node (skip sentinel)
    curr_node = linked_list.sentinel.next

    # traverse the entire list
    while curr_node is not None:
        if curr_node.value == target:
            occur += 1
        curr_node = curr_node.next

    return occur


def test_count():
    """Test count function"""
    ll = SLList()
    ll.insert_last(1)
    ll.insert_last(2)
    ll.insert_last(2)
    ll.insert_last(3)
    ll.insert_last(2)

    assert count(ll, 2) == 3
    assert count(ll, 1) == 1
    assert count(ll, 3) == 1
    assert count(ll, 5) == 0

    empty_ll = SLList()
    assert count(empty_ll, 1) == 0

    print("count() tests passed!")


if __name__ == "__main__":
    test_count()

# %%


def get_nth(linked_list: 'SLList', index: int) -> Any:
    """
    Get the data value stored in the node at the given index position.
    Uses C numbering convention (0-indexed).
    """
    # validate index is in valid range
    assert 0 <= index < linked_list.size, f"Index {
        index} out of range [0..{linked_list.size-1}]"

    # start from the first actual node (skip sentinel)
    curr_node = linked_list.sentinel.next

    # traverse to the desired index
    for _ in range(index):
        curr_node = curr_node.next

    return curr_node.value


def test_get_nth():
    """Test get_nth function"""
    ll = SLList()
    ll.insert_last(10)
    ll.insert_last(20)
    ll.insert_last(30)
    ll.insert_last(40)

    assert get_nth(ll, 0) == 10
    assert get_nth(ll, 1) == 20
    assert get_nth(ll, 2) == 30
    assert get_nth(ll, 3) == 40

    try:
        get_nth(ll, 4)
        assert False, "Should have raised assertion error"
    except AssertionError:
        pass

    print("get_nth() tests passed!")


if __name__ == "__main__":
    test_get_nth()

# %%


def delete_list(linked_list: 'SLList') -> None:
    """
    Deallocate all nodes in the list and reset to empty state.
    Sets the sentinel's next pointer to NULL and size to 0.
    """
    # start from the first actual node
    curr_node = linked_list.sentinel.next

    # traverse and delete each node
    while curr_node is not None:
        # save reference to next node before deleting current
        next_node = curr_node.next
        del curr_node
        curr_node = next_node

    # reset the list to empty state
    linked_list.sentinel.next = None
    linked_list.size = 0


def test_delete_list():
    """Test delete_list function"""
    ll = SLList()
    ll.insert_last(1)
    ll.insert_last(2)
    ll.insert_last(3)

    assert ll.size == 3
    delete_list(ll)
    assert ll.size == 0
    assert ll.sentinel.next is None

    # test on already empty list
    delete_list(ll)
    assert ll.size == 0

    print("delete_list() tests passed!")


if __name__ == "__main__":
    test_delete_list()

# %%


def pop(linked_list: 'SLList') -> Any:
    """
    Remove the front node from a non-empty list and return its data.
    This is the inverse of Push/insert_first.
    """
    # ensure list is not empty
    assert linked_list.size > 0, "Cannot pop from empty list"

    # get reference to the first actual node
    first_node = linked_list.sentinel.next

    # save the data to return
    data = first_node.value

    # unlink the first node (advance head pointer)
    linked_list.sentinel.next = first_node.next

    # deallocate the unlinked node
    del first_node

    # decrement size
    linked_list.size -= 1

    return data


def test_pop():
    """Test pop function"""
    ll = SLList()
    ll.insert_last(1)
    ll.insert_last(2)
    ll.insert_last(3)

    assert pop(ll) == 1
    assert ll.size == 2
    assert pop(ll) == 2
    assert ll.size == 1
    assert pop(ll) == 3
    assert ll.size == 0

    try:
        pop(ll)
        assert False, "Should have raised assertion error"
    except AssertionError:
        pass

    print("pop() tests passed!")


if __name__ == "__main__":
    test_pop()

# %%


def insert_nth(linked_list: 'SLList', index: int, data: Any) -> None:
    """
    Insert a new node at any index within the list.
    Similar to Push but works at any position in range [0..length].
    """
    # validate index is in valid range [0..length]
    assert 0 <= index <= linked_list.size, f"Index {
        index} out of range [0..{linked_list.size}]"

    # start from sentinel
    curr_node = linked_list.sentinel

    # traverse to the node just before insertion point
    for _ in range(index):
        curr_node = curr_node.next

    # create new node and insert it
    new_node = Node(data, curr_node.next)
    curr_node.next = new_node

    # increment size
    linked_list.size += 1


def test_insert_nth():
    """Test insert_nth function"""
    ll = SLList()

    insert_nth(ll, 0, 10)
    assert get_nth(ll, 0) == 10
    assert ll.size == 1

    insert_nth(ll, 1, 30)
    assert get_nth(ll, 1) == 30
    assert ll.size == 2

    insert_nth(ll, 1, 20)
    assert get_nth(ll, 0) == 10
    assert get_nth(ll, 1) == 20
    assert get_nth(ll, 2) == 30
    assert ll.size == 3

    insert_nth(ll, 0, 5)
    assert get_nth(ll, 0) == 5

    print("insert_nth() tests passed!")


if __name__ == "__main__":
    test_insert_nth()

# %%


def sorted_insert(linked_list: 'SLList', new_node: 'Node') -> None:
    """
    Insert a node into a sorted list in the correct position.
    The list must be sorted in increasing order.
    """
    # start from sentinel
    curr_node = linked_list.sentinel

    # find the correct position to insert
    while curr_node.next is not None and curr_node.next.value < new_node.value:
        curr_node = curr_node.next

    # insert the node
    new_node.next = curr_node.next
    curr_node.next = new_node

    # increment size
    linked_list.size += 1


def test_sorted_insert():
    """Test sorted_insert function"""
    ll = SLList()
    ll.insert_last(1)
    ll.insert_last(3)
    ll.insert_last(5)

    new_node = Node(4)
    sorted_insert(ll, new_node)

    assert get_nth(ll, 0) == 1
    assert get_nth(ll, 1) == 3
    assert get_nth(ll, 2) == 4
    assert get_nth(ll, 3) == 5
    assert ll.size == 4

    new_node2 = Node(0)
    sorted_insert(ll, new_node2)
    assert get_nth(ll, 0) == 0

    new_node3 = Node(10)
    sorted_insert(ll, new_node3)
    assert get_nth(ll, ll.size - 1) == 10

    print("sorted_insert() tests passed!")


if __name__ == "__main__":
    test_sorted_insert()

# %%


def insert_sort(linked_list: 'SLList') -> None:
    """
    Rearrange the nodes of a list so they are sorted in increasing order.
    Uses SortedInsert() to build a new sorted list.
    """
    if linked_list.size <= 1:
        return

    # create a new sorted list
    if TYPE_CHECKING:
        sorted_list = linked_list.__class__()
    else:
        # import the SLList class dynamically
        sorted_list = type(linked_list)()

    # take each node from original list and insert into sorted list
    while linked_list.sentinel.next is not None:
        # remove first node from original list
        node = linked_list.sentinel.next
        linked_list.sentinel.next = node.next
        linked_list.size -= 1

        # insert into sorted list
        sorted_insert(sorted_list, node)

    # copy sorted list back to original
    linked_list.sentinel.next = sorted_list.sentinel.next
    linked_list.size = sorted_list.size


def test_insert_sort():
    """Test insert_sort function"""
    ll = SLList()
    ll.insert_last(5)
    ll.insert_last(1)
    ll.insert_last(4)
    ll.insert_last(2)
    ll.insert_last(3)

    insert_sort(ll)

    assert get_nth(ll, 0) == 1
    assert get_nth(ll, 1) == 2
    assert get_nth(ll, 2) == 3
    assert get_nth(ll, 3) == 4
    assert get_nth(ll, 4) == 5
    assert ll.size == 5

    # test empty list
    empty_ll = SLList()
    insert_sort(empty_ll)
    assert empty_ll.size == 0

    # test single element
    single = SLList()
    single.insert_last(42)
    insert_sort(single)
    assert single.size == 1
    assert get_nth(single, 0) == 42

    print("insert_sort() tests passed!")


if __name__ == "__main__":
    test_insert_sort()

# %%


def append(list_a: 'SLList', list_b: 'SLList') -> None:
    """
    Append list_b onto the end of list_a, then set list_b to empty.
    """
    # if list_a is empty, just point it to list_b
    if list_a.size == 0:
        list_a.sentinel.next = list_b.sentinel.next
        list_a.size = list_b.size
    else:
        # find the last node of list_a
        curr_node = list_a.sentinel
        while curr_node.next is not None:
            curr_node = curr_node.next

        # attach list_b to the end
        curr_node.next = list_b.sentinel.next
        list_a.size += list_b.size

    # set list_b to empty
    list_b.sentinel.next = None
    list_b.size = 0


def test_append():
    """Test append function"""
    list_a = SLList()
    list_a.insert_last(1)
    list_a.insert_last(2)

    list_b = SLList()
    list_b.insert_last(3)
    list_b.insert_last(4)

    append(list_a, list_b)

    assert list_a.size == 4
    assert list_b.size == 0
    assert get_nth(list_a, 0) == 1
    assert get_nth(list_a, 1) == 2
    assert get_nth(list_a, 2) == 3
    assert get_nth(list_a, 3) == 4

    # Test appending to empty list
    list_c = SLList()
    list_d = SLList()
    list_d.insert_last(5)
    append(list_c, list_d)
    assert list_c.size == 1
    assert get_nth(list_c, 0) == 5

    print("append() tests passed!")


if __name__ == "__main__":
    test_append()

# %%


def front_back_split(source: 'SLList', front: 'SLList', back: 'SLList') -> None:
    """
    Split a list into front and back halves.
    If the length is odd, the extra element goes in the front list.
    """
    # handle short lists
    if source.size < 2:
        front.sentinel.next = source.sentinel.next
        front.size = source.size
        back.sentinel.next = None
        back.size = 0
        return

    # use slow/fast pointer technique
    slow = source.sentinel.next
    fast = source.sentinel.next

    # fast moves 2 steps, slow moves 1 step
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    # slow is now at the last node of front half
    # split the list at this point
    front.sentinel.next = source.sentinel.next
    back.sentinel.next = slow.next
    slow.next = None

    # calculate sizes
    front.size = (source.size + 1) // 2
    back.size = source.size // 2


def test_front_back_split():
    """Test front_back_split function"""
    source = SLList()
    source.insert_last(1)
    source.insert_last(2)
    source.insert_last(3)
    source.insert_last(4)
    source.insert_last(5)

    front = SLList()
    back = SLList()

    front_back_split(source, front, back)

    assert front.size == 3
    assert back.size == 2
    assert get_nth(front, 0) == 1
    assert get_nth(front, 1) == 2
    assert get_nth(front, 2) == 3
    assert get_nth(back, 0) == 4
    assert get_nth(back, 1) == 5

    # test even length
    source2 = SLList()
    for i in range(1, 5):
        source2.insert_last(i)

    front2 = SLList()
    back2 = SLList()
    front_back_split(source2, front2, back2)

    assert front2.size == 2
    assert back2.size == 2

    print("front_back_split() tests passed!")


if __name__ == "__main__":
    test_front_back_split()

# %%


def remove_duplicates(linked_list: 'SLList') -> None:
    """
    Remove duplicate nodes from a sorted list.
    The list should be sorted in increasing order.
    """
    if linked_list.size <= 1:
        return

    curr_node = linked_list.sentinel.next

    while curr_node is not None and curr_node.next is not None:
        # if current value equals next value, remove next node
        if curr_node.value == curr_node.next.value:
            duplicate = curr_node.next
            curr_node.next = duplicate.next
            del duplicate
            linked_list.size -= 1
        else:
            # only advance if no duplicate was removed
            curr_node = curr_node.next


def test_remove_duplicates():
    """Test remove_duplicates function"""
    ll = SLList()
    ll.insert_last(1)
    ll.insert_last(2)
    ll.insert_last(2)
    ll.insert_last(3)
    ll.insert_last(3)
    ll.insert_last(3)
    ll.insert_last(4)

    remove_duplicates(ll)

    assert ll.size == 4
    assert get_nth(ll, 0) == 1
    assert get_nth(ll, 1) == 2
    assert get_nth(ll, 2) == 3
    assert get_nth(ll, 3) == 4

    # test no duplicates
    ll2 = SLList()
    ll2.insert_last(1)
    ll2.insert_last(2)
    ll2.insert_last(3)
    remove_duplicates(ll2)
    assert ll2.size == 3

    print("remove_duplicates() tests passed!")


if __name__ == "__main__":
    test_remove_duplicates()

# %%


def move_node(dest: 'SLList', source: 'SLList') -> None:
    """
    Remove the front node from source and push it onto dest.
    """
    # ensure source is not empty
    assert source.size > 0, "Cannot move node from empty list"

    # get the front node from source
    node = source.sentinel.next

    # unlink it from source
    source.sentinel.next = node.next
    source.size -= 1

    # push it onto dest
    node.next = dest.sentinel.next
    dest.sentinel.next = node
    dest.size += 1


def test_move_node():
    """Test move_node function"""
    dest = SLList()
    dest.insert_last(1)
    dest.insert_last(2)

    source = SLList()
    source.insert_last(3)
    source.insert_last(4)

    move_node(dest, source)

    assert dest.size == 3
    assert source.size == 1
    assert get_nth(dest, 0) == 3
    assert get_nth(dest, 1) == 1
    assert get_nth(dest, 2) == 2
    assert get_nth(source, 0) == 4

    print("move_node() tests passed!")


if __name__ == "__main__":
    test_move_node()

# %%


def alternating_split(source: 'SLList', a: 'SLList', b: 'SLList') -> None:
    """
    Split source list into two sublists with alternating elements.
    Elements at even indices go to 'a', odd indices go to 'b'.
    """
    # clear destination lists
    a.sentinel.next = None
    a.size = 0

    b.sentinel.next = None
    b.size = 0

    is_even = True

    while source.size > 0:
        if is_even:
            move_node(a, source)
        else:
            move_node(b, source)
        is_even = not is_even


def test_alternating_split():
    """Test alternating_split function"""
    source = SLList()
    for i in range(1, 7):
        source.insert_last(i)

    a = SLList()
    b = SLList()

    alternating_split(source, a, b)

    assert source.size == 0
    assert a.size == 3
    assert b.size == 3
    assert get_nth(a, 0) == 5
    assert get_nth(a, 1) == 3
    assert get_nth(a, 2) == 1
    assert get_nth(b, 0) == 6
    assert get_nth(b, 1) == 4
    assert get_nth(b, 2) == 2

    print("alternating_split() tests passed!")


if __name__ == "__main__":
    test_alternating_split()

# %%


def shuffle_merge(a: 'SLList', b: 'SLList') -> 'SLList':
    """
    Merge two lists alternately into a single list.
    Takes nodes alternately from each list.
    """
    # create result list
    result = type(a)()

    # use a pointer to build at the end
    tail = result.sentinel

    while a.size > 0 or b.size > 0:
        # take from 'a' if available
        if a.size > 0:
            node = a.sentinel.next
            a.sentinel.next = node.next
            a.size -= 1

            tail.next = node
            tail = node

        # take from 'b' if available
        if b.size > 0:
            node = b.sentinel.next
            b.sentinel.next = node.next
            b.size -= 1

            tail.next = node
            tail = node

    # terminate the list
    tail.next = None

    # count the size
    curr = result.sentinel.next
    while curr is not None:
        result.size += 1
        curr = curr.next

    return result


def test_shuffle_merge():
    """Test shuffle_merge function"""
    a = SLList()
    a.insert_last(1)
    a.insert_last(3)
    a.insert_last(5)

    b = SLList()
    b.insert_last(2)
    b.insert_last(4)
    b.insert_last(6)

    result = shuffle_merge(a, b)

    assert result.size == 6
    assert a.size == 0
    assert b.size == 0
    assert get_nth(result, 0) == 1
    assert get_nth(result, 1) == 2
    assert get_nth(result, 2) == 3
    assert get_nth(result, 3) == 4
    assert get_nth(result, 4) == 5
    assert get_nth(result, 5) == 6

    print("shuffle_merge() tests passed!")


if __name__ == "__main__":
    test_shuffle_merge()

# %%


def sorted_merge(a: 'SLList', b: 'SLList') -> 'SLList':
    """
    Merge two sorted lists into one sorted list.
    Uses MoveNode to splice nodes together.
    """
    # create result list
    result = type(a)()
    tail = result.sentinel

    while a.size > 0 and b.size > 0:
        # compare front nodes and move the smaller one
        if a.sentinel.next.value <= b.sentinel.next.value:
            node = a.sentinel.next
            a.sentinel.next = node.next
            a.size -= 1
        else:
            node = b.sentinel.next
            b.sentinel.next = node.next
            b.size -= 1

        # append to result
        tail.next = node
        tail = node
        result.size += 1

    # append remaining nodes from whichever list has nodes left
    if a.size > 0:
        tail.next = a.sentinel.next
        result.size += a.size
        a.sentinel.next = None
        a.size = 0
    elif b.size > 0:
        tail.next = b.sentinel.next
        result.size += b.size
        b.sentinel.next = None
        b.size = 0

    return result


def test_sorted_merge():
    """Test sorted_merge function"""
    a = SLList()
    a.insert_last(1)
    a.insert_last(3)
    a.insert_last(5)

    b = SLList()
    b.insert_last(2)
    b.insert_last(4)
    b.insert_last(6)

    result = sorted_merge(a, b)

    assert result.size == 6
    assert a.size == 0
    assert b.size == 0
    assert get_nth(result, 0) == 1
    assert get_nth(result, 1) == 2
    assert get_nth(result, 2) == 3
    assert get_nth(result, 3) == 4
    assert get_nth(result, 4) == 5
    assert get_nth(result, 5) == 6

    print("sorted_merge() tests passed!")


if __name__ == "__main__":
    test_sorted_merge()

# %%


def merge_sort(linked_list: 'SLList') -> None:
    """
    Sort a list using recursive merge sort algorithm.
    Uses FrontBackSplit and SortedMerge.
    """
    # base case: lists of length 0 or 1 are already sorted
    if linked_list.size <= 1:
        return

    # split into front and back halves
    front = type(linked_list)()
    back = type(linked_list)()
    front_back_split(linked_list, front, back)

    # recursively sort both halves
    merge_sort(front)
    merge_sort(back)

    # merge the sorted halves
    sorted_list = sorted_merge(front, back)

    # copy result back to original list
    linked_list.sentinel.next = sorted_list.sentinel.next
    linked_list.size = sorted_list.size


def test_merge_sort():
    """Test merge_sort function"""
    ll = SLList()
    ll.insert_last(5)
    ll.insert_last(2)
    ll.insert_last(8)
    ll.insert_last(1)
    ll.insert_last(9)
    ll.insert_last(3)

    merge_sort(ll)

    assert ll.size == 6
    assert get_nth(ll, 0) == 1
    assert get_nth(ll, 1) == 2
    assert get_nth(ll, 2) == 3
    assert get_nth(ll, 3) == 5
    assert get_nth(ll, 4) == 8
    assert get_nth(ll, 5) == 9

    # test empty list
    empty_ll = SLList()
    merge_sort(empty_ll)
    assert empty_ll.size == 0

    # test single element
    single = SLList()
    single.insert_last(42)
    merge_sort(single)
    assert single.size == 1

    print("merge_sort() tests passed!")


if __name__ == "__main__":
    test_merge_sort()

# %%


def sorted_intersect(a: 'SLList', b: 'SLList') -> 'SLList':
    """
    Create a new list representing the intersection of two sorted lists.
    Uses Push() style building (allocates new nodes).
    """
    # create result list
    result = type(a)()

    # pointers for traversing both lists
    curr_a = a.sentinel.next
    curr_b = b.sentinel.next

    while curr_a is not None and curr_b is not None:
        if curr_a.value == curr_b.value:
            # found a common element
            result.insert_last(curr_a.value)
            curr_a = curr_a.next
            curr_b = curr_b.next
        elif curr_a.value < curr_b.value:
            curr_a = curr_a.next
        else:
            curr_b = curr_b.next

    return result


def test_sorted_intersect():
    """Test sorted_intersect function"""
    a = SLList()
    a.insert_last(1)
    a.insert_last(2)
    a.insert_last(3)
    a.insert_last(4)
    a.insert_last(5)

    b = SLList()
    b.insert_last(2)
    b.insert_last(4)
    b.insert_last(6)

    result = sorted_intersect(a, b)

    assert result.size == 2
    assert get_nth(result, 0) == 2
    assert get_nth(result, 1) == 4

    # test no intersection
    c = SLList()
    c.insert_last(1)
    c.insert_last(3)

    d = SLList()
    d.insert_last(2)
    d.insert_last(4)

    result2 = sorted_intersect(c, d)
    assert result2.size == 0

    print("sorted_intersect() tests passed!")


if __name__ == "__main__":
    test_sorted_intersect()

# %%


def reverse(linked_list: 'SLList') -> None:
    """
    Reverse a list by rearranging all .next pointers.
    Uses the "Push" strategy - iteratively move nodes to front.
    """
    if linked_list.size <= 1:
        return

    # build result by moving nodes to front
    result = None

    while linked_list.sentinel.next is not None:
        # remove front node
        node = linked_list.sentinel.next
        linked_list.sentinel.next = node.next

        # push onto result (at front)
        node.next = result
        result = node

    # update the list
    linked_list.sentinel.next = result


def test_reverse():
    """Test reverse function"""
    ll = SLList()
    ll.insert_last(1)
    ll.insert_last(2)
    ll.insert_last(3)
    ll.insert_last(4)

    reverse(ll)

    assert ll.size == 4
    assert get_nth(ll, 0) == 4
    assert get_nth(ll, 1) == 3
    assert get_nth(ll, 2) == 2
    assert get_nth(ll, 3) == 1

    # test single element
    single = SLList()
    single.insert_last(5)
    reverse(single)
    assert single.size == 1
    assert get_nth(single, 0) == 5

    # test empty list
    empty = SLList()
    reverse(empty)
    assert empty.size == 0

    print("reverse() tests passed!")


if __name__ == "__main__":
    test_reverse()

# %%


def recursive_reverse(linked_list: 'SLList') -> None:
    """
    Recursively reverse a list in one pass.
    """
    def reverse_helper(node: Optional['Node']) -> Optional['Node']:
        """
        Recursively reverse the list starting at node.
        Returns the new head of the reversed list.
        """

        # base case: empty list or single node
        if node is None or node.next is None:
            return node

        # recursively reverse the rest of the list
        new_head = reverse_helper(node.next)

        # reverse the link
        node.next.next = node
        node.next = None

        return new_head

    if linked_list.size <= 1:
        return

    # reverse starting from first actual node
    new_head = reverse_helper(linked_list.sentinel.next)
    linked_list.sentinel.next = new_head


def test_recursive_reverse():
    """Test recursive_reverse function"""
    ll = SLList()
    ll.insert_last(1)
    ll.insert_last(2)
    ll.insert_last(3)
    ll.insert_last(4)

    recursive_reverse(ll)

    assert ll.size == 4
    assert get_nth(ll, 0) == 4
    assert get_nth(ll, 1) == 3
    assert get_nth(ll, 2) == 2
    assert get_nth(ll, 3) == 1

    # test single element
    single = SLList()
    single.insert_last(5)
    recursive_reverse(single)
    assert single.size == 1
    assert get_nth(single, 0) == 5

    # test empty list
    empty = SLList()
    recursive_reverse(empty)
    assert empty.size == 0

    print("recursive_reverse() tests passed!")


if __name__ == "__main__":
    test_recursive_reverse()
