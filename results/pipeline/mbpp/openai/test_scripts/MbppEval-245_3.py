import numpy as np

def max_sum(arr):
    dp = np.zeros(len(arr))
    increasing_dp = np.zeros(len(arr))
    decreasing_dp = np.zeros(len(arr))

    for i in range(len(arr)):
        dp[i] = arr[i]  # Initialize the value with the element itself
        for j in range(i):
            if arr[j] < arr[i]:  # If the element at j can be appended to the subsequence ending at i
                dp[i] = max(dp[i], dp[j] + arr[i])  # Update to the maximum sum

    return dp

def check(candidate):
    assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
    assert max_sum([80, 60, 30, 40, 20, 10]) == 210
    assert max_sum([2, 3 ,14, 16, 21, 23, 29, 30]) == 138

check(max_sum)