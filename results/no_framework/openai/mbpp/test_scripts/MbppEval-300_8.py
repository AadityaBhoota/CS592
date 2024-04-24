def count_binary_seq(n):
    if n == 0:
        return 1.0
    
    dp = [[0.0 for _ in range(n + 1)] for _ in range(n + 1)]
    
    dp[0][0] = 1.0
    
    for i in range(1, n + 1):
        dp[i][0] = dp[i - 1][1]
        dp[i][i] = dp[i - 1][i - 1]
        
        for j in range(1, i):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
    
    count = sum(dp[n])
    
    return count

# Test cases




def check(candidate):
    assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001)

check(count_binary_seq)