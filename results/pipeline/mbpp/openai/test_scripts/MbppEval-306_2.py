def max_sum_increasing_subseq(a, n, index, k):
    max_sum = [0] * n
    
    for i in range(index):
        max_sum[i] = a[i]
        for j in range(i):
            if a[i] > a[j] and max_sum[i] < max_sum[j] + a[i]:
                max_sum[i] = max_sum[j] + a[i]
    
    max_sum_ik = max_sum[index]
    
    for i in range(index+1, k):
        for j in range(index):
            if a[i] > a[j] and max_sum[i] < max_sum[j] + a[i]:
                max_sum[i] = max_sum[j] + a[i]
        max_sum_ik = max(max_sum_ik, max_sum[i])
    
    return max_sum_ik

def check(candidate):
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71

check(max_sum_increasing_subseq)