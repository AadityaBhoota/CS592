def get_total_number_of_sequences(m, n):
    dp = [[0] * (n+1) for _ in range(m+1)]

    # Base case: there is 1 sequence of length 1 for each valid integer
    for i in range(1, m+1):
        dp[i][1] = 1

    for j in range(2, n+1):
        for i in range(1, m+1):
            min_val = max(1, i//2)
            for k in range(min_val, i):
                dp[i][j] += dp[k][j-1]

    return sum(dp[i][n] for i in range(1, m+1))

def check(candidate):
    assert get_total_number_of_sequences(10, 4) == 4
    assert get_total_number_of_sequences(5, 2) == 6
    assert get_total_number_of_sequences(16, 3) == 84

check(get_total_number_of_sequences)