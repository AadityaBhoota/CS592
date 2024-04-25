def get_total_number_of_sequences(m, n):
    dp = [[0] * (m+1) for _ in range(n)]
    
    for i in range(1, m+1):
        dp[0][i] = 1
    
    for i in range(1, n):
        for j in range(1, m+1):
            for k in range(j//2, j+1):
                dp[i][j] += dp[i-1][k]
    
    return sum(dp[n-1])

# Test cases




def check(candidate):
    assert get_total_number_of_sequences(10, 4) == 4
    assert get_total_number_of_sequences(5, 2) == 6
    assert get_total_number_of_sequences(16, 3) == 84

check(get_total_number_of_sequences)