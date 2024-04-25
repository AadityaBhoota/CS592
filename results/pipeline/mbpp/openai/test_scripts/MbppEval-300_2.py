def count_binary_seq(n): 
    count = 0  # Variable to count sequences where sums are equal
    
    for i in range(2**(2*n)):
        seq = format(i, f'0{2*n}b')  # Get the binary sequence for current number
        first_n_sum = sum(int(bit) for bit in seq[:n])  # Sum of first n bits
        last_n_sum = sum(int(bit) for bit in seq[n:])  # Sum of last n bits
        
        if first_n_sum == last_n_sum:
            count += 1
    
    return count

def check(candidate):
    assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001)

check(count_binary_seq)