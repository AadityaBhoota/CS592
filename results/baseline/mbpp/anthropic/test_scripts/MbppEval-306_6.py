def max_sum_increasing_subseq(a, n, index, k):
    if index >= n or k >= n:
        return 0

    # Include the kth element
    include_kth = a[k] + max_sum_increasing_subseq(a, n, index, k + 1)

    # Exclude the kth element
    exclude_kth = max_sum_increasing_subseq(a, n, index, k + 1)

    # Find the maximum sum increasing subsequence
    max_sum = max(include_kth, exclude_kth)

    # If the current index is less than the kth index, update the maximum sum
    if index < k:
        max_sum = max(max_sum, a[index] + max_sum_increasing_subseq(a, n, index + 1, k))

    return max_sum

def check(candidate):
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71

check(max_sum_increasing_subseq)