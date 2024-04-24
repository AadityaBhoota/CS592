def get_total_number_of_sequences(m, n):
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    for i in range(1, m+1):
        dp[1][i] = 1

    for i in range(2, n+1):
        for j in range(1, m+1):
            for k in range(j//2, j):
                dp[i][j] += dp[i-1][k]

    return sum(dp[n])

# Test cases




def check(candidate):
    assert get_total_number_of_sequences(10, 4) == 4
    assert get_total_number_of_sequences(5, 2) == 6
    assert get_total_number_of_sequences(16, 3) == 84

check(get_total_number_of_sequences)