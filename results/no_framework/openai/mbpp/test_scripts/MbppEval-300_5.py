def count_binary_seq(n):
    # The total number of binary sequences of length 2n is 2^(2n)
    total_sequences = 2**(2*n)
    
    # Initialize count to 0
    count = 0
    
    # Iterate over all possible ways to split the binary sequence using n bits
    for i in range(n + 1):
        # Calculate the number of ways to choose i bits from n bits
        ways_to_choose_i_bits = math.comb(n, i)
        
        # For a given split with i bits in the first half, all other bits are fixed
        # So, the total number of valid sequences for this split is 2^i
        count += ways_to_choose_i_bits * 2**i
    
    return count

# Test the function




def check(candidate):
    assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001)

check(count_binary_seq)