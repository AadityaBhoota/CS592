def sequence(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[dp[i - 1]] + dp[i - dp[i - 1]]

    return dp[n]

# Test cases




def check(candidate):
    assert sequence(10) == 6
    assert sequence(2) == 1
    assert sequence(3) == 2

check(sequence)