def smallest_change(arr):
    n = len(arr)
    # Create a 2D dynamic programming table to store the minimum changes required
    dp = [[0] * n for _ in range(n)]

    # Compute the minimum changes required for each subarray
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if i == j:
                dp[i][j] = 0
            elif arr[i] == arr[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1

    # Return the minimum changes required for the entire array
    return dp[0][n - 1]

def check(candidate):

    # Check some simple cases
    assert candidate([1,2,3,5,4,7,9,6]) == 4
    assert candidate([1, 2, 3, 4, 3, 2, 2]) == 1
    assert candidate([1, 4, 2]) == 1
    assert candidate([1, 4, 4, 2]) == 1

    # Check some edge cases that are easy to work out by hand.
    assert candidate([1, 2, 3, 2, 1]) == 0
    assert candidate([3, 1, 1, 3]) == 0
    assert candidate([1]) == 0
    assert candidate([0, 1]) == 1


check(smallest_change)