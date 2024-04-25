def get_total_number_of_sequences(m, n):
    count = 0
    
    def count_sequences(start, length):
        nonlocal count
        if length == 0:
            count += 1
            return
        for i in range(start, m + 1):
            if i >= 2 * start and i <= m:
                count_sequences(i, length - 1)
    
    count_sequences(1, n)
    return count

def check(candidate):
    assert get_total_number_of_sequences(10, 4) == 4
    assert get_total_number_of_sequences(5, 2) == 6
    assert get_total_number_of_sequences(16, 3) == 84

check(get_total_number_of_sequences)