def max_sum_increasing_subseq(a, n, index, k):
    max_sum = a[index]
    
    for i in range(index):
        if a[i] < a[index]:
            max_sum = max(max_sum, a[i] + max_sum_increasing_subseq(a, n, i, k))

    return max_sum

# Testing the function with the examples provided




def check(candidate):
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71

check(max_sum_increasing_subseq)