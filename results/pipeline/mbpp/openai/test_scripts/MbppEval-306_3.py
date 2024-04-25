def max_sum_increasing_subseq(a, n, index, k):
    if index == 0:
        return a[0]
    
    dp = [0] * n
    dp[0] = a[0]
    
    for i in range(1, index + 1):
        dp[i] = a[i]
        for j in range(i):
            if a[i] > a[j]:
                dp[i] = max(dp[i], dp[j] + a[i])
    
    max_sum = dp[index]
    
    for i in range(index+1, k):
        if a[i] > a[index]:
            max_sum = max(max_sum, dp[index] + a[i])

    return max_sum

def check(candidate):
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71

check(max_sum_increasing_subseq)