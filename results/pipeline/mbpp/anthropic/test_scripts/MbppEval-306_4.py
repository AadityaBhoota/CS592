def max_sum_increasing_subseq(a, n, i, k):
    dp = [0] * n
    
    # Initialize dp[i] to a[i]
    for i in range(n):
        dp[i] = a[i]
    
    # Find the maximum sum of increasing subsequence up to index i
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + a[i])
    
    # Find the maximum sum of increasing subsequence that includes the k-th element
    for j in range(i+1, k):
        if a[j] < a[k]:
            dp[k] = max(dp[k], dp[j] + a[k])
    
    return dp[k]

def check(candidate):
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71

check(max_sum_increasing_subseq)