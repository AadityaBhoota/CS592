def get_total_number_of_sequences(m, n):
    """
    Write a function that takes in positive integers m and n and finds the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
    """
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base case: There is 1 sequence of length 1 for each valid value
    for i in range(1, m + 1):
        dp[1][i] = 1

    # Fill the rest of the table
    for length in range(2, n + 1):
        for max_value in range(1, m + 1):
            for prev_value in range(1, max_value // 2 + 1):
                dp[length][max_value] += dp[length - 1][prev_value]

    return sum(dp[n])

def check(candidate):
    assert get_total_number_of_sequences(10, 4) == 4
    assert get_total_number_of_sequences(5, 2) == 6
    assert get_total_number_of_sequences(16, 3) == 84

check(get_total_number_of_sequences)