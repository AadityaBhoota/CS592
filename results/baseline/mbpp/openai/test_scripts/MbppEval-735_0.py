def set_middle_bits(n):
    num_bits = n.bit_length()
    if num_bits <= 2:
        return n
    
    mask = (1 << (num_bits - 1)) - 2  # Create a mask with ones in the middle bits
    
    return n ^ mask

# Test cases




def check(candidate):
    assert toggle_middle_bits(9) == 15
    assert toggle_middle_bits(10) == 12
    assert toggle_middle_bits(11) == 13
    assert toggle_middle_bits(0b1000001) == 0b1111111
    assert toggle_middle_bits(0b1001101) == 0b1110011

check(set_middle_bits)