def get_total_number_of_sequences(m, n): 
    dp = [[0 for j in range(m+1)] for i in range(n)]
    
    for j in range(1, m+1): 
        dp[0][j] = 1
        
    for i in range(1, n): 
        for j in range(1, m+1): 
            dp[i][j] = dp[i][j-1] + dp[i-1][j//2]
            
    return dp[n-1][m]

# Test cases




def check(candidate):
    assert get_total_number_of_sequences(10, 4) == 4
    assert get_total_number_of_sequences(5, 2) == 6
    assert get_total_number_of_sequences(16, 3) == 84

check(get_total_number_of_sequences)