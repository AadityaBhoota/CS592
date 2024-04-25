def get_total_number_of_sequences(m, n):
    def count_sequences(prev, curr_len, n, m):
        if curr_len == n:
            return 1

        total_sequences = 0
        for next_num in range(2 * prev, m + 1):
            total_sequences += count_sequences(next_num, curr_len + 1, n, m)

        return total_sequences

    total_sequences = 0
    for start_num in range(1, m - n + 2):
        total_sequences += count_sequences(start_num, 1, n, m)

    return total_sequences

def check(candidate):
    assert get_total_number_of_sequences(10, 4) == 4
    assert get_total_number_of_sequences(5, 2) == 6
    assert get_total_number_of_sequences(16, 3) == 84

check(get_total_number_of_sequences)