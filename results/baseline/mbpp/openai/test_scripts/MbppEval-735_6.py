def set_middle_bits(n):  
    '''
    Write a python function to toggle bits of the number except the first and the last bit. 
    Examples:
    toggle_middle_bits(9) == 15
    toggle_middle_bits(10) == 12
    toggle_middle_bits(11) == 13
    '''
def toggle_middle_bits(n):
    first_bit = n & 1
    last_bit = n & (1 << (n.bit_length() - 1))
    middle_bits = n & ~((1 << (n.bit_length() - 1)) | 1)
    toggled_middle_bits = middle_bits ^ ((1 << (middle_bits.bit_length() - 1)) - 1)
    
    result = first_bit | toggled_middle_bits | last_bit
    return result

def check(candidate):
    assert toggle_middle_bits(9) == 15
    assert toggle_middle_bits(10) == 12
    assert toggle_middle_bits(11) == 13
    assert toggle_middle_bits(0b1000001) == 0b1111111
    assert toggle_middle_bits(0b1001101) == 0b1110011

check(set_middle_bits)