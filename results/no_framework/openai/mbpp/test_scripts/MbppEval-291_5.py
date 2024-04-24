def count_no_of_ways(n, k):
    # Initialize the base cases
    dp = [[0, 0] for _ in range(n+1)]
    dp[1][False] = k
    for i in range(2, n+1):
        dp[i][False] = (k-1) * (dp[i-1][False] + dp[i-1][True])
        dp[i][True] = dp[i-1][False]

    return sum(dp[n])

# Test the function with the provided examples




def check(candidate):
    assert count_no_of_ways(2, 4) == 16
    assert count_no_of_ways(3, 2) == 6
    assert count_no_of_ways(4, 4) == 228

check(count_no_of_ways)