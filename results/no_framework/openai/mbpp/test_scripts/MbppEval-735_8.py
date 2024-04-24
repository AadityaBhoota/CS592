def set_middle_bits(n):
    # Finding the number of bits present in the number
    num_bits = n.bit_length()
    
    # Creating a mask to toggle the middle bits
    mask = (2 ** (num_bits - 1)) - 2
    
    # Toggling the middle bits
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