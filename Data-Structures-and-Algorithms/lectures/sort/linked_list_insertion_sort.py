import matplotlib.pyplot as plt
import time
import numpy as np
from scipy.optimize import curve_fit

# Question 2: Node and LinkedList Implementation


class Node:
    """Node class for singly linked list"""

    def __init__(self, data, nextNode=None):
        self.data = data
        self.next = nextNode


class LinkedList:
    """Singly linked list implementation with magic methods"""

    def __init__(self, data_list=None):
        self.head = None
        self._length = 0

        if data_list:
            self.head = Node(data_list[0])
            curr_node = self.head
            self._length = 1

            for data in data_list[1:]:
                curr_node.next = Node(data)
                curr_node = curr_node.next
                self._length += 1

    def __len__(self):
        """Return the length of the linked list"""
        return self._length

    def __getitem__(self, index):
        """Get item at given index"""
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")

        curr_node = self.head

        for _ in range(index):
            curr_node = curr_node.next

        return curr_node.data

    def __setitem__(self, index, value):
        """Set item at given index"""
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range")

        curr_node = self.head
        for _ in range(index):
            curr_node = curr_node.next

        curr_node.data = value

    def __str__(self):
        """String representation of the linked list"""
        result = []
        curr_node = self.head

        while curr_node is not None:
            result.append(str(curr_node.data))
            curr_node = curr_node.next

        return " -> ".join(result)


# insertion sort algorithm (from CLRS)

def insertionSort(A):
    """
    Insertion sort algorithm that works on both LinkedList and Python list.
    Based on CLRS Algorithm (Chapter 2).
    """
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1

        while i > -1 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1

        A[i + 1] = key


# testing the LinkedList and insertionSort

print("QUESTION 2: Testing LinkedList with Insertion Sort\n")

test_list = LinkedList([5, 2, 8, 1, 9, 3])
print("Before sorting:", test_list)
insertionSort(test_list)
print("After sorting:", test_list)
print()


# Question 3: Worst Case Analysis on LinkedList

print("\nQUESTION 3: Analyzing Worst Case on LinkedList\n")

sizes_ll = []
times_ll = []

print("Running experiments on LinkedList (reverse sorted)...")
for n in range(10, 201, 10):
    reverse_sorted = list(range(n, 0, -1))
    ll = LinkedList(reverse_sorted)

    start = time.time()
    insertionSort(ll)
    end = time.time()

    sizes_ll.append(n)
    times_ll.append(end - start)
    print(f"n = {n:3d}, time = {end - start:.6f} seconds")

print()


# Question 4: Worst Case Analysis on Python List

print("\nQUESTION 4: Analyzing Worst Case on Python List\n")

sizes_list = []
times_list = []

print("Running experiments on Python List (reverse sorted)...")
for n in range(10, 1001, 20):
    reverse_sorted = list(range(n, 0, -1))

    start = time.time()
    insertionSort(reverse_sorted)
    end = time.time()

    sizes_list.append(n)
    times_list.append(end - start)
    if n % 100 == 10:  # print every 5th measurement
        print(f"n = {n:4d}, time = {end - start:.6f} seconds")

print()


# curve fitting
print("CURVE FITTING RESULTS")


def cubic(n, a, b, c, d):
    """Cubic function: T(n) = an³ + bn² + cn + d"""
    return a * n**3 + b * n**2 + c * n + d


def quadratic(n, a, b, c):
    """Quadratic function: T(n) = an² + bn + c"""
    return a * n**2 + b * n + c


# fit LinkedList data to cubic
params_ll, _ = curve_fit(cubic, sizes_ll, times_ll)
n_fit_ll = np.linspace(10, 200, 100)
times_fit_ll = cubic(n_fit_ll, *params_ll)

print("LinkedList (Cubic Fit):")
print(f"  T(n) = {params_ll[0]:.6e}n³ + {params_ll[1]:.6e}n² + "
      f"{params_ll[2]:.6e}n + {params_ll[3]:.6e}\n")

# fit Python List data to quadratic
params_list, _ = curve_fit(quadratic, sizes_list, times_list)
n_fit_list = np.linspace(10, 1000, 100)
times_fit_list = quadratic(n_fit_list, *params_list)

print("Python List (Quadratic Fit):")
print(f"  T(n) = {params_list[0]:.6e}n² + {params_list[1]:.6e}n + "
      f"{params_list[2]:.6e}\n")


# plotting Results
plt.figure(figsize=(12, 7))

# LinkedList plot
plt.scatter(sizes_ll, times_ll, label='LinkedList (measured)',
            alpha=0.6, s=50, color='blue', marker='o')
plt.plot(n_fit_ll, times_fit_ll,
         label=f'LinkedList fit: {
             params_ll[0]:.2e}n³ + {params_ll[1]:.2e}n² + '
         f'{params_ll[2]:.2e}n + {params_ll[3]:.2e}',
         linewidth=2.5, color='darkblue')

# python List plot
plt.scatter(sizes_list, times_list,
            label='Python List (measured)',
            alpha=0.6, s=50, color='red', marker='s')
plt.plot(n_fit_list, times_fit_list,
         label=f'Python List fit: {
             params_list[0]:.2e}n² + {params_list[1]:.2e}n + '
         f'{params_list[2]:.2e}',
         linewidth=2.5, color='darkred')

plt.xlabel('Input Size (n)', fontsize=12)
plt.ylabel('Time (seconds)', fontsize=12)
plt.title('Insertion Sort Worst Case: LinkedList vs Python List\n'
          '(Reverse Sorted Input)', fontsize=14, fontweight='bold')

plt.legend(fontsize=10, loc='upper left')
plt.grid(True, alpha=0.3, linestyle='--')
plt.tight_layout()
plt.show()

print("\nQUESTION 5: Theoretical Analysis")
print("""
From CLRS, the worst-case running time of INSERTION-SORT is Θ(n²).

For a Python List (array):
- getting/setting an element: O(1)
- the while loop runs O(j) times for position j
- total: sum from j=1 to n-1 is j = n(n-1)/2 = Θ(n²)
- our empirical result matches: O(n²)

For a LinkedList:
- Getting/setting an element at index i: O(i) (need to traverse)
- For position j, we do O(j) comparisons, each taking O(j) time to access
- Total: sum from j=1 to n-1 is j² = n(n-1)(2n-1)/6 = Θ(n³)
- Our empirical result matches: O(n³)

Conclusion: The LinkedList implementation is significantly slower
(O(n³) vs O(n²)) due to the O(n) cost of random access in linked lists.
""")
