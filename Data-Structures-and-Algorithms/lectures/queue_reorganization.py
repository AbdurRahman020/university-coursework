# Queue Reorganization

class ListNode:
    """Node for singly linked list"""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorganize_queue(head):
    """
    Reorganizes a queue of 2n students in O(n) time and O(1) space.

    Algorithm:
    1. Find the middle of the list (first n elements)
    2. Reverse the second half in place
    3. Interleave the two halves

    Time Complexity: O(n) - three linear passes
    Space Complexity: O(1) - only pointer manipulation

    Args:
        head: Head of the linked list with 2n students

    Returns:
        Head of the reorganized list
    """
    if not head or not head.next:
        return head

    # step 1: find middle using two-pointer technique (Floyd's algorithm)
    # slow moves 1 step, fast moves 2 steps
    # when fast reaches end, slow is at middle
    slow = head
    fast = head
    prev_slow = None

    while fast and fast.next:
        prev_slow = slow
        slow = slow.next
        fast = fast.next.next

    # split the list into two halves
    second_half = slow
    prev_slow.next = None  # end first half

    # step 2: Reverse the second half in place
    reversed_second = reverse_list(second_half)

    # step 3: Interleave the two halves
    return interleave(head, reversed_second)


def reverse_list(head):
    """
    Reverses a singly linked list in place.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Algorithm (CLRS style):
        prev ← NIL
        curr ← head
        while curr ≠ NIL
            next ← curr.next
            curr.next ← prev
            prev ← curr
            curr ← next
        return prev
    """
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


def interleave(first, second):
    """
    Interleaves two linked lists by alternating nodes.

    Time Complexity: O(n)
    Space Complexity: O(1)

    Algorithm:
        dummy ← new node
        curr ← dummy
        while first ≠ NIL and second ≠ NIL
            curr.next ← first
            first ← first.next
            curr ← curr.next

            curr.next ← second
            second ← second.next
            curr ← curr.next
        return dummy.next
    """
    dummy = ListNode(0)
    curr = dummy

    while first and second:
        # take one from first half
        curr.next = first
        first = first.next
        curr = curr.next

        # take one from second half
        curr.next = second
        second = second.next
        curr = curr.next

    # append remaining nodes (shouldn't happen with 2n students)
    if first:
        curr.next = first
    if second:
        curr.next = second

    return dummy.next


# helper functions for testing
def create_list(values):
    """Creates a linked list from a list of values"""
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def list_to_array(head):
    """Converts a linked list to an array"""
    result = []
    curr = head

    while curr:
        result.append(curr.val)
        curr = curr.next

    return result


def print_list(head, label="List"):
    """Prints a linked list"""
    arr = list_to_array(head)
    print(f"{label}: {' → '.join(map(str, arr))}")


# test Cases for Problem 1
print("PROBLEM: QUEUE REORGANIZATION\n")

print("Test Case 1: 6 students (A, B, C, D, E, F)")

values = ['A', 'B', 'C', 'D', 'E', 'F']
head = create_list(values)
print_list(head, "Original queue")

print("  First half: A → B → C")
print("  Second half: D → E → F")
print("  Reversed: F → E → D")

head = reorganize_queue(head)
print_list(head, "Reorganized")
expected = ['A', 'F', 'B', 'E', 'C', 'D']
actual = list_to_array(head)

print(f"Expected: {expected}")
print(f"Result: {'PASS' if actual == expected else 'FAIL'}\n")

print("Test Case 2: 10 students (1 to 10)")

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
head = create_list(values)
print_list(head, "Original queue")

print("  First half: 1 → 2 → 3 → 4 → 5")
print("  Second half: 6 → 7 → 8 → 9 → 10")
print("  Reversed: 10 → 9 → 8 → 7 → 6")

head = reorganize_queue(head)
print_list(head, "Reorganized")
expected = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
actual = list_to_array(head)

print(f"Expected: {expected}")
print(f"Result: {'PASS' if actual == expected else 'FAIL'}\n")


print("Test Case 3: 4 students (1 to 4)")

values = [1, 2, 3, 4]
head = create_list(values)
print_list(head, "Original queue")
head = reorganize_queue(head)
print_list(head, "Reorganized")
expected = [1, 4, 2, 3]
actual = list_to_array(head)

print(f"Expected: {expected}")
print(f"Result: {'PASS' if actual == expected else 'FAIL'}\n")

print("""
\nCOMPLEXITY ANALYSIS - Queue Reorganization:
-------------------------------------------
Time Complexity: O(n)
  - Finding middle: O(n) using two-pointer technique
  - Reversing second half: O(n)
  - Interleaving: O(n)
  - Total: O(n) + O(n) + O(n) = O(n)

Space Complexity: O(1)
  - Only constant number of pointers used
  - No auxiliary data structures
  - Modification done in place
""")
