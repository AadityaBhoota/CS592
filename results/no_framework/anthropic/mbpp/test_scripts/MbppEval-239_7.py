def get_total_number_of_sequences(m, n):
    """
    Finds the number of possible sequences of length n, such that each element
    is a positive integer and is greater than or equal to twice the previous
    element but less than or equal to m.
    """
    # Base case: if n = 1, the number of sequences is m
    if n == 1:
        return m

    # Recursive case: the number of sequences of length n is the sum of the
    # number of sequences of length n-1 starting with each possible value
    total = 0
    for i in range(1, m+1):
        for j in range(max(1, 2*i), m+1):
            total += get_total_number_of_sequences(m, n-1)
    return total

def check(candidate):
    assert get_total_number_of_sequences(10, 4) == 4
    assert get_total_number_of_sequences(5, 2) == 6
    assert get_total_number_of_sequences(16, 3) == 84

check(get_total_number_of_sequences)