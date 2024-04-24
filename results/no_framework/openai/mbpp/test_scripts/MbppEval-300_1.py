def count_binary_seq(n):
    if n == 0:
        return 1
    # Initialize count to store the total count of valid sequences
    count = 0
    
    # Generate all binary sequences of length 2n
    for i in range(2**(2*n)):
        # Convert the number to binary representation
        binary_str = bin(i)[2:].zfill(2*n)
        
        # Take the sum of first and last n bits
        sum_first_n = sum(int(bit) for bit in binary_str[:n])
        sum_last_n = sum(int(bit) for bit in binary_str[n:])
        
        # If the sums are equal, increment the count
        if sum_first_n == sum_last_n:
            count += 1
    
    return count

# Test cases




def check(candidate):
    assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001)

check(count_binary_seq)