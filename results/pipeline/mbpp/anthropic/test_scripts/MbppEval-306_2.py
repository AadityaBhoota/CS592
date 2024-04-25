def max_sum_increasing_subseq(a, n, index, k):
    dp = [0] * n
    dp[0] = a[0]

    for i in range(1, index + 1):
        if a[i] > a[i-1]:
            dp[i] = dp[i-1] + a[i]
        else:
            dp[i] = dp[i-1]

    for i in range(index + 1, k + 1):
        dp[i] = max(dp[i], dp[index] + a[i])

    return dp[k]

def check(candidate):
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71

check(max_sum_increasing_subseq)