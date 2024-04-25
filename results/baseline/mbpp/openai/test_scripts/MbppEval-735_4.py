def set_middle_bits(n):
    # Extract the first and last bits of the number
    first_bit = n & 1
    last_bit = n & (1 << (n.bit_length() - 1))
    
    # Toggle all bits except the first and last bits
    middle_bits = n ^ (n & (2**n.bit_length() - 1)) >> 1
    
    # Combine the first, middle, and last bits to get the final result
    result = first_bit | middle_bits | last_bit
    
    return result

# Test cases




def check(candidate):
    assert toggle_middle_bits(9) == 15
    assert toggle_middle_bits(10) == 12
    assert toggle_middle_bits(11) == 13
    assert toggle_middle_bits(0b1000001) == 0b1111111
    assert toggle_middle_bits(0b1001101) == 0b1110011

check(set_middle_bits)