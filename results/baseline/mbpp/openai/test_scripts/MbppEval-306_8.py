def max_sum_increasing_subseq(a, n, index, k):
    max_sum = [0] * n
    max_sum[index] = a[index]

    for i in range(index + 1, n):
        if a[i] > a[index]:
            max_sum[i] = max(max_sum[i], max_sum[index] + a[i])
        else:
            max_sum[i] = max(max_sum[i], max_sum[index])

    return max_sum[k]

# Examples




def check(candidate):
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71

check(max_sum_increasing_subseq)