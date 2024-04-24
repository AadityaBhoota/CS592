def max_sum_increasing_subseq(a, n, index, k):
    """
    Find the maximum sum of increasing subsequence from prefix until ith index
    and also including a given kth element which is after i, i.e., k > i.
    """
    if index >= n or k >= n:
        return 0

    # Include the current element
    include = a[index] + max_sum_increasing_subseq(a, n, index + 1, k)

    # Exclude the current element
    exclude = max_sum_increasing_subseq(a, n, index + 1, k)

    # Include the kth element
    include_kth = a[k] + max_sum_increasing_subseq(a, n, index, k + 1)

    # Return the maximum of the three cases
    return max(include, exclude, include_kth)

def check(candidate):
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71

check(max_sum_increasing_subseq)