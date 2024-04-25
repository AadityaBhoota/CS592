def get_total_number_of_sequences(m, n):
    # Create a 2D table to store the number of sequences
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base case: there is 1 sequence of length 1, which is [1]
    for i in range(1, m + 1):
        dp[1][i] = 1

    # Fill the table using dynamic programming
    for length in range(2, n + 1):
        for max_value in range(1, m + 1):
            for prev_value in range(1, max(1, max_value // 2) + 1):
                dp[length][max_value] += dp[length - 1][prev_value]

    # The total number of sequences is the sum of all values in the last row
    return sum(dp[n])

def check(candidate):
    assert get_total_number_of_sequences(10, 4) == 4
    assert get_total_number_of_sequences(5, 2) == 6
    assert get_total_number_of_sequences(16, 3) == 84

check(get_total_number_of_sequences)