def get_total_number_of_sequences(m, n):
    """
    Write a function that takes in positive integers m and n and finds the number of possible sequences of length n, such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
    """
    def helper(start, length):
        if length == 1:
            return m - start + 1
        total = 0
        for i in range(max(start, 1), (m // 2) + 1):
            total += helper(i, length - 1)
        return total

    return helper(1, n)

def check(candidate):
    assert get_total_number_of_sequences(10, 4) == 4
    assert get_total_number_of_sequences(5, 2) == 6
    assert get_total_number_of_sequences(16, 3) == 84

check(get_total_number_of_sequences)