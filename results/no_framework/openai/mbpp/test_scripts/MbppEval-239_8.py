def get_total_number_of_sequences(m, n):
    if n == 0:
        return 0
    
    total = 0
    for i in range(1, m+1):
        total += get_total_number_of_sequences_util(m, n-1, i)
        
    return total

def get_total_number_of_sequences_util(m, n, prev):
    if n == 0:
        return 1
    
    total = 0
    for i in range(prev*2, m+1):
        total += get_total_number_of_sequences_util(m, n-1, i)
        
    return total

# Test the function with the given examples




def check(candidate):
    assert get_total_number_of_sequences(10, 4) == 4
    assert get_total_number_of_sequences(5, 2) == 6
    assert get_total_number_of_sequences(16, 3) == 84

check(get_total_number_of_sequences)