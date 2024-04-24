def toggle_middle_bits(n):
    if n < 3:
        return n
    
    # Calculate the number of bits in the input number n
    num_bits = n.bit_length()
    
    # Generate a mask that has 1s in all positions except for the first and last bits
    mask = (1 << (num_bits - 1)) - 2
    
    # Toggle the middle bits by bitwise XOR with the mask
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