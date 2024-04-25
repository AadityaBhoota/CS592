def eulerian_num(n, m):
    """
    Find the Eulerian number a(n, m).

    Args:
        n (int): The value of n.
        m (int): The value of m.

    Returns:
        int: The Eulerian number a(n, m).
    """
    if m == 0:
        return 1
    
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    # Initialize the base cases
    for i in range(1, n+1):
        dp[i][0] = 1
    
    # Compute the Eulerian numbers using the recurrence relation
    for i in range(2, n+1):
        for j in range(1, min(i, m)+1):
            dp[i][j] = (i-j) * dp[i-1][j-1] + (j+1) * dp[i-1][j]
    
    return dp[n][m]

def check(candidate):
    assert eulerian_num(3, 1) == 4
    assert eulerian_num(4, 1) == 11
    assert eulerian_num(5, 3) == 26

check(eulerian_num)