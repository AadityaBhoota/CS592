def get_total_number_of_sequences(m, n):
    if n == 1:
        return m

    dp = [[0] * (m+1) for _ in range(n)]
    for i in range(1, m+1):
        dp[0][i] = 1
        
    for i in range(1, n):
        for j in range(1, m+1):
            dp[i][j] = sum(dp[i-1][j//2+1:])
    
    return sum(dp[-1])

# Test the function with the given examples




def check(candidate):
    assert get_total_number_of_sequences(10, 4) == 4
    assert get_total_number_of_sequences(5, 2) == 6
    assert get_total_number_of_sequences(16, 3) == 84

check(get_total_number_of_sequences)