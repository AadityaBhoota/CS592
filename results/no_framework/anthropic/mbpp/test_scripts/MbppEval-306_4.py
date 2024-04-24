def max_sum_increasing_subseq(a, n, index, k):
    """
    Find the maximum sum of increasing subsequence from prefix until the ith index
    and also including the given kth element which is after the ith index.
    """
    # Create a 2D array to store the maximum sum of increasing subsequence
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if i == j:
                dp[i][j] = a[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + a[i - 1])

    # Find the maximum sum of increasing subsequence
    max_sum = 0
    for j in range(1, min(index + 1, k) + 1):
        max_sum = max(max_sum, dp[index + 1][j] + a[k - 1])

    return max_sum

def check(candidate):
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71

check(max_sum_increasing_subseq)