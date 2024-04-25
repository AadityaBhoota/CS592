import math

def count_binary_seq(n):
    total_count = 2**(2*n)  # Total number of possible binary sequences of length 2n
    valid_count = 0
    
    for i in range(n+1):
        count_first_n_bits = i
        count_last_n_bits = n - i
        valid_count += math.comb(n, count_first_n_bits) * (2 ** count_last_n_bits)  # Count valid sequences for each case
    
    return valid_count

def check(candidate):
    assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001)

check(count_binary_seq)