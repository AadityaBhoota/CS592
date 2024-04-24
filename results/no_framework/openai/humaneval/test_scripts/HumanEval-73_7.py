def smallest_change(arr):
    n = len(arr)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for gap in range(1, n):
        left = 0
        for right in range(gap, n):
            if arr[left] == arr[right]:
                dp[left][right] = dp[left+1][right-1]
            else:
                dp[left][right] = 1 + min(dp[left][right-1], dp[left+1][right])

            left += 1

    return dp[0][n-1]

# Test cases




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