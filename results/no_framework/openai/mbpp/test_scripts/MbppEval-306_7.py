def max_sum_increasing_subseq(a, n, index, k):
    dp = [0] * n

    dp[index] = a[index]

    for i in range(index+1, n):
        if a[i] > a[index]:
            dp[i] = max(dp[i], dp[index]+a[i])
        else:
            dp[i] = max(dp[i], dp[index])

    # Add the kth element to the maximum sum
    if k > index:
        dp[k] = max(dp[k], dp[index]+a[k])

    return max(dp)

# Test cases




def check(candidate):
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71

check(max_sum_increasing_subseq)