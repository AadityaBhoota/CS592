def largest_subset(arr, n):
    dp = [0] * n
    for a in arr:
        for i in range(n - 1, 0, -1):
            if a % i == 0:
                dp[i] = max(dp[i], dp[i - 1] + 1)
    return max(dp)

def check(candidate):
    assert largest_subset([ 1, 3, 6, 13, 17, 18 ]) == 4
    assert largest_subset([10, 5, 3, 15, 20]) == 3
    assert largest_subset([18, 1, 3, 6, 13, 17]) == 4

check(largest_subset)