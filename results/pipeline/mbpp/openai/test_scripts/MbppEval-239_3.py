def get_total_number_of_sequences(m, n): 
    count = 0
    
    def generate_sequence(current_seq, m, previous_value, n):
        nonlocal count
        
        if len(current_seq) == n:
            valid = all(prev * 2 <= curr <= m for prev, curr in zip(current_seq, current_seq[1:]))
            if valid:
                count += 1
        else:
            for num in range(previous_value*2, m+1):
                generate_sequence(current_seq + [num], m, num, n)
    
    generate_sequence([], m, 0, n)
    
    return count

def check(candidate):
    assert get_total_number_of_sequences(10, 4) == 4
    assert get_total_number_of_sequences(5, 2) == 6
    assert get_total_number_of_sequences(16, 3) == 84

check(get_total_number_of_sequences)