def max_sum_increasing_subseq(a, n, index, k):
    dp = [0] * n
    dp[index] = a[index]

    for i in range(index+1, k):
        for j in range(i):
            if a[i] > a[j]:
                dp[i] = max(dp[i], dp[j] + a[i])

    return dp[k-1]

# Test cases




def check(candidate):
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71

check(max_sum_increasing_subseq)