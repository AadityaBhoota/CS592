def max_sum_increasing_subseq(a, n, index, k):
    max_sum = 0
    dp = [0] * n

    # Find maximum sum of increasing subsequence from prefix until index
    for i in range(index):
        dp[i] = a[i]
        for j in range(i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j] + a[i])

    # Include the element at position k and find the maximum sum
    for i in range(index+1, k):
        dp[i] = a[i]
        for j in range(index, i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j] + a[i])

    max_sum = max(dp[:k])

    return max_sum

# Test cases




def check(candidate):
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71

check(max_sum_increasing_subseq)