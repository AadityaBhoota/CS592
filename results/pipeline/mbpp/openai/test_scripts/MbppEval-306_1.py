def max_sum_increasing_subseq(a, n, index, k):
    if index >= n or k >= n:
        return 0
    
    if a[index] < a[k]:
        include_current = a[index] + max_sum_increasing_subseq(a, n, k, k+1)
        exclude_current = max_sum_increasing_subseq(a, n, index, k+1)
        
        return max(include_current, exclude_current)
    else:
        return max_sum_increasing_subseq(a, n, k, k+1)

def check(candidate):
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71

check(max_sum_increasing_subseq)