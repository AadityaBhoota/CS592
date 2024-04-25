def max_sum_increasing_subseq(a, n, index, k):
    """
    Find the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i.
    """
    if k <= index or k >= n:
        return 0

    # Create a memoization table to store the maximum sum
    dp = [[0] * (k + 1) for _ in range(index + 1)]

    # Initialize the first row
    dp[0][0] = a[0]

    # Fill the dynamic programming table
    for i in range(1, index + 1):
        for j in range(i + 1, k + 1):
            if a[i] < a[j]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + a[j])
            else:
                dp[i][j] = dp[i - 1][j]

    # Find the maximum sum
    max_sum = 0
    for j in range(index + 1, k + 1):
        max_sum = max(max_sum, dp[index][j])

    return max_sum

def check(candidate):
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71

check(max_sum_increasing_subseq)