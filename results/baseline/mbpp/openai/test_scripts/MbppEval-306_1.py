def max_sum_increasing_subseq(a, n, index, k):
    dp = [0] * (n+1)

    for i in range(1, n+1):
        dp[i] = a[i-1]
        for j in range(1, i):
            if a[i-1] > a[j-1] and j < index:
                dp[i] = max(dp[i], dp[j] + a[i-1])
            elif j == index:
                dp[i] = max(dp[i], dp[j] + a[i-1], dp[i-1] + a[k-1])

    return max(dp)

# Test cases




def check(candidate):
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71

check(max_sum_increasing_subseq)