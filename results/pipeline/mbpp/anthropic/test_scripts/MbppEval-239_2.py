def get_total_number_of_sequences(m, n):
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    # Base case: sequences of length 1
    for i in range(1, m+1):
        dp[i][1] = 1
    
    # Compute the number of sequences
    for j in range(2, n+1):
        for i in range(1, m+1):
            for k in range(max(1, i//2), i):
                dp[i][j] += dp[k][j-1]
    
    # Sum up the values in the last column
    return sum(dp[i][n] for i in range(1, m+1))

def check(candidate):
    assert get_total_number_of_sequences(10, 4) == 4
    assert get_total_number_of_sequences(5, 2) == 6
    assert get_total_number_of_sequences(16, 3) == 84

check(get_total_number_of_sequences)