def get_total_number_of_sequences(m, n):
    """
    Write a function that takes in positive integers m and n and finds the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
    """
    if n == 1:
        return m
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        dp[i][1] = 1
    
    for i in range(2, n + 1):
        for j in range(1, m + 1):
            for k in range(1, j // 2 + 1):
                dp[j][i] += dp[k][i - 1]
    
    return sum(dp[i][n] for i in range(1, m + 1))

def check(candidate):
    assert get_total_number_of_sequences(10, 4) == 4
    assert get_total_number_of_sequences(5, 2) == 6
    assert get_total_number_of_sequences(16, 3) == 84

check(get_total_number_of_sequences)