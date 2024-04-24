def count_binary_seq(n):
    """
    Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.

    Examples:
    count_binary_seq(1) == 2.0
    count_binary_seq(2) == 6.0
    count_binary_seq(3) == 20.0
    """
    if n == 0:
        return 1.0

    dp = [[0] * (n + 1) for _ in range(2 ** n)]

    # Base case: When the first n bits have a sum of 0, the last n bits must also have a sum of 0.
    dp[0][0] = 1.0

    for i in range(1, 2 ** n):
        for j in range(n + 1):
            if j > 0:
                dp[i][j] += dp[i - 1][j - 1]  # Add the previous sequence with one more 1 in the first n bits
            if j < n:
                dp[i][j] += dp[i - 1][j]  # Add the previous sequence with one more 0 in the first n bits

    total = 0.0
    for i in range(2 ** n):
        total += dp[i][n]

    return total

def check(candidate):
    assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001)

check(count_binary_seq)