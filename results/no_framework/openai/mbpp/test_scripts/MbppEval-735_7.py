def set_middle_bits(n):
    if n == 0 or n == 1:  # Edge case handling
        return n
    
    # Determine the number of bits in the number
    num_bits = n.bit_length()
    
    # Create a mask with set bits in all positions except the first and last bit
    mask = (1 << (num_bits - 2)) - 1
    
    # Toggle the middle bits of the number using XOR with the mask
    result = n ^ mask
    
    return result

# Test cases




def check(candidate):
    assert toggle_middle_bits(9) == 15
    assert toggle_middle_bits(10) == 12
    assert toggle_middle_bits(11) == 13
    assert toggle_middle_bits(0b1000001) == 0b1111111
    assert toggle_middle_bits(0b1001101) == 0b1110011

check(set_middle_bits)