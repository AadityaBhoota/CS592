def max_sum_increasing_subseq(a, n, index, k):
    max_sum = [0] * (k - index + 1)
    max_sum[0] = a[index]

    for i in range(index + 1, k + 1):
        curr_sum = a[i]
        for j in range(index, i):
            if a[i] > a[j]:
                curr_sum = max(curr_sum, a[i] + max_sum[j - index])
        max_sum[i - index] = curr_sum
    
    return max(max_sum)

def check(candidate):
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71

check(max_sum_increasing_subseq)