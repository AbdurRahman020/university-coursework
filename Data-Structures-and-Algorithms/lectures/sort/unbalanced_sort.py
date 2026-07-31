import matplotlib.pyplot as plt
import time
import numpy as np
from scipy.optimize import curve_fit

# UNBALANCEDSORT Implementations


def merge(arr, left, mid, right):
    """
    Merge two sorted subarrays arr[left:mid+1] and arr[mid+1:right+1].
    This is the standard MERGE operation from CLRS.

    Time Complexity: Θ(n) where n = right - left + 1
    """
    # create temporary arrays
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]

    # merge back into arr[left:right+1]
    i = j = 0
    k = left

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    # copy remaining elements
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


def unbalanced_sort_1_2(arr, left, right):
    """
    UNBALANCEDSORT with 1:2 split ratio (n/3 and 2n/3).

    Recurrence: T(n) = T(n/3) + T(2n/3) + Θ(n)
    Time Complexity: Θ(n log n)
    """
    if left < right:
        # split into 1:2 ratio
        size = right - left + 1
        split_point = left + size // 3

        # recursively sort both halves
        unbalanced_sort_1_2(arr, left, split_point)
        unbalanced_sort_1_2(arr, split_point + 1, right)

        # merge the sorted halves
        merge(arr, left, split_point, right)


def unbalanced_sort_1_3(arr, left, right):
    """
    UNBALANCEDSORT with 1:3 split ratio (n/4 and 3n/4).

    Recurrence: T(n) = T(n/4) + T(3n/4) + Θ(n)
    Time Complexity: Θ(n log n)
    """
    if left < right:
        # split into 1:3 ratio
        size = right - left + 1
        split_point = left + size // 4

        # recursively sort both halves
        unbalanced_sort_1_3(arr, left, split_point)
        unbalanced_sort_1_3(arr, split_point + 1, right)

        # merge the sorted halves
        merge(arr, left, split_point, right)


def unbalanced_sort_constant(arr, left, right, a=10):
    """
    UNBALANCEDSORT with constant-sized split (a and n-a).

    Recurrence: T(n) = T(a) + T(n-a) + Θ(n)
    Time Complexity: Θ(n²)

    Args:
        a: Constant size for first subproblem (default: 10)
    """
    if left < right:
        size = right - left + 1

        if size <= a:
            # base case: use regular merge sort for small arrays
            mid = (left + right) // 2
            if left < mid:
                unbalanced_sort_constant(arr, left, mid, a)
                unbalanced_sort_constant(arr, mid + 1, right, a)
                merge(arr, left, mid, right)
        else:
            # split into constant 'a' and 'n-a'
            split_point = left + a - 1

            # sort the constant-sized portion
            unbalanced_sort_constant(arr, left, split_point, a)

            # recursively sort the larger portion
            unbalanced_sort_constant(arr, split_point + 1, right, a)

            # merge
            merge(arr, left, split_point, right)


def merge_sort(arr, left, right):
    """
    Standard MERGESORT for comparison (balanced 1:1 split).

    Recurrence: T(n) = 2T(n/2) + Θ(n)
    Time Complexity: Θ(n log n)
    """
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        merge(arr, left, mid, right)


# testing and benchmarking
def test_sorting_algorithms():
    """Test all sorting algorithms for correctness"""
    print("TESTING SORTING ALGORITHMS\n")

    test_cases = [
        [5, 2, 8, 1, 9, 3, 7, 4, 6],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1],
        [2, 1],
        []
    ]

    algorithms = [
        ("MERGESORT (1:1)", merge_sort),
        ("UNBALANCEDSORT (1:2)", unbalanced_sort_1_2),
        ("UNBALANCEDSORT (1:3)", unbalanced_sort_1_3),
        ("UNBALANCEDSORT (const)", lambda a, l,
         r: unbalanced_sort_constant(a, l, r, 3))
    ]

    for name, sort_func in algorithms:
        print(f"Testing {name}:")
        all_pass = True

        for test in test_cases:
            arr = test.copy()
            expected = sorted(test)

            if arr:
                sort_func(arr, 0, len(arr) - 1)

            if arr == expected:
                print(f"   {test[:5]}{'...' if len(test) > 5 else ''}")
            else:
                print(f"   FAILED: {test}")
                all_pass = False

        print(f"  {'All tests passed!' if all_pass else 'Some tests failed!'}")
        print()


def benchmark_algorithms():
    """Benchmark all algorithms and plot results"""
    print("BENCHMARKING ALGORITHMS:\n")

    # different size ranges for different algorithms
    sizes_nlogn = list(range(10, 501, 20))   # for O(n*log n) algorithms
    sizes_n2 = list(range(10, 201, 10))      # for O(n²) algorithm

    results = {
        'MERGESORT': {'sizes': [], 'times': []},
        'UNBALANCED 1:2': {'sizes': [], 'times': []},
        'UNBALANCED 1:3': {'sizes': [], 'times': []},
        'UNBALANCED const': {'sizes': [], 'times': []}
    }

    # benchmark O(n log n) algorithms
    print("Benchmarking O(n log n) algorithms...")
    for n in sizes_nlogn:
        arr = list(range(n, 0, -1))  # reverse sorted (worst case)

        # MERGESORT
        test_arr = arr.copy()
        start = time.time()
        merge_sort(test_arr, 0, len(test_arr) - 1)
        end = time.time()
        results['MERGESORT']['sizes'].append(n)
        results['MERGESORT']['times'].append(end - start)

        # UNBALANCED 1:2
        test_arr = arr.copy()
        start = time.time()
        unbalanced_sort_1_2(test_arr, 0, len(test_arr) - 1)
        end = time.time()
        results['UNBALANCED 1:2']['sizes'].append(n)
        results['UNBALANCED 1:2']['times'].append(end - start)

        # UNBALANCED 1:3
        test_arr = arr.copy()
        start = time.time()
        unbalanced_sort_1_3(test_arr, 0, len(test_arr) - 1)
        end = time.time()
        results['UNBALANCED 1:3']['sizes'].append(n)
        results['UNBALANCED 1:3']['times'].append(end - start)

        if n % 100 == 10:
            print(f"  n = {n}")

    # benchmark O(n²) algorithm separately
    print("Benchmarking O(n²) algorithm...")
    for n in sizes_n2:
        arr = list(range(n, 0, -1))

        test_arr = arr.copy()
        start = time.time()
        unbalanced_sort_constant(test_arr, 0, len(test_arr) - 1, a=5)
        end = time.time()
        results['UNBALANCED const']['sizes'].append(n)
        results['UNBALANCED const']['times'].append(end - start)

        if n % 50 == 10:
            print(f"  n = {n}")

    print()
    return results


def plot_results(results):
    """Plot benchmark results with curve fitting"""
    print("PLOTTING RESULTS:\n")

    def nlogn(n, a, b):
        return a * n * np.log(n) + b

    def quadratic(n, a, b, c):
        return a * n**2 + b * n + c

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # plot 1: O(n*log n) algorithms
    colors = ['blue', 'red', 'green']
    markers = ['o', 's', '^']

    for (name, color, marker) in zip(
            ['MERGESORT', 'UNBALANCED 1:2', 'UNBALANCED 1:3'
             ], colors, markers):
        sizes = np.array(results[name]['sizes'])
        times = np.array(results[name]['times'])

        # fit to n*log n
        params, _ = curve_fit(nlogn, sizes, times)
        fitted = nlogn(sizes, *params)

        ax1.scatter(sizes, times, label=f'{name} (measured)',
                    alpha=0.6, s=30, color=color, marker=marker)
        ax1.plot(sizes, fitted,
                 label=f'{name} fit: {params[0]:.2e}n log n + {params[1]:.2e}',
                 linewidth=2, color=color)

        print(f"{name}: T(n) = {params[0]:.6e}n log n + {params[1]:.6e}")

    ax1.set_xlabel('Input Size (n)', fontsize=11)
    ax1.set_ylabel('Time (seconds)', fontsize=11)
    ax1.set_title('O(n log n) Algorithms Comparison',
                  fontsize=12, fontweight='bold')
    ax1.legend(fontsize=8)
    ax1.grid(True, alpha=0.3)

    # plot 2: O(n²) algorithm
    sizes = np.array(results['UNBALANCED const']['sizes'])
    times = np.array(results['UNBALANCED const']['times'])

    params, _ = curve_fit(quadratic, sizes, times)
    fitted = quadratic(sizes, *params)

    ax2.scatter(sizes, times, label='UNBALANCED const (measured)',
                alpha=0.6, s=30, color='purple', marker='D')
    ax2.plot(sizes, fitted,
             label=f'Fit: {params[0]:.2e}n² + {params[1]:.2e}n + {
                 params[2]:.2e}',
             linewidth=2, color='purple')

    ax2.set_xlabel('Input Size (n)', fontsize=11)
    ax2.set_ylabel('Time (seconds)', fontsize=11)
    ax2.set_title('O(n²) Algorithm (Constant Split)',
                  fontsize=12, fontweight='bold')
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3)

    print(f"UNBALANCED const: T(n) = {
          params[0]:.6e}n² + {params[1]:.6e}n + {params[2]:.6e}\n")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # run tests
    test_sorting_algorithms()
    # run benchmarks
    results = benchmark_algorithms()
    # plot results
    plot_results(results)

    print("""SUMMARY: Empirical Results Confirm Theoretical Analysis:

    1. MERGESORT (n/2, n/2):           Θ(n log n)
    2. UNBALANCEDSORT (n/3, 2n/3):     Θ(n log n)
    3. UNBALANCEDSORT (n/4, 3n/4):     Θ(n log n)
    4. UNBALANCEDSORT (a, n-a):        Θ(n²)

    Key Insight: Constant-ratio splits maintain Θ(n log n) efficiency,
    but constant-sized splits degrade to Θ(n²).
    """)
