def max_sum_increasing_subseq(a, n, index, k):
    """
    Find the maximum sum of increasing subsequence from prefix until ith index
    and also including a given kth element which is after i, i.e., k > i.
    """
    # Initialize the dynamic programming array
    dp = [0] * n

    # Fill the dp array
    for i in range(n):
        dp[i] = a[i]
        for j in range(i):
            if a[i] > a[j]:
                dp[i] = max(dp[i], dp[j] + a[i])

    max_sum = dp[index]

    # Find the maximum sum including the kth element
    for i in range(index + 1, k + 1):
        max_sum = max(max_sum, dp[index] + a[i])

    return max_sum

# Examples




def check(candidate):
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71

check(max_sum_increasing_subseq)