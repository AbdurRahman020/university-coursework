def counting_sort(A, k):
    """
    Counting Sort algorithm from CLRS.

    Args:
        A: Input array (1-indexed conceptually, but 0-indexed in Python)
        k: Maximum value in array A (assumes elements are in range 0 to k)

    Returns:
        B: Sorted array
    """
    n = len(A)

    # step 1: initialize arrays B and C
    # B will store the sorted output (1-indexed behavior simulated)
    B = [0] * n
    # C will store counts (0 to k inclusive)
    C = [0] * (k + 1)

    # step 2-3: initialize C to all zeros (already done above)

    # step 4-5: count occurrences of each element
    for j in range(n):
        C[A[j]] += 1
    # now C[i] contains the number of elements equal to i

    # step 7-8: convert counts to cumulative counts
    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]
    # now C[i] contains the number of elements less than or equal to i

    # step 11-13: build the sorted array B
    # process from end to maintain stability
    for j in range(n - 1, -1, -1):
        # -1 for 0-indexing
        B[C[A[j]] - 1] = A[j]
        # decrement to handle duplicates
        C[A[j]] -= 1

    return B
