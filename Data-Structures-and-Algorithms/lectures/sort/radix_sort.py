def counting_sort_for_radix(arr, digit_position):
    """
    Modified counting sort that sorts based on a specific digit position.
    This version is STABLE - maintains relative order of equal elements.

    Args:
        arr: Input array
        digit_position: Which digit to sort by (0 = least significant)

    Returns:
        Sorted array based on the specified digit
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # digits 0-9

    # count occurrences of each digit at the given position
    for i in range(n):
        digit = (arr[i] // (10 ** digit_position)) % 10
        count[digit] += 1

    # convert to cumulative counts
    for i in range(1, 10):
        count[i] += count[i - 1]

    # build output array (going backwards for stability)
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // (10 ** digit_position)) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    return output


def radix_sort(arr):
    """
    Radix Sort using Counting Sort as the stable sort.
    Sorts from least significant digit (LSD) to most significant digit (MSD).

    Args:
        arr: Input array of non-negative integers

    Returns:
        Sorted array
    """
    if not arr:
        return arr

    # find the maximum number to determine number of digits (d)
    max_num = max(arr)
    d = len(str(max_num))  # number of digits

    # sort by each digit, starting from least significant (i = 0)
    for digit_position in range(d):
        arr = counting_sort_for_radix(arr, digit_position)
        print(f"After sorting digit {digit_position + 1}: {arr}")

    return arr


def radix_sort_quiet(arr):
    """Radix sort without printing intermediate steps."""
    if not arr:
        return arr

    max_num = max(arr)
    d = len(str(max_num))

    for digit_position in range(d):
        arr = counting_sort_for_radix(arr, digit_position)

    return arr
