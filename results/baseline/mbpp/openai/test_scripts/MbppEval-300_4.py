def count_binary_seq(n):
    if n == 0:
        return 1
    
    dp = [[0 for _ in range(2*n+1)] for _ in range(n+1)]
    
    # Initializing the base case
    dp[0][0] = 1
    
    # Dynamic programming to compute the count of all binary sequences
    for i in range(1, n+1):
        for j in range(2*n+1):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] if j > 0 and j < 2*n else dp[i-1][j-1] if j == 0 else dp[i-1][j+1]

    return float(dp[n][n])

# Testing the function with the given examples




def check(candidate):
    assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001)

check(count_binary_seq)