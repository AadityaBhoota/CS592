def max_sub_array_sum_repeated(a, n, k):
    dp = [float('-inf')] * n
    max_sum = float('-inf')
    
    for _ in range(k):
        for i in range(n):
            dp[i] = max(dp[i-1] + a[i], a[i]) if i > 0 else a[i]
            max_sum = max(max_sum, dp[i])

    return max_sum

# Examples




def check(candidate):
    assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
    assert max_sub_array_sum_repeated([-1, 10, 20], 3, 2) == 59
    assert max_sub_array_sum_repeated([-1, -2, -3], 3, 3) == -1

check(max_sub_array_sum_repeated)