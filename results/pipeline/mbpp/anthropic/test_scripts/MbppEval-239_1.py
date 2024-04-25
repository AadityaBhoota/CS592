def get_total_number_of_sequences(m, n):
    if n == 1:
        return m
    if m < 2:
        return 0
    
    total = 0
    for first_element in range(2, m+1):
        total += get_total_number_of_sequences(min(m, first_element * 2), n-1)
    
    return total

def check(candidate):
    assert get_total_number_of_sequences(10, 4) == 4
    assert get_total_number_of_sequences(5, 2) == 6
    assert get_total_number_of_sequences(16, 3) == 84

check(get_total_number_of_sequences)