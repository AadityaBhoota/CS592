def max_sum_increasing_subseq(a, n, index, k):
    dp = [0] * n

    for i in range(n):
        dp[i] = max(dp[j] for j in range(i) if a[j] < a[i]) + a[i]
        
    max_sum = dp[index]
    
    for i in range(index+1, k):
        max_sum = max(max_sum, max(dp[j] for j in range(i) if a[j] < a[i]) + a[i])
    
    return max_sum

# Test cases




def check(candidate):
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71

check(max_sum_increasing_subseq)