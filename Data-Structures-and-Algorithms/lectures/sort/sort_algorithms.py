from typing import List

# %% Bubble Sort


def bubble_sort(arr: List) -> List:
    n = len(arr)
    # base case: if the array has only one element, it's already sorted
    if n == 1:
        return arr

    # iterate through the array
    for i in range(n):
        # last i elements are already in place, so no need to check them
        for j in range(0, n-i-1):
            # swap if the element found is greater than the next element
            if arr[j] >= arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


if __name__ == '__main__':
    test_cases = [
        ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
        ([3, 0, 2, 5, -1, 4, 1], [-1, 0, 1, 2, 3, 4, 5]),
        ([1], [1]),
        ([], []),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # already sorted
        ([5, 5, 5, 5], [5, 5, 5, 5])         # all elements the same
    ]

    for arr, expected in test_cases:
        result = bubble_sort(arr)
        assert result == expected, f'For {
            arr}, expected {expected} but got {result}'

    print("All test cases passed!")

# %% Merge Sort


def merge_sort(arr):
    n = len(arr)

    # base case: if the array has only one element, it's already sorted
    if n <= 1:
        return arr

    # divide the array into two halves
    mid = n // 2

    # recursively sort the left and right halves
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    # merge the sorted halves
    return merge(left_arr, right_arr)


def merge(left_arr, right_arr):
    merged_arr = []
    i = j = 0
    m, n = len(left_arr), len(right_arr)

    # merge the two sorted arrays into a single sorted array
    while i < m and j < n:
        if left_arr[i] <= right_arr[j]:
            merged_arr.append(left_arr[i])
            i += 1
        else:
            merged_arr.append(right_arr[j])
            j += 1

    # append remaining elements
    merged_arr.extend(left_arr[i:])
    merged_arr.extend(right_arr[j:])

    return merged_arr


if __name__ == '__main__':
    test_cases = [
        ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
        ([3, 0, 2, 5, -1, 4, 1], [-1, 0, 1, 2, 3, 4, 5]),
        ([1], [1]),
        ([], []),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 5, 5, 5], [5, 5, 5, 5]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([0.1, 0.5, 0.2, 0.4], [0.1, 0.2, 0.4, 0.5]),
        ([2, 1], [1, 2]),
        ([1, 2], [2, 1]),
    ]

    passed_count = failed_count = 0

    for arr, expected in test_cases:
        result = merge_sort(arr)
        if result == expected:
            passed_count += 1
        else:
            failed_count += 1
            print(f'FAIL: For {arr}, expected {expected} but got {result}')

    print(f"\nTests passed: {passed_count}")
    print(f"Tests failed: {failed_count}")

# %% Quick Sort


def partition(arr: List[int], left: int, right: int) -> int:
    # select pivot element (using middle element)
    mid = left + (right - left) // 2
    pivot_value = arr[mid]

    # move pivot element to end
    arr[mid], arr[right] = arr[right], arr[mid]
    store_index = left

    # partitioning
    for i in range(left, right):
        if arr[i] < pivot_value:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1

    # move pivot element to its final place
    arr[right], arr[store_index] = arr[store_index], arr[right]

    return store_index


def quicksort(arr: List[int], left: int, right: int) -> None:
    if left < right:
        # partitioning index
        pivot = partition(arr, left, right)

        # recursively sort elements before and after partition
        quicksort(arr, left, pivot - 1)
        quicksort(arr, pivot + 1, right)


if __name__ == '__main__':
    test_cases = [
        ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),     # regular unsorted
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),     # already sorted
        ([4, 3, 2, 1], [1, 2, 3, 4]),           # reverse order
        ([5, 5, 5, 5], [5, 5, 5, 5]),           # all elements the same
        # add a failing test case for demonstration
        ([3, 2, 1], [1, 2, 3]),                 # should pass
        # should fail to check the incorrect case
        ([2, 1], [2, 1]),
    ]

    passed_count = failed_count = 0

    for arr, expected in test_cases:
        # copy original array for testing
        original_arr = arr.copy()
        quicksort(arr, 0, len(arr) - 1)
        if arr == expected:
            passed_count += 1
        else:
            failed_count += 1
            print(f'FAIL: For {original_arr}, expected {
                  expected} but got {arr}')

    print(f"\nTests passed: {passed_count}")
    print(f"Tests failed: {failed_count}")

# %% Selection Sort


def selection_sort(arr: List) -> List:
    n = len(arr)

    # traverse through all elements of the array
    for i in range(n):
        # assume the current index as the minimum
        min_index = i
        # check for the minimum element in the unsorted part of the array
        for j in range(i+1, n):
            # update the minimum index if a smaller element is found
            if arr[j] < arr[min_index]:
                min_index = j

        # swap the minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


if __name__ == '__main__':
    test_cases = [
        ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
        ([3, 0, 2, 5, -1, 4, 1], [-1, 0, 1, 2, 3, 4, 5]),
        ([1], [1]),
        ([], []),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),          # already sorted
        ([5, 5, 5, 5], [5, 5, 5, 5]),                # all elements the same
        ([10, 9, 8, 7, 6, 5], [5, 6, 7, 8, 9, 10]),  # reverse order
        # mixed positive and negative
        ([1, -2, 0, 3, -1], [-2, -1, 0, 1, 3]),
        ([2, 2, 2, 2, 2], [2, 2, 2, 2, 2])           # all same elements
    ]

    for arr, expected in test_cases:
        result = selection_sort(arr)
        assert result == expected, f'For {
            arr}, expected {expected} but got {result}'

    print("All test cases passed!")

# %% Insertion Sort


def insertion_sort(arr: List) -> List:
    n = len(arr)
    # base case: if the array has only one element, it's already sorted
    if n == 1:
        return arr

    # iterate through the array starting from the second element
    for i in range(1, n):
        # store the current element as the key
        key = arr[i]
        # initialize j to the index before i
        j = i - 1
        # move elements of arr[0..i-1], that are greater than key, to one
        # position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        # insert the key into its correct position in sorted part of the array
        arr[j+1] = key

    return arr


if __name__ == '__main__':
    test_cases = [
        ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
        ([3, 0, 2, 5, -1, 4, 1], [-1, 0, 1, 2, 3, 4, 5]),
        ([1], [1]),                                      # single element
        ([], []),                                        # empty array
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),              # already sorted
        # all elements the same
        ([5, 5, 5, 5], [5, 5, 5, 5]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),                    # reverse order
    ]

    passed_count = failed_count = 0

    for arr, expected in test_cases:
        result = insertion_sort(arr)
        if result == expected:
            passed_count += 1
        else:
            failed_count += 1
            print(f'FAIL: For {arr}, expected {expected} but got {result}')

    print(f"\nTests passed: {passed_count}")
    print(f"Tests failed: {failed_count}")

# %% Bucket Sort


def bucket_sort(arr: List) -> List:
    n = len(arr)

    # create empty buckets
    buckets = [[] for _ in range(n)]

    # distribute elements into buckets
    for num in arr:
        # calculate the index of the bucket for the current element
        bucket_index = int(n * num)
        # append the element to the corresponding bucket
        buckets[bucket_index].append(num)

    # sort each bucket using an auxiliary sorting algorithm (insertion sort)
    for bucket in buckets:
        insertion_sort(bucket)

    # concatenate sorted buckets to form the final sorted array
    i = 0
    for bucket in buckets:
        for num in bucket:
            arr[i] = num
            i += 1

    return arr


if __name__ == '__main__':
    test_cases = [
        ([0.5, 0.1, 0.4, 0.3, 0.2], [0.1, 0.2, 0.3, 0.4, 0.5]),
        ([0.9, 0.7, 0.2, 0.1, 0.8], [0.1, 0.2, 0.7, 0.8, 0.9]),
        ([0.5], [0.5]),                                        # single element
        ([], []),                                              # empty array
        ([0.99, 0.01, 0.5, 0.25], [0.01, 0.25, 0.5, 0.99]),    # mixed elements
        # all elements the same
        ([0.1, 0.1, 0.1], [0.1, 0.1, 0.1]),
    ]

    for arr, expected in test_cases:
        result = bucket_sort(arr)
        assert result == expected, f'For {
            arr}, expected {expected} but got {result}'

    print("All test cases passed!")
