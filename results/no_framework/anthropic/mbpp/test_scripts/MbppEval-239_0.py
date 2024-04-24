def get_total_number_of_sequences(m, n):
    """
    Finds the number of possible sequences of length n, such that each element is a positive
    integer and is greater than or equal to twice the previous element but less than or equal to m.
    """
    # Create a 2D array to store the number of sequences of length i ending with j
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base case: there is 1 sequence of length 1 ending with each valid number
    for j in range(1, m + 1):
        dp[1][j] = 1

    # Compute the number of sequences for each length and ending value
    for i in range(2, n + 1):
        for j in range(1, m + 1):
            for k in range(1, j // 2 + 1):
                dp[i][j] += dp[i - 1][k]

    # Return the sum of all valid sequences
    return sum(dp[n])

def check(candidate):
    assert get_total_number_of_sequences(10, 4) == 4
    assert get_total_number_of_sequences(5, 2) == 6
    assert get_total_number_of_sequences(16, 3) == 84

check(get_total_number_of_sequences)