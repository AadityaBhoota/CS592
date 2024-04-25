def get_total_number_of_sequences(m, n):
    count = 0
    for first_element in range(1, m+1):
        current_element = first_element
        for _ in range(n-1):
            current_element = max(current_element * 2, current_element + 1)
            if current_element > m:
                break
        else:
            count += 1
    return count

def check(candidate):
    assert get_total_number_of_sequences(10, 4) == 4
    assert get_total_number_of_sequences(5, 2) == 6
    assert get_total_number_of_sequences(16, 3) == 84

check(get_total_number_of_sequences)