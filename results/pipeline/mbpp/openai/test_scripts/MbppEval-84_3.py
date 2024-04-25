def sequence(n):
    dp = [0, 1, 1] + [0] * (n - 2)
    
    for i in range(3, n + 1):
        dp[i] = dp[dp[i-1]] + dp[i - dp[i-1]]
    
    return dp[n]

def check(candidate):
    assert sequence(10) == 6
    assert sequence(2) == 1
    assert sequence(3) == 2

check(sequence)