def smallest_change(arr):
    n = len(arr)
    dp = [[float('inf')] * (n // 2 + 1) for _ in range(n // 2 + 1)]
    dp[0][0] = 0

    for i in range(1, n // 2 + 1):
        dp[i][0] = dp[i - 1][0] + abs(arr[i - 1] - arr[n - i])

    for i in range(1, n // 2 + 1):
        for j in range(1, min(i, n // 2 - i + 1) + 1):
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1] + abs(arr[i - 1] - arr[n - i]))

    return dp[n // 2][n // 2 if n % 2 == 0 else n // 2 + 1]

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