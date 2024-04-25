def get_total_number_of_sequences(m, n):
    if n == 1:
        return m
    count = 0
    for i in range(1, m//2 + 1):
        count += get_total_number_of_sequences(i, n - 1)
    return count

# Test cases




def check(candidate):
    assert get_total_number_of_sequences(10, 4) == 4
    assert get_total_number_of_sequences(5, 2) == 6
    assert get_total_number_of_sequences(16, 3) == 84

check(get_total_number_of_sequences)