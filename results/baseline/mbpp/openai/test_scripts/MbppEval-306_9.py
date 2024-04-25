def max_sum_increasing_subseq(arr, n, i, k):
    if i >= n or k >= n:
        return 0

    incl_k = 0
    if k > i and arr[k] > arr[i]:
        incl_k = max_sum_increasing_subseq(arr, n, k, k+1) + arr[k]

    excl_k = max_sum_increasing_subseq(arr, n, i, k+1)

    return max(incl_k, excl_k)


# Test cases




def check(candidate):
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71

check(max_sum_increasing_subseq)