def smallest_change(arr):
    n = len(arr)
    
    # Create a 2D array to store the lengths of LPS
    dp = [[0] * n for _ in range(n)]
    
    # Fill the diagonal elements (single-element LPS)
    for i in range(n):
        dp[i][i] = 1
    
    # Compute the lengths of LPS for different substrings
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if arr[i] == arr[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    
    # Calculate the minimum number of changes required
    return n - dp[0][n - 1]

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