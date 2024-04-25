def sequence(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 1
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    for i in range(4, n+1):
        dp[i] = dp[dp[i-1]] + dp[i - dp[i-1]]
    return dp[n]

# Test the function with example cases




def check(candidate):
    assert sequence(10) == 6
    assert sequence(2) == 1
    assert sequence(3) == 2

check(sequence)