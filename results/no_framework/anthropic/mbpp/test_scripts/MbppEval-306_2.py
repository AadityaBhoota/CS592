def max_sum_increasing_subseq(a, n, index, k):
    # Create a 2D array to store the maximum sum of increasing subsequence
    dp = [[0] * (k + 1) for _ in range(n)]

    # Initialize the first row of the 2D array
    for j in range(k + 1):
        if j <= index:
            dp[0][j] = a[0]
        else:
            dp[0][j] = float('-inf')

    # Fill the 2D array
    for i in range(1, n):
        for j in range(k + 1):
            if j <= i:
                dp[i][j] = max(dp[i - 1][j], a[i] + dp[i - 1][j - 1])
            else:
                dp[i][j] = max(dp[i - 1][j], a[i] + dp[i - 1][j - 1] if j > 0 else float('-inf'))

    # Find the maximum value in the last row of the 2D array
    return max(dp[n - 1])

def check(candidate):
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
    assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
    assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71

check(max_sum_increasing_subseq)