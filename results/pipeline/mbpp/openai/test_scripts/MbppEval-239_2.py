def get_total_number_of_sequences(m, n): 
    count = 0

    def generate_sequences(length, max_val, sequence):
        nonlocal count
        if length == n:
            count += 1
            return
        for value in range(max_val * 2, m+1):
            if all(value >= 2 * elem and value <= m for elem in sequence):
                generate_sequences(length + 1, value, sequence + [value])

    generate_sequences(0, 1, [])

    return count

def check(candidate):
    assert get_total_number_of_sequences(10, 4) == 4
    assert get_total_number_of_sequences(5, 2) == 6
    assert get_total_number_of_sequences(16, 3) == 84

check(get_total_number_of_sequences)